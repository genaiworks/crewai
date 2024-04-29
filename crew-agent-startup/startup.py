from crewai import Agent, Task, Process, Crew
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.llms import Ollama

load_dotenv()

api = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.1)

# To load gemini (this api is for free: https://makersuite.google.com/app/apikey)
# api_gemini = os.environ.get("GEMINI-API-KEY")
# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro", verbose=True, temperature=0.1, google_api_key=api_gemini
# )

# To Load Local models through Ollama
# mistral = Ollama(model="mistral")

marketer = Agent(
    role="Market Research Analyst",
    goal="Find out how big is the demand for my services and suggest how to reach the widest possible customer base.",
    backstory="""You are an expert in understanding the market demand, target audience, and competition.  This is 
    crucial for validating whether an idea fulfill a market need and has the potential to attract
    wide audience.  You are good at coming up with ideas on how to appeal to widest possible audience.
    """,
    verbose =True,
    allow_delegation=False,
    llm=llm 
)
technologist = Agent(role="Technology Expert",
    goal="Make assessment on how technologically feasible the company is and what type of technology the company needs to adopt in order to be successful",
    backstory="""You are visionary in the realm of technology, with deep understanding of both current
    and emerging technological trends.  Your expertise lies not in knowing the technology but in
    foreseeing how it can be leveraged to solve real world problms and drive business innovation.
    You have knack for identifying which technological solution best fit different business 
    models and needs, ensuring that companies stay ahead of the curve.  Your insights are crucial
    in aligning technology with business strategies, ensuing that the technological adoption not only
    enhances operational efficiency but also provide a competitive edge in the market.
    """,
    verbose =True,
    allow_delegation=True,
    llm=llm 
    )

business_consultant = Agent(role="Business Development Consultant",
     goal="Evaluate and advise on the business model, scalability, and potential revenue streams to ensure long-term sustainability and profitability",
    backstory="""You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas 
		into viable business models. You have a keen understanding of various industries and are adept at identifying and developing potential revenue streams. 
		Your experience in scalability ensures that a business can grow without compromising its values or operational efficiency. Your advice is not just
		about immediate gains but about building a resilient and adaptable business that can thrive in a changing market.""",
    verbose =True,
    allow_delegation=True,
    llm=llm 
    )

task1 = Task(
    description=""" 
        Analyze what the market demand for plugs for holes in AI consultant in legal domain. 
		Write a detailed report with description of what the ideal customer might look like, and how to reach the widest possible audience. The report has to 
		be concise with at least 10 bullet points and it has to address the most important areas when it comes to marketing this type of business.
    """,
    agent=marketer,
)

task2 = Task(
    description=""" 
        Analyze what the market demand for plugs for holes in AI consultant in legal domain.. Write a detailed report 
		with description of which technologies the business needs to use in become expert consultant in generative ai domain. The report has to be concise with 
		at least 10  bullet points and it has to address the most important areas when it comes to manufacturing this type of business. 
    """,
    agent=technologist,
)

task3 = Task(
    description=""" 
Analyze and summarize marketing and technological report and write a detailed business plan with 
		description of how to make a sustainable and profitable "for generative ai consultanting" business. 
		The business plan has to be concise with 
		at least 10  bullet points, 5 goals and it has to contain a time schedule for which goal should be achieved and when.
    """,
    agent=business_consultant,
)

crew = Crew(
    agents=[marketer, technologist, business_consultant],
    tasks=[task1,task2,task3],
    verbose=2,
    process=Process.sequential,
)

result = crew.kickoff()

print("**********************************")
print(result)

