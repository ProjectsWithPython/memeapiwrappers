import requests
import aiohttp
import asyncio
from typing import Union

lists_of_categories = ["animal","career","celebrity","dev","explicit"
        ,"fashion","food","history","money","movie","music",
        "political","religion","science","sport","travel"]

def get_chuck_norris_joke(category=None, as_dict_response=False) -> Union[str, dict]:
    if category is None:
        data_raw = requests.get("https://api.chucknorris.io/jokes/random")
        response = data_raw.json()
        if as_dict_response:
            return response
        else:
            return response["value"]
    else:
        if category not in lists_of_categories:
            return lists_of_categories
        else:
            data_raw = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")
            response = data_raw.json()
            if as_dict_response:
                return response
            else:
                return response["value"]


async def async_get_chuck_norris_joke(category=None, as_dict_response=False):
    if category is None:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.chucknorris.io/jokes/random") as response:
                data = asyncio.create_task(response.json())
                if as_dict_response:
                    return await data
                else:
                   res =  await data
                   return res['value']
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.chucknorris.io/jokes/random?category={category}") as response:
                data = asyncio.create_task(response.json())
                if as_dict_response:
                    return await data
                else:
                    res =  await data
                    return res['value']
        


# Testing
if __name__ == '__main__':              
    async def main():
        print(await async_get_chuck_norris_joke(asDictRes=True))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

