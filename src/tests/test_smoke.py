import sys
sys.path.append("src")

from zikora import health

def test_health():
    assert health() == "ok"
