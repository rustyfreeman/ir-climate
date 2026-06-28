
from .loader import load_codes
from .climate import IRClimate

async def async_setup_entry(hass, entry, async_add_entities):
    db = load_codes(entry.data["codes_file"])

    async_add_entities([
        IRClimate(hass, entry, db)
    ])
