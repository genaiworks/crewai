# Create Agents
from crewai import Crew, Process
from agents import YoutubeAutomationAgents
from tasks import YouTubeAutomationTask
from tools.youtube_video_detail_tool import YouTubeVideoDetailsTool
from tools.youtube_video_search_tool import YouTubeVideoSearchToolInput
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

OpenAIGPT= ChatOpenAI(
    model="gpt-3.5-turbo"
)
youtube_video_details_tool = YouTubeVideoDetailsTool()
youtube_video_search_tool =YouTubeVideoSearchToolInput()

agents = YoutubeAutomationAgents()

youtube_coordinator = agents.youtube_coordinator()
researcher = agents.researcher(youtube_video_search_tool=youtube_video_search_tool,
                               youtube_video_details_tool=youtube_video_details_tool)
title_creator = agents.title_creator()
description_creator = agents.description_creator()
email_creator = agents.email_creator()

#Background info about youtube video
video_topic = "Automating Tasks Using CrewAI"
video_details="""
In this video, we are diving into the innovative ways I'm using CrewAI
to automate my YouTube channel.  From conducting thorough research to 
streamline video preparation, CrewAI is revolutionizing how I create content.
But that's not all - I'm also exploring how to harness the power to CrewAI to 
generate personalized emails for my subscribers.  Join me in this journey as I 
unlock the potential of AI to enhance YouTube channel.
"""

# Create tasks
tasks = YouTubeAutomationTask()
youtube_coordinator_task= tasks.youtube_coordinator_task(video_topic=video_topic,video_details=video_details,agent=youtube_coordinator )
researcher_task=tasks.researcher_task(video_topic=video_topic,video_details=video_details,agent=researcher )
title_creator_task=tasks.title_creator_task(video_topic=video_topic,video_details=video_details,agent=title_creator)
description_creator_task=tasks.description_creator_task(video_topic=video_topic,video_details=video_details,agent=description_creator)
email_creator_task=tasks.email_creator_task(video_topic-video_topic,video_details=video_details,agent=email_creator)

# Create Tools
crew = Crew(
    agents=[
        youtube_coordinator,
        researcher,
        title_creator,
        description_creator,
        email_creator,
    ],
    tasks=[
        youtube_coordinator_task,
        researcher_task,
        title_creator_task,
        description_creator_task,
        email_creator_task,
    ],
    process= Process.hierarchical,
    manager_llm=OpenAIGPT
)

results = crew.kickoff()
print("Crew Usage", crew.usage_metrics)
print("Crew work completed")
print(results)