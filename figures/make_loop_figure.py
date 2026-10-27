# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Xavier Callens (SocrateAI Lab). See NOTICE.
"""Draw the Elenchus loop figure (English and French) with the Okabe-Ito palette.

Usage: python make_loop_figure.py [output_dir]
Writes elenchus-loop-en.{png,svg} and elenchus-loop-fr.{png,svg}.
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

# Okabe-Ito colour-blind-safe palette
OI = {
    "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73", "yellow": "#F0E442",
    "blue": "#0072B2", "vermillion": "#D55E00", "purple": "#CC79A7", "black": "#000000",
}

TEXT = {
    "en": {
        "title": "The Elenchus loop",
        "centre": "Every claim is\ncross-examined\nbefore it is believed",
        "stages": [
            ("AI proposes", "agents suggest ideas,\nproofs and code"),
            ("Calculation explores", "simulations and numbers\ntest the idea first"),
            ("Lean judges", "the proof checker accepts\nor rejects each step"),
            ("Humans decide\nwhat it means", "and whether to publish,\nincluding the failures"),
        ],
        "levels_title": "Four confidence levels",
        "levels": [
            ("A", "the judge looked", OI["green"]),
            ("L", "it is in a serious book", OI["blue"]),
            ("C", "someone reasoned,\nnobody machine-checked", OI["orange"]),
            ("X", "a pencil sketch", OI["purple"]),
        ],
        "foot": "Claims are written down before the test. Each test has a case that must pass and one that must fail.\n"
                "The maker is not the checker. Negative results are published. No human mathematician has reviewed this work.",
    },
    "fr": {
        "title": "La boucle Elenchus",
        "centre": "Chaque affirmation\nest interrogée\navant d'être crue",
        "stages": [
            ("L'IA propose", "des agents suggèrent idées,\npreuves et programmes"),
            ("Le calcul explore", "simulations et nombres\nmettent l'idée à l'épreuve"),
            ("Lean juge", "le vérificateur de preuves\naccepte ou refuse chaque pas"),
            ("L'humain décide\ndu sens", "et de publier, y compris\nles échecs"),
        ],
        "levels_title": "Quatre niveaux de confiance",
        "levels": [
            ("A", "le juge a regardé", OI["green"]),
            ("L", "c'est écrit dans\nun livre sérieux", OI["blue"]),
            ("C", "quelqu'un a raisonné,\npersonne n'a vérifié à la machine", OI["orange"]),
            ("X", "une esquisse au crayon", OI["purple"]),
        ],
        "foot": "L'affirmation est écrite avant le test. Chaque test a un cas qui doit réussir et un cas qui doit échouer.\n"
                "Celui qui fait n'est pas celui qui vérifie. Les résultats négatifs sont publiés. Aucun mathématicien humain n'a relu ce travail.",
    },
}

STAGE_COLOURS = [OI["vermillion"], OI["sky"], OI["green"], OI["orange"]]
# box centres (x, y) clockwise from top-left
CENTRES = [(2.6, 6.3), (7.4, 6.3), (7.4, 3.3), (2.6, 3.3)]
BOX_W, BOX_H = 3.6, 1.9


def draw(lang: str, out_dir: Path) -> list[Path]:
    t = TEXT[lang]
    fig, ax = plt.subplots(figsize=(10, 8.6), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.4, 8.0)
    ax.axis("off")
    ax.set_aspect("equal")
    fig.patch.set_facecolor("white")
    ax.text(5, 7.75, t["title"], ha="center", va="center", fontsize=20, weight="bold", color=OI["black"])
    for (cx, cy), (head, sub), col in zip(CENTRES, t["stages"], STAGE_COLOURS):
        box = FancyBboxPatch((cx - BOX_W / 2, cy - BOX_H / 2), BOX_W, BOX_H,
                             boxstyle="round,pad=0.05,rounding_size=0.25", linewidth=2.2,
                             edgecolor=col, facecolor=col + "22")
        ax.add_patch(box)
        ax.text(cx, cy + 0.38, head, ha="center", va="center", fontsize=14, weight="bold", color=OI["black"])
        ax.text(cx, cy - 0.5, sub, ha="center", va="center", fontsize=10.5, color="#333333")
    # clockwise arrows: top-left -> top-right -> bottom-right -> bottom-left -> top-left
    arrows = [((4.45, 6.3), (5.55, 6.3)), ((7.4, 5.3), (7.4, 4.3)), ((5.55, 3.3), (4.45, 3.3)), ((2.6, 4.3), (2.6, 5.3))]
    for a, b in arrows:
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=22, linewidth=2.2, color="#444444"))
    ax.text(5, 4.8, t["centre"], ha="center", va="center", fontsize=11.5, style="italic", color="#333333")
    ax.text(5, 1.55, t["levels_title"], ha="center", va="center", fontsize=13, weight="bold", color=OI["black"])
    xs = [1.25, 3.75, 6.25, 8.75]
    for x, (letter, words, col) in zip(xs, t["levels"]):
        ax.add_patch(plt.Circle((x, 0.75), 0.33, color=col))
        ax.text(x, 0.75, letter, ha="center", va="center", fontsize=14, weight="bold", color="white")
        ax.text(x, 0.05, words, ha="center", va="top", fontsize=9.5, color="#222222")
    ax.text(5, -1.2, t["foot"], ha="center", va="center", fontsize=8.6, color="#444444")
    outs = []
    for ext in ("png", "svg"):
        p = out_dir / f"elenchus-loop-{lang}.{ext}"
        meta = {"Date": None} if ext == "svg" else {}
        fig.savefig(p, bbox_inches="tight", facecolor="white", metadata=meta)
        outs.append(p)
    plt.close(fig)
    return outs


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    for lang in ("en", "fr"):
        for p in draw(lang, out_dir):
            print(p.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
