# pywal16-wpgtk-script

A simple script to enable the use of pywal 16 colors in wpgtk.

## Installation 

Clone the repo
```bash
git clone https://github.com/EJ-PJ/pywal16-wpgtk-script.git
```

In your configuration file 'wpg.conf', change the value of the 'execute_cmd' setting to 'true', 
and set the 'command' value to the path of the Python script.

```bash
execute_cmd = true
```

```bash
command = python3 /path/to/the/script/pywal16-wpgtk-script.py --flag
```

## Usage 

By simply passing the flags to the scripts you can ither choose between 'darken' or 'lighten'

```bash
pywal16-wpgtk-script.py [--darken | --lighten] [-d | -l]

options:
    -d --darken	    Use 16 color output "darken"
    -l --ligth	    Use 16 color output "lighten"
```

For example you can edit the flag value of the script.

```bash
command = python3 /path/to/the/script/pywal16-wpgtk-script.py --darken
```

Or directly use the 'Options' tab in the wpg GUI by enabling the 'Run command after' 
option and editing the 'command' entry.

![alt text](https://github.com/EJ-PJ/pywal16-wpgtk-script/wpgtk-gui-example.png?raw=true)

