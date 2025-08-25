import sys
import os

# ensure src folder is in path
sys.path.append(os.path.abspath("src"))

from zikora import health


def test_health():
    assert health() == "ok"
