# from crewai import Agent
from textwrap import dedent
from crewai.agent import Agent
from langchain_openai import ChatOpenAI
from tools.youtube_video_detail_tool import YouTubeVideoDetailsTool
from tools.youtube_video_search_tool import YouTubeVideoSearchToolInput
from langchain.agents import load_tools

human_tools = load_tools(["human"])
youtube_video_details_tool = YouTubeVideoDetailsTool()
youtube_video_search_tool =YouTubeVideoSearchToolInput()

class YoutubeAutomationAgents():
    #Agent Per Task 
    # coordinator ensure we do the research first then create the title, then description then email etc.
    def youtube_coordinator(self):
        return Agent(
            role="YouTube Coordinator",
            goal="""
                Oversee the YouTube prepartion process including market research,
                title ideation, description, and email announcement creation required
                to make a YouTube video.
            """,
            backstory=""" As a methodical and detailed oriented coordinator, you are 
                responsible for overseeing the project.  When creating YouTube videos, you follow the following
                process to create a video that has high chance of becoming viral.
                1. Search youtube to find 15 other video on the same topic and analyze their title.
                2. Create a list of 10 potential titles that are less than 70 characteres.
                3. Write a description for the youtube video.
                4. Write an email that can be sent to all subscribers to promote the new video.
            """,
            allow_delegation=True,
            verbose=True,
        )

    def researcher(self):
        return Agent(
            role="YouTube researcher",
            goal=""" For a given topic and description for a new YouTube video, find a 
            minimum of 15 high performing videos on the same topic with the ultimate
            goal of populating the research table which will be use by other agents
            to help them generate titles and other aspects of the YouTube video that
            we are plannint to create
            """,
            backstory=""" As a methodical researcher you are responsible for overseeing
            researchers who actively search youtube to find high performance youtube videos
            on the same topic.
            """,
            verbose = True,
            allow_delegation=True,
            tools=[youtube_video_detail_tool,youtube_video_search_tool],

        )

    def title_creator(self):
        return Agent(
            role="Title Creator",
            goal="""Create 10 titles for a given youtube video topic and description.
                You should also use previous research to help generate the titles.
                The titles should be less than 70 characters and should have a high 
                click through rate.
            """,
            backstory="""As a title creator you are responsible for creating 10 potential
                titles for a given Youtube video topic and description.
            """,
            verbose = True,
        )

    def description_creator(self):
        return Agent(
            role="Description Creator",
            goal="""Create description for a given youtube video topic and description.
                You should also use previous research to help generate the titles.
                The titles should be less than 70 characters and should have a high 
                click through rate.
            """,
            backstory="""As a description creator you are responsible for creating 10 potential
                titles for a given Youtube video topic and description.
            """,
            verbose = True,
        )

    def email_creator(self):
        return Agent(
            role="Email Creator ",
            goal="""Create an email to send to the marketing team to promote the new 
             YouTube video """,
            backstory="""As an email creator, you are responsible for creating an
                email to send to the marketing team to promote the new YouTube video.
                It is vital that you ONLY ask for human feedback after you have created the email.
                DO NOT ask the human to create the email for you.
            """,
            verbose = True,
            allow_delegation=True,
            tools=[human_tools],
        )