# -*- coding: utf-8 -*-
"""Own-word opening explanations for the Learn tool (repo content: CC0).

Two layers:
  OPENINGS: per-opening {intro, traps}  (intro = idea/main plans, traps = variants & traps)
  MOVE_NOTES: SAN -> one-sentence "why this move" note (fallback is generated in build-openings.py)
Everything here is written by us in our own words — no copied text.
"""

# key, name, eco display, wikipedia slug, matcher keywords (lowercase substrings of the PGN Opening name)
OPENINGS = [
    ("italian",      "Italian Game (Giuoco Piano)",        "C50–C54", "Italian_Game",              ["giuoco", "italian game", "piano"]),
    ("ruylopez",     "Ruy Lopez (Spanish Opening)",       "C60–C99", "Spanish_Opening",           ["ruy lopez", "spanish", "berlin", "closed"]),
    ("scotch",       "Scotch Game",                       "C44–C45", "Scotch_Game",               ["scotch"]),
    ("evans",        "Evans Gambit",                      "C51–C52", "Evans_Gambit",              ["evans"]),
    ("kingsgambit",  "King's Gambit",                     "C30–C39", "King's_Gambit",             ["king's gambit", "kga", "kgd"]),
    ("vienna",       "Vienna Game",                       "C25–C29", "Vienna_Game",               ["vienna"]),
    ("philidor",     "Philidor Defence",                  "C41",     "Philidor_Defence",          ["philidor"]),
    ("petrov",       "Petrov's Defence",                  "C42–C43", "Petrov's_Defence",          ["petrov", "russian"]),
    ("fourknights",  "Four Knights Game",                 "C46–C49", "Four_Knights_Game",         ["four knights"]),
    ("twoknights",   "Two Knights Defence",               "C55–C59", "Two_Knights_Defence",       ["two knights", "fegatello"]),
    ("french",       "French Defence",                    "C00–C19", "French_Defence",            ["french"]),
    ("sicilian",     "Sicilian Defence",                  "B20–B99", "Sicilian_Defence",          ["sicilian"]),
    ("carokann",     "Caro–Kann Defence",                 "B10–B19", "Caro–Kann_Defence",         ["caro"]),
    ("scandinavian", "Scandinavian Defence",              "B01",     "Scandinavian_Defence",      ["scandinavian", "centre counter"]),
    ("alekhine",     "Alekhine's Defence",                "B02–B05", "Alekhine's_Defence",        ["alekhine"]),
    ("pirc",         "Pirc / Modern Defence",             "B07–B09", "Pirc_Defence",              ["pirc", "modern"]),
    ("qgd",          "Queen's Gambit Declined",           "D30–D69", "Queen's_Gambit_Declined",   None),  # matched via ECO+name logic
    ("qga",          "Queen's Gambit Accepted",           "D20–D29", "Queen's_Gambit_Accepted",   ["queen's gambit accepted", "qga"]),
    ("slav",         "Slav Defence",                      "D10–D19", "Slav_Defence",              ["slav"]),
    ("semislav",     "Semi-Slav Defence",                 "D43–D49", "Semi-Slav_Defence",         ["semi-slav", "semi slav"]),
    ("kid",          "King's Indian Defence",             "E60–E99", "King's_Indian_Defence",     ["king's indian", "king indian"]),
    ("nimzo",        "Nimzo-Indian Defence",              "E20–E59", "Nimzo-Indian_Defence",      ["nimzo"]),
    ("qid",          "Queen's Indian Defence",            "E00–E19", "Queen's_Indian_Defence",    ["queen's indian"]),
    ("grunfeld",     "Grünfeld Defence",                  "D70–D99", "Grünfeld_Defence",          ["grunfeld", "grünfeld"]),
    ("london",       "London System",                     "D00–D06", "London_System",             ["london"]),
    ("english",      "English Opening",                   "A10–A39", "English_Opening",           ["english"]),
]

INTROS = {
 "italian": ("1.e4 e5 2.Nf3 Nc6 3.Bc4 — White develops quickly and aims the bishop at the weak f7 square. "
             "The Italian is one of the oldest openings: direct, principled, and rich in tactics.",
             "Variants & traps: 3...Bc5 leads to the quiet Giuoco Piano; 3...Be7 is the Two Knights Defence territory. "
             "Trap: after 4.c3 Nf6 5.d4 exd4 6.cxd4?? Bb4+ wins material — take with 6.e5! instead. Black can also play the sharp 3...d6 (Hungarian)."),
 "ruylopez": ("1.e4 e5 2.Nf3 Nc6 3.Bb5 — the Spanish Opening: White pins the knight and keeps long-term pressure on e5 "
              "without committing pawns. The most popular opening at master level for 500 years.",
              "Variants & traps: 3...a6 4.Ba4 Nf6 is the main line (Berlin 4...d6 and Marshall 4...Nf6 are famous sub-variants). "
              "Trap: the Open Ruy (5.d4) is double-edged; Black's ...Bb4+ pin tricks and the Exchange variation (4.Bxc6) are quieter but solid."),
 "scotch": ("1.e4 e5 2.Nf3 Nc6 3.d4 — White strikes the center immediately and avoids the deep theory of the Italian. "
            "After 3...exd4 White usually recaptures with the knight (3...d6 allows 4.d5).",
            "Variants & traps: 4.Nxd4 Bc5 5.Nb3 (the 'Scotch Gambit' 5.c3!? is risky but fun); 4...Nf6 5.Nc3 is the main line. "
            "Trap: 4.d5?! Nxd5? no — after 3...exd4 4.d5?? Nxd5 5.Nxd5 Qxd5 loses the queen-side development race."),
 "evans": ("1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 — White sacrifices a pawn for rapid development and open lines against f7. "
           "Romantic, tactical, and still dangerous at every level.",
           "Variants & traps: 4...Bxb4 5.c3 is the accepted Evans; 5...Ba5 6.d4 exd4 is the main line. "
           "Trap: the 'Compromised Defence' 5...Bc5?! 6.bxc5 d6 7.Bb5+ looks scary for Black but 7...Nfd7 defends; White's 6.e5!? is the sharp try."),
 "kingsgambit": ("1.e4 e5 2.f4 — the King's Gambit: White sacrifices a pawn for a fast attack on f7. "
                "The most romantic opening in chess.",
                "Variants & traps: 2...exf4 is forced; after 3.Nf3 g5 4.Bc4 g4 5.O-O Black must defend accurately (5...Qg5?! loses to 6.Ne5). "
                "Trap: 3.d4 (declined) is solid; the 'Cunningham' 3.Bc4 is unsound but tricky."),
 "vienna": ("1.e4 e5 2.Nc3 — the Vienna Game: White prepares f4 (a mini King's Gambit) while keeping the knight flexible.",
           "Variants & traps: 2...Nf6 3.f4 is the main Vienna; 3...Bc5 4.f4 exf4 transposes to the King's Gambit. "
           "Trap: after 3.f4 exf4 4.d4 Qh4+ 5.Ke2 the king walk is dangerous for White — 5...d5! 6.exd5 Bg4+ is fine for Black."),
 "philidor": ("1.e4 e5 2.Nf3 d6 — Black defends e5 solidly with the pawn, a classical, compact setup.",
             "Variants & traps: 3.d4 exd4 4.Nxd4 Nf6 5.Nc3 is the main line (the 'Lion' 3...g6 is a modern try). "
             "Trap: 3.Nc3?! Nf6 4.d4 exd4 5.Nxd4 Nxe4?? loses to 6.Qxd8+ — but Black simply plays 5...c6."),
 "petrov": ("1.e4 e5 2.Nf3 Nf6 — Petrov's Defence: Black symmetrically attacks e4 and invites an open game.",
            "Variants & traps: 3.Nxe5 d6 4.Nf3 Nxe4 is the main line; the 'Classical' 3.d4 is solid. "
            "Trap: 3.Nxe5?! d6 4.Nf3 Nxe4 5.d3 (5.Qe2 is safer) — 5...Be7! and Black regains the pawn with a better game."),
 "fourknights": ("1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 — all four knights are out: symmetric, maneuvering, drawish at top level but full of tactics.",
               "Variants & traps: 4.d4 exd4 5.Nxd4 (or 5.e5) leads to open play; 4.Bb5 is the Spanish Four Knights. "
               "Trap: 4.d3?! is passive; Black equalizes easily with 4...Bb4."),
 "twoknights": ("1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 — the Two Knights Defence: Black counter-attacks f2 immediately, leading to the sharp Fried Liver / Fegatello.",
               "Variants & traps: 4.d3 is quiet; 4.Ng5!? is the Fried Liver Attack (4...d5 5.exd5 Nxd5?? 6.Nxf7! is the famous trap — 5...Na5! is the correct defence). 4...h6 5.Nxf7 is the Fegatello."),
 "french": ("1.e4 e6 — the French Defence: Black builds a solid pawn chain (d5) and counter-attacks on the queenside or the center. "
            "Black's most popular answer to 1.e4.",
            "Variants & traps: 2.d4 d5 3.Nc3 (Winawer 3...Bb4, Classical 3...Nf6) or 3.Nd2 (Tarrasch); the Advance 3.e5 c5 4.c3 is tense. "
            "Trap: in the Winawer, 4.e5 c5 5.a3 Bxc3 6.bxc3 Qc7 7.Qg4!? (Poisoned Pawn) — 7...Qf6!? is the cool defence."),
 "sicilian": ("1.e4 c5 — the Sicilian: Black fights asymmetrically for the d4 square and the queenside, leading to the richest opening complex in chess.",
             "Variants & traps: 2.Nf3 d6 (Najdorf/Dragon/Scheveningen territory), 2...e6 (Kan/Taimanov), 2...Nc6 (Classical). "
             "Trap: the Open Sicilian 2.Nf3 3.d4 cxd4 4.Nxd4 — Black must not play 4...Nf6?? 5.Nc3 and ...d5 is awkward; and the 'Najdorf Poisoned Pawn' 6.Bc4 e6 7.Bb3 Qc7 is razor-sharp."),
 "carokann": ("1.e4 c6 — the Caro–Kann: Black prepares ...d5 without weakening, a rock-solid defence.",
             "Variants & traps: 2.d4 d5 3.Nc3 (or 3.Nd2) dxe4 4.Nxe4; the Advance 3.e5 Bf5 is mainline. "
             "Trap: 3.Nd2 dxe4 4.Nxe4 Bf5 5.Ng3 e6?? 6.Nxf5! exf5 7.Qh5+ wins — play 5...Nd7 first."),
 "scandinavian": ("1.e4 d5 — the Scandinavian: Black brings the queen out early, challenges the center, and aims to equalize fast.",
                  "Variants & traps: 2.exd5 Qxd5 3.Nc3 (3...Qa5 4.d4 Nf6 is the main line; 3...Qd8 is solid). "
                  "Trap: 3...Qd6?! 4.d4 Nf6 5.Nf3 Bg4 6.Be2 e6 7.O-O and White is better — the queen gets hunted."),
 "alekhine": ("1.e4 Nf6 — Alekhine's Defence: Black provokes the pawn center (e5/d5/c5) to attack it later. Hypermodern and tricky.",
             "Variants & traps: 2.e5 Nd5 3.d4 d6 4.Nf3 is the main line (Four Pawns Attack 4.c4 Nb6 is wild). "
             "Trap: 2.e5 Nd5 3.c4 Nb6 4.e5? Nd5 5.c5?? loses to 5...g5! — don't overextend."),
 "pirc": ("1.e4 d6 — the Pirc/Modern: Black lets White build a big center, then attacks it with ...Nf6, ...g6, ...Bg7. Flexible and counter-attacking.",
         "Variants & traps: 2.d4 Nf6 3.Nc3 g6 — the Austrian Attack 4.f4 Bg7 5.Nf3 O-O 6.Be2 is dangerous for Black (7.e5!?). "
         "Trap: after 4.f4 Bg7 5.Nf3 O-O 6.Be3 e5?! 7.dxe5 dxe5 8.Qxd8 is bad for Black — play 6...c5 instead."),
 "qgd": ("1.d4 d5 2.c4 — the Queen's Gambit: White offers a pawn to open the center and get rapid development. The queen's-side twin of the King's Gambit.",
         "Variants & traps: 2...e6 (QGD, solid) or 2...c6 (Slav) / 2...dxc4 (QGA); 3.Nc3 Nf6 4.Nf3 e6 is the Orthodox main line. "
         "Trap: in the Orthodox, 4...Be7 5.Bg5 O-O 6.e3 Nbd7 7.Rc1 c5 8.dxc5 Nxc5 9.Bxf6?! gxf6 weakens Black's king but Black is fine — don't fear ...dxc4 gambits."),
 "qga": ("1.d4 d5 2.c4 dxc4 — the Queen's Gambit Accepted: Black takes the pawn and returns it later for free development.",
         "Variants & traps: 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 is the main line. "
         "Trap: 3.e4?! d5! 4.e5 d4 wins a piece for Black — the 'Central Europe' 3.Nc3 is safer but 3...e5!? is fine."),
 "slav": ("1.d4 d5 2.c4 c6 — the Slav: Black supports d5 with ...c6 instead of ...e6, keeping the bishop free. Very solid.",
         "Variants & traps: 3.Nf3 Nf6 4.Nc3 dxc4 (Semi-Slav move order too) — the Exchange 4.a4!? is tricky; 4.e3 e6 5.b3 is mainline. "
         "Trap: after 4.Nc3 dxc4 5.e3 b5?! 6.a4! and Black's queenside pawns collapse."),
 "semislav": ("1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 e6 — the Semi-Slav: Slav structure with the ...e6 bishop active. Sharp and popular at elite level.",
              "Variants & traps: 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 is the main Meran/Anti-Moscow territory. "
              "Trap: 6.Bd3?! dxc4 7.Bxc4 b5 8.Be2 Bb7 9.O-O b4!? 10.Na4 c5! 11.dxc5 Nxc5 wins a piece — the famous Botvinnik trap."),
 "kid": ("1.d4 Nf6 2.c4 g6 — the King's Indian: Black fianchettos and counter-attacks e4/e5 with ...e5 or ...c5. One of the most fighting defences.",
         "Variants & traps: 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 (mainline Mar del Plata) — the Sämisch 4...O-O 5.f3 c5 6.e4 Nc6 is critical. "
         "Trap: in the Classical, 7.O-O Nc6 8.d5 Ne5?! 9.Nxe5! dxe5 10.Qxd8 wins — Black must play 8...Na5."),
 "nimzo": ("1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 — the Nimzo-Indian: Black pins the knight to double White's pawns, the strategically deepest defence to 1.d4.",
           "Variants & traps: 4.e3 O-O 5.Bd3 d5 6.Nf3 c5 7.O-O dxc4 8.Bxc4 Nbd7; the Rubinstein 4.Qc2 is the main alternative. "
           "Trap: 4.e3 O-O 5.Bd3 d5 6.Nf3 c5 7.O-O dxc4 8.Bxc4 cxd4?! 9.exd4 Nc6 10.Bg5 and White regains the pawn with pressure — play 8...b5! instead."),
 "qid": ("1.d4 Nf6 2.c4 e6 3.Nf3 b6 — the Queen's Indian: Black fianchettos the bishop to b7 and plays ...d5 later. Solid and hypermodern.",
        "Variants & traps: 4.g3 Ba6 (or 4...Bb7 mainline) 5.b3 d5 6.Bg2 Be7 7.O-O O-O; the Kasparov 4.g3 Ba6 5.b3 b6 is sharp. "
        "Trap: 4.Nc3 Bb7 5.Bg5 h6 6.Bh4 g5 7.Bg3 Ne4 — the 'Queen's Indian trap' — 8.Qc2! f5 9.e3 wins the piece back."),
 "grunfeld": ("1.d4 Nf6 2.c4 g6 3.Nc3 d5 — the Grünfeld: Black attacks the big center with ...dxc4 and ...Bg7 pressure. Dynamic and popular at top level.",
             "Variants & traps: 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 (or 7.Nf3) — the Russian System 5...Nxc3 6.bxc3 c5 is mainline. "
             "Trap: 4.Nf3 Bg7 5.cxd5 O-O 6.e4 Nxd5 7.Nxd5 exd5?? no — 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Nf3 and White has a lasting center."),
 "london": ("1.d4 d5 2.Bf4 (or 2.Nf3 Nf6 3.Bf4) — the London System: a simple, repeatable setup with Bf4, e3, Nbd2, c3, O-O. Popular at all levels.",
            "Variants & traps: 2...Nf6 3.Nf3 e6 4.e3 c5 5.c3 Nc6 6.Bd3 Bd6 is the main line; Black can play 2...Bf5!? or the sharp 2...c5. "
            "Trap: 4...Bd6 5.Nbd2 O-O 6.e3 e5?! 7.dxe5 Nxe5 8.Nxe5 Bxe5?? loses to 9.Nxe5 — careful with ...e5 breaks."),
 "english": ("1.c4 — the English Opening: White controls d5 from the flank and often transposes to d4 or Réti structures. Positional and flexible.",
             "Variants & traps: 1...e5 (Reversed Sicilian) 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 d5 is critical; 1...c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 is the Symmetrical English. "
             "Trap: 1...e5 2.Nc3 Nf6 3.Nf3 Nc6 4.e3?! d5 5.d4 exd4 6.exd4?? d4! wins a piece — play 4.g3 instead."),
}

# SAN -> why-this-move note (own words). Fallback generated in build-openings.py.
MOVE_NOTES = {
 "e4": "Claims the central e4 square, opens the queen's and bishop's diagonals, and stakes a claim on d5/f5.",
 "d4": "Controls the center from a protected square and prepares c4/e4 pawn breaks or a quick Nf3+Bishops development.",
 "c4": "The English: controls d5 from the flank without blocking the c-pawn — flexible and hard to punish.",
 "Nf3": "Develops the knight with tempo and attacks e5; the most flexible first move for White.",
 "Nc3": "Develops toward the center and adds support to e4/d4 pawn breaks.",
 "g3": "Prepares the fianchetto of the king's bishop (Bg2) — a flexible, hypermodern setup.",
 "b3": "Prepares Bb2 fianchetto and can transpose to English/London structures.",
 "e3": "A quiet, solid move: supports d4 and opens the bishop's diagonal without weakening anything.",
 "d3": "Supports the e4 pawn and opens the queen's bishop diagonal — solid but a bit passive.",
 "c3": "Supports a d4 pawn break and prepares b4/Qb3 ideas in gambit lines.",
 "f4": "A pawn gambit strike against e5/f7 — aggressive and double-edged.",
 "b4": "The Evans Gambit pawn offer: opens the a1–h8 diagonal and speeds up development.",
 "Bb5": "The Ruy Lopez move: pins the c6 knight and pressures f7/e5 indirectly.",
 "Bc4": "Aims at f7, the weakest square around the black king — quick development with threats.",
 "Bb4+": "Checks and pins the c3 knight, forcing weaknesses or exchanges (Nimzo/Winawer idea).",
 "Bd3": "Develops the bishop to a solid square, eyeing h7 and supporting e4/d4.",
 "Be2": "A flexible developing move that keeps the king's options open (often before castling).",
 "Bf4": "The London System bishop: eyes the long diagonal toward h6 and supports e3/d4.",
 "Bg5": "Pins the f6 knight against the queen — wins time by forcing a reaction.",
 "O-O": "Castles kingside: king to safety, rook to the center — the standard development move.",
 "O-O-O": "Castles queenside: king safety plus the rook lands on the d-file, often in open/queen-side pawn games.",
 "a6": "Asks the bishop to retreat (Ruy Lopez) or prevents Bb5/Nb5 — a useful waiting/forcing pawn move.",
 "a5": "Gains space on the queenside and kicks the bishop/knight (Ruy Lopez main line).",
 "b5": "Gains queenside space and attacks c4 — typical in gambits and the Grünfeld.",
 "c5": "The Sicilian/central counter: fights for d4 immediately, often with tempo.",
 "c6": "Supports a coming ...d5 break while keeping the light-squared bishop free (Caro/Slav/QGD).",
 "d5": "The central break: challenges e4/c4 and opens the position for both sides.",
 "d6": "Supports e5 and prepares ...Nf6/...Be7 — solid, slightly passive (Philidor/Pirc/Sicilian).",
 "e5": "The central pawn push: grabs space and opens lines; often the critical test of an opening.",
 "e6": "Supports d5 and opens the queen's bishop — the French/Slav/QGD building block.",
 "g6": "Prepares the ...Bg7 fianchetto and weakens the long diagonal — hypermodern (KID/Grünfeld/Pirc).",
 "Nf6": "Develops and attacks e4 — Black's most active reply to 1.e4 and the start of many Indian defences.",
 "Nc6": "Defends e5 and develops toward the center — the main classical reply to 1.e4 e5.",
 "exd4": "Captures in the center, opening the e-file and clarifying the pawn structure.",
 "exd5": "Central capture that usually leads to an open game or a pawn-up gambit structure.",
 "exf4": "Accepts the gambit pawn: Black takes the pawn and must then survive the attack.",
 "dxc4": "Captures the gambit pawn (Grünfeld/QGA): Black takes and plans to give it back for development.",
 "fxe4": "Recaptures in the center, keeping material balance while opening the f-file.",
 "Qxd4": "Recaptures the pawn with the queen — active but the queen can become a target.",
 "Qe2": "A safe developing move that protects e4 and keeps castling options open (Petrov/Italian).",
 "Qh4": "An aggressive queen move that often comes with check ideas (Vienna/KG lines).",
 "Qh5": "Threatens mate on f7 (Scholar's-style ideas) — Black must react precisely.",
 "Bd7": "Develops the bishop behind the pawn shield, eyeing h3 and supporting ...e5/c5 breaks.",
 "Be7": "A solid developing square behind the pawns; prepares ...O-O and ...d5 breaks.",
 "Bb7": "Fianchettoes the queen's bishop on the long diagonal (QID/Grünfeld-style pressure on e4).",
 "Bg7": "Completes the kingside fianchetto — the hallmark of KID/Grünfeld/Pirc setups.",
 "Bd6": "Develops with tempo toward h2 and supports a ...e5/d5 central break.",
 "Bxf3": "Exchanges the knight, often doubling pawns or removing a defender (trade to simplify).",
 "Bxc6": "The Ruy exchange: doubles Black's pawns but opens the a/b files for White's rooks.",
 "Nxe4": "Captures the e4 pawn — grabbing material while opening the position.",
 "Nxe5": "Wins the e5 pawn, usually in Petrov/Scotch-type positions.",
 "Nxd4": "Recaptures the gambit pawn with the knight, centralizing it.",
 "Nxd5": "Central capture; often leads to an isolated queen's pawn or open play.",
 "g5": "A kingside pawn push to gain space and kick a knight on f4/h4 — double-edged.",
 "h6": "Kicks the bishop on g5 and prepares ...g5 — a standard prophylactic move.",
 "h5": "Gains kingside space; often a prelude to ...g5 attacks.",
}
