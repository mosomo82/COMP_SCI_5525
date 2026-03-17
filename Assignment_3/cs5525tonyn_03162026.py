"""
HyperLogistics Package Tracker CLI
CS5525 Demo — Tony N — 03/16/2026
Stdlib only; compatible with python:3-alpine (no pip).
"""

import sys
import os
from datetime import date

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
STATUSES = ["Processing", "In Transit", "Out for Delivery", "Delivered"]

PACKAGES = [
    {
        "id": "HL-2026-00101",
        "description": "Industrial Sensor Array",
        "type": "Fragile",
        "weight_kg": 4.2,
        "origin": "Seattle, WA",
        "destination": "Boston, MA",
        "route": ["Seattle, WA", "Spokane, WA", "Billings, MT", "Minneapolis, MN", "Chicago, IL", "Boston, MA"],
        "current_hop": 3,
        "status": "In Transit",
        "eta": date(2026, 3, 20),
    },
    {
        "id": "HL-2026-00247",
        "description": "Medical Supply Kit",
        "type": "Priority",
        "weight_kg": 1.8,
        "origin": "Dallas, TX",
        "destination": "Miami, FL",
        "route": ["Dallas, TX", "Houston, TX", "New Orleans, LA", "Tampa, FL", "Miami, FL"],
        "current_hop": 4,
        "status": "Out for Delivery",
        "eta": date(2026, 3, 17),
    },
    {
        "id": "HL-2026-00389",
        "description": "Automotive Parts Set",
        "type": "Heavy",
        "weight_kg": 22.5,
        "origin": "Detroit, MI",
        "destination": "Phoenix, AZ",
        "route": ["Detroit, MI", "Indianapolis, IN", "St. Louis, MO", "Oklahoma City, OK", "Albuquerque, NM", "Phoenix, AZ"],
        "current_hop": 1,
        "status": "Processing",
        "eta": date(2026, 3, 24),
    },
    {
        "id": "HL-2026-00412",
        "description": "Consumer Electronics Bundle",
        "type": "Standard",
        "weight_kg": 3.1,
        "origin": "San Jose, CA",
        "destination": "New York, NY",
        "route": ["San Jose, CA", "Las Vegas, NV", "Denver, CO", "Kansas City, MO", "Pittsburgh, PA", "New York, NY"],
        "current_hop": 5,
        "status": "Delivered",
        "eta": date(2026, 3, 16),
    },
    {
        "id": "HL-2026-00558",
        "description": "Pharmaceutical Shipment",
        "type": "Priority",
        "weight_kg": 0.9,
        "origin": "Atlanta, GA",
        "destination": "Portland, OR",
        "route": ["Atlanta, GA", "Nashville, TN", "St. Louis, MO", "Denver, CO", "Salt Lake City, UT", "Portland, OR"],
        "current_hop": 2,
        "status": "In Transit",
        "eta": date(2026, 3, 21),
    },
    {
        "id": "HL-2026-00634",
        "description": "Lab Equipment",
        "type": "Fragile",
        "weight_kg": 7.6,
        "origin": "Chicago, IL",
        "destination": "San Diego, CA",
        "route": ["Chicago, IL", "Kansas City, MO", "Albuquerque, NM", "Phoenix, AZ", "San Diego, CA"],
        "current_hop": 0,
        "status": "Processing",
        "eta": date(2026, 3, 22),
    },
    {
        "id": "HL-2026-00721",
        "description": "Textbooks & Office Supplies",
        "type": "Standard",
        "weight_kg": 11.3,
        "origin": "Austin, TX",
        "destination": "Charlotte, NC",
        "route": ["Austin, TX", "Baton Rouge, LA", "Birmingham, AL", "Atlanta, GA", "Charlotte, NC"],
        "current_hop": 3,
        "status": "Out for Delivery",
        "eta": date(2026, 3, 17),
    },
    {
        "id": "HL-2026-00895",
        "description": "Smart Home Device Pack",
        "type": "Standard",
        "weight_kg": 2.4,
        "origin": "Portland, OR",
        "destination": "Philadelphia, PA",
        "route": ["Portland, OR", "Boise, ID", "Salt Lake City, UT", "Cheyenne, WY", "Omaha, NE", "Columbus, OH", "Philadelphia, PA"],
        "current_hop": 4,
        "status": "In Transit",
        "eta": date(2026, 3, 23),
    },
]

# Build a lookup dict by tracking ID
PKG_INDEX = {p["id"]: p for p in PACKAGES}

# ---------------------------------------------------------------------------
# Terminal width helper
# ---------------------------------------------------------------------------
def _tw():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
def print_banner():
    width = max(_tw(), 60)
    inner = width - 2  # inside the border chars
    line = "═" * inner
    tag1 = "H Y P E R L O G I S T I C S"
    tag2 = "Package Tracking System  •  v2026.3"
    tag3 = "Real-time Shipment Intelligence"

    print(f"╔{line}╗")
    print(f"║{tag1.center(inner)}║")
    print(f"║{'─' * inner}║")
    print(f"║{tag2.center(inner)}║")
    print(f"║{tag3.center(inner)}║")
    print(f"╚{line}╝")
    print()

# ---------------------------------------------------------------------------
# Summary table
# ---------------------------------------------------------------------------
_COL_WIDTHS = {
    "id":    14,
    "desc":  28,
    "type":  10,
    "orig":  16,
    "dest":  16,
    "stat":  18,
    "eta":   12,
    "kg":     6,
}

def _row(*cells, widths):
    parts = []
    keys = list(widths.keys())
    for i, cell in enumerate(cells):
        w = widths[keys[i]]
        parts.append(str(cell).ljust(w)[:w])
    return "│ " + " │ ".join(parts) + " │"

def _sep(widths, left="├", mid="┼", right="┤", fill="─"):
    return left + mid.join(fill * (w + 2) for w in widths.values()) + right

def print_table():
    w = _COL_WIDTHS
    header = _row("Tracking ID", "Description", "Type", "Origin", "Destination",
                   "Status", "ETA", "kg", widths=w)
    print("  SHIPMENT SUMMARY")
    print(_sep(w, "┌", "┬", "┐"))
    print(header)
    print(_sep(w))
    for p in PACKAGES:
        print(_row(
            p["id"], p["description"], p["type"],
            p["origin"], p["destination"],
            p["status"], p["eta"].strftime("%b %d, %Y"), f"{p['weight_kg']:.1f}",
            widths=w,
        ))
    print(_sep(w, "└", "┴", "┘"))
    print()

# ---------------------------------------------------------------------------
# Stats overview
# ---------------------------------------------------------------------------
def print_stats():
    counts = {s: 0 for s in STATUSES}
    total_weight = 0.0
    for p in PACKAGES:
        counts[p["status"]] += 1
        total_weight += p["weight_kg"]

    status_icons = {
        "Processing":       "⏳",
        "In Transit":       "🚚",
        "Out for Delivery": "📦",
        "Delivered":        "✅",
    }

    width = max(_tw(), 60)
    inner = width - 2
    bar_max = inner - 30  # space for the bar itself

    print("  FLEET STATUS OVERVIEW")
    print("┌" + "─" * inner + "┐")
    for status in STATUSES:
        count = counts[status]
        icon  = status_icons[status]
        pct   = (count / len(PACKAGES)) * 100 if PACKAGES else 0
        filled = int(bar_max * count / len(PACKAGES)) if PACKAGES else 0
        bar = "█" * filled + "░" * (bar_max - filled)
        label = f" {icon} {status:<18} {count:>2} pkgs  {pct:5.1f}%  {bar}"
        print(f"│{label:<{inner}}│")
    divider = f"│  {'─' * (inner - 4)}  │"
    print(divider)
    summary = f"  Total packages: {len(PACKAGES)}   Total weight: {total_weight:.1f} kg"
    print(f"│{summary:<{inner}}│")
    print("└" + "─" * inner + "┘")
    print()

# ---------------------------------------------------------------------------
# Detailed route view
# ---------------------------------------------------------------------------
def print_detail(pkg_id: str):
    p = PKG_INDEX.get(pkg_id)
    if p is None:
        print(f"  [!] Tracking ID '{pkg_id}' not found in system.\n")
        return

    width = max(_tw(), 60)
    inner = width - 2

    print("┌" + "═" * inner + "┐")
    print(f"│  PACKAGE DETAIL — {p['id']:<{inner - 20}}│")
    print("├" + "─" * inner + "┤")

    fields = [
        ("Description",  p["description"]),
        ("Type",         p["type"]),
        ("Weight",       f"{p['weight_kg']} kg"),
        ("Origin",       p["origin"]),
        ("Destination",  p["destination"]),
        ("Status",       p["status"]),
        ("ETA",          p["eta"].strftime("%A, %B %d, %Y")),
    ]
    for label, value in fields:
        line = f"  {label:<14}: {value}"
        print(f"│{line:<{inner}}│")

    print("├" + "─" * inner + "┤")
    print(f"│{'  ROUTE HOPS':^{inner}}│")
    print("├" + "─" * inner + "┤")

    route = p["route"]
    current = p["current_hop"]
    for i, hop in enumerate(route):
        if i < current:
            marker = "  ✓"
            connector = "  │"
        elif i == current:
            marker = "  ▶"
            connector = "  │"
        else:
            marker = "   "
            connector = "   "

        hop_line = f"{marker}  [{i + 1}] {hop}"
        if i == current:
            hop_line += "  ◀ current location"
        print(f"│{hop_line:<{inner}}│")

        if i < len(route) - 1:
            print(f"│{connector:<{inner}}│")

    print("└" + "═" * inner + "┘")
    print()

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print_banner()
    print_table()
    print_stats()

    # Always show route detail for the first package (Docker-safe default)
    print(f"  DETAILED ROUTE — {PACKAGES[0]['id']}")
    print()
    print_detail(PACKAGES[0]["id"])

    # Interactive TTY mode
    if sys.stdin.isatty():
        print("  ─── Interactive Lookup ───")
        print("  Enter a Tracking ID to view route details (or 'q' to quit).")
        print()
        while True:
            try:
                raw = input("  Tracking ID > ").strip().upper()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if raw in ("Q", "QUIT", "EXIT", ""):
                break
            print_detail(raw)


if __name__ == "__main__":
    main()
