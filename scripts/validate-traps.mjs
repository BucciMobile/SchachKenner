#!/usr/bin/env node
/* Validates the Hasenfuß trap library (docs/js/traps.js) with chess.js.
 *
 * For every fixed trap (botColor + scripted `line` + `expected` beginner
 * replies):
 *   - replaying bot line and expected replies alternately is fully legal
 *     and ends in CHECKMATE (the trap springs if the player cooperates)
 *   - at least one legal player reply at some ply counters the trap
 *     (runtime rule in docs/play.html: bot's next scripted move is illegal,
 *     or it is the final scripted move but not mate)
 * For reactive traps (Fool's mate pattern):
 *   - after 1.g4 (and 1.f3 e5 2.g4) the bot has an immediate mate
 *   - after 1.e4 it does not
 *
 * Usage:
 *   node scripts/validate-traps.mjs                       # needs chess.js resolvable
 *   CHESSJS_PATH=/path/to/chess.js node scripts/validate-traps.mjs
 * CI (trap-check.yml) installs chess.js@1.4.0 and sets CHESSJS_PATH.
 */
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const chessPath = process.env.CHESSJS_PATH || "chess.js";
const { Chess } = require(chessPath);

const code = readFileSync(new URL("../docs/js/traps.js", import.meta.url), "utf8");
new Function(code)();                       // sets globalThis.SCHACHKENNER_TRAPS
const traps = globalThis.SCHACHKENNER_TRAPS;

if (!Array.isArray(traps) || traps.length < 3) {
  console.error("FAIL: SCHACHKENNER_TRAPS missing or too small");
  process.exit(1);
}

const ids = new Set();
let failures = 0;
const fail = msg => { failures++; console.error("FAIL: " + msg); };

// Reference implementation of the runtime rule used by docs/play.html:
// after the player's move at ply k, simulate the bot's next scripted move.
function classifyAfterPlayerMove(trap, ch, playerPly) {
  const L = trap.line.length;
  const botPly = trap.botColor === "w" ? playerPly + 1 : playerPly;
  const next = trap.line[botPly];
  if (!next) return "countered";
  const sim = new Chess(ch.fen());
  let sm = null;
  try { sm = sim.move(next); } catch { sm = null; }
  if (sm && sim.isCheckmate()) return "losing";
  if (!sm || botPly === L - 1) return "countered";
  return "continue";
}

for (const t of traps) {
  if (!t.id || ids.has(t.id)) fail(`duplicate/missing id: ${t.id}`);
  ids.add(t.id);
  if (!t.name || !t.tip) fail(`${t.id}: missing name/tip`);
  if (t.botColor !== "w" && t.botColor !== "b") fail(`${t.id}: bad botColor`);

  if (t.reactive) {
    // Fool's mate pattern checks
    if (t.botColor !== "b") fail(`${t.id}: reactive trap should be botColor "b"`);
    if (!Array.isArray(t.fallback) || !t.fallback.length) fail(`${t.id}: fallback moves missing`);
    if (!Number.isInteger(t.survivePlies) || t.survivePlies < 1) fail(`${t.id}: bad survivePlies`);
    const g4 = new Chess(); g4.move("f4"); g4.move("e6"); g4.move("g4");
    const mateAfterG4 = g4.moves({ verbose: true }).some(m => {
      const s = new Chess(g4.fen()); try { s.move(m); } catch { return false; }
      return s.isCheckmate();
    });
    if (!mateAfterG4) fail(`${t.id}: no immediate mate after 1.f4 e6 2.g4??`);
    const f3g4 = new Chess(); f3g4.move("f3"); f3g4.move("e5"); f3g4.move("g4");
    const mateAfterF3G4 = f3g4.moves({ verbose: true }).some(m => {
      const s = new Chess(f3g4.fen()); try { s.move(m); } catch { return false; }
      return s.isCheckmate();
    });
    if (!mateAfterF3G4) fail(`${t.id}: no immediate mate after 1.f3 e5 2.g4??`);
    const e4 = new Chess(); e4.move("e4");
    const mateAfterE4 = e4.moves({ verbose: true }).some(m => {
      const s = new Chess(e4.fen()); try { s.move(m); } catch { return false; }
      return s.isCheckmate();
    });
    if (mateAfterE4) fail(`${t.id}: black should have NO immediate mate after 1.e4`);
    console.log(`ok  ${t.id} (reactive): fool's-mate pattern verified`);
    continue;
  }

  // fixed trap
  const L = t.line.length;
  if (!Array.isArray(t.line) || L < 2) { fail(`${t.id}: line too short`); continue; }
  const expLen = t.botColor === "w" ? L - 1 : L;
  if (!Array.isArray(t.expected) || t.expected.length !== expLen)
    fail(`${t.id}: expected length ${t.expected && t.expected.length} != ${expLen}`);

  // 1) full replay along expected replies must be legal and end in mate
  const ch = new Chess();
  let legal = true;
  for (let k = 0; k < L && legal; k++) {
    if (t.botColor === "w") {
      try { ch.move(t.line[k]); } catch { legal = false; break; }
      if (k < L - 1) { try { ch.move(t.expected[k]); } catch { legal = false; break; } }
    } else {
      try { ch.move(t.expected[k]); } catch { legal = false; break; }
      try { ch.move(t.line[k]); } catch { legal = false; break; }
    }
  }
  if (!legal) fail(`${t.id}: scripted line + expected replies are not all legal`);
  else if (!ch.isCheckmate()) fail(`${t.id}: expected line does NOT end in checkmate (${ch.pgn()})`);
  else console.log(`ok  ${t.id}: line legal, ends in mate — ${ch.pgn().split("\n").filter(l => l.includes("1.")).join("").trim()}`);

  // 2) counterable: enumerate every legal reply at every player ply
  const Lp = t.botColor === "w" ? L - 1 : L;
  let anyCounter = false;
  for (let k = 0; k < Lp && legal && !anyCounter; k++) {
    // rebuild the position before the player's k-th move
    const pos = new Chess();
    for (let j = 0; j < k; j++) {
      if (t.botColor === "w") { pos.move(t.line[j]); pos.move(t.expected[j]); }
      else { pos.move(t.expected[j]); pos.move(t.line[j]); }
    }
    if (t.botColor === "w") pos.move(t.line[k]);   // bot just played line[k]; player to move
    if (pos.turn() === t.botColor) continue;
    for (const m of pos.moves({ verbose: true })) {
      const s = new Chess(pos.fen()); s.move(m);
      if (classifyAfterPlayerMove(t, s, k) === "countered") { anyCounter = true; break; }
    }
  }
  if (legal && !anyCounter) fail(`${t.id}: trap is NOT counterable under the runtime rule`);
}

if (failures) { console.error(`\n${failures} failure(s)`); process.exit(1); }
console.log(`\nAll ${traps.length} traps OK (${traps.filter(t => !t.reactive).length} fixed, ${traps.filter(t => t.reactive).length} reactive).`);
