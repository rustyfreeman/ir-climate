
import voluptuous as vol
from homeassistant import config_entries

DOMAIN = "ir_climate"

class IRClimateConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input
            )

        schema = vol.Schema({
            vol.Required("name"): str,
            vol.Required("codes_file"): str,
            vol.Required("mqtt_topic"): str,
        })

        return self.async_show_form(step_id="user", data_schema=schema)
