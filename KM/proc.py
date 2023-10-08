import time

from typing import overload
from pypresence import Presence

globIP = ""

def replaceSpecificCipher(cipher: str) -> str:
    """
    replace given cipher with registered keywards 
    """
    global globIP
    cipher = cipher.replace("/:global ip:/", globIP)
    return cipher

class RPCprocess:
    RPC_on = False

    def __init__(self, RPCinfo: dict[str, str], instantglobIP: str) -> None:
        r"""
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
        self.RPCinfo = RPCinfo
        self.clientID = self.RPCinfo["clientID"]
        
        self.details = replaceSpecificCipher(self.RPCinfo["details"])
        self.state = replaceSpecificCipher(self.RPCinfo["state"])
        self.large_image = self.RPCinfo["large_image"]
        self.large_text = self.RPCinfo["large_text"]
        self.small_image = self.RPCinfo["small_image"]
        self.small_text = self.RPCinfo["small_text"]
        self.start = self.RPC = None
        self.closed = RPCprocess.RPC_on = False
        global globIP
        globIP = instantglobIP


    def start_RPC(self, RPCinfo: dict[str, str]) -> str:
        r"""
        starts RPC with the client `RPCinfo['clientID']` 

        Parameters
        -----------
        RPCinfo: `class`: dict::

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

        self.RPCinfo = RPCinfo

        self.clientID = self.RPCinfo["clientID"]

        self.details = replaceSpecificCipher(self.RPCinfo["details"])
        self.state = replaceSpecificCipher(self.RPCinfo["state"])
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
                        match = "match"
        )

        print("RPC started")
        RPCprocess.RPC_on = True

        return "RPC started"
    

    def update_RPC(self, RPCinfo: dict[str, str]) -> str:
        r"""
        updates RPC with the client `RPCinfo['clientID']` 

        Parameters
        -----------
        RPCinfo: `class`: dict::

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

        self.RPCinfo = RPCinfo

        self.clientID = self.RPCinfo["clientID"]

        self.details = replaceSpecificCipher(self.RPCinfo["details"])
        self.state = replaceSpecificCipher(self.RPCinfo["state"])
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
                        match = "match"
        )
        
        print("RPC updated")

        return "updated"


    def close_RPC(self) -> str:
        r"""(^^;

        instantly close previous RPC

        """

        if self.RPC is not None:
            
            try:
                self.RPC.close(
                
                )
            except Exception: ...
            
            self.closed = True
            print("RPC closed")
            
        self.start = None
        RPCprocess.RPC_on = False

        return "closed"
    

    def _do_continue(self) -> None:
        if self.closed:
            if self.RPC is not None:
                self.RPC.update(

                )

            self.closed = False
        
    @property
    def closed(self):
        return self.closed
    
    @property
    def closed(self):
        return self.RPC
    
    @property
    def rpc(self):
        return self.RPC
    
    @overload
    def update_RPC(self, RPCinfo: None) -> str: ...

    # if the RPC is on
    @classmethod
    async def status(
                    cls,
                    *,
                    obj: dict[str, int] = ...
    ) -> str | dict | None: ...


    @staticmethod
    def start(
            *arg,
            game: str = None
    ) -> str | None: ...

    @staticmethod
    def stop(
            *arg
    ) -> None: ...
