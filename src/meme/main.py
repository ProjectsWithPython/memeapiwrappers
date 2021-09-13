import requests
import asyncio
import random
import aiohttp
from typing import Union

def get_meme(raw_dict_response=False, get_only_meme_image=False):
    data = requests.get("https://api.imgflip.com/get_memes")
    response = data.json()
    if raw_dict_response:
        return response
    else:
        length = len(response['data']['memes'])
        random_int = random.randint(0, length)
        if get_only_meme_image:
            return response['data']['memes'][random_int]['url']
        else:
            return response['data']['memes'][random_int]



async def async_get_image(raw_dict_response=False, get_only_meme_image=False):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.imgflip.com/get_memes") as response:
            if raw_dict_response:
                data = await response.json()
                return data
            else:
                data = await response.json()
                length = len(data['data']['memes'])
                random_int = random.randint(0, length)
                if get_only_meme_image:
                    return data['data']['memes'][random_int]['url']
                else:
                    return data['data']['memes'][random_int]



if __name__ == '__main__':
    async def main():
        print(await async_get_image())
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
