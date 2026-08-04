/* Shared utilities for Case File 01 exercises.
   Mirrors the fitting machinery of src/make_figures.py:
   design matrix [1, t-1900, sin/cos pairs], ordinary least squares, R²,
   amplitude of a sin/cos pair. Seeded PRNG so every run is reproducible. */
"use strict";

/* ---------- palette (keep in sync with _shared.css) ---------- */
const C = {
  ink: "#1B2A3A", inkSoft: "#44586C", claim: "#C7772E", claimDeep: "#9A5A1F",
  claimTint: "#FBF1E4", rebut: "#0E7C7B", rebutDeep: "#0A5C5B",
  rebutTint: "#E4F1F0", grey: "#7C8B99", hair: "#DFE6EC", band: "#EDF2F6",
};

/* ---------- seeded randomness ---------- */
function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function gaussian(rand) {           // Box–Muller
  let u = 0, v = 0;
  while (u === 0) u = rand();
  while (v === 0) v = rand();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

/* ---------- small stats ---------- */
const mean = (a) => a.reduce((s, v) => s + v, 0) / a.length;
function std(a) {
  const m = mean(a);
  return Math.sqrt(a.reduce((s, v) => s + (v - m) * (v - m), 0) / a.length);
}
function linfit(x, y) {             // least-squares line: returns [slope, intercept]
  const mx = mean(x), my = mean(y);
  let sxy = 0, sxx = 0;
  for (let i = 0; i < x.length; i++) { sxy += (x[i] - mx) * (y[i] - my); sxx += (x[i] - mx) * (x[i] - mx); }
  const b = sxy / sxx;
  return [b, my - b * mx];
}
function r2(y, yhat) {
  const m = mean(y);
  let ssr = 0, sst = 0;
  for (let i = 0; i < y.length; i++) { ssr += (y[i] - yhat[i]) ** 2; sst += (y[i] - m) ** 2; }
  return 1 - ssr / sst;
}

/* ---------- linear algebra: solve A x = b (Gaussian elimination, partial pivot) ---------- */
function solve(A, b) {
  const n = A.length;
  const M = A.map((row, i) => [...row, b[i]]);
  for (let c = 0; c < n; c++) {
    let p = c;
    for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r;
    [M[c], M[p]] = [M[p], M[c]];
    const piv = M[c][c];
    for (let r = c + 1; r < n; r++) {
      const f = M[r][c] / piv;
      for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r--) {
    let s = M[r][n];
    for (let k = r + 1; k < n; k++) s -= M[r][k] * x[k];
    x[r] = s / M[r][r];
  }
  return x;
}
/* least squares via normal equations: X (rows) n×p, y n → beta p */
function lstsq(X, y) {
  const n = X.length, p = X[0].length;
  const A = Array.from({ length: p }, () => new Array(p).fill(0));
  const b = new Array(p).fill(0);
  for (let i = 0; i < n; i++) {
    const xi = X[i];
    for (let j = 0; j < p; j++) {
      b[j] += xi[j] * y[i];
      for (let k = j; k < p; k++) A[j][k] += xi[j] * xi[k];
    }
  }
  for (let j = 0; j < p; j++) for (let k = 0; k < j; k++) A[j][k] = A[k][j];
  return solve(A, b);
}

/* ---------- the L&S11-style model: [1, t-1900, sin/cos per period] ---------- */
function designRow(t, periods, trend) {
  const row = [1];
  if (trend) row.push(t - 1900);
  for (const P of periods) {
    const w = 2 * Math.PI / P;
    row.push(Math.sin(w * t), Math.cos(w * t));
  }
  return row;
}
function fitCycles(t, y, periods, trend = true) {
  const X = t.map((ti) => designRow(ti, periods, trend));
  const beta = lstsq(X, y);
  const predict = (tt) => tt.map((ti) => {
    const row = designRow(ti, periods, trend);
    let s = 0;
    for (let j = 0; j < row.length; j++) s += row[j] * beta[j];
    return s;
  });
  const amp = (i) => {                      // amplitude of i-th sin/cos pair
    const k = (trend ? 2 : 1) + 2 * i;
    return Math.hypot(beta[k], beta[k + 1]);
  };
  return { beta, predict, amp, r2cal: r2(y, predict(t)) };
}

/* ---------- canvas chart helper (devicePixelRatio-aware) ---------- */
function Chart(canvas, opts = {}) {
  const M = Object.assign({ ml: 46, mr: 12, mt: 10, mb: 30 }, opts.margin || {});
  const self = {
    canvas, ctx: canvas.getContext("2d"),
    xlim: opts.xlim || [0, 1], ylim: opts.ylim || [0, 1],
    W: 0, H: 0,
  };
  function fit() {
    const dpr = window.devicePixelRatio || 1;
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    }
    self.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    self.W = w; self.H = h;
  }
  self.x = (v) => M.ml + (v - self.xlim[0]) / (self.xlim[1] - self.xlim[0]) * (self.W - M.ml - M.mr);
  self.y = (v) => self.H - M.mb - (v - self.ylim[0]) / (self.ylim[1] - self.ylim[0]) * (self.H - M.mt - M.mb);
  self.begin = function (xlim, ylim) {
    fit();
    if (xlim) self.xlim = xlim;
    if (ylim) self.ylim = ylim;
    self.ctx.clearRect(0, 0, self.W, self.H);
  };
  self.clipPlot = function (fn) {
    const c = self.ctx;
    c.save(); c.beginPath();
    c.rect(M.ml, M.mt, self.W - M.ml - M.mr, self.H - M.mt - M.mb);
    c.clip(); fn(); c.restore();
  };
  self.line = function (xs, ys, style = {}) {
    const c = self.ctx;
    c.save();
    c.strokeStyle = style.color || C.ink;
    c.lineWidth = style.width || 1.5;
    c.setLineDash(style.dash || []);
    c.globalAlpha = style.alpha ?? 1;
    c.lineJoin = "round";
    c.beginPath();
    let started = false;
    for (let i = 0; i < xs.length; i++) {
      if (!isFinite(ys[i])) { started = false; continue; }
      const px = self.x(xs[i]), py = self.y(ys[i]);
      if (!started) { c.moveTo(px, py); started = true; } else c.lineTo(px, py);
    }
    c.stroke(); c.restore();
  };
  self.dots = function (xs, ys, style = {}) {
    const c = self.ctx;
    c.save(); c.fillStyle = style.color || C.ink; c.globalAlpha = style.alpha ?? 1;
    for (let i = 0; i < xs.length; i++) {
      c.beginPath(); c.arc(self.x(xs[i]), self.y(ys[i]), style.r || 3, 0, 7); c.fill();
    }
    c.restore();
  };
  self.band = function (x0, x1, color = C.band) {
    const c = self.ctx;
    c.save(); c.fillStyle = color;
    c.fillRect(self.x(x0), M.mt, self.x(x1) - self.x(x0), self.H - M.mt - M.mb);
    c.restore();
  };
  self.hline = function (v, style = {}) { self.line(self.xlim, [v, v], style); };
  self.vline = function (v, style = {}) {
    const c = self.ctx;
    c.save(); c.strokeStyle = style.color || C.grey; c.lineWidth = style.width || 1;
    c.setLineDash(style.dash || []);
    c.beginPath(); c.moveTo(self.x(v), M.mt); c.lineTo(self.x(v), self.H - M.mb); c.stroke();
    c.restore();
  };
  self.text = function (str, xv, yv, style = {}) {
    const c = self.ctx;
    c.save();
    c.fillStyle = style.color || C.inkSoft;
    c.font = (style.font || "11.5px") + " " + (style.family || "-apple-system,'Segoe UI',Roboto,sans-serif");
    c.textAlign = style.align || "left";
    c.textBaseline = style.baseline || "alphabetic";
    c.fillText(str, style.px ? xv : self.x(xv), style.px ? yv : self.y(yv));
    c.restore();
  };
  self.axes = function (o = {}) {
    const c = self.ctx;
    c.save();
    c.strokeStyle = C.hair; c.lineWidth = 1; c.fillStyle = C.inkSoft;
    c.font = "11px -apple-system,'Segoe UI',Roboto,sans-serif";
    const xt = o.xticks || [], yt = o.yticks || [];
    for (const v of yt) {
      const py = self.y(v);
      c.globalAlpha = 0.9; c.beginPath(); c.moveTo(M.ml, py); c.lineTo(self.W - M.mr, py); c.stroke();
      c.globalAlpha = 1; c.textAlign = "right"; c.textBaseline = "middle";
      c.fillText(o.yfmt ? o.yfmt(v) : String(v), M.ml - 6, py);
    }
    for (const v of xt) {
      const px = self.x(v);
      c.textAlign = "center"; c.textBaseline = "top";
      c.fillText(o.xfmt ? o.xfmt(v) : String(v), px, self.H - M.mb + 6);
      c.globalAlpha = 0.55; c.beginPath(); c.moveTo(px, self.H - M.mb); c.lineTo(px, self.H - M.mb + 3);
      c.strokeStyle = C.grey; c.stroke(); c.strokeStyle = C.hair; c.globalAlpha = 1;
    }
    c.strokeStyle = C.grey; c.beginPath();
    c.moveTo(M.ml, M.mt); c.lineTo(M.ml, self.H - M.mb); c.lineTo(self.W - M.mr, self.H - M.mb); c.stroke();
    if (o.xlabel) {
      c.textAlign = "center"; c.textBaseline = "bottom"; c.fillStyle = C.inkSoft;
      c.fillText(o.xlabel, M.ml + (self.W - M.ml - M.mr) / 2, self.H - 2);
    }
    if (o.ylabel) {
      c.translate(11, M.mt + (self.H - M.mt - M.mb) / 2); c.rotate(-Math.PI / 2);
      c.textAlign = "center"; c.textBaseline = "middle";
      c.fillText(o.ylabel, 0, 0);
    }
    c.restore();
  };
  return self;
}

/* nice tick positions */
function ticks(lo, hi, n = 6) {
  const span = hi - lo, step0 = span / n;
  const mag = Math.pow(10, Math.floor(Math.log10(step0)));
  let step = mag;
  for (const m of [1, 2, 2.5, 5, 10]) if (step0 / (m * mag) <= 1) { step = m * mag; break; }
  const t = [];
  for (let v = Math.ceil(lo / step) * step; v <= hi + 1e-9; v += step) t.push(Math.round(v * 1e9) / 1e9);
  return t;
}

function debounceRedraw(fn) {
  let raf = null;
  const go = () => { if (raf) return; raf = requestAnimationFrame(() => { raf = null; fn(); }); };
  window.addEventListener("resize", go);
  return go;
}
