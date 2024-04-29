"""
Searching specific video topics we want to learn and find 10 to 15 videos on that topic.
"""
from datetime import timezone
import datetime
from typing import Type,List
from urllib import request
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel,Field
import os

class YouTubeVideoSearchToolInput(BaseTool):
    keyword=Field(..., description="The search keyword")
    max_results:int = Field(10, description="The maximum number of results to return")

class VideoSearchResult(BaseTool):
    video_id: str
    title: str
    channel_id: str
    channel_title: str
    days_since_published: int

class YouTubeVideoSearchTool(BaseTool):
    name: str = "Search YouTube Videos"
    description: str ="Searches YouTube videos based on a keyword and return a list of video search results"
    args_schema: Type[BaseModel] = YouTubeVideoSearchToolInput

    def _run(self, keyword:str, max_results: int=10) -> List[VideoSearchResult]:
        api_key = os.getenv("YOUTUBE_API_KEY")
        url = "https://www.googleapis.com/youtube/v3/search"
        params={
            "part": "snippet",
            "q": keyword,
            "maxResults": max_results,
            "type": "video",
            "key": api_key
        }
        response = request.get(url, params=params)
        response.raise_for_status()
        items = response.json().get("items", [])

        results=[]
        for item in items:
            video_id= item["id"]["videoId"]
            title= item["snippet"]["title"]
            channel_id= item["snippet"]["channelId"]
            channel_title= item["snippet"]["channelTitle"]
            publish_date = datetime.fromisoformat(
                item["snippet"]["publishedAt"].replace('Z', "+00:00")).astimezone(timezone.utc)
            days_since_published= (datetime.now(timezone.utc) - publish_date).days
            video_search_result = VideoSearchResult(video_id=video_id,title=title,channel_id=channel_id,channel_title=channel_title,days_since_published=days_since_published)
            results.append(video_search_result)

        return results
        
