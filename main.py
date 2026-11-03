"""Report how stale each application's last update is.

Usage: python3 main.py apps.csv [--now 2026-11-01] [--max-days 90]
CSV columns: application,last_update (ISO date).
Age over max-days is OVERDUE, over 80% of it is DUE SOON, else OK.
Oldest first, so the worst staleness is on top.
"""
import argparse, csv, sys
from datetime import date


def report(rows, now, max_days):
    out = []
    for row in rows:
        age = (now - date.fromisoformat(row["last_update"].strip())).days
        if age > max_days:
            verdict = "OVERDUE"
        elif age > 0.8 * max_days:
            verdict = "DUE SOON"
        else:
            verdict = "OK"
        out.append((row["application"], age, verdict))
    return sorted(out, key=lambda r: -r[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--now", default=None)
    parser.add_argument("--max-days", type=int, default=90)
    args = parser.parse_args(argv)
    now = date.fromisoformat(args.now) if args.now else date.today()
    with open(args.path, newline="", encoding="utf-8") as f:
        for app, age, verdict in report(list(csv.DictReader(f)), now, args.max_days):
            print(f"{app}: {verdict} ({age} days since update)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
