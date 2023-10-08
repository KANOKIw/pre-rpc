import subprocess
import psutil
import os
import json
import sys
import time
import winshell
import glob
import random
import gc
from pypresence import Presence


update_sec = 5
nwsfr = None
pyexe = ""



def raiseError(__err, exx = None):
    console_command = 'cmd.exe'

    base = "echo 10 ERROR: " + __err
    command = base
    
    amount = random.randint(70, 100)
    for i in range(1, (amount *9) +1, amount):
        command = command + f" && echo. && echo. && echo During handling of the above exception, another exception occurred && echo. && echo. && " + base.replace("10 ", f"{i} ")

    if exx:
        command = command + f" && echo. && echo. && echo. && echo. && echo THIS IS AN ERROR raised at {__file__} && echo. && echo {exx} && echo Due to the above exceptions, {os.path.basename(__file__)} has exited."

    subprocess.run([console_command, '/k', command])




def win_cmd(__message: str, sourtcut_path: str, self_filename: str) -> None:
    console_command = 'cmd.exe'

    base = "echo 10 INFO: " + __message
    command = base

    amount = random.randint(70, 100)
    for i in range(1, (amount *9) +1, amount):
        command = command + f" && echo. && echo. && echo Putting shourtcut file into {winshell.startup()}, this can take a while && echo. && echo. && " + base.replace("10 ", f"{i} ")

    command = command + f" && echo. && echo. && echo. && echo. && echo {self_filename}: Succesfully RPC Setup Done. && echo Now you can close this window..."

    subprocess.run([console_command, '/k', command])




def raiseAlrRunningError(self_filename) -> None:
    console_command = 'cmd.exe'
    __err = f"FileAlreadyRunningError: && echo     There is a {self_filename} running already"

    base = "echo 10 ERROR: " + __err
    command = base
    for i in range(1, 659, 73):
        command = command + f" && echo. && echo. && echo During handling of the above exception, another exception occurred && echo. && echo. && " + base.replace("10 ", f"{i} ")

    command = command + f" && echo. && echo. && echo. && echo. && echo THIS IS AN ERROR raised at {__file__} && echo. && echo Due to the above exceptions, {os.path.basename(__file__)} has exited."

    subprocess.run([console_command, '/k', command])




def checkfile() -> dict | list | tuple:
    try:
        with open("RPCconfig.cfg", encoding="utf-8") as f:
            config = json.load(f)
            update_sec = config["update_sec"]

            RPC = config["RPC"]
            keylist = ["clientID", "details", "state", "large_image", "large_text", "small_image", "small_text"]
            for RPCinfo in RPC:
                for key in keylist:
                    RPC[RPCinfo][key]
                
    except Exception as e:
        if e.__class__ == FileNotFoundError:
            with open("RPCconfig.cfg", "w", encoding="utf-8") as f:
                config = {
                    "update_sec": 15,
                    "RPC": {
                        "Example.exe": {
                            "clientID": "1234567890",
                            "details": "Playing Example",
                            "state": "no one is playing",
                            "large_image": None,
                            "large_text": None,
                            "small_image": None,
                            "small_text": None
                        }
                    },
                    "Hello": "Yo"
                }
                json.dump(config, f, ensure_ascii=False, indent=4)
            raiseError(f"{type(e).__name__}: && echo     {str(e)}", "but this is not an error && echo app automatically written EXAMPLE RPCconfig.cfg, change its contents or you can't run this app")
        else:
            raiseError(f"{type(e).__name__}: && echo     {str(e)}", "check RPCconfig.cfg contents...more info: (read the error)")
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


    def start_RPC(self, RPCinfo) -> str:
        """ starts self RPC object """

        print("RPC RUNNING")
        
        self.RPCinfo = RPCinfo

        self.clientID = self.RPCinfo["clientID"]

        self.details = self.RPCinfo["details"]
        self.state = self.RPCinfo["state"]
        self.large_image = self.RPCinfo["large_image"]
        self.large_text = self.RPCinfo["large_text"]
        self.small_image = self.RPCinfo["small_image"]
        self.small_text = self.RPCinfo["small_text"]

        self.RPC = Presence(self.clientID)
        
        self.RPC.connect(
            
        )

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
    

    def update_RPC(self, RPCinfo) -> None:
        """ update RPC """

        self.RPCinfo = RPCinfo

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
        print("RPC updated")

        return "updated"

    def close_RPC(self) -> None:
        """ temporary close self RPC object """

        if self.RPC is not None:
            print("RPC closed")
            try:
                self.RPC.close(
                
                )
            except Exception: ...
            
        self.start = None

        return "closed"
        
    @classmethod
    def status(
        cls,
        *,
        obj: dict[str, int] = {},
        ): ...

    @staticmethod
    def stop(
        
    ): ...




def monitor_Game_exe(config: dict[str, str]):
    global update_sec
    RPC_on = None
    RPC = RPCprocess(config["RPC"][list(config["RPC"].keys())[0]])
    config = checkfile()
    prev_game = None

    while True:
        Game_exe_status = False
        done = False
        prev = config
        config = checkfile()

        update_sec = int(config["update_sec"])

        if prev != config:
            print("config/file updated")
            if RPC.RPC is not None:
                try:
                    RPC.update_RPC(config["RPC"][prev_game])
                except KeyError: ...

        for proc in psutil.process_iter(["name"]):
            for Game_filename in config["RPC"]:
                if done:
                    break

                if proc.info["name"] == Game_filename:
                    if RPC_on is None or prev_game != Game_filename:
                        RPCinfo = config["RPC"][Game_filename]
                        if RPC.RPC is not None:
                            RPC.close_RPC()

                        # _ #
                        del RPC
                        gc.collect()
                        # _ #
                        RPC = RPCprocess(RPCinfo)
                        RPC_on = RPC.start_RPC(RPCinfo)
                        prev_game = Game_filename
                        Game_exe_status = True
                        done = True
                        break
                    else:
                        done = True
                        break

        if not done:
            if RPC_on is not None:
                if RPC.RPC is not None:
                    RPC.close_RPC()
                RPC_on = None

        if Game_exe_status:
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == prev_game:
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
    fpn = 0
    
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"].replace(".exe", "").replace(".py", "") == self_filename.replace(".exe", "").replace(".py", ""):
            fpn += 1

        if fpn > 2:
            raiseAlrRunningError(self_filename)
            sys.exit()
            
    config = checkfile()

    shortcut_name = "RPC - しょーとかっと for すたーとあっぷ coded by KANOKIw"

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
                shortcut.description = f"{self_filename}.exe made by KANOKIw"
                shortcut.working_directory = os.path.dirname(script_path)

            print("Done.")
            __message = f"Setting up this process to startup apps."
            win_cmd(__message, shortcut_path, self_filename)

        while True:
            try:
                monitor_Game_exe(config)
                
            except Exception as e:
                if e.__class__ != RuntimeError:
                    raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
                else:
                    continue

    except Exception as e:
        raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
        sys.exit()


