from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from travel_tools.search_tool import SearchTools
from travel_tools.calculator_tool import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide /Local tour guide talk to travel agent to plan the trip


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

    def expert_travel_agent(self):
        #Agent should be result driven and clear goal in mind
        #backstory is just their resume
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. 
                             I have decade of experience making travel itineraries."""),
            goal=dedent(f"""Create a 8-day itinrary with detailed per day plans,
                        include budget, packing suggestions and safety tips.
                        """),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    #all the places to go inside the country
    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert in analyzing travel data to pick ideal travel destinations"""),
            goal=dedent(f"""Select best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgable local guide with extensive information about the city, 
                             its attractions and customs"""),
            goal=dedent(f"""provide the best insights about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

