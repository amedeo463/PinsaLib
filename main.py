# Import every individual needed instruction
# for the sake of performance, and to save
# some memory in case you have a potato
# device.
from os import remove, mkdir, rmdir
from shutil import copytree, copy2, rmtree
from requests import get
from zipfile import ZipFile

# Allows to use different paths without editing any script manually.
# Also, these are not constants, don't get fooled.
# Changed these from constants to normal variables when it was too late.
# Oh yeah have I mentioned that scripts on the web are supported?
SD_CARD = "[UNSET]" # SD card
WORKDIR = "./temp/" # Work directory (temp directory)
SPATH = "[UNSET]" # Path or URL to the script to run.

ISURL = False # Is the script to run an URL?
__do_log = False # Print out logs?

attributes = set()

# instruction that translates paths.
def dir_transl(path: str) -> str:
    path = path.strip()

    if path.upper().startswith("SD:"):
        path = path.replace("SD:", SD_CARD+"/", 1)
    elif path.upper().startswith("WORK:"):
        path = path.replace("WORK:", WORKDIR+"/", 1)
    
    return path

def prints(*values):
    print(*values)

def printl(*values):
    if __do_log:
        print(*values)

def copy(fname: str, dest: str) -> None: # copy a file and paste it somewhere else.
    printl("Copying", fname, "to", dest)
        
    # Below how I used to implement the copy function in
    # PScrInt.
    #open(dest, "wb").write(open(fname, "rb").read())
    #[ COPY DATA TO DEST  ] [ READ FILE DATA       ]
    copy2(fname, dest)

def delete(fname: str) -> None: # delete a file.
    printl("deleting", fname)
    remove(fname)

def newdir(dir_: str) -> None: # create a directory.
    printl("Creating directory", dir_)
    try:
        mkdir(dir_)
    except:
        printl("Directory already exists, ignoring")
        
def copydir(dir_: str, dest: str) -> None: # copy the contents of a directory from one place to another.
    printl("Copying contents of", dir_, "to", dest)
    copytree(dir_, dest)

def deldir(dir_: str) -> None: # delete a directory.
    printl("Deleting", dir_)
    rmdir(dir_)
    
def rdeldir(dir_: str) -> None:
    printl("Recursively deleting", dir_)
    rmtree(dir_)

def download(url: str, saveas: str) -> None: # download a file and save it.
    printl(f"Downloading {url} and saving as {saveas}")
    open(saveas, "wb").write(get(url).content)
   #[ CREATE DEST    ] [ GET AND SAVE DATA   ]

def extract(fname: str, dest) -> None: # extract the contents of a .zip file
    printl(f"Extracting {fname} in {dest}")
    ZipFile(fname, 'r').extractall(dest)
   #[ READ ZIP FILE   ] [ EXTRACT IT   ]
    
def yninput(ask: str, e_msg: str = "Not valid!") -> str:
    while True:
        res = input(ask).lower()
        if res == "y":
            return True
        elif res == "n":
            return False
        else:
            print(e_msg)
    
def pause():
    input("Press [RETURN] to continue...")