import os
import subprocess
import sys

import utils


def main():

    # install git
    if not utils.check_executable("git"):
        subprocess.call(["conda", "install", "-c", "anaconda", "git", "-y"])

    # update conda-git-deployment
    print "conda-git-deployment"
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    subprocess.call(["git", "pull"], cwd=path)


if __name__ == "__main__":

    if utils.get_arguments()["update"]:
        main()

    # execute install
    args = [
        "python", os.path.join(os.path.dirname(__file__), "environment.py")
    ]

    args.extend(sys.argv[1:])

    subprocess.call(args)
