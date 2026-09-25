import subprocess

def run(cmd):
    # deliberately unsafe, to give the scanner something to find
    return subprocess.call(cmd, shell=True)
