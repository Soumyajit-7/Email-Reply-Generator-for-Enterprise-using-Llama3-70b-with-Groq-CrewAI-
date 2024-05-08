import json
import os

import requests
from langchain.tools import tool

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools
from Utils import print_agent_output
from Utils import GROQ_LLM
import os

import requests
from langchain.tools import tool
#api_key=os.getenv("GROQ_API_KEY")
import json  # Import the JSON module to parse JSON strings
from langchain_core.agents import AgentFinish

from langchain_groq import ChatGroq

GROQ_LLM = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"
        )

agent_finishes  = []

import json
from typing import Union, List, Tuple, Dict
from langchain.schema import AgentFinish
from Agents import EmailAgents
from Tasks import EmailTasks
search_tool = DuckDuckGoSearchRun()

##
agents = EmailAgents()
tasks = EmailTasks()

EMAIL=input("Enter the email: ")

## Agents
categorizer_agent = agents.make_categorizer_agent()
researcher_agent = agents.make_researcher_agent()
email_writer_agent = agents.make_email_writer_agent()

## Tasks
categorize_email = tasks.categorize_email(EMAIL)
research_info_for_email = tasks.research_info_for_email(EMAIL)
draft_email = tasks.draft_email(EMAIL)

from crewai import Crew, Process

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[categorizer_agent, researcher_agent, email_writer_agent],
    tasks=[categorize_email, research_info_for_email, draft_email],
    verbose=2,
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    step_callback=lambda x: print_agent_output(x,"MasterCrew Agent")
)

# Kick off the crew's work
results = crew.kickoff()


# Print the results
print("Crew Work Results:")
print(results)

# print(f"Categorize Email: {categorize_email.output}")
print(crew.usage_metrics)
