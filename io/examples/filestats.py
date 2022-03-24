#!/usr/bin/env python3
import sys
import os
import time


def fileinfo(files):
    maxlength = str(len(max(files, key=len)))
    # Use of ^ for centering and the use of a nested {}  ~   {:>12{}}
    fmt = "{:" + maxlength + "} {:^9} {:^9} {:^9} {:>12{}}"
    pieces = ("Name:", "Exists?", "File?", "Dir?", "Size(bytes)", "")
    # Use of *pieces to splat pieces into an argument list
    print(fmt.format(*pieces))
    for afile in files:
        print(fmt.format(afile, str(os.path.exists(afile)),
                         str(os.path.isfile(afile)), str(os.path.isdir(afile)),
                         os.path.getsize(afile), ","))


def allstats(afile):
    tag = ["mode", "inode#", "device#", "#links", "user", "group", "bytes",
           "last access", "last modified", "change/creation time"]
    print("File Stats for:", afile)
    stats = os.stat(afile)
    fmt = "{:>22} : {}"
    for i, stat in enumerate(stats):
        print(fmt.format(tag[i], stat))


def datestats(afile):
    print("More Stats for:", afile)
    stats = os.stat(afile)
    print("Last Access:", time.ctime(stats.st_atime))
    print("Last Modified:", time.ctime(stats.st_mtime))
    print("Last Change:", time.ctime(stats.st_ctime))


def main():
    cwd = os.getcwd()
    print("Current Directory:", cwd)
    newdir = "afolder/asubfolder"
    os.makedirs(newdir, exist_ok=True)

    # Get list of files and get info about first 5
    filelist = sorted(os.listdir(cwd))[:5]
    fileinfo(filelist)

    # Get stats on a file
    allstats(sys.argv[0])
    datestats(sys.argv[0])


if __name__ == "__main__":
    main()
