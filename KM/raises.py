"""(^^;

Most Plite Visually Error Method
---------------------------------
Will just open cmd.exe and echo there? `uwu`
Hate Exceptions

"""

import subprocess
import random
import winshell
import os


__all__ = (
    'raiseError',
    'win_cmd',
    'raiseAlrRunningError'
)


class NoReturn:
    """ due to exiting """


def raiseError(__err, *, exx = None) -> NoReturn:
    console_command = 'cmd.exe'

    base = "echo 10 ERROR: " + __err
    command = base

    amount = random.randint(70, 100)
    for i in range(1, (amount *9) +1, amount):
        command = command + f" && echo. && echo. && echo During handling of the above exception, another exception occurred && echo. && echo. && " + base.replace("10 ", f"{i} ")

    if exx:
        command = command + f" && echo. && echo. && echo. && echo. && echo THIS IS AN ERROR raised at {__file__} && echo. \
&& echo {exx} && echo Due to the above exceptions, {os.path.basename(__file__)}(parents) has exited."

    subprocess.run([console_command, '/k', command])



def win_cmd(__message: str, sourtcut_path: str, self_filename: str) -> NoReturn:
    console_command = 'cmd.exe'

    base = "echo 10 INFO: " + __message
    command = base

    amount = random.randint(70, 100)
    for i in range(1, (amount *9) +1, amount):
        command = command + f" && echo. && echo. && echo Putting shourtcut file into {winshell.startup()}, this can take a while && echo. && echo. && " + base.replace("10 ", f"{i} ")

    command = command + f" && echo. && echo. && echo. && echo. && echo {self_filename}: Succesfully RPC Setup Done. && echo Now you can close this window..."

    subprocess.run([console_command, '/k', command])



def raiseAlrRunningError(self_filename) -> NoReturn:
    console_command = 'cmd.exe'
    __err = f"FileAlreadyRunningError: && echo     There is a same program running already(excepted filename: {self_filename})"

    base = "echo 10 ERROR: " + __err
    command = base
    for i in range(1, 659, 73):
        command = command + f" && echo. && echo. && echo During handling of the above exception, another exception occurred && echo. && echo. && " + base.replace("10 ", f"{i} ")

    command = command + f" && echo. && echo. && echo. && echo. && echo THIS IS AN ERROR raised at {__file__} && echo. \
&& echo Due to the above exceptions, {os.path.basename(__file__)} and {self_filename}(parents) has exited."

    subprocess.run([console_command, '/k', command])
