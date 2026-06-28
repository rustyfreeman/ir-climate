
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import HVACMode, ClimateEntityFeature
from homeassistant.const import UnitOfTemperature

from .resolver import Resolver
from .transport import MQTTTransport
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the climate platform from a config entry."""
    db = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        IRClimate(hass, entry, db)
    ])

class IRClimate(ClimateEntity):

    def __init__(self, hass, entry, db):
        self.hass = hass

        self._attr_name = entry.data["name"]
        self._attr_hvac_modes = [
            HVACMode.OFF,
            HVACMode.COOL,
            HVACMode.HEAT,
            HVACMode.DRY,
            HVACMode.FAN_ONLY,
            HVACMode.AUTO,
        ]

        self._attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
        self._attr_temperature_unit = UnitOfTemperature.CELSIUS

        self._resolver = Resolver(db)
        self._transport = MQTTTransport(hass, entry.data["mqtt_topic"])

        self._attr_hvac_mode = HVACMode.OFF
        self._attr_target_temperature = 24

    async def async_set_hvac_mode(self, hvac_mode):
        self._attr_hvac_mode = hvac_mode

        if hvac_mode == HVACMode.OFF:
            code = self._resolver.get_code("off")
        else:
            code = self._resolver.get_code(
                hvac_mode.lower().replace("_only",""),
                self._attr_target_temperature
            )

        await self._transport.send(code)
        self.async_write_ha_state()

    async def async_set_temperature(self, **kwargs):
        if "temperature" not in kwargs:
            return

        self._attr_target_temperature = int(kwargs["temperature"])

        if self._attr_hvac_mode in (HVACMode.COOL, HVACMode.HEAT):
            code = self._resolver.get_code(
                self._attr_hvac_mode.lower(),
                self._attr_target_temperature
            )
            await self._transport.send(code)

        self.async_write_ha_state()
