# RG57H3
Results of reverse engineering the RG57H3(B)/BGCEF-M remote that came with a Trotec PAC 2100 X air conditioner

# Repo files
- main.py - Py3 script that was used to generate the IRP notation for all the codes
- raw_commands.txt - Output from running main.py
- broadlink.txt - All the commands converted to Broadlink base64 format
- 9999.json - [SmartIR](https://github.com/smartHomeHub/SmartIR) codes JSON file to control the AC
- ha_automation.yaml - A Home Assistant automation that will send out temperature readouts to the AC every 30 seconds.