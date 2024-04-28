import json
import os 
import requests 
from langchain.tools import tool

class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 3
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': "application/json"
        }
        response = requests.request("POST", url,headers=headers, data=payload)
        if 'organic' not in response.json():
            return "cannot find organic"
        else:
            results = response.json()["organic"]
            string =[]
            for result in results[:top_result_to_return]:
                try:
                    string.append('/n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}"
                    ]))
                except KeyError:
                    next
            return '\n'.join(string)