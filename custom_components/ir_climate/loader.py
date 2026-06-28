
import yaml
from pathlib import Path

def load_codes(file_name: str):
    path = Path("/config/ir_climate") / file_name

    if not path.exists():
        raise FileNotFoundError(f"Missing IR code file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
