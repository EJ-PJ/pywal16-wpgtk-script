import wpgtk
import subprocess
import sys

def get_wal_arg():

    WAL_ARG = sys.argv

    if (len(WAL_ARG) == 1) or (len(WAL_ARG) > 2):
        error_output(error_num=1)
        sys.exit(0)

    if (WAL_ARG[1] == "--darken") or (WAL_ARG[1] == "-d"):
        print("pywal16_wpgtk_script: using 16 color output 'darken'\n")
        return "darken"
    elif WAL_ARG[1] == "--lighten" or (WAL_ARG[1] == "-l"):
        print("pywal16_wpgtk_script: using 16 color output 'lighten'\n")
        return "lighten"
    else:
        error_output(error_num=2, wrong_arg=WAL_ARG[1])

def error_output(error_num, wrong_arg=''):

    ERR_MSG_PYWL = "pywal16_wpgtk_script"
    ERR_MSG_1 = "error: Too many or very few arguments"
    ERR_MSG_2 = f"error: '{wrong_arg}' Is not a valid argument"

    if error_num == 1:
        print(ERR_MSG_PYWL, ERR_MSG_1)
        sys.exit(0)
    elif error_num == 2:
        print(ERR_MSG_PYWL, ERR_MSG_2)
        sys.exit(0)

def exec_wal():

    WALL_DIR = wpgtk.data.config.WALL_DIR
    WALL_NAME = subprocess.check_output(['wpg', '-c'])

    DECODE_WALL_NAME = WALL_NAME.decode("utf-8").strip() #Decodes WALL_NAME since it cames as an object of type 'byte'

    WALL_FILE =  WALL_DIR + '/' + DECODE_WALL_NAME

    subprocess.run(["wal", "-i", WALL_FILE, "--cols16", get_wal_arg()])

def main():
    exec_wal()

main()
