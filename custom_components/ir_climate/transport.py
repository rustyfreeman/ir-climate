
import json
from homeassistant.components import mqtt
import logging
_LOGGER = logging.getLogger(__name__)

class MQTTTransport:
    def __init__(self, hass, topic):
        self.hass = hass
        self.topic = topic

    async def send(self, code: str):
        _LOGGER.warning("IR sending to %s: %s...", self.topic, code[:20])
        
        payload = {
            "ir_code_to_send": code
        }

        await mqtt.async_publish(
            self.hass,
            self.topic,
            json.dumps(payload),
            qos=0,
            retain=False,
        )
