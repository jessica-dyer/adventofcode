from pathlib import Path
from aocd import get_data
from dotenv import load_dotenv
import os
from pathlib import Path
import inspect

root_dir = Path(__file__).resolve().parent.parent  # adjust as needed
load_dotenv(dotenv_path=root_dir / ".env")

# Get the session token
SESSION = os.getenv("AOC_TOKEN")


def get_caller_dir() -> Path:
    """Returns the directory of the calling script."""
    frame = inspect.stack()[2]  # [0]=current, [1]=this fn, [2]=caller
    caller_file = frame.filename
    return Path(caller_file).resolve().parent


def load_input(year: int, day: int):
    caller_dir = get_caller_dir()
    input_path = caller_dir / "input.txt"

    if data_available_locally(path=input_path):
        return input_path.read_text()
    else:
        data = get_data(session=SESSION, day=day, year=year)
        input_path.write_text(data)
        return data


def data_available_locally(path: Path):
    return path.exists()

if __name__ == "__main__":
   print("foo")