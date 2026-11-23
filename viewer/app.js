// The Universal — 3Dビューア v2（DOC-02 §3-6、DOC-03 §3・§3.6・§7、ADR-0004）
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { CSS2DRenderer, CSS2DObject } from "three/addons/renderers/CSS2DRenderer.js";

// ---------------------------------------------------------------- 定数
// テーマごとの色（DOC-03 §7.1）。LEVEL_COLORS と EP は applyTheme() で差し替える
const PALETTES = {
  dark: { bg: 0x0b0b0b, line: 0xf2efe8, lineCss: "#f2efe8", presented: "#a8a297", ringOpacity: 0.07, linkOpacity: 0.13, dimOpacity: 0.15,
    levels: ["#5c5c5c", "#e9dcc0", "#e6be96", "#e0966d", "#d46a45", "#c8402a"],
    ep: { fact: "#e8e4da", theory: "#7f9bbf", debate: "#c8402a", normative: "#a28bbd", hypothesis: "#8fab8a", unknown: "#8d887e" } },
  light: { bg: 0xffffff, line: 0x141414, lineCss: "#141414", presented: "#7a756c", ringOpacity: 0.10, linkOpacity: 0.18, dimOpacity: 0.3,
    levels: ["#9e9a92", "#c9b48a", "#d39a6c", "#d27a52", "#c95a3a", "#b8361f"],
    ep: { fact: "#1a1a1a", theory: "#2f4b6e", debate: "#c8402a", normative: "#6b4e8a", hypothesis: "#4d6b4a", unknown: "#7a7a7a" } },
};
let PAL = PALETTES[document.documentElement.dataset.theme === "light" ? "light" : "dark"];
let LEVEL_COLORS = PAL.levels;
const LEVEL_NAMES = ["未学習", "認知", "説明できる", "専門的に理解", "統合・応用", "批判的に検証"];
const TYPE_EN = { theme: "Theme", concept: "Concept", event: "Event", actor: "Actor", theory: "Theory", evidence: "Evidence", question: "Question", method: "Method" };
const TYPE_JA = { theme: "テーマ", concept: "概念", event: "出来事", actor: "主体", theory: "理論", evidence: "証拠", question: "問い", method: "思考法" };
const EP_TEXT = { fact: ["事実", "観測・測定・史料で確認できる"], theory: ["理論", "強い証拠に支えられた説明"],
  debate: ["論争", "学説・解釈が競合している"], normative: ["規範", "価値・望ましさの問題"],
  hypothesis: ["仮説", "予測・未検証の説明"], unknown: ["未知", "現時点で確定できない"] };
let EP = {};
const setEP = () => { EP = Object.fromEntries(Object.entries(EP_TEXT).map(([k, [ja, d]]) => [k, [ja, PAL.ep[k], d]])); };
setEP();

// 設定（端末に保存。使えない環境では保存しない）
const memo = {};   // 保存できない環境でも、開いている間は設定を保つ
const store = {
  get(k, d) { if (k in memo) return memo[k]; try { return localStorage.getItem("tu." + k) || d; } catch { return d; } },
  set(k, v) { memo[k] = v; try { localStorage.setItem("tu." + k, v); } catch { /* 保存できない環境 */ } },
};
const CONF_EN = { high: "Confidence high", medium: "Confidence medium", low: "Confidence low" };
const EDGE_EN = { causes: "causes", enables: "enables", requires: "requires", part_of: "part of", precedes: "precedes",
  supports: "supports", contradicts: "contradicts", analogous: "analogous", instance_of: "instance of", applies: "applies",
  evidence_for: "evidence for", raises: "raises", addresses: "addresses" };
const EDGE_JA = { causes: "原因となる", enables: "可能にする", requires: "前提とする", part_of: "部分である", precedes: "先行する",
  supports: "支持する", contradicts: "対立する", analogous: "類比", instance_of: "事例である", applies: "適用する",
  evidence_for: "証拠となる", raises: "問いを生む", addresses: "答えようとする" };
const STATUS_EN = { "not-started": "Not started", presented: "Presented", "in-progress": "In progress", assessed: "Assessed", done: "Done",
  open: "Open", exploring: "Exploring", answered: "Answered", "open-problem": "Open problem" };
const SCALE_EN = { 1: "DOMAINS", 2: "THEMES", 3: "CONCEPTS", 4: "DETAILS" };
const TICKS = [[13.8e9, "13.8 GYR"], [1e9, "1 GYR"], [1e8, "100 MYR"], [1e7, "10 MYR"], [1e6, "1 MYR"],
  [1e5, "100 KYR"], [1e4, "10 KYR"], [1e3, "1 KYR"], [1e2, "100 YR"], [0, "NOW"], [-30, "+30 YR"]];
const xOfYa = (ya) => (ya >= 0 ? -10 * Math.log10(1 + ya) : 10 * Math.log10(1 + Math.abs(ya)));

const $ = (s) => document.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const safeUrl = (u) => (/^https?:\/\//.test(u || "") ? u : "");
const safePdf = (f) => (/^output\/[\w./-]+\.pdf$/.test(f || "") ? f : "");

let G, byId = {}, mode = ["cyl", "flat", "plane"].includes(store.get("view", "cyl")) ? store.get("view", "cyl") : "cyl", selected = null;
const meshes = [], labels = {};
let modeTween = null, camTween = null;

// ---------------------------------------------------------------- シーン
const scene = new THREE.Scene();
scene.fog = new THREE.Fog(PAL.bg, 120, 420);
const camera = new THREE.PerspectiveCamera(46, innerWidth / innerHeight, 0.1, 3000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.setClearColor(PAL.bg);
$("#scene").appendChild(renderer.domElement);
const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize(innerWidth, innerHeight);
Object.assign(labelRenderer.domElement.style, { position: "absolute", top: "0", left: "0", pointerEvents: "none" });
$("#scene").appendChild(labelRenderer.domElement);

// 縦長の画面（iPhone）では時間軸を縦に置く（下が過去、上が現在）。OrbitControls は作成時の camera.up を使うため、向きが変わったら作り直す。
let portrait = innerHeight > innerWidth;
let controls;
function makeControls(resetView) {
  const target = controls ? controls.target.clone() : new THREE.Vector3(-45, 0, 0);
  controls?.dispose();
  camera.up.set(...(portrait ? [1, 0, 0] : [0, 1, 0]));
  if (resetView) camera.position.set(...(portrait ? [-45, 80, 160] : [-42, 42, 112]));
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.minDistance = 8;
  controls.maxDistance = 420;
  controls.target.copy(target);
  setPlaneControls(mode === "plane");
  controls.addEventListener("change", () => typeof wake === "function" && wake());
}
function setPlaneControls(on) {
  controls.enableRotate = !on;
  controls.mouseButtons.LEFT = on ? THREE.MOUSE.PAN : THREE.MOUSE.ROTATE;
  controls.touches.ONE = on ? THREE.TOUCH.PAN : THREE.TOUCH.ROTATE;
  controls.screenSpacePanning = true;
}
makeControls(true);

// 種類ごとのワイヤーフレームの形
const SHAPES = {
  theme: new THREE.IcosahedronGeometry(1.7, 1), concept: new THREE.IcosahedronGeometry(0.75, 0),
  event: new THREE.OctahedronGeometry(0.95), actor: new THREE.BoxGeometry(1.1, 1.1, 1.1),
  theory: new THREE.DodecahedronGeometry(0.95), evidence: new THREE.TetrahedronGeometry(1.1),
  question: new THREE.TorusGeometry(0.75, 0.12, 4, 20), method: starGeometry(0.85),
};
const EDGES = Object.fromEntries(Object.entries(SHAPES).map(([k, g]) => [k, new THREE.EdgesGeometry(g)]));
// 当たり判定は形によらず共通の見えない球で行う（細い形でもタップできるように）
const HIT_GEOM = new THREE.SphereGeometry(1.3, 10, 8);
const HIT_MAT = new THREE.MeshBasicMaterial({ visible: false });

// 思考法：2つの正四面体を組み合わせた星形（出来事の八面体と見分けるため）
function starGeometry(r) {
  const a = new THREE.TetrahedronGeometry(r).toNonIndexed();
  const b = new THREE.TetrahedronGeometry(r).toNonIndexed();
  b.rotateY(Math.PI / 2);
  b.rotateX(Math.PI);
  const pa = a.getAttribute("position").array, pb = b.getAttribute("position").array;
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute([...pa, ...pb], 3));
  return g;
}

const groups = {};
for (const k of ["nodes", "links", "hot", "layersCyl", "layersFlat", "layersPlane", "axis", "domains"]) { groups[k] = new THREE.Group(); scene.add(groups[k]); }

// ---------------------------------------------------------------- 読み込み
fetch("viewer/data/graph.json", { cache: "no-store" })
  .then((r) => r.json())
  .then(init)
  .catch((e) => { $("#loading").innerHTML = '<div class="wordmark">THE UNIVERSAL</div><small>' + esc(e.message) + "</small>"; });

function init(g) {
  G = g;
  G.nodes.forEach((n) => {
    byId[n.id] = n;
    const [x, y, z] = n.pos.flat;
    n.pos.plane = [x, -z + (y - 7) * 0.35, 0];   // DOC-03 §3.7
  });
  $("#ver").textContent = `MAP V${G.map_version} — ${G.stats.nodes} NODES — ${G.stats.edges} RELATIONS`;
  buildLayers();
  buildDomains();
  buildNodes();
  applyMode(false);
  if (mode === "plane") placeCamera(false);
  buildMenu();
  const mq = matchMedia("(prefers-color-scheme: light)");
  const onScheme = () => { if (store.get("theme", "auto") === "auto") applyTheme(); };
  mq.addEventListener ? mq.addEventListener("change", onScheme) : mq.addListener(onScheme);
  $("#loading").classList.add("hidden");
  const fromHash = () => { let h = ""; try { h = decodeURIComponent(location.hash.slice(1)); } catch { h = ""; } if (byId[h] && h !== selected) select(h, true); };
  fromHash();
  addEventListener("hashchange", fromHash);
  animate();
}

// ---------------------------------------------------------------- 時間の層（ワイヤーフレームの輪／枠）と時間軸
function buildLayers() {
  matRing = new THREE.LineBasicMaterial({ color: PAL.line, transparent: true, opacity: PAL.ringOpacity });
  matAxis = new THREE.LineBasicMaterial({ color: PAL.line, transparent: true, opacity: 0.22 });
  groups.axis.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-106, 0, 0), new THREE.Vector3(20, 0, 0)]), matAxis));
  for (const [ya, lab] of TICKS) {
    const x = xOfYa(ya);
    const pts = [];
    for (let k = 0; k <= 96; k++) { const a = (k / 96) * Math.PI * 2; pts.push(new THREE.Vector3(x, 17 * Math.cos(a), 17 * Math.sin(a))); }
    groups.layersCyl.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), matRing));
    const rect = [[-9, -46], [24, -46], [24, 46], [-9, 46], [-9, -46]].map(([y, z]) => new THREE.Vector3(x, y, z));
    groups.layersFlat.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(rect), matRing));
    // 2D：時間の目盛りの縦線
    groups.layersPlane.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(x, -45, 0), new THREE.Vector3(x, 45, 0)]), matRing));
    const el = document.createElement("div");
    el.className = "tick";
    el.textContent = lab;
    const o = new CSS2DObject(el);
    o.position.set(x, 0, 0);
    o.center.set(0.5, -0.8);
    groups.axis.add(o);
  }
}

function domainAnchor(i, m) {
  const th = ((2 * Math.PI) / 10) * (i + 0.5);
  if (m === "plane") return new THREE.Vector3(-110, -(i - 4.5) * 9, 0);
  return m === "cyl" ? new THREE.Vector3(-110, 19 * Math.cos(th), 19 * Math.sin(th)) : new THREE.Vector3(-110, 26, (i - 4.5) * 9);
}
let matRing, matAxis;

function buildPlaneLanes() {
  // 2D：レーンの境界線（D01〜D10）
  for (let i = 0; i <= 10; i++) {
    const y = 45 - i * 9;
    groups.layersPlane.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-106, y, 0), new THREE.Vector3(20, y, 0)]), matRing));
  }
}

function buildDomains() {
  buildPlaneLanes();
  G.domains.forEach((d, i) => {
    const el = document.createElement("div");
    el.className = "dlbl";
    el.innerHTML = `<b>${esc(d.id)}</b><span>${esc(d.ja)}</span>`;
    const o = new CSS2DObject(el);
    o.userData = { i };
    groups.domains.add(o);
  });
}

// ---------------------------------------------------------------- ノード
function buildNodes() {
  for (const n of G.nodes) {
    const base = new THREE.Color(nodeColor(n));
    // 当たり判定用の面（ほぼ透明）＋ワイヤーフレーム
    const hit = new THREE.Mesh(HIT_GEOM, HIT_MAT);
    const wire = new THREE.LineSegments(EDGES[n.type] || EDGES.concept, new THREE.LineBasicMaterial({ color: base, transparent: true, opacity: 0.95 }));
    wire.rotation.set((n.id.length * 0.37) % 3, (n.id.length * 0.61) % 3, 0);
    hit.add(wire);
    hit.userData = { id: n.id, wire };
    hit.position.fromArray(n.pos.cyl);
    groups.nodes.add(hit);
    meshes.push(hit);
    const el = document.createElement("div");
    el.className = "lbl l" + n.level;
    el.textContent = n.title.ja;
    const o = new CSS2DObject(el);
    o.center.set(0.5, 1.7);
    hit.add(o);
    labels[n.id] = o;
  }
}
function nodeColor(n) {
  return n.understanding.status === "presented" && n.understanding.level === 0 ? PAL.presented : LEVEL_COLORS[n.understanding.level] || LEVEL_COLORS[0];
}

// テーマの適用（DOC-03 §7.1）：CSS変数と3Dの色を差し替える
function applyTheme() {
  const s = store.get("theme", "auto");
  const dark = s === "dark" || (s === "auto" && !matchMedia("(prefers-color-scheme: light)").matches);
  const name = dark ? "dark" : "light";
  document.documentElement.dataset.theme = name;
  document.querySelector('meta[name="theme-color"]')?.setAttribute("content", dark ? "#0b0b0b" : "#ffffff");
  PAL = PALETTES[name];
  LEVEL_COLORS = PAL.levels;
  setEP();
  renderer.setClearColor(PAL.bg);
  scene.fog.color.set(PAL.bg);
  matRing?.color.set(PAL.line); if (matRing) matRing.opacity = PAL.ringOpacity;
  matAxis?.color.set(PAL.line);
  meshes.forEach((m) => m.userData.wire.material.color.set(nodeColor(byId[m.userData.id])));
  buildLinks();
  buildHot();
  if (selected) renderPanel(byId[selected]);
  const on = document.querySelector(".sections button.on")?.dataset.sec;
  if (on && !$("#menu").classList.contains("hidden")) showSection(on, $("#menu-body").classList.contains("reading"));
  wake();
}

const meshOf = (id) => meshes.find((m) => m.userData.id === id);
const posOf = (id) => meshOf(id).position.clone();

// グループ内の線を外すとき、GPUメモリも解放する
function clearGroup(g) {
  for (const c of [...g.children]) { c.geometry?.dispose(); c.material?.dispose(); g.remove(c); }
}

function curvePoints(a, b, segs = 14) {
  const mid = a.clone().add(b).multiplyScalar(0.5);
  const off = mid.clone().setX(0);
  if (off.lengthSq() < 1e-6) off.set(0, 1, 0);
  mid.add(off.normalize().multiplyScalar(3 + a.distanceTo(b) * 0.08));
  return new THREE.QuadraticBezierCurve3(a, mid, b).getPoints(segs);
}

// すべての関係と親子関係を、極細・低不透明度の線で描く（密度で構造を見せる）
function buildLinks() {
  clearGroup(groups.links);
  const pos = [];
  const push = (a, b) => { const p = curvePoints(a, b); for (let i = 0; i < p.length - 1; i++) pos.push(p[i].x, p[i].y, p[i].z, p[i + 1].x, p[i + 1].y, p[i + 1].z); };
  for (const e of G.edges) push(posOf(e.from), posOf(e.to));
  for (const n of G.nodes) if (n.parent && byId[n.parent]) push(posOf(n.id), posOf(n.parent));
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3));
  groups.links.add(new THREE.LineSegments(g, new THREE.LineBasicMaterial({ color: PAL.line, transparent: true, opacity: selected ? 0.04 : PAL.linkOpacity })));
}

function buildHot() {
  clearGroup(groups.hot);
  if (!selected) return;
  for (const e of G.edges) {
    if (e.from !== selected && e.to !== selected) continue;
    const g = new THREE.BufferGeometry().setFromPoints(curvePoints(posOf(e.from), posOf(e.to), 28));
    const col = e.type === "contradicts" ? 0xc8402a : PAL.line;
    groups.hot.add(new THREE.Line(g, new THREE.LineBasicMaterial({ color: col, transparent: true, opacity: 0.9 })));
  }
  const n = byId[selected];
  if (n.parent && byId[n.parent]) {
    const g = new THREE.BufferGeometry().setFromPoints(curvePoints(posOf(n.id), posOf(n.parent), 20));
    groups.hot.add(new THREE.Line(g, new THREE.LineDashedMaterial({ color: PAL.line, dashSize: 0.8, gapSize: 0.6, transparent: true, opacity: 0.6 })));
    groups.hot.children.at(-1).computeLineDistances();
  }
}

// ---------------------------------------------------------------- 表示切替
function applyMode(animateIt = true) {
  wake();
  const from = meshes.map((m) => m.position.clone());
  const to = meshes.map((m) => new THREE.Vector3().fromArray(byId[m.userData.id].pos[mode]));
  const axFrom = groups.axis.position.clone();
  const axTo = mode === "cyl" ? new THREE.Vector3(0, 0, 0) : mode === "plane" ? new THREE.Vector3(0, -49, 0) : new THREE.Vector3(0, -12, 50);
  groups.layersCyl.visible = mode === "cyl";
  groups.layersFlat.visible = mode === "flat";
  groups.layersPlane.visible = mode === "plane";
  setPlaneControls(mode === "plane");
  store.set("view", mode);
  document.querySelectorAll("[data-view]").forEach((b) => b.classList.toggle("on", b.dataset.view === mode));
  groups.domains.children.forEach((c) => c.position.copy(domainAnchor(c.userData.i, mode)));
  document.querySelectorAll("#foot [data-mode]").forEach((b) => b.classList.toggle("on", b.dataset.mode === mode));
  if (!animateIt) {
    meshes.forEach((m, i) => m.position.copy(to[i]));
    groups.axis.position.copy(axTo);
    buildLinks();
    buildHot();
    return;
  }
  clearGroup(groups.links);
  clearGroup(groups.hot);
  const t0 = performance.now();
  modeTween = (now) => {
    const k = Math.min(1, (now - t0) / 1000), e = k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
    meshes.forEach((m, i) => m.position.lerpVectors(from[i], to[i], e));
    groups.axis.position.lerpVectors(axFrom, axTo, e);
    if (k >= 1) { modeTween = null; buildLinks(); buildHot(); }
  };
}
function setView(m) {
  if (mode === m) return;
  const was = mode;
  mode = m;
  applyMode(true);
  if (m === "plane" || was === "plane") placeCamera(true);
}
document.querySelectorAll("#foot [data-mode]").forEach((b) => (b.onclick = () => setView(b.dataset.mode)));

// 表示に合わせた初期の視点。2Dは平面を真上から見る（DOC-03 §3.7）
function placeCamera(animateIt) {
  const target = new THREE.Vector3(-45, 0, 0);
  const end = mode === "plane" ? new THREE.Vector3(-45, 0, portrait ? 290 : 165)
    : new THREE.Vector3(...(portrait ? [-45, 80, 160] : [-42, 42, 112]));
  if (!animateIt) { camera.position.copy(end); controls.target.copy(target); controls.update(); return; }
  const p0 = camera.position.clone(), t0c = controls.target.clone(), t0 = performance.now();
  camTween = (now) => {
    const k = Math.min(1, (now - t0) / 1000), e = 1 - Math.pow(1 - k, 3);
    camera.position.lerpVectors(p0, end, e);
    controls.target.lerpVectors(t0c, target, e);
    if (k >= 1) camTween = null;
  };
}

// ---------------------------------------------------------------- 選択と詳細パネル
const ray = new THREE.Raycaster();
const ptr = new THREE.Vector2();
let down = null, activePointers = 0, multiTouch = false;
renderer.domElement.addEventListener("pointerdown", (e) => {
  activePointers++;
  if (activePointers > 1) multiTouch = true;
  down = { x: e.clientX, y: e.clientY, t: performance.now() };
});
renderer.domElement.addEventListener("pointercancel", () => { activePointers = Math.max(0, activePointers - 1); multiTouch = activePointers > 0; });
renderer.domElement.addEventListener("pointerup", (e) => {
  activePointers = Math.max(0, activePointers - 1);
  const wasMulti = multiTouch;
  if (activePointers === 0) multiTouch = false;
  if (wasMulti || !down || performance.now() - down.t > 600 || Math.hypot(e.clientX - down.x, e.clientY - down.y) > 8) return;
  ptr.set((e.clientX / innerWidth) * 2 - 1, -(e.clientY / innerHeight) * 2 + 1);
  ray.setFromCamera(ptr, camera);
  const hit = ray.intersectObjects(meshes.filter((m) => m.visible), false)[0];
  if (hit) select(hit.object.userData.id, false);
});

function related(id) {
  const s = new Set([id]);
  for (const e of G.edges) { if (e.from === id) s.add(e.to); if (e.to === id) s.add(e.from); }
  const n = byId[id];
  if (n.parent) s.add(n.parent);
  G.nodes.forEach((x) => { if (x.parent === id) s.add(x.id); });
  return s;
}

function select(id, fly) {
  wake();
  selected = id;
  history.replaceState(null, "", "#" + encodeURIComponent(id));
  const rel = related(id);
  meshes.forEach((m) => {
    const on = rel.has(m.userData.id);
    m.userData.wire.material.opacity = on ? 1 : PAL.dimOpacity;
    m.material.opacity = m.userData.id === id ? 0.35 : on ? 0.08 : 0.02;
    m.scale.setScalar(m.userData.id === id ? 1.8 : 1);
  });
  Object.entries(labels).forEach(([k, o]) => o.element.classList.toggle("sel", k === id));
  buildLinks();
  buildHot();
  renderPanel(byId[id]);
  if (fly) flyTo(id);
}

function clearSelection() {
  wake();
  selected = null;
  history.replaceState(null, "", location.pathname);
  meshes.forEach((m) => { m.userData.wire.material.opacity = 0.95; m.material.opacity = 0.08; m.scale.setScalar(1); });
  Object.values(labels).forEach((o) => o.element.classList.remove("sel"));
  buildLinks();
  clearGroup(groups.hot);
  $("#panel").classList.add("hidden");
  setOffset(false);
}
$("#panel-close").onclick = clearSelection;

// 下からせり上がるパネルで選択ノードが隠れないよう、描画の中心を画面上部へずらす
function setOffset(on) {
  if (on && innerWidth < 900) camera.setViewOffset(innerWidth, innerHeight, 0, innerHeight * 0.27, innerWidth, innerHeight);
  else if (on) camera.setViewOffset(innerWidth, innerHeight, 210, 0, innerWidth, innerHeight);
  else camera.clearViewOffset();
}

function flyTo(id) {
  const n = byId[id];
  const target = modeTween ? new THREE.Vector3().fromArray(n.pos[mode]) : posOf(id);
  const dir = mode === "plane" ? new THREE.Vector3(0, 0, 1) : camera.position.clone().sub(controls.target).normalize();
  const endPos = target.clone().add(dir.multiplyScalar(36));
  const p0 = camera.position.clone(), t0c = controls.target.clone(), t0 = performance.now();
  camTween = (now) => {
    const k = Math.min(1, (now - t0) / 1000), e = 1 - Math.pow(1 - k, 3);
    camera.position.lerpVectors(p0, endPos, e);
    controls.target.lerpVectors(t0c, target, e);
    if (k >= 1) camTween = null;
  };
}

function levelBar(lv) {
  return `<div class="levels">${LEVEL_COLORS.slice(1).map((c, i) => `<i style="background:${i < lv ? c : "var(--empty)"}"></i>`).join("")}</div>`;
}

function renderPanel(n) {
  const ep = EP[n.epistemic];
  const lv = n.understanding.level;
  const out = G.edges.filter((e) => e.from === n.id), inc = G.edges.filter((e) => e.to === n.id);
  const relItem = (e, other, dir) => `<li><span class="rt">${dir === "out" ? "→" : "←"} ${EDGE_EN[e.type] || e.type}</span>` +
    `<span class="rel" data-id="${esc(other)}">${esc(byId[other]?.title.ja || other)}</span>` +
    `<span class="tag" style="background:${EP[e.epistemic][1]}">${EP[e.epistemic][0]}</span>` +
    `<span class="note">${esc(EDGE_JA[e.type] || "")}${e.note ? "　" + esc(e.note) : ""}</span></li>`;
  const children = G.nodes.filter((x) => x.parent === n.id);
  const srcs = n.sources.map((s) => `<li>${safeUrl(s.url) ? `<a href="${esc(safeUrl(s.url))}" target="_blank" rel="noopener">${esc(s.title)}</a>` : esc(s.title)}` +
    (s.existence === "verified" ? "" : `<span class="note">実在未確認</span>`) + "</li>").join("");
  const persp = (n.perspectives || []).map((p) => `<li><span class="rt">${esc(p.label)}</span><span class="note" style="color:var(--ink2)">${esc(p.view)}</span></li>`).join("");
  const sess = n.curriculum.map((c) => {
    const s = G.sessions[c];
    const pdfs = (s?.lessons || []).map(safePdf).filter(Boolean)
      .map((f, i, a) => ` <a href="${esc(f)}" target="_blank" rel="noopener">${a.length > 1 ? "VOL. " + "AB"[i] : "PDF"}</a>`).join("");
    return `<li><span class="rt">${esc(c)}</span>${esc(s?.title || "")}${pdfs}</li>`;
  }).join("");
  const time = n.time ? esc(n.time.label) : "Timeless";
  const ver = { verified: "Verified", pending: "Pending", unverified: "Unverified" }[n.verification];
  $("#panel-body").innerHTML = `
    <div class="kick">${TYPE_EN[n.type]} — <span class="ep-dot" style="background:${ep[1]}"></span>${ep[0]} — ${CONF_EN[n.confidence]}</div>
    <h2>${esc(n.title.ja)}</h2><div class="en">${esc(n.title.en || "")}</div>
    <p>${esc(n.summary)}</p>
    ${n.body ? `<p>${esc(n.body)}</p>` : ""}
    <div class="kick">${time} — ${ver}</div>
    ${n.time?.uncertainty ? `<p class="small" style="margin-top:6px">不確実性：${esc(n.time.uncertainty)}</p>` : ""}
    <h3>UNDERSTANDING</h3>
    ${levelBar(lv)}
    <div class="small">L${lv} ${LEVEL_NAMES[lv]}　／　目標 L${n.target_level}${n.understanding.status === "presented" ? "　／　講義提示済み・未評価" : n.understanding.status === "assessed" ? "　／　評価済み" : ""}</div>
    ${persp ? `<h3>PERSPECTIVES</h3><ul>${persp}</ul>` : ""}
    <h3>LOCATION</h3><ul>
      <li><span class="rt">Domain</span>${n.domains.map((d) => esc(d + " " + (G.domains.find((x) => x.id === d)?.ja || ""))).join("、")}</li>
      ${n.parent ? `<li><span class="rt">Parent</span><span class="rel" data-id="${esc(n.parent)}">${esc(byId[n.parent]?.title.ja)}</span></li>` : ""}
    </ul>
    ${children.length ? `<h3>CHILDREN — ${children.length}</h3><ul>${children.map((c) => `<li><span class="rt">${TYPE_EN[c.type]}</span><span class="rel" data-id="${esc(c.id)}">${esc(c.title.ja)}</span></li>`).join("")}</ul>` : ""}
    ${out.length + inc.length ? `<h3>RELATIONS — ${out.length + inc.length}</h3><ul>${out.map((e) => relItem(e, e.to, "out")).join("")}${inc.map((e) => relItem(e, e.from, "in")).join("")}</ul>` : ""}
    <h3>SOURCES</h3>${srcs ? `<ul>${srcs}</ul>` : `<p class="small">未登録（今後のサイクルで調査・検証）</p>`}
    ${sess ? `<h3>LESSONS</h3><ul>${sess}</ul>` : ""}
    <p class="small" style="margin-top:22px;font-family:var(--mono);letter-spacing:.1em">${esc(n.id)}</p>`;
  $("#panel").classList.remove("hidden");
  $("#panel").scrollTop = 0;
  setOffset(true);
  $("#panel-body").querySelectorAll(".rel").forEach((el) => (el.onclick = () => select(el.dataset.id, true)));
}

// ---------------------------------------------------------------- メニュー（DOC-03 §3.6）
function openMenu(sec) {
  $("#menu").classList.remove("hidden");
  if (sec) showSection(sec, false);
}
function closeMenu() { $("#menu").classList.add("hidden"); wake(); }
$("#btn-menu").onclick = () => openMenu(document.querySelector(".sections button.on")?.dataset.sec || "index");
$("#menu-close").onclick = closeMenu;
const goNode = (id) => { closeMenu(); select(id, true); };
addEventListener("keydown", (e) => { if (e.key !== "Escape") return; if (!$("#menu").classList.contains("hidden")) closeMenu(); else if (selected) clearSelection(); });

function showSection(sec, reading = true) {
  document.querySelectorAll(".sections button").forEach((b) => b.classList.toggle("on", b.dataset.sec === sec));
  $("#menu-body").classList.toggle("reading", reading);
  const c = $("#menu-content");
  c.innerHTML = `<button class="textbtn back" id="back">← MENU</button>` + RENDER[sec]();
  c.scrollTop = 0;
  $("#back").onclick = () => $("#menu-body").classList.remove("reading");
  c.querySelectorAll("[data-node]").forEach((el) => (el.onclick = (ev) => { ev.stopPropagation(); goNode(el.dataset.node); }));
  c.querySelectorAll("[data-theme]").forEach((el) => (el.onclick = () => { store.set("theme", el.dataset.theme); applyTheme(); showSection("settings", $("#menu-body").classList.contains("reading")); }));
  c.querySelectorAll("[data-view]").forEach((el) => (el.onclick = () => { setView(el.dataset.view); showSection("settings", $("#menu-body").classList.contains("reading")); }));
}

function buildMenu() {
  document.querySelectorAll(".sections button").forEach((b) => (b.onclick = () => showSection(b.dataset.sec, true)));
  const run = () => {
    const q = $("#q").value.trim().toLowerCase(), dom = $("#f-domain").value;
    meshes.forEach((m) => (m.visible = !dom || byId[m.userData.id].domains.includes(dom)));
    groups.links.visible = !dom;
    wake();
    if (!q && !dom) { $("#search-results").innerHTML = ""; return; }
    const hits = G.nodes.filter((n) => (!dom || n.domains.includes(dom)) && (!q || n.title.ja.toLowerCase().includes(q) || (n.title.en || "").toLowerCase().includes(q) || n.summary.toLowerCase().includes(q) || n.id.includes(q))).slice(0, 40);
    $("#search-results").innerHTML = hits.length ? hits.map((n) => `<li data-node="${esc(n.id)}"><span class="v">${esc(n.title.ja)}</span><span class="r">${TYPE_EN[n.type]}</span></li>`).join("")
      : `<li><span class="v small">該当なし</span></li>`;
    $("#search-results").querySelectorAll("[data-node]").forEach((el) => (el.onclick = () => goNode(el.dataset.node)));
  };
  $("#q").addEventListener("input", run);
  G.domains.forEach((d) => $("#f-domain").insertAdjacentHTML("beforeend", `<option value="${esc(d.id)}">${esc(d.id)} ${esc(d.ja)}</option>`));
  $("#f-domain").addEventListener("change", run);
  showSection("index", false);
}

const lvSwatch = (n) => `<i class="lv" style="background:${nodeColor(n)}"></i>`;
const yaOf = (n) => (n.time ? n.time.start_ya : -1e12);

const RENDER = {
  index() {
    const kids = {};
    G.nodes.forEach((n) => { if (n.parent) (kids[n.parent] ||= []).push(n); });
    const sortT = (a, b) => yaOf(b) - yaOf(a) || a.title.ja.localeCompare(b.title.ja, "ja");
    const tree = (id, depth) => (kids[id] || []).sort(sortT).map((c) =>
      `<li class="d${Math.min(depth, 4)}" data-node="${esc(c.id)}">${lvSwatch(c)}<span>${esc(c.title.ja)}</span><span class="ty">${TYPE_EN[c.type]}</span></li>` + tree(c.id, depth + 1)).join("");
    const doms = G.domains.map((d) => {
      const themes = G.nodes.filter((n) => n.type === "theme" && n.domains[0] === d.id).sort(sortT);
      const count = G.nodes.filter((n) => n.domains[0] === d.id).length;
      return `<details class="dom"${d.id === "D01" ? " open" : ""}><summary><span class="id">${esc(d.id)}</span>
        <span class="ja">${esc(d.ja)}<span class="en">${esc(d.en)}</span></span><span class="n">${count}</span></summary>
        ${themes.map((t) => `<div class="theme"><div class="th" data-node="${esc(t.id)}"><span>${esc(t.title.ja)}</span><small>${esc(t.time ? t.time.label : "TIMELESS")}</small></div>
          <ul class="tree">${tree(t.id, 3)}</ul></div>`).join("")}</details>`;
    }).join("");
    return `<div class="sec-title">Index</div><p class="sec-lead">領域 → テーマ → 概念・出来事 → 詳細。行を選ぶと、地図のその場所へ移動します。左の小さな四角は理解レベルです。</p>${doms}`;
  },
  lessons() {
    return `<div class="sec-title">Lessons</div><p class="sec-lead">カリキュラムと教材。教材は前編・後編のPDFで届きます。</p>` +
      G.phases.map((ph) => `<div class="legend-block"><h4>${esc(ph.id)} — ${esc(ph.title)}</h4><ul class="rows">` +
        ph.sessions.map((s) => `<li><span class="k">${esc(s.id.split("-")[1])}</span><span class="v">${esc(s.title)}${s.lessons.map(safePdf).filter(Boolean).map((f, i, a) =>
          `<a href="${esc(f)}" target="_blank" rel="noopener">${a.length > 1 ? "VOL. " + "AB"[i] : "PDF"} ↗</a>`).join("")}</span><span class="r">${STATUS_EN[s.status] || s.status}</span></li>`).join("") +
        `</ul></div>`).join("");
  },
  reports() {
    return `<div class="sec-title">Reports</div><p class="sec-lead">サイクルごとの変更点レポート。知識の追加・訂正と、あなたの理解への影響をまとめています。</p><ul class="rows">` +
      G.reports.map((r) => `<li><span class="k">${esc(r.id)}</span><span class="v">${esc(r.title)}${safePdf(r.pdf) ? `<a href="${esc(r.pdf)}" target="_blank" rel="noopener">PDF ↗</a>` : ""}</span><span class="r">${esc(r.date)}</span></li>`).join("") + `</ul>`;
  },
  questions() {
    return `<div class="sec-title">Questions</div><p class="sec-lead">問いの在庫。あなたの疑問と未解明の問題が、学習計画の出発点になります。</p><ul class="rows">` +
      G.questions.map((q) => `<li${q.nodes[0] ? ` data-node="${esc(q.nodes[0])}"` : ""}><span class="k">${esc(q.id.replace("qq.", "Q"))}</span><span class="v">${esc(q.text)}</span><span class="r">${STATUS_EN[q.status] || q.status}</span></li>`).join("") + `</ul>`;
  },
  legend() {
    const icon = (t) => {
      const paths = { theme: "M17 4 L29 11 L29 23 L17 30 L5 23 L5 11 Z M17 4 L17 30 M5 11 L29 23 M29 11 L5 23", concept: "M17 8 L25 13 L25 21 L17 26 L9 21 L9 13 Z",
        event: "M17 5 L29 17 L17 29 L5 17 Z M5 17 L29 17", actor: "M9 9 H25 V25 H9 Z M9 9 L14 5 H30 L25 9 M25 25 L30 21 V5",
        theory: "M17 5 L28 13 L24 27 L10 27 L6 13 Z", evidence: "M17 5 L29 28 L5 28 Z", question: "M17 9 A8 8 0 1 1 16.9 9 Z", method: "M17 5 L27 24 L7 24 Z M17 29 L7 10 L27 10 Z" };
      return `<svg viewBox="0 0 34 34"><path d="${paths[t]}" fill="none" stroke="currentColor" stroke-width="1"/></svg>`;
    };
    return `<div class="sec-title">Legend</div><p class="sec-lead">地図の読み方。</p>
      <div class="legend-block"><h4>COLOR — あなたの理解レベル</h4>
        <div class="grad">${LEVEL_COLORS.map((c) => `<i style="background:${c}"></i>`).join("")}</div>
        <div class="grad" style="margin-top:6px">${LEVEL_NAMES.map((t, i) => `<span>L${i}<br>${t}</span>`).join("")}</div>
        <p style="margin-top:14px">色が濃い（赤い）ほど理解が深いことを表します。明るい灰色は「講義を受けたが、まだ評価していない」ノードです。レベルは、あなたの回答を評価したときだけ上がります。</p></div>
      <div class="legend-block"><h4>SHAPE — ノードの種類</h4>
        ${Object.keys(TYPE_EN).map((t) => `<div class="legend-row">${icon(t)}<span>${TYPE_JA[t]}　<span class="small">${TYPE_EN[t]}</span></span></div>`).join("")}</div>
      <div class="legend-block"><h4>LABEL — 認識の種類</h4>
        ${Object.values(EP).map(([ja, c, d]) => `<div class="legend-row"><span class="ep-chip" style="background:${c}">${ja}</span><span>${d}</span></div>`).join("")}
        <p style="margin-top:10px">関係の線のうち、赤は「対立する」関係です。</p></div>
      <div class="legend-block"><h4>SPACE — 座標</h4>
        <p><b>CYLINDER</b>　中心の軸が時間です（対数目盛り：1目盛りで10倍）。iPhoneの縦画面では下が過去、上が現在。円周の方向が10の領域、中心からの距離が詳細度（外側ほど詳細）。軸のすぐ近くには、時間を持たない思考法などが並びます。輪は時間の目盛りです。</p>
        <p><b>UNROLLED</b>　円筒を切り開いた表示。奥行きが領域のレーン、高さが詳細度（上ほど概観）。</p>
        <p><b>2D</b>　平面図。時間の軸に沿って、10の領域が帯（レーン）になって並びます。帯の中では上ほど概観です。1本指で移動、ピンチで拡大・縮小。</p>
        <p><b>SCALE</b>　近づくほど詳しいラベルが現れます（DOMAINS → THEMES → CONCEPTS → DETAILS）。</p></div>
      <div class="legend-block"><h4>GESTURE — 操作</h4>
        <p>ドラッグで回転、ピンチで拡大・縮小、2本指で移動。ノードをタップすると詳細と関係線が現れます。MENU の INDEX から目次で探すこともできます。</p></div>`;
  },
  settings() {
    const th = store.get("theme", "auto");
    const opt = (attr, v, label, cur) => `<button data-${attr}="${v}" class="${cur === v ? "on" : ""}">${label}</button>`;
    return `<div class="sec-title">Settings</div><p class="sec-lead">表示の設定。この端末に保存されます。</p>
      <div class="legend-block"><h4>THEME — 配色</h4><div class="opts">${opt("theme", "auto", "AUTO", th)}${opt("theme", "light", "LIGHT", th)}${opt("theme", "dark", "DARK", th)}</div>
        <p class="small">AUTO は端末のライト／ダークの設定に従います。</p></div>
      <div class="legend-block"><h4>VIEW — 表示</h4><div class="opts">${opt("view", "cyl", "3D CYLINDER", mode)}${opt("view", "flat", "3D UNROLLED", mode)}${opt("view", "plane", "2D PLANE", mode)}</div>
        <p class="small">画面下部の切替と同じです。2D は全体の位置関係を一度に見るのに向いています。</p></div>`;
  },
  about() {
    return `<div class="sec-title">About</div>
      <p class="sec-lead">An intellectual production model for understanding this universe.</p>
      <div class="legend-block"><h4>PURPOSE</h4><p>宇宙・自然・生命・人間・文明・政治・経済・技術・思想・文化・芸術を、相互につながった一つの地図として学ぶための、個人用のシステムです。地図はClaudeが調べ、独立した検証を経て毎週更新します。あなたの理解の深さは、あなたの回答の評価だけで更新されます。</p>
      <p>目標は「何でも分かる人」になることではなく、「どこまで分かっていて、何が分かっていないか」を理解し、自分の言葉で説明・分析・予測できるようになることです。</p></div>
      <div class="legend-block"><h4>VERSION</h4><ul class="rows">
        <li><span class="k">Map</span><span class="v">v${esc(G.map_version)}</span></li>
        <li><span class="k">System</span><span class="v">${esc(G.system_version)}</span></li>
        <li><span class="k">Session</span><span class="v">${esc(G.current_session)}</span></li>
        <li><span class="k">Updated</span><span class="v">${esc(G.generated_at.slice(0, 10))}</span></li></ul></div>`;
  },
};

// ---------------------------------------------------------------- 意味的ズーム（DOC-03 §3.4）
const tmp = new THREE.Vector3();
let labelTick = 0;
function updateLabels(force) {
  if (!force && labelTick++ % 3) return;
  // 2Dは全体を一度に見る表示なので、同じ距離でも1段詳しく出す
  const d = camera.position.distanceTo(controls.target) * (mode === "plane" ? 0.55 : 1);
  document.body.classList.toggle("plane", mode === "plane");
  document.body.classList.toggle("portrait", portrait);
  const maxLevel = d > 190 ? 1 : d > 95 ? 2 : d > 45 ? 3 : 4;
  $("#scale").textContent = SCALE_EN[maxLevel];
  const showDomains = mode === "plane" || maxLevel <= 2;   // 2Dでは領域名を常に出す（DOC-03 §3.7）
  groups.domains.visible = showDomains;
  if (!groups.domains.visible) groups.domains.children.forEach((c) => (c.visible = false));
  const cand = [];
  for (const m of meshes) {
    const n = byId[m.userData.id], o = labels[n.id];
    o.visible = false;
    if (!m.visible || (n.level > maxLevel && n.id !== selected)) continue;
    m.getWorldPosition(tmp);
    const dist = camera.position.distanceTo(tmp);
    tmp.project(camera);
    if (tmp.z > 1 || Math.abs(tmp.x) > 1.1 || Math.abs(tmp.y) > 1.1) continue;
    const sx = ((tmp.x + 1) / 2) * innerWidth, sy = ((1 - tmp.y) / 2) * innerHeight - 16;
    const fs = n.level === 2 ? 14 : 11;
    const w = Math.min(n.title.ja.length, 22) * fs, h = fs + 6;
    const pri = (n.id === selected ? -100 : 0) + n.level * 10 + dist / 50;
    cand.push({ o, pri, r: [sx - w / 2, sy - h / 2, sx + w / 2, sy + h / 2] });
  }
  // 領域名も重なり判定に含める（優先度は高め）
  if (showDomains) {
    for (const c of groups.domains.children) {
      c.visible = false;
      c.getWorldPosition(tmp);
      tmp.project(camera);
      if (tmp.z > 1 || Math.abs(tmp.x) > 1.05 || Math.abs(tmp.y) > 1.05) continue;
      const sx = ((tmp.x + 1) / 2) * innerWidth, sy = ((1 - tmp.y) / 2) * innerHeight;
      const shown = mode === "plane" && portrait ? c.element.querySelector("b").textContent : c.element.textContent;
      const w = shown.length * 9;
      cand.push({ o: c, pri: mode === "plane" ? -200 : -50, r: [sx - w / 2, sy - 9, sx + w / 2, sy + 9] });
    }
  }
  cand.sort((a, b) => a.pri - b.pri);
  const placed = [];
  for (const c of cand) {
    if (placed.length >= 70) break;
    const [a1, b1, a2, b2] = c.r;
    // 上部の題字・下部の操作部とは重ねない
    if (b1 < 70 || b2 > innerHeight - 56) continue;
    if (placed.some(([x1, y1, x2, y2]) => a1 < x2 && a2 > x1 && b1 < y2 && b2 > y1)) continue;
    placed.push(c.r);
    c.o.visible = true;
  }
}

// ---------------------------------------------------------------- ループ
// 全画面メニューが開いている間と、動きのない間は描画しない（iPhoneの電池・発熱対策）
let dirty = 8;
const wake = () => (dirty = Math.max(dirty, 8));
function animate(now) {
  requestAnimationFrame(animate);
  if (!$("#menu").classList.contains("hidden")) return;
  const t = now ?? performance.now();
  if (modeTween) { modeTween(t); wake(); }
  if (camTween) { camTween(t); wake(); }
  if (controls.update()) wake();
  if (dirty <= 0) return;
  dirty--;
  updateLabels(true);
  renderer.render(scene, camera);
  labelRenderer.render(scene, camera);
}
for (const ev of ["pointerdown", "pointermove", "wheel", "touchmove", "resize", "hashchange"]) addEventListener(ev, wake, { passive: true });

addEventListener("resize", () => {
  const p = innerHeight > innerWidth;
  if (p !== portrait) { portrait = p; makeControls(mode !== "plane" && !selected); if (mode === "plane") placeCamera(false); }
  camera.aspect = innerWidth / innerHeight;
  setOffset(!$("#panel").classList.contains("hidden"));
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
  labelRenderer.setSize(innerWidth, innerHeight);
});
