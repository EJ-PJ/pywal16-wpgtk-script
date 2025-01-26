import wpgtk
import subprocess
import re

WALL_DIR = wpgtk.data.config.WALL_DIR
WALL_NAME = str(subprocess.check_output(['wpg', '-c']))

WALL_FILE =  WALL_DIR + '/' + WALL_NAME

PARSE_WALL_FILE = re.findall(r"'(.*?)'", WALL_FILE)

print("WALL DIR: ", type(WALL_DIR))
print("WALL NAME: ", type(WALL_NAME))
print("WALL FILE: ", WALL_FILE)
print("PARSE WALL FILE: ", PARSE_WALL_FILE)
