import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import WebsiteSearchTool

os.environ["OPENAI_API_KEY"]="sk-"
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'

ws_tool = WebsiteSearchTool(website="https://www.artificialintelligence-news.com/")

# Define your agents with roles and goals
scraper = Agent(
  role='Summarizer of websites',
  goal='Ask the user for a list of URLs then go each given website, scrape the content, and provide the full content to the writer agent so that it can then be summarized.',
  backstory="""You work at a leading tech think tank.
  Your expertise is taking URLs and getting getting just the text based content of them.""",
  verbose=True,
  allow_delegation=False,
  tools=[ws_tool]
  # tools=[WebsiteSearchTool]
)

writer = Agent(
  role='Tech Content Summarizer and Writer',
  goal='Craft compelling short form content on AI advancements based on long-form text passed to you',
  backstory="""You are a renowned Content Creator, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Take a list of websites that contain AI content, read/scrape the content and 
  then pass it to the writer agent.""",
  expected_output="Full analysis report in bullet points",
  agent=scraper
)

task2 = Task(
  description="""Using the text provided by scraper agent, develop a short and compelling and interesting short form summary
  of the text provided to you about AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[scraper, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)