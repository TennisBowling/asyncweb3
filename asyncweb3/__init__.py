import asyncio
import aiohttp


class Asyncweb3:
    def __init__(self, provider: str, *, session: aiohttp.ClientSession=None):
        self.provider = provider
        
        async def create_session():
            self.session = session or aiohttp.ClientSession()

        asyncio.get_event_loop().run_until_complete(create_session())
    
    def __aenter__(self):
        return self
    
    def __aexit__(self, *args):
        pass
    
    async def net_version(self):
        """net_version of the standard api."""
        async with self.session.post(self.provider, json={'jsonrpc': '2.0', 'method': 'net_version', 'params': [], 'id': 1}, headers={'Content-type': 'application/json'}) as resp:
            return (await resp.json())['result']

def asyncweb3(provider: str, *, session: aiohttp.ClientSession=None):
    """The recommended way to start using asyncweb3. It takes a ``provider`` which should be a json-rpc http/https url, as well as an optional ``session`` kwarg that needs to be an aiohttp.ClientSession.\n
    It's recommeded to use it as such:\n
    .. code-block:: python
    
      async with asyncweb3.asyncweb3('http://localhost:8545') as w3:
          w3.function()
    """
