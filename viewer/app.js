// The Universal — 3Dビューア（DOC-02 §3-6、DOC-03 §3）
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { CSS2DRenderer, CSS2DObject } from "three/addons/renderers/CSS2DRenderer.js";

const LEVEL_COLORS = ["#6b7280", "#60a5fa", "#22d3ee", "#34d399", "#facc15", "#fb923c"];
const LEVEL_NAMES = ["L0 未学習", "L1 認知", "L2 説明", "L3 専門理解", "L4 統合応用", "L5 批判的検証"];
const TYPE_JA = { theme: "テーマ", concept: "概念", event: "出来事", actor: "主体", theory: "理論", evidence: "証拠", question: "問い", method: "思考法" };
const EP_JA = { fact: "事実", theory: "理論", debate: "論争", normative: "規範", hypothesis: "仮説", unknown: "未知" };
const CONF_JA = { high: "確信度 高", medium: "確信度 中", low: "確信度 低" };
const EDGE_JA = { causes: "原因となる", enables: "可能にする", requires: "前提とする", part_of: "部分である", precedes: "先行する",
  supports: "支持する", contradicts: "対立する", analogous: "類比", instance_of: "事例である", applies: "適用する",
  evidence_for: "証拠となる", raises: "問いを生む", addresses: "答えようとする" };
const EDGE_COLORS = { causes: "#f87171", enables: "#fbbf24", requires: "#a78bfa", precedes: "#64748b", supports: "#34d399",
  contradicts: "#fb7185", evidence_for: "#22d3ee", raises: "#f0abfc", addresses: "#93c5fd", applies: "#facc15" };
const TICKS = [[13.8e9, "138億年前"], [1e9, "10億年前"], [1e8, "1億年前"], [1e7, "1000万年前"], [1e6, "100万年前"],
  [1e5, "10万年前"], [1e4, "1万年前"], [1e3, "1000年前"], [1e2, "100年前"], [0, "現在"], [-30, "30年後"]];
const xOfYa = (ya) => (ya >= 0 ? -10 * Math.log10(1 + ya) : 10 * Math.log10(1 + Math.abs(ya)));

const $ = (s) => document.querySelector(s);
const safeUrl = (u) => (/^https?:\/\//.test(u || "") ? u : "");
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

let G, byId = {}, mode = "cyl", selected = null;
const meshes = [], labels = {};
let modeTween = null, camTween = null;

// グループ内の線を外すとき、GPUメモリも解放する（iPhoneでのメモリ不足を防ぐ）
function clearGroup(g) {
  for (const c of [...g.children]) {
    c.geometry?.dispose();
    c.material?.dispose();
    g.remove(c);
  }
}

// ---------------------------------------------------------------- シーン
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x05060f, 0.0035);
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 3000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.setClearColor(0x05060f);
$("#scene").appendChild(renderer.domElement);
const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize(innerWidth, innerHeight);
Object.assign(labelRenderer.domElement.style, { position: "absolute", top: "0", left: "0", pointerEvents: "none" });
$("#scene").appendChild(labelRenderer.domElement);

// 縦長の画面（iPhone）では時間軸を縦に置く（下が過去、上が現在）。横長では横（左が過去）。
// OrbitControls は作成時の camera.up を使うため、向きが変わったら作り直す。
let portrait = innerHeight > innerWidth;
let controls;
function makeControls(resetView) {
  const target = controls ? controls.target.clone() : new THREE.Vector3(-45, 0, 0);
  controls?.dispose();
  camera.up.set(...(portrait ? [1, 0, 0] : [0, 1, 0]));
  if (resetView) camera.position.set(...(portrait ? [-45, 70, 150] : [-40, 55, 150]));
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.minDistance = 8;
  controls.maxDistance = 420;
  controls.target.copy(target);
}
makeControls(true);

scene.add(new THREE.AmbientLight(0xffffff, 0.75));
const dl = new THREE.DirectionalLight(0xffffff, 0.9);
dl.position.set(30, 80, 60);
scene.add(dl);

// 星空
{
  const g = new THREE.BufferGeometry();
  const n = 1800, p = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    const r = 600 + Math.random() * 900, t = Math.random() * Math.PI * 2, u = Math.acos(2 * Math.random() - 1);
    p.set([r * Math.sin(u) * Math.cos(t) - 50, r * Math.sin(u) * Math.sin(t), r * Math.cos(u)], i * 3);
  }
  g.setAttribute("position", new THREE.BufferAttribute(p, 3));
  scene.add(new THREE.Points(g, new THREE.PointsMaterial({ color: 0x8899bb, size: 1.6, sizeAttenuation: true, fog: false })));
}

const GEOMS = {
  theme: new THREE.SphereGeometry(1.5, 24, 16), concept: new THREE.SphereGeometry(0.8, 18, 12),
  event: new THREE.OctahedronGeometry(1.0), actor: new THREE.BoxGeometry(1.2, 1.2, 1.2),
  theory: new THREE.IcosahedronGeometry(1.0), evidence: new THREE.TetrahedronGeometry(1.15),
  question: new THREE.TorusGeometry(0.75, 0.26, 10, 24), method: new THREE.DodecahedronGeometry(0.85),
};

const worldGroup = new THREE.Group();
scene.add(worldGroup);
const axisGroup = new THREE.Group();
scene.add(axisGroup);
const edgeGroup = new THREE.Group();
scene.add(edgeGroup);
const treeGroup = new THREE.Group();
scene.add(treeGroup);
const domainGroup = new THREE.Group();
scene.add(domainGroup);

// ---------------------------------------------------------------- 読み込み
fetch("viewer/data/graph.json", { cache: "no-store" })
  .then((r) => r.json())
  .then(init)
  .catch((e) => { $("#loading").innerHTML = "読み込みに失敗しました<br><small>" + esc(e.message) + "</small>"; });

function init(g) {
  G = g;
  G.nodes.forEach((n) => (byId[n.id] = n));
  $("#ver").textContent = `地図 v${G.map_version}｜${G.stats.nodes} ノード｜${G.stats.edges} 関係`;
  buildAxis();
  buildDomains();
  buildNodes();
  buildTree();
  buildLegend();
  buildSearch();
  applyMode(false);
  $("#loading").classList.add("hidden");
  setTimeout(() => ($("#hint").style.opacity = 0), 6000);
  const hash = decodeURIComponent(location.hash.slice(1));
  if (byId[hash]) select(hash, true);
  animate();
}

function buildAxis() {
  const mat = new THREE.LineBasicMaterial({ color: 0x334155 });
  const geo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(xOfYa(13.8e9) - 4, 0, 0), new THREE.Vector3(xOfYa(-30) + 2, 0, 0)]);
  axisGroup.add(new THREE.Line(geo, mat));
  for (const [ya, lab] of TICKS) {
    const el = document.createElement("div");
    el.className = "tick";
    el.textContent = lab;
    const o = new CSS2DObject(el);
    o.position.set(xOfYa(ya), 0, 0);
    o.center.set(0.5, -0.6);
    axisGroup.add(o);
    const ring = new THREE.Mesh(new THREE.RingGeometry(0.0, 0.25, 12), new THREE.MeshBasicMaterial({ color: 0x64748b }));
    ring.position.set(xOfYa(ya), 0, 0);
    ring.rotation.y = Math.PI / 2;
    axisGroup.add(ring);
  }
}

function domainAnchor(i, m) {
  const sector = (2 * Math.PI) / 10, th = sector * (i + 0.5);
  return m === "cyl" ? new THREE.Vector3(-108, 18 * Math.cos(th), 18 * Math.sin(th)) : new THREE.Vector3(-108, 22, (i - 4.5) * 9);
}

function buildDomains() {
  G.domains.forEach((d, i) => {
    const el = document.createElement("div");
    el.className = "dlbl";
    el.textContent = `${d.id} ${d.ja}`;
    const o = new CSS2DObject(el);
    o.userData = { i };
    domainGroup.add(o);
  });
  // 円筒モードの領域の境界線
  const mat = new THREE.LineBasicMaterial({ color: 0x1e293b, transparent: true, opacity: 0.6 });
  for (let i = 0; i < 10; i++) {
    const th = ((2 * Math.PI) / 10) * i;
    const pts = [new THREE.Vector3(-104, 16 * Math.cos(th), 16 * Math.sin(th)), new THREE.Vector3(18, 16 * Math.cos(th), 16 * Math.sin(th))];
    const l = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), mat);
    l.userData.cylOnly = true;
    domainGroup.add(l);
  }
}

function buildNodes() {
  for (const n of G.nodes) {
    const col = new THREE.Color(LEVEL_COLORS[n.understanding.level] || LEVEL_COLORS[0]);
    const mat = new THREE.MeshStandardMaterial({ color: col, emissive: col, emissiveIntensity: n.understanding.status === "presented" ? 0.55 : 0.3,
      roughness: 0.5, metalness: 0.1, transparent: true, opacity: 1 });
    const m = new THREE.Mesh(GEOMS[n.type] || GEOMS.concept, mat);
    m.userData.id = n.id;
    m.position.fromArray(n.pos.cyl);
    worldGroup.add(m);
    meshes.push(m);
    const el = document.createElement("div");
    el.className = "lbl l" + n.level;
    el.textContent = n.title.ja;
    const o = new CSS2DObject(el);
    o.center.set(0.5, 1.6);   // ノードの少し上に表示（CSSのtransformは上書きされるため center で指定）
    m.add(o);
    labels[n.id] = o;
  }
}

function buildTree() {
  clearGroup(treeGroup);
  const pts = [];
  for (const n of G.nodes) {
    if (!n.parent || !byId[n.parent]) continue;
    pts.push(posOf(n.id), posOf(n.parent));
  }
  const g = new THREE.BufferGeometry().setFromPoints(pts);
  treeGroup.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: 0x1e3a5f, transparent: true, opacity: 0.35 })));
}

const posOf = (id) => meshes.find((m) => m.userData.id === id).position.clone();

// ---------------------------------------------------------------- 表示切替
function applyMode(animateIt = true) {
  const from = meshes.map((m) => m.position.clone());
  const to = meshes.map((m) => new THREE.Vector3().fromArray(byId[m.userData.id].pos[mode]));
  const axFrom = axisGroup.position.clone();
  const axTo = mode === "cyl" ? new THREE.Vector3(0, 0, 0) : new THREE.Vector3(0, -12, 50);
  domainGroup.children.forEach((c) => { if (c.userData.cylOnly) c.visible = mode === "cyl"; });
  domainGroup.children.filter((c) => c.isCSS2DObject).forEach((c) => c.position.copy(domainAnchor(c.userData.i, mode)));
  $("#btn-mode").textContent = mode === "cyl" ? "展開" : "円筒";
  if (!animateIt) {
    meshes.forEach((m, i) => m.position.copy(to[i]));
    axisGroup.position.copy(axTo);
    buildTree();
    refreshEdges();
    return;
  }
  const t0 = performance.now();
  modeTween = (now) => {
    const k = Math.min(1, (now - t0) / 1000), e = k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
    meshes.forEach((m, i) => m.position.lerpVectors(from[i], to[i], e));
    axisGroup.position.lerpVectors(axFrom, axTo, e);
    if (k >= 1) { modeTween = null; buildTree(); refreshEdges(); }
  };
  clearGroup(treeGroup);
  clearGroup(edgeGroup);
}

$("#btn-mode").onclick = () => { mode = mode === "cyl" ? "flat" : "cyl"; applyMode(true); };
$("#btn-legend").onclick = () => { $("#legend").classList.toggle("hidden"); $("#search").classList.add("hidden"); };
$("#btn-search").onclick = () => {
  $("#search").classList.toggle("hidden");
  $("#legend").classList.add("hidden");
  if (!$("#search").classList.contains("hidden")) $("#q").focus();
};

// ---------------------------------------------------------------- 選択・詳細パネル
const ray = new THREE.Raycaster();
const ptr = new THREE.Vector2();
let down = null, activePointers = 0, multiTouch = false;
renderer.domElement.addEventListener("pointerdown", (e) => {
  activePointers++;
  if (activePointers > 1) multiTouch = true;
  down = { x: e.clientX, y: e.clientY, t: performance.now() };
});
const pointerEnd = () => { activePointers = Math.max(0, activePointers - 1); };
renderer.domElement.addEventListener("pointercancel", () => { pointerEnd(); multiTouch = activePointers > 0; });
renderer.domElement.addEventListener("pointerup", (e) => {
  pointerEnd();
  const wasMulti = multiTouch;
  if (activePointers === 0) multiTouch = false;
  if (wasMulti || !down || performance.now() - down.t > 600 || Math.hypot(e.clientX - down.x, e.clientY - down.y) > 8) return;
  ptr.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
  ray.setFromCamera(ptr, camera);
  const hit = ray.intersectObjects(meshes.filter((m) => m.visible), false)[0];
  if (hit) select(hit.object.userData.id, false);
});

function select(id, fly) {
  selected = id;
  history.replaceState(null, "", "#" + encodeURIComponent(id));
  meshes.forEach((m) => {
    const rel = id === m.userData.id || G.edges.some((e) => (e.from === id && e.to === m.userData.id) || (e.to === id && e.from === m.userData.id));
    m.material.opacity = rel ? 1 : 0.25;
    m.scale.setScalar(m.userData.id === id ? 1.7 : 1);
  });
  Object.entries(labels).forEach(([k, o]) => o.element.classList.toggle("sel", k === id));
  refreshEdges();
  renderPanel(byId[id]);
  if (fly) flyTo(id);
}

function clearSelection() {
  selected = null;
  history.replaceState(null, "", location.pathname);
  meshes.forEach((m) => { m.material.opacity = 1; m.scale.setScalar(1); });
  Object.values(labels).forEach((o) => o.element.classList.remove("sel"));
  clearGroup(edgeGroup);
  $("#panel").classList.add("hidden");
  setOffset(false);
}

// 下からせり上がるパネルで選択ノードが隠れないよう、描画の中心を画面上部へずらす
function setOffset(on) {
  if (on && innerWidth < 900) camera.setViewOffset(innerWidth, innerHeight, 0, innerHeight * 0.28, innerWidth, innerHeight);
  else camera.clearViewOffset();
}
$("#panel-close").onclick = clearSelection;

function refreshEdges() {
  clearGroup(edgeGroup);
  if (!selected) return;
  for (const e of G.edges) {
    if (e.from !== selected && e.to !== selected) continue;
    const a = posOf(e.from), b = posOf(e.to);
    const mid = a.clone().add(b).multiplyScalar(0.5);
    mid.add(mid.clone().setX(0).normalize().multiplyScalar(4));
    const curve = new THREE.QuadraticBezierCurve3(a, mid, b);
    const g = new THREE.BufferGeometry().setFromPoints(curve.getPoints(24));
    const mat = new THREE.LineBasicMaterial({ color: EDGE_COLORS[e.type] || 0x94a3b8, transparent: true, opacity: 0.9 });
    edgeGroup.add(new THREE.Line(g, mat));
  }
}

function flyTo(id) {
  // 表示切替の途中なら、移動先の座標で飛ぶ
  const n = byId[id];
  const target = modeTween ? new THREE.Vector3().fromArray(n.pos[mode]) : posOf(id);
  const dir = camera.position.clone().sub(controls.target).normalize();
  const endPos = target.clone().add(dir.multiplyScalar(38));
  const p0 = camera.position.clone(), t0c = controls.target.clone(), t0 = performance.now();
  camTween = (now) => {
    const k = Math.min(1, (now - t0) / 900), e = 1 - Math.pow(1 - k, 3);
    camera.position.lerpVectors(p0, endPos, e);
    controls.target.lerpVectors(t0c, target, e);
    if (k >= 1) camTween = null;
  };
}

function renderPanel(n) {
  const lv = n.understanding.level;
  const bars = LEVEL_COLORS.slice(1).map((c, i) => `<i style="background:${i < lv ? c : "#1f2937"}"></i>`).join("");
  const doms = n.domains.map((d) => G.domains.find((x) => x.id === d)).map((d) => `<span class="chip">${d.id} ${esc(d.ja)}</span>`).join("");
  const out = G.edges.filter((e) => e.from === n.id), inc = G.edges.filter((e) => e.to === n.id);
  const relItem = (e, other, dir) => `<li><span class="rel-type">${dir === "out" ? "→" : "←"} ${EDGE_JA[e.type] || e.type}</span>` +
    `<span class="rel" data-id="${other}">${esc(byId[other]?.title.ja || other)}</span>` +
    ` <span class="chip ep ep-${e.epistemic}" style="font-size:10px;padding:1px 6px">${EP_JA[e.epistemic]}</span>` +
    (e.note ? `<div class="small">${esc(e.note)}</div>` : "") + "</li>";
  const children = G.nodes.filter((x) => x.parent === n.id);
  const srcs = n.sources.map((s) => `<li>${safeUrl(s.url) ? `<a href="${esc(safeUrl(s.url))}" target="_blank" rel="noopener">${esc(s.title)}</a>` : esc(s.title)}` +
    (s.existence === "verified" ? "" : ` <span class="small">［実在未確認］</span>`) + "</li>").join("");
  const persp = (n.perspectives || []).map((p) => `<li><b>${esc(p.label)}</b>：${esc(p.view)}</li>`).join("");
  const sess = n.curriculum.map((c) => {
    const s = G.sessions[c];
    const pdfs = (s?.lessons || []).filter((f) => /^output\/[\w./-]+\.pdf$/.test(f))
      .map((f, i, a) => ` <a href="${esc(f)}" target="_blank" rel="noopener">PDF${a.length > 1 ? "（" + "前後"[i] + "編）" : ""}</a>`).join("");
    return `<li>${esc(c)} ${esc(s?.title || "")}${pdfs}</li>`;
  }).join("");
  $("#panel-body").innerHTML = `
    <h2>${esc(n.title.ja)}</h2><div class="en">${esc(n.title.en || "")}</div>
    <div class="chips">
      <span class="chip">${TYPE_JA[n.type]}</span>
      <span class="chip ep ep-${n.epistemic}">${EP_JA[n.epistemic]}</span>
      <span class="chip">${CONF_JA[n.confidence]}</span>
      ${n.time ? `<span class="chip">${esc(n.time.label)}</span>` : `<span class="chip">時間を持たない</span>`}
      <span class="chip">${n.verification === "verified" ? "検証済み" : n.verification === "pending" ? "検証待ち" : "未検証"}</span>
    </div>
    <p>${esc(n.summary)}</p>
    ${n.time?.uncertainty ? `<p class="small">不確実性：${esc(n.time.uncertainty)}</p>` : ""}
    ${n.body ? `<p>${esc(n.body)}</p>` : ""}
    ${persp ? `<h3>別の見方</h3><ul>${persp}</ul>` : ""}
    <h3>あなたの理解</h3>
    <div class="ulevel">${bars}</div>
    <div class="small">${LEVEL_NAMES[lv]}（目標 L${n.target_level}）${n.understanding.status === "presented" ? "｜講義提示済み・未評価" : n.understanding.status === "assessed" ? "｜評価済み" : ""}</div>
    <h3>領域</h3><div class="chips">${doms}</div>
    ${n.parent ? `<h3>上位</h3><ul><li><span class="rel" data-id="${n.parent}">${esc(byId[n.parent]?.title.ja)}</span></li></ul>` : ""}
    ${children.length ? `<h3>下位（${children.length}）</h3><ul>${children.map((c) => `<li><span class="rel" data-id="${c.id}">${esc(c.title.ja)}</span></li>`).join("")}</ul>` : ""}
    ${out.length + inc.length ? `<h3>関係（${out.length + inc.length}）</h3><ul>${out.map((e) => relItem(e, e.to, "out")).join("")}${inc.map((e) => relItem(e, e.from, "in")).join("")}</ul>` : ""}
    ${srcs ? `<h3>出典</h3><ul>${srcs}</ul>` : `<h3>出典</h3><p class="small">未登録（今後のサイクルで調査・検証）</p>`}
    ${sess ? `<h3>カリキュラム</h3><ul>${sess}</ul>` : ""}
    <p class="small">ID：${esc(n.id)}</p>`;
  $("#panel").classList.remove("hidden");
  $("#panel").scrollTop = 0;
  setOffset(true);
  $("#panel-body").querySelectorAll(".rel").forEach((el) => (el.onclick = () => select(el.dataset.id, true)));
}

// ---------------------------------------------------------------- 検索・凡例
function buildSearch() {
  const sel = $("#f-domain");
  G.domains.forEach((d) => sel.insertAdjacentHTML("beforeend", `<option value="${d.id}">${d.id} ${esc(d.ja)}</option>`));
  const run = () => {
    const q = $("#q").value.trim().toLowerCase(), dom = sel.value;
    const hits = G.nodes.filter((n) => (!dom || n.domains.includes(dom)) &&
      (!q || n.title.ja.toLowerCase().includes(q) || (n.title.en || "").toLowerCase().includes(q) || n.summary.toLowerCase().includes(q) || n.id.includes(q)))
      .slice(0, 40);
    $("#results").innerHTML = hits.map((n) => `<li data-id="${n.id}">${esc(n.title.ja)}<small>${TYPE_JA[n.type]}・${EP_JA[n.epistemic]}</small></li>`).join("");
    $("#results").querySelectorAll("li").forEach((li) => (li.onclick = () => { $("#search").classList.add("hidden"); select(li.dataset.id, true); }));
    // 領域フィルタは3D上でも反映
    meshes.forEach((m) => (m.visible = !dom || byId[m.userData.id].domains.includes(dom)));
  };
  $("#q").addEventListener("input", run);
  sel.addEventListener("change", run);
  run();
}

function buildLegend() {
  $("#lg-levels").innerHTML = LEVEL_NAMES.map((t, i) => `<div class="lg-row"><span class="sw" style="background:${LEVEL_COLORS[i]}"></span>${t}</div>`).join("") +
    `<div class="small">明るく光るノード＝講義提示済み・未評価</div>`;
  const shapes = { theme: "大きい球", concept: "球", event: "八面体", actor: "立方体", theory: "二十面体", evidence: "四面体", question: "リング", method: "十二面体" };
  $("#lg-types").innerHTML = Object.entries(shapes).map(([k, v]) => `<div class="lg-row"><span class="chip">${TYPE_JA[k]}</span>${v}</div>`).join("");
}

// ---------------------------------------------------------------- 意味的ズーム（DOC-03 §3.4）
// 距離で表示する詳細度を決め、さらに画面上で重なるラベルは優先度の低いものから隠す。
const tmp = new THREE.Vector3();
let labelTick = 0;
function updateLabels() {
  if (labelTick++ % 3) return;            // 3フレームに1回で十分
  const d = camera.position.distanceTo(controls.target);
  const maxLevel = d > 190 ? 1 : d > 95 ? 2 : d > 45 ? 3 : 4;
  const cand = [];
  for (const m of meshes) {
    const n = byId[m.userData.id], o = labels[n.id];
    o.visible = false;
    if (!m.visible || (n.level > maxLevel && n.id !== selected)) continue;
    m.getWorldPosition(tmp);
    const dist = camera.position.distanceTo(tmp);
    tmp.project(camera);
    if (tmp.z > 1 || Math.abs(tmp.x) > 1.1 || Math.abs(tmp.y) > 1.1) continue;
    const sx = (tmp.x + 1) / 2 * innerWidth, sy = (1 - tmp.y) / 2 * innerHeight - 16;
    const fs = n.level === 2 ? 13 : 11;
    const w = Math.min(n.title.ja.length, 22) * fs, h = fs + 5;
    const pri = (n.id === selected ? -100 : 0) + n.level * 10 + dist / 50;
    cand.push({ o, pri, r: [sx - w / 2, sy - h / 2, sx + w / 2, sy + h / 2] });
  }
  cand.sort((a, b) => a.pri - b.pri);
  const placed = [];
  for (const c of cand) {
    if (placed.length >= 70) break;
    const [a1, b1, a2, b2] = c.r;
    if (placed.some(([x1, y1, x2, y2]) => a1 < x2 && a2 > x1 && b1 < y2 && b2 > y1)) continue;
    placed.push(c.r);
    c.o.visible = true;
  }
}

// ---------------------------------------------------------------- ループ
function animate(now) {
  requestAnimationFrame(animate);
  const t = now ?? performance.now();
  if (modeTween) modeTween(t);
  if (camTween) camTween(t);
  controls.update();
  updateLabels();
  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
}

addEventListener("resize", () => {
  const p = innerHeight > innerWidth;
  if (p !== portrait) { portrait = p; makeControls(true); }
  camera.aspect = innerWidth / innerHeight;
  setOffset(!$("#panel").classList.contains("hidden"));
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
  labelRenderer.setSize(innerWidth, innerHeight);
});
