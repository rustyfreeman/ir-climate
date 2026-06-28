
import json
from homeassistant.components import mqtt

class MQTTTransport:
    def __init__(self, hass, topic):
        self.hass = hass
        self.topic = topic

    async def send(self, code: str):
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
