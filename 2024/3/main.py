import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from lib.utils import load_input


INPUT = load_input(year=2024, day=3)