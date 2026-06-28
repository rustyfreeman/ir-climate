# IR Climate

Home Assistant integration for learned IR AC control via MQTT (Zigbee2MQTT UFO-R11 compatible).

## Features
- Climate entity
- YAML IR database
- MQTT transport
- Works with learned IR codes

## Install
Add to HACS as custom repository.

## Config
Use config flow in Home Assistant UI.

## Adding IR Codes

### Method 1: UI (Learn) button
Use the `learn` action in the device actions menu. This will learn one code and store it with a default name. You can rename it later in the UI.

### Method 2: Manual YAML (Best for large sets)
1. Put your codes in `climate/ir_climate_yourname.yaml`
2. Add to `climate/configuration.yaml`:

```yaml
- platform: ir_climate
  name: 'Your AC Name'
  device: yourdevice
  ir_codes_file: ir_climate_yourname.yaml
```

3. Restart HA, then open Configuration → Devices → yourdevice → Edit device
4. Click **Learn** for each state, paste your code, and give it a proper name.

#### YAML file format:
```yaml
spec_version: 1
mappings:
  on: AAAA
  off: BBBB
  fan_auto: CCCC
  fan_low: DDDD
  mode_cool: EEEE
  # etc.
```

This way you keep your IR codes in version control and can add them all at once.

## Advanced: Remote Control Emulation (Zigbee2MQTT 1.41+)

The integration supports Zigbee2MQTT's remote control emulation via `ir_bridge` MQTT topic. See the **Remote Control** section in the UI settings.
