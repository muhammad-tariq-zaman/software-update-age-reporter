import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from datetime import date
from main import report

NOW = date(2026, 11, 1)


def row(app, last):
    return {"application": app, "last_update": last}


class TestUpdateAge(unittest.TestCase):
    def test_overdue(self):
        self.assertEqual(report([row("A", "2026-06-01")], NOW, 90)[0][2], "OVERDUE")

    def test_due_soon(self):
        self.assertEqual(report([row("A", "2026-08-15")], NOW, 90)[0][2], "DUE SOON")

    def test_ok(self):
        self.assertEqual(report([row("A", "2026-10-15")], NOW, 90)[0][2], "OK")

    def test_oldest_first(self):
        result = report([row("New", "2026-10-01"), row("Old", "2026-01-01")], NOW, 90)
        self.assertEqual(result[0][0], "Old")
