### memeapiwrappers

*What is this wrapper for?*


*Its a api wrapper, which has meme images, chuck norris jokes and much more coming in future*


*Ok great How do I use it*


**In `memeapiwrappers` we have two types of functions `async` and `sync`. We recommand you using `async` so it doesnt block your code because its an api request.**


**YOU NEED `aiohttp` for this package, make sure you install it**


*Ok ok, where are the examples**


*Lets get started with `async` first*


```py
import asyncio
from meme.main import async_get_meme
async def main():
    very_funny_meme = await async_get_meme() # Two optional args
    print(very_funny_meme)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


**Chuck Norris Example**


```py
import asyncio
from chucknorris.main import async_get_chuck_norris_joke
async def main():
    very_funny_meme = await async_get_chuck_norris_joke() # Two optional args
    print(very_funny_meme)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


**Now the `sync` functions**


```py
from meme.main import get_meme
print(get_meme()) # Optional args
```

```py
from chucknorris.main import get_chuck_norris_joke
print(get_chuck_norris_joke()) # Optional args
```