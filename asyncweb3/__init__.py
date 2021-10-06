import aiohttp


class Asyncweb3:
    def __init__(self, provider: str, *, session: aiohttp.ClientSession=None):
        self.provider = provider
        
        self.session = session or aiohttp.ClientSession()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        pass
    
    async def net_version(self):
        """net_version of the standard api."""
        async with self.session.post(self.provider, json={'jsonrpc': '2.0', 'method': 'net_version', 'params': [], 'id': 1}, headers={'Content-type': 'application/json'}) as resp:
            return (await resp.json())['result']

def asyncweb3(provider: str, *, session: aiohttp.ClientSession=None) -> Asyncweb3:
    """The recommended way to start using asyncweb3. It takes a ``provider`` which should be a json-rpc http/https url, as well as an optional ``session`` kwarg that needs to be an aiohttp.ClientSession.\n
    It's recommeded to use it as such:\n
    .. code-block:: python
    
      async with asyncweb3.asyncweb3('http://localhost:8545') as w3:
          w3.function()
    """
    return Asyncweb3(provider, session=session)
