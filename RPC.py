import requests
import psutil
import os
import sys
import winshell
import glob
import inspect
import json
import gc
import time

from KM import (
    basemthd as bm,
    raises
)

config_fp = "RPCconfig.cfg"
globIP = requests.get('https://ifconfig.me').text
# yaml

if __name__ == "__main__":
    self_filename = os.path.basename(__file__).replace(".py", ".exe")
    fpn = 0

    # check if this process is duped
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"].replace(".exe", "").replace(".py", "") == self_filename.replace(".exe", "").replace(".py", ""):
            fpn += 1

        if fpn > 2:
            raises.raiseAlrRunningError(self_filename)
            sys.exit()

    config = bm.check_config(config_fp)

    shortcut_name = "RPC - shortcut for startup coded by KANOKIw"

    try:
        update_sec = int(config["update_sec"])
        startup_path = os.path.expandvars(winshell.startup())
        shortcut_path = os.path.join(startup_path, "*.lnk")
        matching_shortcuts = glob.glob(shortcut_path)

        shortcut_exists = any(shortcut_name in os.path.basename(shortcut) for shortcut in matching_shortcuts)

        if not shortcut_exists:
            print("No matched shourtcut found, creating new...")
            script_path = os.path.abspath(sys.argv[0])
            startup_folder = winshell.startup()
            
            shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")

            with winshell.shortcut(shortcut_path) as shortcut:
                shortcut.path = script_path
                shortcut.description = f"{self_filename}.exe made by KANOKIw"
                shortcut.working_directory = os.path.dirname(script_path)

            # Show setup progress at the first run
            # 
            __message = f"Setting up this app to startup apps."
            raises.win_cmd(__message, shortcut_path, self_filename)

        while (True):
            try:
                bm.monitor_Game_exe(config, globIP, path=config_fp)
                
            except Exception as e:
                # When modified config, a bad timing will raise RuntimeError
                #  
                if e.__class__ != RuntimeError:
                    raises.raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
                    sys.exit()
                # Continue as it doesn't affects the process badly
                # 
                else:
                    continue

    except Exception as e:
        raises.raiseError(f"{type(e).__name__}: && echo     {str(e)}", "Please contant KANOKIw")
        sys.exit()
