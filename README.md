# pywal16-wpgtk-script

A simple script to enable the use of pywal 16 colors in wpgtk.

## Installation 

Clone the repo
```bash
git clone https://github.com/EJ-PJ/pywal16-wpgtk-script.git
```

In your configuration file `wpg.conf` , change the value of the `execute_cmd` setting to `true`.

```bash
execute_cmd = true
```

And set the `command` value to the path of the python script `pywal16-wpgtk-script.py`.

```bash
command = python3 /path/where/you/clone/the/repo/pywal16-wpgtk-script.py --flag
```

Or directly use the `Options` tab in the wpg GUI by enabling the `Run command after` 
option and editing the `Command` entry by setting the the path of the python script.

<img src="./wpgtk-gui-example.png" alt="wpgtk gui example" width="700">


## Usage 

By simply passing the flag to the script you can ither choose between `darken` or `lighten` 

```bash
pywal16-wpgtk-script.py [--darken | -d | --lighten | -l]

options:
    -d --darken	    Use 16 color output "darken"
    -l --ligthen    Use 16 color output "lighten"
```

For example you can edit the flag value of the script.
