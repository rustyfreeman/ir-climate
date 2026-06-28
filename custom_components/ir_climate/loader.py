import yaml
from pathlib import Path

def load_codes(hass, file_name: str):
    # Looks in <config>/custom_components/ir_climate/codes/<file>
    path = Path(__file__).parent / "codes" / file_name
    
    if not path.exists():
        raise FileNotFoundError(f"Missing IR code file: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)