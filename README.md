# crewai Platform for Multi Agent Systems

IMPORTANT RESOURCES
LangChain Build in Tools:
    https://python.langchain.com/docs/integrations/tools/

LangChain Tutorials:
    https://github.com/kyrolabs/awesome-langchain

CrewAI Repository
    https://github.com/joaomdmoura/crewAI?tab=readme-ov-file#why-crewai

CrewAI Examples:
    https://github.com/joaomdmoura/crewAI-examples.git

CrewAI is a new tool that allows us to create our own teams of autonomous agents, all of them working for us.

Each agent is an expert in a different task, and they all work together to help us achieve our goal. This goal can be either crafting an email based on some research, creating a business plan, writing a book, creating a blog post, etc.

All we have to do is think of the process and tasks that would be required to achieve our goal, and assign those tasks to our crew of agents. They will do all the work for us.

Define the goal of the crew

To set up crew we consider following concepts:

1. Tasks:
    These are the tasks our agents will perfmorm.  Each task is assigned to an agent.  Each task has following properties:
        1. Description
        2. Agent: Agent that will perform the task
        3. Context: 
        4. Async Execution: Whether or not task need to be executed simultanously with other tasks.
    Task Properties:
        Description: Concise statement of what task entails
        Agent: Which agent is responsible for the task, if not crew determines who takes on.
        Expected Output: Expected output of a task
        Tools: Functions or capabilities that the agent can utilize to perform a task.  These instructions can be simple activity like search or more complex interaction with other agents.
        Async Execution
        Callback
        Context
    
    Creating Tasks Cheat Sheet:
        - Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
        - Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
        - Ensure tasks are descriptive, providing clear instructions and expected deliverables.
    
    Key Steps for Task Creation:
    1. Identify the Desired Outcome: Define what success looks like for your project.
        - A detailed 7 day travel itenerary.

    2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
        - Itenerary Planning: develop a detailed plan for each day of the trip.
        - City Selection: Analayze and pick the best cities to visit.
        - Local Tour Guide: Find a local expert to provide insights and recommendations.

    3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

    4. Task Description Template:
    - Use this template as a guide to define each task in your CrewAI application. 
    - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.


2. Agents:
    These are the AI agentts that will be working for us.   Each agent is an expert in different task.
    Agent:
        They think for themselves and complete their tasks without us having to tell what step to take.  They are coded with LangChain all we need is an initial prompt telling them what we expect from them.  We need to write prompt to perfrm the task that we assign to the agent.
        Agents have ability to reach out to another and delegate work and ask questions.

        Agent does following:
        1. Thought
        2. Agent
        3. Action Input
        4. Observation

        Agents are like employees, work on own and work together share information.
            1. Writer
            2. Researcher

        Agent Properties:
            Role:
                Agent function within the crew
            Goal:
                It guides the agent's decision process.
            Backstory:
                Provide context to agent's role and goal.
            Tools:
                capabilities that agent can use.
            Max iter
            Max RPM:    
                Max number of request per minute       
            Verbose:
                Allow us to see what is going on.
            Allow delegation

    Example:
    Here are example of agents that help us solve problem.
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, it's attractions and customs"""),
            goal=dedent( f"""Provide the BEST insights about the selected city"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    #properties orient how each of these agents should behave
    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT4,
        )

3. Tools:
    These are the tools our agents will use to perform their tasks. For example
    1. Search engine: Agents can use tools to search internet
    2. Summarizer
    3. Translator
    4. Calculations: Agents can use tools to perform calculations

Process:
        A process dictates the way that our agent will work together.  We will use sequential process, which means each agent will work one after another.
        Process define how agents will work together.
        How tasks will be assigned.
        How agents will interact with each other.
        Process invoke agents to work sequentially.

LangChain Agents:
    Private GPT: Interact privately with your documents using the power of GPT, 100% privately, no data leaks GitHub 
    CollosalAI Chat: implement LLM with RLHF, powered by the Colossal-AI project GitHub 
    AgentGPT: AI Agents with Langchain & OpenAI (Vercel / Nextjs) GitHub 
    Local GPT: Inspired on Private GPT with the GPT4ALL model replaced with the Vicuna-7B model and using the InstructorEmbeddings instead of LlamaEmbeddings GitHub 
    GPT Researcher: GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks. GitHub 
    ThinkGPT: Agent techniques to augment your LLM and push it beyond its limits GitHub 
    Camel-AutoGPT: role-playing approach for LLMs and auto-agents like BabyAGI & AutoGPT GitHub 
    RasaGPT: RasaGPT is the first headless LLM chatbot platform built on top of Rasa and Langchain. GitHub 
    SkyAGI: Emerging human-behavior simulation capability in LLM agents GitHub 
    PyCodeAGI: A small AGI experiment to generate a Python app given what app the user wants to build GitHub 
    BabyAGI UI: Make it easier to run and develop with babyagi in a web app, like a ChatGPT GitHub 
    SuperAgent: Deploy LLM Agents to production GitHub 
    Voyager: An Open-Ended Embodied Agent with Large Language Models GitHub 
    ix: Autonomous GPT-4 agent platform GitHub 
    DuetGPT: A conversational semi-autonomous developer assistant, AI pair programming without the copypasta. GitHub 
    Multi-Modal LangChain agents in Production: Deploy LangChain Agents and connect them to Telegram GitHub 
    DemoGPT: DemoGPT enables you to create quick demos by just using prompt. It applies ToT approach on Langchain documentation tree. GitHub 
    SuperAGI: SuperAGI - A dev-first open source autonomous AI agent framework GitHub 
    Autonomous HR Chatbot: An autonomous agent that can answer HR related queries autonomously using the tools it has on hand GitHub 
    BlockAGI: BlockAGI conducts iterative, domain-specific research, and outputs detailed narrative reports to showcase its findings GitHub 
    waggledance.ai: An opinionated, concurrent system of AI Agents. It implements Plan-Validate-Solve with data and tools for general goal-solving. GitHub 
    Elasticsearch Agent: ElasticSearch agent based on ElasticSearch, LangChain and GPT 4 GitHub 
    CrewAI: Cutting-edge framework for orchestrating role-playing, autonomous AI agents. GitHub 

Reference: 
    https://www.pinecone.io/learn/series/langchain/langchain-tools/

Custom Tools:
    from langchain.tools import BaseTool
    from math import pi
    from typing import Union
    class CircumferenceTool(BaseTool):
      name = "Circumference calculator"
      description = "use this tool when you need to calculate a circumference using the radius of a circle"

    def _run(self, radius: Union[int, float]):
        return float(radius)*2.0*pi

class PythagorasTool(BaseTool):
    name = "Hypotenuse calculator"
    description = desc
    
    def _run(
        self,
        adjacent_side: Optional[Union[int, float]] = None,
        opposite_side: Optional[Union[int, float]] = None,
        angle: Optional[Union[int, float]] = None
    ):
        # check for the values we have been given
        if adjacent_side and opposite_side:
            return sqrt(float(adjacent_side)**2 + float(opposite_side)**2)
        elif adjacent_side and angle:
            return adjacent_side / cos(float(angle))
        elif opposite_side and angle:
            return opposite_side / sin(float(angle))
        else:
            return "Could not calculate the hypotenuse of the triangle. Need two or more of `adjacent_side`, `opposite_side`, or `angle`."
    
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")
tools = [PythagorasTool()]

One large crew broken down into multiple task to achieve one large goal.