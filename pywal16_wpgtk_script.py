import wpgtk
import subprocess
import re
import sys


def get_wal_arg():

    WAL_ARG = sys.argv

    if((len(WAL_ARG) == 1) or (len(WAL_ARG) > 2)):
        print("pywal16_wpgtk_script:", error_output())
        sys.exit(0)

    return WAL_ARG[1]

def error_output():

    err_msg = "error: Too many or very few arguments"
    return err_msg

def exec_wal():

    WALL_DIR = wpgtk.data.config.WALL_DIR
    WALL_NAME = subprocess.check_output(['wpg', '-c'])

    DECODE_WALL_NAME = WALL_NAME.decode("utf-8").strip() #Decodes WALL_NAME since it cames as an object of type 'byte'

    WALL_FILE =  WALL_DIR + '/' + DECODE_WALL_NAME

    subprocess.run(["wal", "-i", WALL_FILE, "--cols16", get_wal_arg()])

def main():
    exec_wal()

main()
