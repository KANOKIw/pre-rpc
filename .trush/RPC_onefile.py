import subprocess
import psutil
import os
import json
import sys
import time
import winshell
import glob
from pypresence import Presence



update_sec = 5


def raiseError(__err, exx = None):
    console_command = 'cmd.exe'

    base = "echo 10 ERROR: " + __err
    command = base
    for i in range(1, 659, 73):
        command = command + f" && echo. && echo. && echo During handling of the above exception, another exception occurred && echo. && echo. && " + base.replace("10 ", f"{i} ")

    if exx:
        command = command + f" && echo. && echo. && echo. && echo. && echo THIS IS AN ERROR raised at {__file__} && echo. && echo {exx} && echo Due to the above errors, {os.path.basename(__file__)} has exited."

    subprocess.run([console_command, '/k', command])


def win_cmd(__message: str, sourtcut_path: str, self_filename: str) -> None:
    console_command = 'cmd.exe'

    base = "echo 10 INFO: " + __message
    command = base
    for i in range(1, 659, 73):
        command = command + f" && echo. && echo. && echo Putting shourtcut file into {winshell.startup()}, this can take a while && echo. && echo. && " + base.replace("10 ", f"{i} ")

    command = command + f" && echo. && echo. && echo. && echo. && echo {self_filename}: Succesfully RPC Setup Done. && echo Now you can close this window..."

    subprocess.run([console_command, '/k', command])


def checkfile() -> dict | list | tuple:
    try:
        with open("RPCconfig.cfg", encoding="utf-8") as f:
            config = json.load(f)
            Game_filename = config["Game_filename"]
            update_sec = config["update_sec"]
            with open(Game_filename): ...
            RPC = config["RPC"]
            keylist = ["clientID", "details", "state", "large_image", "large_text", "small_image", "small_text"]
            for key in keylist:
                RPC[key]
    except Exception as e:
        raiseError(f"{type(e).__name__}: && echo     {str(e)}", "put RPCconfig.cfg file in the directory or check its contents...more info: (read the error)")
        sys.exit()
    
    return config



class RPCprocess:
    """|coro| 

    The base for this program

    RPC object: `self.RPC`

    Parameters
    -----------
    RPCinfo: `class`: dict[`str`, `str`]
        dict object keys includes [clientID, details, state]
    
    Methods
    --------
    start_RPC: `class` method -> `str`: ...
        starts self RPC object
    
    close_RPC: `class` method -> `None`: ...
        temporary close self RPC object -> `None`
        
    """

    def __init__(self, RPCinfo: dict[str, str]) -> None:
        self.RPCinfo = RPCinfo
        self.clientID = self.RPCinfo["clientID"]
        
        self.details = self.RPCinfo["details"]
        self.state = self.RPCinfo["state"]
        self.large_image = self.RPCinfo["large_image"]
        self.large_text = self.RPCinfo["large_text"]
        self.small_image = self.RPCinfo["small_image"]
        self.small_text = self.RPCinfo["small_text"]
        self.start = None
        self.RPC = None

    def start_RPC(self) -> str:
        """ starts self RPC object """

        self.RPCinfo = checkfile()["RPC"]

        self.clientID = self.RPCinfo["clientID"]

        self.details = self.RPCinfo["details"]
        self.state = self.RPCinfo["state"]
        self.large_image = self.RPCinfo["large_image"]
        self.large_text = self.RPCinfo["large_text"]
        self.small_image = self.RPCinfo["small_image"]
        self.small_text = self.RPCinfo["small_text"]

        self.RPC = Presence(self.clientID)
        print("RPC RUNNING")
        self.RPC.connect()

        self.start = int(time.time())
        self.RPC.update(
            details = self.details,
            state = self.state,
            large_image = self.large_image,
            large_text = self.large_text,
            small_image = self.small_image,
            small_text = self.small_text,
            start = self.start,
            party_id = "HHF",
            join = "join",
            spectate = "spectate",
            match = "match",
        )

        return "RPC started"
    
    def update_RPC(self) -> None:
        """ update RPC """

        self.RPCinfo = checkfile()["RPC"]

        self.clientID = self.RPCinfo["clientID"]

        self.details = self.RPCinfo["details"]
        self.state = self.RPCinfo["state"]
        self.large_image = self.RPCinfo["large_image"]
        self.large_text = self.RPCinfo["large_text"]
        self.small_image = self.RPCinfo["small_image"]
        self.small_text = self.RPCinfo["small_text"]

        self.RPC.update(
            details = self.details,
            state = self.state,
            large_image = self.large_image,
            large_text = self.large_text,
            small_image = self.small_image,
            small_text = self.small_text,
            start = self.start,
            party_id = "HHF",
            join = "join",
            spectate = "spectate",
            match = "match",
        )
        print("updated")

    def close_RPC(self) -> None:
        """ temporary close self RPC object """

        print("RPC closed")
        self.RPC.close()
        self.start = None

    @classmethod
    def status(
        cls,
        *,
        obj: dict[str, int] = {}
        ): ...



def monitor_Game_exe(Game_filename, RPCinfo):
    global update_sec
    RPC_on = None
    RPC = RPCprocess(RPCinfo)
    config = checkfile()

    while True:
        Game_exe_status = False
        prev = config
        config = checkfile()

        update_sec = int(config["update_sec"])

        if prev != config:
            if RPC.RPC is not None:
                RPC.update_RPC()

        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] == Game_filename:
                if RPC_on is None and not Game_exe_status:
                    RPC_on = RPC.start_RPC()
                    Game_exe_status = True
                break
        else:
            if RPC_on is not None:
                if RPC.RPC is not None:
                    RPC.close_RPC()
                RPC_on = None

        if Game_exe_status:
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == Game_filename:
                    break
            else:
                if RPC_on is not None:
                    if RPC.RPC is not None:
                        RPC.close_RPC()
                    RPC_on = None
                Game_exe_status = False
                
        time.sleep(update_sec)




if __name__ == "__main__":
    self_filename = os.path.basename(__file__)

    config = checkfile()
    Game_filename = config["Game_filename"]

    Gamename = Game_filename.replace('.exe', "").replace(".py", "")
    shortcut_name = Gamename + " - RPC - しょーとかっと for すたーとあっぷ"

    try:
        update_sec = int(config["update_sec"])

        startup_path = os.path.expandvars(winshell.startup())

        shortcut_path = os.path.join(startup_path, "*.lnk")

        matching_shortcuts = glob.glob(shortcut_path)

        shortcut_exists = any(shortcut_name in os.path.basename(shortcut) for shortcut in matching_shortcuts)
    
        if not shortcut_exists:
            print("Creating new shourtcut...")
            script_path = os.path.abspath(sys.argv[0])
            startup_folder = winshell.startup()
            
            shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")

            with winshell.shortcut(shortcut_path) as shortcut:
                shortcut.path = script_path
                shortcut.description = f"{Gamename} RPC exe made by KANOKIw"
                shortcut.working_directory = os.path.dirname(script_path)
                
            print("Done.")
            __message = f"Setting up this process to startup."
            win_cmd(__message, shortcut_path, self_filename)
            
            while True:
                try:
                    monitor_Game_exe(Game_filename, config["RPC"])
                except Exception as e:
                    if e.__class__ != RuntimeError:
                        raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
                    else:
                        continue

    except Exception as e:
        raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
        sys.exit()
