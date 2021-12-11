# ev-as
Assembler for EvScripts from Pokemon BDSP

# Usage
Takes an EvScript (.ev) file and assembles it and repacks it into the Unity ev_script bundle.

Example: src/main.py -i d05r0114.ev -o Dpr/ev_scripts -s d05r0114

# EvScript
EvScript refers to scripts with an assembly-like syntax that use EvCmd's as defined by BDSP. All currently known EvCmd's can be found in ev_cmd.csv, and examples for EvScripts can be found in the examples directly.
If you want to edit existing scripts the best way is by dumping all the scripts with ev-parse and then editing them before assembling and repacking them with this program.