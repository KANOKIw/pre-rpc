"""(^^;

Base Methods for RPC Prog
--------------------------
might be only used once a run

errors are caused with raises.py

"""

import json
import sys
import time
import gc
import psutil
import os
import inspect

from . import proc as RPCproc

from . import (
    raises
)


__all__ = (
    'checkfile',
    'monitor_Game_exe'
)


class loop:
    """ never returns """


def current_line(*arg, **kwarg) -> int:
    fr = inspect.currentframe().f_back
    return fr.f_lineno


def check_config(path: str = None) -> dict:
    r"""(^^;

    check config object -> `dict` 

    >>> 'RPCconfig.cfg': fp, must be the type like below::

        >>> {
            'clientID': int,
            'details': str | None,
            'state': str | None,
            'large_image': str | None,
            'large_text': str | None,
            'small_image': str | None,
            'small_text': str | None
        }

    """

    if not path:
        path = "RPCconfig.cfg"

    try:
        with open(path, encoding="utf-8") as f:
            config = json.load(f)
            config["update_sec"]

            RPC = config["RPC"]
            keylist = ["clientID", "details", "state", "large_image", "large_text", "small_image", "small_text"]
            for RPCinfo in RPC:
                for key in keylist:
                    RPC[RPCinfo][key]

    except Exception as e:
        if e.__class__ == FileNotFoundError:
            with open(path, "w", encoding="utf-8") as f:
                config = {
                    "update_sec": 15,
                    "RPC": {
                        "Example.exe": {
                            "clientID": "1234567890",
                            "details": "Playing Example",
                            "state": "only me is playing",
                            "large_image": None,
                            "large_text": None,
                            "small_image": None,
                            "small_text": None
                        }
                    },
                    "Hello": "Yo"
                }
                json.dump(config, f, ensure_ascii=False, indent=4)
            raises.raiseError(f"{type(e).__name__}: && echo     {str(e)}", exx=f"but this is not an error && echo app automatically written EXAMPLE {path}, change its contents or you can't run this app")
        else:
            raises.raiseError(f"{type(e).__name__}: && echo     {str(e)}", exx=f"check {path} contents...more info: (read the error)")
        sys.exit()
    
    return config


def monitor_Game_exe(config: dict[str, str], globIP: str, *, path: str = None, update_sec: int = 1) -> loop:
    r"""(^^;

    monitor game file given

    Parameters
    -----------
    config: `class`: dict[str, str]:

    before giving, call check_config()::

        >>> {
            'clientID': int,
            'details': str | None,
            'state': str | None,
            'large_image': str | None,
            'large_text': str | None,
            'small_image': str | None,
            'small_text': str | None
        }
    
    update_sec: `class`: int = 1
        the base update rate(per sec)
        shouldn't give as every loop will do check_config(config)

    """

    if not path:
        path = "RPCconfig.cfg"

    RPC_on = prev_game = None
    RPC = RPCproc.RPCprocess(config["RPC"][list(config["RPC"].keys())[0]], globIP)
    config = check_config(path)
    RPCed_Games = []

    while True:
        Game_exe_status = done = False
        prev = config
        config = check_config(path)
        app_list = []
        update_sec = int(config["update_sec"])


        if prev != config:
            print("INFO UPDATE: config/file updated")
            if RPC.RPC is not None:
                try:
                    RPC.update_RPC(config["RPC"][prev_game])
                except KeyError: ...


        for proc in psutil.process_iter(["name"]):
            app_list.append(proc.info["name"])
            for Game_filename in config["RPC"]: # *1
                if done:
                    break

                if proc.info["name"] == Game_filename:
                    if RPC_on is None or prev_game != Game_filename:
                        if Game_filename not in RPCed_Games:
                            RPCinfo = config["RPC"][Game_filename]
                            if RPC.RPC is not None:
                                RPC.close_RPC()

                            # _ #
                            del RPC
                            gc.collect()
                            # \ #
                            RPC = RPCproc.RPCprocess(RPCinfo, globIP)
                            RPC_on = RPC.start_RPC(RPCinfo)
                            print("INFO started at: 311")
                            RPCed_Games.append(Game_filename)
                            prev_game = Game_filename
                            Game_exe_status = done = True
                            break
                        else:
                            continue # to *1
                    else:
                        continue # to *1
        

        for game in RPCed_Games:
            if game not in app_list:
                RPCed_Games.remove(game)
        

        if not done:
            print(f"INFO RPC.RPC at {current_line()}: ", RPC.RPC)
            if len(RPCed_Games) > 0:
                prev_game = RPCed_Games[-1]
                if RPC.clientID == config["RPC"][prev_game]["clientID"]:
                    pass
                
                elif RPC.RPC is not None:
                    RPC.close_RPC()
                    # _|_ #
                    del RPC
                    gc.collect()
                    # *\* #
                    RPCinfo = config["RPC"][prev_game]
                    RPC = RPCproc.RPCprocess(RPCinfo, globIP)
                    print(f"INFO started at: {current_line()}")
                    RPC_on = RPC.start_RPC(RPCinfo)

            if prev_game in app_list:
                Game_exe_status = done = True
            else:
                try:
                    RPCed_Games.remove(prev_game)
                    print(RPCed_Games)
                    
                    try:
                        prev_game = RPCed_Games[-1]

                    except IndexError: ...
                except ValueError: ...
                

        print("INFO prev_game(=current RPC): ", prev_game)
        if not done:
            if RPC_on is not None:
                if RPC.RPC is not None:
                    RPC.close_RPC()
                    if prev_game not in app_list:
                        try:
                            RPCed_Games.remove(prev_game)
                            print(RPCed_Games)
                            prev_game = RPCed_Games[-1]
                        except ValueError: ...
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

        print("DATA RPCed_Games: ", RPCed_Games)
        time.sleep(update_sec)
