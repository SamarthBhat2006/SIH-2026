"""
Infographic Generator Module
Renders AI-generated infographic briefs as professional visual PNG images
using matplotlib with a dark, NTRO-branded design.
"""

import io
import re
import textwrap
from pathlib import Path
from datetime import datetime
from typing import Dict, List

from config.settings import OUTPUTS_DIR


class InfographicGenerationError(Exception):
    """Custom exception for infographic generation errors."""
    pass


def _clean(text: str) -> str:
    """Remove non-ASCII / emoji characters safe for matplotlib text rendering."""
    return re.sub(r'[^\x00-\x7F]+', '', str(text)).strip()


def _wrap(text: str, width: int) -> List[str]:
    """Wrap text to a maximum character width."""
    return textwrap.wrap(_clean(str(text)), width=width) or [""]


def _parse_infographic_brief(markdown_text: str) -> Dict:
    """
    Parse the structured markdown infographic brief into a data dict.
    Returns: headline, stats, panels, key_message, footer
    """
    data = {
        "headline": "",
        "stats": [],
        "panels": [],
        "key_message": "",
        "footer": "",
    }

    lines = markdown_text.split("\n")
    current_section = None
    current_panel = None

    for line in lines:
        stripped = line.strip()

        # ── Section headers ──────────────────────────────────────────────────
        if re.search(r'##\s.*Headline', stripped, re.I):
            current_section = "headline"
            current_panel = None
        elif re.search(r'##\s.*Key Stats', stripped, re.I):
            current_section = "stats"
            current_panel = None
        elif re.search(r'##\s.*Visual Layout', stripped, re.I):
            current_section = "layout"
            current_panel = None
        elif re.search(r'##\s.*Section Panels', stripped, re.I):
            current_section = "panels"
            current_panel = None
        elif re.search(r'##\s.*Key Message', stripped, re.I):
            if current_panel:
                data["panels"].append(current_panel)
                current_panel = None
            current_section = "key_message"
        elif re.search(r'##\s.*Footer', stripped, re.I):
            current_section = "footer"

        # Panel sub-headers
        elif re.search(r'###\s.*Panel\s*\d+', stripped, re.I) and current_section == "panels":
            if current_panel:
                data["panels"].append(current_panel)
            raw_title = re.sub(r'^#+\s*Panel\s*\d+\s*[:\-]?\s*', '', stripped, flags=re.I)
            current_panel = {"title": _clean(raw_title)[:40], "bullets": []}

        # ── Content extraction ───────────────────────────────────────────────
        elif current_section == "headline":
            clean = stripped.strip("*").strip()
            if clean and not clean.startswith("#"):
                data["headline"] = _clean(clean)[:100]

        elif current_section == "stats" and "|" in stripped:
            if "Label" not in stripped and "---" not in stripped and stripped.startswith("|"):
                parts = [p.strip() for p in stripped.split("|") if p.strip()]
                if len(parts) >= 2:
                    label = _clean(parts[0])[:35].strip()
                    value = _clean(parts[1])[:60].strip()
                    if label:
                        data["stats"].append({"label": label or "Stat", "value": value or "N/A"})

        elif current_panel is not None and stripped.startswith(("•", "-", "*")):
            bullet = stripped.lstrip("•-* ").strip()
            bullet_clean = _clean(bullet)
            if bullet_clean:
                current_panel["bullets"].append(bullet_clean[:120])

        elif current_section == "key_message" and stripped and not stripped.startswith("#"):
            km = _clean(stripped)
            if km:
                data["key_message"] = (data["key_message"] + " " + km).strip()

        elif current_section == "footer" and stripped and not stripped.startswith("#"):
            f = _clean(stripped)
            if f:
                data["footer"] = f[:120]

    if current_panel:
        data["panels"].append(current_panel)

    return data


def build_infographic_image(markdown_text: str, doc_title: str = "") -> Path:
    """
    Render a professional dark-themed infographic PNG from the structured
    markdown brief. Returns the path to the saved PNG file.

    Requires matplotlib (pip install matplotlib).
    """
    try:
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive backend, safe for server use
        import matplotlib.pyplot as plt
        from matplotlib.patches import FancyBboxPatch
    except ImportError:
        raise InfographicGenerationError(
            "matplotlib is not installed. Run: pip install matplotlib"
        )

    # ── Parse data ───────────────────────────────────────────────────────────
    data = _parse_infographic_brief(markdown_text)

    headline  = data["headline"] or _clean(doc_title) or "Intelligence Infographic"
    stats     = data["stats"][:4]
    panels    = data["panels"][:3]
    key_msg   = data["key_message"] or "Immediate action and coordinated response are required."
    footer    = data["footer"] or "Source: NTRO Intelligence Brief | Classification: Internal"

    # Pad stats to exactly 4
    _fallback_stats = [
        {"label": "Target Audience", "value": "NTRO Operators"},
        {"label": "Objective",       "value": "Inform & Alert"},
        {"label": "Source Type",     "value": "Intelligence Brief"},
        {"label": "Output Format",   "value": "Infographic PNG"},
    ]
    while len(stats) < 4:
        stats.append(_fallback_stats[len(stats) % 4])

    # ── Color palette (NTRO dark theme) ──────────────────────────────────────
    C_BG       = "#0D1B2A"
    C_HEADER   = "#12253A"
    C_CARD     = "#1A2B3C"
    C_PANEL_BG = "#162032"
    C_BORDER   = "#2C4057"
    C_MSG_BG   = "#1A2F50"
    C_TEXT     = "#F0F4F8"
    C_MUTED    = "#8DA3B9"
    C_NTRO_PK  = "#FF4D6D"
    C_ACCENTS  = ["#E63946", "#FFB703", "#06D6A0", "#4361EE"]

    FIG_W = 14.0
    FIG_H = 20.0
    DPI   = 120

    fig = plt.figure(figsize=(FIG_W, FIG_H), facecolor=C_BG, dpi=DPI)
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    ax.set_facecolor(C_BG)

    # ── Drawing helpers ───────────────────────────────────────────────────────
    def rrect(x, y, w, h, color, radius=0.15, ec="none", lw=1.5, zorder=2, alpha=1.0):
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor=color, edgecolor=ec, linewidth=lw,
            alpha=alpha, zorder=zorder
        )
        ax.add_patch(box)

    def t(x, y, s, size=10, color=C_TEXT, ha="left", va="center",
          bold=False, zorder=5, alpha=1.0):
        ax.text(x, y, str(s),
                fontsize=size, color=color, ha=ha, va=va,
                fontweight="bold" if bold else "normal",
                zorder=zorder, alpha=alpha,
                transform=ax.transData)

    def hline(x0, x1, y, color, lw=1.0, zorder=3):
        ax.plot([x0, x1], [y, y], color=color, linewidth=lw, zorder=zorder,
                solid_capstyle="round")

    cur_y = FIG_H  # tracking vertical position top → down

    # ── HEADER ───────────────────────────────────────────────────────────────
    hdr_h = 3.4
    rrect(0, cur_y - hdr_h, FIG_W, hdr_h, C_HEADER, radius=0.0, zorder=1)
    # Top accent stripe
    ax.axhline(cur_y, color=C_ACCENTS[0], linewidth=6, zorder=3)

    # NTRO badge
    badge_x = FIG_W - 2.1
    rrect(badge_x, cur_y - 0.78, 1.8, 0.50, C_NTRO_PK, radius=0.12, zorder=4)
    t(badge_x + 0.9, cur_y - 0.53, "NTRO CORE",
      size=9, color="white", ha="center", bold=True, zorder=5)

    # "INFOGRAPHIC" tag
    t(0.55, cur_y - 0.65, "INTELLIGENCE  INFOGRAPHIC",
      size=8, color=C_MUTED, ha="left", bold=False, zorder=4)

    # Headline text (wrapped, large)
    hl_lines = _wrap(headline.upper(), 52)
    for i, hl in enumerate(hl_lines[:3]):
        t(0.55, cur_y - 1.35 - i * 0.60,
          hl, size=19 if i == 0 else 16,
          color=C_TEXT, bold=True, ha="left", zorder=4)

    # Thin accent line at header bottom
    hline(0.55, FIG_W - 0.55, cur_y - hdr_h + 0.45, C_ACCENTS[0], lw=1.8)
    cur_y -= hdr_h + 0.35

    # ── SECTION LABEL ────────────────────────────────────────────────────────
    t(0.55, cur_y - 0.05, "KEY STATISTICS",
      size=8, color=C_MUTED, bold=True, ha="left", zorder=4)
    cur_y -= 0.5

    # ── STAT CARDS ROW ───────────────────────────────────────────────────────
    card_gap = 0.28
    card_w   = (FIG_W - 1.1 - card_gap * 3) / 4
    card_h   = 2.0

    for i, stat in enumerate(stats):
        cx = 0.55 + i * (card_w + card_gap)
        cy = cur_y - card_h
        acc = C_ACCENTS[i % 4]

        # Card background + border
        rrect(cx, cy, card_w, card_h, C_CARD, ec=acc, lw=1.5, radius=0.14, zorder=2)
        # Accent top bar
        rrect(cx, cy + card_h - 0.14, card_w, 0.14, acc, radius=0.0, zorder=3)

        mid_x = cx + card_w / 2

        # Value
        val_lines = _wrap(stat["value"], 16)
        t(mid_x, cy + card_h * 0.60, val_lines[0],
          size=12, color=acc, bold=True, ha="center", zorder=4)
        if len(val_lines) > 1:
            t(mid_x, cy + card_h * 0.43, val_lines[1],
              size=10, color=acc, bold=True, ha="center", zorder=4)

        # Label
        lbl_lines = _wrap(stat["label"], 18)
        t(mid_x, cy + 0.28, lbl_lines[0],
          size=8, color=C_MUTED, ha="center", zorder=4)

    cur_y -= card_h + 0.5

    # ── SECTION LABEL ────────────────────────────────────────────────────────
    t(0.55, cur_y - 0.05, "INTELLIGENCE PANELS",
      size=8, color=C_MUTED, bold=True, ha="left", zorder=4)
    cur_y -= 0.5

    # ── CONTENT PANELS ───────────────────────────────────────────────────────
    panel_gap = 0.28
    n_panels  = max(len(panels), 1)
    panel_w   = (FIG_W - 1.1 - panel_gap * (n_panels - 1)) / n_panels
    panel_h   = 4.6

    if panels:
        for i, panel in enumerate(panels):
            acc  = C_ACCENTS[i % 4]
            px   = 0.55 + i * (panel_w + panel_gap)
            py   = cur_y - panel_h

            rrect(px, py, panel_w, panel_h, C_PANEL_BG, ec=C_BORDER, lw=1.2, radius=0.15, zorder=2)
            # Panel header strip
            rrect(px, py + panel_h - 0.65, panel_w, 0.65, acc, radius=0.0, zorder=3)

            # Panel title
            ptitle = panel.get("title", f"Panel {i+1}")
            pt_lines = _wrap(ptitle, max(int(panel_w * 7), 15))
            t(px + panel_w / 2, py + panel_h - 0.30,
              pt_lines[0][:32], size=10, color="white",
              bold=True, ha="center", va="center", zorder=4)

            # Bullet points
            bullet_y = py + panel_h - 0.95
            for j, bullet in enumerate(panel.get("bullets", [])[:5]):
                if bullet_y < py + 0.25:
                    break
                b_lines = _wrap(bullet, max(int(panel_w * 8), 20))

                # Bullet circle
                ax.plot(px + 0.24, bullet_y, 'o', markersize=5,
                        color=acc, zorder=4)

                for k, bl in enumerate(b_lines[:3]):
                    t(px + 0.42, bullet_y - k * 0.27,
                      bl, size=8.5, color=C_TEXT, ha="left", va="center", zorder=4)

                bullet_y -= (0.28 * min(len(b_lines[:3]), 2)) + 0.52
    else:
        # Placeholder if no panels parsed
        rrect(0.55, cur_y - panel_h, FIG_W - 1.1, panel_h,
              C_PANEL_BG, radius=0.15, zorder=2)
        t(FIG_W / 2, cur_y - panel_h / 2,
          "Intelligence content from source document.",
          size=11, color=C_MUTED, ha="center", va="center", zorder=3)

    cur_y -= panel_h + 0.45

    # ── KEY MESSAGE BANNER ────────────────────────────────────────────────────
    msg_h = 1.65
    rrect(0.55, cur_y - msg_h, FIG_W - 1.1, msg_h, C_MSG_BG, radius=0.15, zorder=2)
    # Left accent stripe
    rrect(0.55, cur_y - msg_h, 0.08, msg_h, C_ACCENTS[0], radius=0.0, zorder=3)

    t(0.85, cur_y - 0.35, "KEY MESSAGE",
      size=8, color=C_ACCENTS[0], bold=True, ha="left", va="center", zorder=4)

    km_lines = _wrap(key_msg, 95)
    for i, ml in enumerate(km_lines[:3]):
        t(0.85, cur_y - 0.70 - i * 0.32,
          ml, size=9, color=C_TEXT, ha="left", va="center", zorder=4)

    cur_y -= msg_h + 0.4

    # ── FOOTER ────────────────────────────────────────────────────────────────
    footer_h = 0.65
    rrect(0, cur_y - footer_h, FIG_W, footer_h, C_HEADER, radius=0.0, zorder=2)
    ax.axhline(cur_y, color=C_ACCENTS[0], linewidth=3, zorder=3)

    ft_clean = _clean(footer)
    t(0.55, cur_y - footer_h / 2,
      ft_clean[:100], size=8, color=C_MUTED, ha="left", va="center", zorder=4)
    ts = datetime.now().strftime("%d %b %Y, %H:%M")
    t(FIG_W - 0.55, cur_y - footer_h / 2,
      f"Generated: {ts}", size=8, color=C_MUTED, ha="right", va="center", zorder=4)

    # ── SAVE FILE ─────────────────────────────────────────────────────────────
    OUTPUTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path  = OUTPUTS_DIR / f"AI_Infographic_{timestamp}.png"

    plt.savefig(
        str(out_path), dpi=DPI,
        bbox_inches="tight",
        facecolor=C_BG, edgecolor="none"
    )
    plt.close(fig)

    return out_path
