#!/usr/bin/env python3
"""Measure a still's tone and colour, optionally against a target look lane.

The lanes and their reference stills are described in ../LOOKS.md. The numbers
are only a check on exposure, palette and finish; the owner's eye decides.

Usage:
  python3 measure_look.py IMAGE [IMAGE ...] [--lane A|B|C|D] [--crop x0,y0,x1,y1]

Columns (0-255 scales):
  sat     mean HSV saturation
  lum     mean luminance
  sd      luminance standard deviation (contrast)
  black   1st-percentile luminance (lifted blacks read high)
  white   99th-percentile luminance (clipped whites read 250+)
  dark%   share of pixels darker than 40
  vig     corner luminance / centre luminance (below 1 = darker corners)
  shR-B   red minus blue in the darkest 20% (negative = cool shadows)
  shG     green minus the red-blue average in the darkest 20% (positive = green-teal shadows)
  hiR-B   red minus blue in the brightest 10% (positive = warm highlights)
"""
import argparse
import statistics

from PIL import Image

# Ranges come from the owner's reference stills (LOOKS.md), widened a little,
# because the references were measured from compressed phone screenshots.
TARGETS = {
    "A": {"sat": (100, 135), "lum": (90, 120), "black": (20, 45), "white": (195, 235),
          "dark%": (0, 12), "vig": (0.45, 0.85), "shR-B": (-80, -15), "hiR-B": (0, 45)},
    # B is locked on LB04 (owner, 2026-11-25): re-centred on LB04 and the B1 reference.
    "B": {"sat": (75, 120), "lum": (85, 110), "black": (5, 45), "white": (185, 235),
          "dark%": (0, 15), "shR-B": (-5, 35), "hiR-B": (35, 80)},
    "C": {"sat": (20, 55), "lum": (55, 85), "sd": (20, 50), "white": (150, 220),
          "dark%": (0, 35)},
    "D": {"sat": (50, 100), "lum": (50, 100), "white": (110, 235), "dark%": (5, 55),
          "shR-B": (-25, 15), "shG": (2, 25), "hiR-B": (-35, 60)},
}

COLUMNS = ["sat", "lum", "sd", "black", "white", "dark%", "vig", "shR-B", "shG", "hiR-B"]


def measure(path, crop=None):
    im = Image.open(path).convert("RGB")
    if crop:
        im = im.crop(crop)
    im.thumbnail((300, 400))
    w, h = im.size
    lum = list(im.convert("L").tobytes())
    sat = list(im.convert("HSV").getchannel("S").tobytes())
    raw = im.tobytes()
    rgb = [(raw[i], raw[i + 1], raw[i + 2]) for i in range(0, len(raw), 3)]

    order = sorted(lum)
    n = len(order)

    def pct(p):
        return order[min(n - 1, int(n * p))]

    def box_mean(x0, y0, x1, y1):
        vals = [lum[y * w + x] for y in range(int(y0), int(y1)) for x in range(int(x0), int(x1))]
        return statistics.fmean(vals)

    cw, ch = w * 0.15, h * 0.15
    corners = statistics.fmean([
        box_mean(0, 0, cw, ch), box_mean(w - cw, 0, w, ch),
        box_mean(0, h - ch, cw, h), box_mean(w - cw, h - ch, w, h),
    ])
    centre = box_mean(w * 0.3, h * 0.3, w * 0.7, h * 0.7)

    lo, hi = pct(0.20), pct(0.90)
    shadows = [p for p, l in zip(rgb, lum) if l <= lo]
    highs = [p for p, l in zip(rgb, lum) if l >= hi]

    def r_minus_b(px):
        return statistics.fmean(p[0] - p[2] for p in px) if px else 0.0

    return {
        "sat": statistics.fmean(sat),
        "lum": statistics.fmean(lum),
        "sd": statistics.pstdev(lum),
        "black": pct(0.01),
        "white": pct(0.99),
        "dark%": 100 * sum(1 for l in lum if l < 40) / n,
        "vig": corners / centre if centre else 0.0,
        "shR-B": r_minus_b(shadows),
        "shG": statistics.fmean(p[1] - (p[0] + p[2]) / 2 for p in shadows) if shadows else 0.0,
        "hiR-B": r_minus_b(highs),
    }


def fmt(key, value):
    return f"{value:.2f}" if key == "vig" else f"{value:.0f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="+")
    ap.add_argument("--lane", choices=sorted(TARGETS))
    ap.add_argument("--crop", help="x0,y0,x1,y1 in source pixels, e.g. to cut phone UI")
    args = ap.parse_args()
    crop = tuple(int(v) for v in args.crop.split(",")) if args.crop else None
    target = TARGETS.get(args.lane, {})

    print("image".ljust(36) + "".join(c.rjust(8) for c in COLUMNS) + ("   off-target" if target else ""))
    for path in args.images:
        m = measure(path, crop)
        misses = [f"{k} {fmt(k, m[k])} (want {lo}-{hi})"
                  for k, (lo, hi) in target.items() if not lo <= m[k] <= hi]
        name = path.rsplit("/", 1)[-1][:35]
        row = name.ljust(36) + "".join(fmt(c, m[c]).rjust(8) for c in COLUMNS)
        if target:
            row += "   " + ("on target" if not misses else "; ".join(misses))
        print(row)


if __name__ == "__main__":
    main()
