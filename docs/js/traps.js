/* SchachKenner "Hasenfuß" trap library — original data, CC0-1.0.
 *
 * Each trap is played by the BOT (the trapper); the human must spot and
 * counter it without knowing which trap was picked:
 *   botColor : color the bot plays ("w"/"b"); the human plays the other
 *   line     : the bot's scripted moves (SAN), in order — fixed traps
 *   expected : the typical beginner replies that let the trap spring
 *              (if the human follows them, the last bot move is checkmate)
 *   reactive : bot waits for a blunder and mates immediately if one appears
 *              (Fool's mate pattern); plays `fallback` moves otherwise and
 *              the trap counts as countered after `survivePlies` own moves
 *   tip      : shown to the player once the trap is revealed
 * Validated by scripts/validate-traps.mjs (chess.js) in CI (trap-check.yml).
 */
(function (root) {
  root.SCHACHKENNER_TRAPS = [
    {
      id: "scholar",
      name: "Scholar's mate (Schäfermatt)",
      botColor: "w",
      line: ["e4", "Qh5", "Bc4", "Qxf7#"],
      expected: ["e5", "Nc6", "Nf6"],
      tip: "Defense: 3...g6! (or already 2...g6) — drive the queen away and f7 is covered. Never allow ...Nf6?? with Qh5+Bc4 lined up."
    },
    {
      id: "scholar-bc4-first",
      name: "Scholar's mate, bishop first (Schäfermatt)",
      botColor: "w",
      line: ["e4", "Bc4", "Qh5", "Qxf7#"],
      expected: ["e5", "Bc5", "Nf6"],
      tip: "Defense: 3...g6! or 3...Qe7 — with the queen on h5 and bishop on c4, ...Nf6?? is mate on f7."
    },
    {
      id: "legal",
      name: "Légal's mate (Légal-Matt)",
      botColor: "w",
      line: ["e4", "Nf3", "Bc4", "Nc3", "Nxe5", "Bxf7+", "Nd5#"],
      expected: ["e5", "d6", "Bg4", "g6", "Bxd1", "Ke7"],
      tip: "Never play 4...g6?? against this setup, and never grab the 'hanging' queen with 5...Bxd1?? — answer 5.Nxe5 with ...Qe7 or ...Nxe5."
    },
    {
      id: "blackburne-shilling",
      name: "Blackburne Shilling Gambit (Nf3#)",
      botColor: "b",
      line: ["e5", "Nc6", "Nd4", "Qg5", "Qxg2", "Qxe4+", "Nf3#"],
      expected: ["e4", "Nf3", "Bc4", "Nxe5", "Nxf7", "Rf1", "Be2"],
      tip: "After 3...Nd4!? simply recapture 4.Nxd4 (or play 4.d3) — never 4.Nxe5?? 5.Nxf7??, which walks into ...Qg5! and a smothered-style Nf3#."
    },
    {
      id: "greco",
      name: "Greco's trap (Bg6#)",
      botColor: "w",
      line: ["e4", "d4", "Bd3", "exf5", "Qh5+", "fxg6", "gxh7+", "Bg6#"],
      expected: ["b6", "Bb7", "f5", "Bxg2", "g6", "Nf6", "Nxh5"],
      tip: "Don't grab pawns while your king is exposed: after 3.Bd3, answer ...f5? keeping 4.Qh5+ in mind — solid is 4.Nf3."
    },
    {
      id: "teed-delmar",
      name: "Teed–Delmar bishop hunt (Bg6#)",
      botColor: "w",
      line: ["d4", "Bg5", "Bh4", "Bg3", "e3", "Bd3", "Qxh5+", "Bg6#"],
      expected: ["f5", "h6", "g5", "f4", "h5", "Rh6", "Rxh5"],
      tip: "The bishop hunt 2.Bg5 h6 3.Bh4 g5 4.Bg3 f4?? is poison — meet it with 5.e3! and never 6...Rh6?? 7...Rxh5??."
    },
    {
      id: "fools-mate",
      name: "Fool's mate (Narrenmatt)",
      botColor: "b",
      reactive: true,
      survivePlies: 2,
      fallback: ["e5", "e6", "d5", "Nf6", "Nc6", "Bc5", "g6"],
      tip: "Never push f3/f4 and g4 early — keep the e1–h4 diagonal closed, otherwise ...Qh4# is mate."
    }
  ];
})(typeof window !== "undefined" ? window : globalThis);
