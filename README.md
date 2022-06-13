# RG57H3
Results of reverse engineering the RG57H3(B)/BGCEF-M remote that came with a Trotec PAC 2100 X air conditioner

# Repo files
- main.py - Py3 script that was used to generate the IRP notation for all the codes
- raw_commands.txt - Output from running main.py
- broadlink.txt - All the commands converted to Broadlink base64 format
- 9999.json - [SmartIR](https://github.com/smartHomeHub/SmartIR) codes JSON file to control the AC
- ha_automation.yaml - A Home Assistant automation that will send out temperature readouts to the AC every 30 seconds.

# How do I integrate my AC to Home Assistant?
1. Buy a Broadlink IR blaster. [RM4 Mini](https://www.amazon.co.uk/dp/B07ZSG9Y67/) if you only want IR functionality, [RM4 Pro](https://www.amazon.co.uk/dp/B083LLLVPN/) if you also want to be able to send 433MHz commands for other devices.
2. [Integrate remote into Home Assistant.](https://www.home-assistant.io/integrations/broadlink/)
3. Install [SmartIR](https://github.com/smartHomeHub/SmartIR) and copy `9999.json` to `config/custom_components/smartir/codes/climate/` if the file hasn't already been merged into SmartIR. Follow SmartIR instructions for setting up the AC, use 9999 for device code. Restart HA.

This is enough to control the AC, use any thermostat card to control the AC. But [Simple Thermostat](https://github.com/nervetattoo/simple-thermostat) is really nice.

# Send temperature updates from HA to AC
1. Add temperature readout codes to `config/.storage/broadlink_remote_XXXXXXXXXXXX_codes` (from `broadlink_remote_codes_ha.json`) - change the key to match your device's ID.
2. Restart Home Assistant after changing the codes file. The codes aren't updated when the file is changed outside of Home Assistant.
3. Create automation
4. Open it in YAML mode
5. Empty it, paste in contents from `ha_automation.yaml`.
6. In each `conditions` statement, set `device_id` and `entity_id` for your temperature sensor, and `device_id` in each service call to point to your remote.

You can revert to the visual editor to simplify getting the required values.

# Why the mismatch between conditions and the readout values being sent to the AC?

The difference compensates for AC's behavior - if set in a sensible way, with a setpoint of 25C set, AC stops cooling at 25.99C. By sending one degree lower values, a 25C setpoint attempts to maintain temperature at 25C.