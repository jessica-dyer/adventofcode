from pathlib import Path


def load_input():
    script_path = Path(__file__).resolve().parent
    input_path = script_path / "input.txt"
    return input_path.read_text()
