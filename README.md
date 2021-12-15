# ev-as
Assembler for EvScripts from Pokemon BDSP

# ev-as Usage
Takes an EvScript (.ev) file and assembles it and repacks it into the Unity ev_script bundle.

Example: src/ev_as.py -i d05r0114.ev -o Dpr/ev_scripts -s d05r0114

# ev-parse
Parser for EvScripts from Pokemon BDSP

# ev-parse Usage
Takes an ev_script file and extracts and parses all of the individual script files

Example:
src/ev_parse.py -i Dpr/ev_script

# Tool Setup
pip install -r requirements.txt

# EvScript
EvScript refers to scripts with an assembly-like syntax that use EvCmd's as defined by BDSP. All currently known EvCmd's can be found in ev_cmd.csv, and examples for EvScripts can be found in the examples directly.
If you want to edit existing scripts the best way is by dumping all the scripts with ev-parse and then editing them before assembling and repacking them with this program.
