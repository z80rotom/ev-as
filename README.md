# ev-as (Multi-Language Fork)

Assembler for EvScripts from Pokemon BDSP

This is a fork of ev-as that aims to add multi-language support, since ev-as defaults to English. Now it's possible to use a command like `python src/ev_as.py --language spanish` to write the macro messages to the Spanish files.

## ev-as Usage

Takes EvScript (.ev) files from the `scripts` folder and assembles them into the Unity ev_script bundle. The tool reads the original ev_script file from the `Dpr` folder and outputs the assembled result to the `bin` folder.

**Important folder structure:**

- **Input ev_script file**: Must be in the `Dpr` folder
- **Script files to assemble**: Must be in the `scripts` folder (not `parsed`)
- **Output assembled file**: Will be placed in the `bin` folder

Basic example: `python src/ev_as.py`

### Multi-Language Support

You can now specify a language when assembling scripts to write macro messages to the appropriate language files:

Example: `python src/ev_as.py --language spanish`

**Language file requirements:**

- Language files must be inside a folder called `AssetFolder`
- Files must be in language-specific export folders: `spanish_Export`, `english_Export`, `french_Export`, `german_Export`
- This follows the same folder structure as the BDSP-Repacker

## ev-parse

Parser for EvScripts from Pokemon BDSP that extracts and decompiles scripts from the Unity ev_script bundle.

### ev-parse Usage

Takes an ev_script file and extracts all individual script files, decompiling them into readable .ev format.

**Input**: ev_script file from the `Dpr` folder  
**Output**: Extracted .ev files will be placed in the `parsed` folder

Example: `python src/ev_parse.py`

**Note**: The `parsed` folder is for output only. When assembling with ev-as, only scripts from the `scripts` folder are used.

## Tool Setup

```bash
pip install -r requirements.txt
```

## EvScript

EvScript refers to scripts with an assembly-like syntax that use EvCmd's as defined by BDSP. All currently known EvCmd's can be found in ev_cmd.csv, and examples for EvScripts can be found in the examples directly.
If you want to edit existing scripts the best way is by dumping all the scripts with ev-parse and then editing them before assembling and repacking them with this program.
