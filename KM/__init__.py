r"""(^^;

A Custom RPC Maker - By `KANOKIw`
--------------------------------
CutomRPC - By KNAOKIw

A grouped unique RPC module

There are mostly available what every discord user ever wanted

This module supports several RPC which was configured or directly modified.
When Simultaneously application actived, won't have a huge bug.
Latest application in the computer relates RPC.

Most known useage::

    >>> from KANOKIw_RPC_modules import (
            proc as RPCproc, # due to using proc as process
            raises,
            baseMethods
        )
    or
    >>> import KANOKIw_RPC_modules
        RPCprocess = KANOKIw_RPC_modules.RPCproc.RPCprocess

CTB::

    >>> while True:
            try:
                baseMethods.monitor_Game_exe(config)
                
            except Exception as e:
                if e.__class__ != RuntimeError:
                    raises.raiseError(__err: str, *, exx = None)
                    sys.exit()                  ^^^^^
                else: ...

not a public package.

"""

from . import (
    basemthd,
    proc,
    raises
)

__title__ = "KANOKIw - RPC"
__author__ = "KANOKIw"
__name__ = "RPC"
__version__ = "0.2.7"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)
