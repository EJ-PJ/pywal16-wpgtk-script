import wpgtk
import subprocess
import argparse

def get_wal_arg():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--cols16",
        help="Use 16 color output \"darken\" or \"lighten\" default: darken\"",
        nargs=1,
        metavar="[method]"
        )
    parser.add_argument(
        "--contrast",
        help="Specify a minimum contrast ratio between pallete colors and the \
        source image according to W3 contrast specifications. \
        Values between 1.5-4.5 typically work best.",
        metavar="[1.0-21.0]",
        nargs=1
        )
    parser.add_argument(
        "-w",
        help="Use last used wallpaper for color generation.",
        action='store_true',
        )
    parser.add_argument(
        "--recursive",
        help="When pywal is given a directory as input and this flag is \
        used: Search for images recursively in subdirectories instead of the root only.",
        action='store_true',
        )

    args = parser.parse_args() #original args

    pyw_args = [] #args that will be send to the 'wal' command

    if args.cols16 != None:
        pyw_args.append("--cols16")
        pyw_args.append(args.cols16[0])

    if args.contrast != None:
        pyw_args.append("--contrast")
        pyw_args.append(args.contrast[0])

    if args.w:
        pyw_args.append("-w")

    if args.recursive:
        pyw_args.append("--recursive")

    return pyw_args

def exec_wal():

    WAL_ARGS = get_wal_arg()

    WALL_DIR = wpgtk.data.config.WALL_DIR
    WALL_NAME = subprocess.check_output(['wpg', '-c'])

    DECODE_WALL_NAME = WALL_NAME.decode("utf-8").strip() #Decodes WALL_NAME since it cames as an object of type 'byte'

    WALL_FILE =  WALL_DIR + '/' + DECODE_WALL_NAME


    WAL_ARGS.insert(0, WALL_FILE)
    WAL_ARGS.insert(0, "-i")
    WAL_ARGS.insert(0, "wal")

    subprocess.run(WAL_ARGS)

def main():
    exec_wal()

main()
