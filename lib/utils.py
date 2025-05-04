from pathlib import Path
from aocd import get_data
import os

# Get the session token
SESSION = os.getenv("AOC_TOKEN")


def load_input(year: int, day: int) -> str:
    from dotenv import load_dotenv
    import os

    load_dotenv()
    session = os.getenv("SESSION_TOKEN")

    input_path = (
        Path(__file__).resolve().parent.parent / "data" / str(year) / f"day{day:02}.txt"
    )
    input_path.parent.mkdir(parents=True, exist_ok=True)

    if input_path.exists():
        return input_path.read_text()
    else:
        data = get_data(session=session, year=year, day=day)
        input_path.write_text(data)
        return data
