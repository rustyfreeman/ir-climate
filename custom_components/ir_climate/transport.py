
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

        payload_str = json.dumps(payload)
        _LOGGER.warning("MQTT payload bytes: %r", payload_str)

        await mqtt.async_publish(
            self.hass,
            self.topic,
            json.dumps(payload),
            qos=0,
            retain=False,
        )
