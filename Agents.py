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

search_tool = DuckDuckGoSearchRun()

class EmailAgents():
    def make_categorizer_agent(self):
        return Agent(
            role='Email Categorizer Agent',
            goal="""take in a email from a human that has emailed out company email address and categorize it \
            into one of the following categories: \
            price_equiry - used when someone is asking for information about pricing \
            customer_complaint - used when someone is complaining about something \
            product_enquiry - used when someone is asking for information about a product feature, benefit or service but not about pricing \\
            customer_feedback - used when someone is giving feedback about a product \
            off_topic when it doesnt relate to any other category """,
            backstory="""You are a master at understanding what a customer wants when they write an email and are able to categorize it in a useful way""",
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: print_agent_output(x,"Email Categorizer Agent"),
        )

    def make_researcher_agent(self):
        return Agent(
            role='Info Researcher Agent',
            goal="""take in a email from a human that has emailed out company email address and the category \
            that the categorizer agent gave it and decide what information you need to search for for the email writer to reply to \
            the email in a thoughtful and helpful way.
            If you DONT think a search will help just reply 'NO SEARCH NEEDED'
            If you dont find any useful info just reply 'NO USEFUL RESESARCH FOUND'
            otherwise reply with the info you found that is useful for the email writer
            """,
            backstory="""You are a master at understanding what information our email writer needs  to write a reply that \
            will help the customer""",
            llm=GROQ_LLM,
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            memory=True,
            tools=[search_tool],
            step_callback=lambda x: print_agent_output(x,"Info Researcher Agent"),
        )

    def make_email_writer_agent(self):
        return Agent(
            role='Email Writer Agent',
            goal="""take in a email from a human that has emailed out company email address, the category \
            that the categorizer agent gave it and the research from the research agent and \
            write a helpful email in a thoughtful and friendly way.

            If the customer email is 'off_topic' then ask them questions to get more information.
            If the customer email is 'customer_complaint' then try to assure we value them and that we are addressing their issues.
            If the customer email is 'customer_feedback' then try to assure we value them and that we are addressing their issues.
            If the customer email is 'product_enquiry' then try to give them the info the researcher provided in a succinct and friendly way.
            If the customer email is 'price_equiry' then try to give the pricing info they requested.

            You never make up information. that hasn't been provided by the researcher or in the email.
            Always sign off the emails in appropriate manner and from Sarah the Resident Manager.
            """,
            backstory="""You are a master at synthesizing a variety of information and writing a helpful email \
            that will address the customer's issues and provide them with helpful information""",
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: print_agent_output(x,"Email Writer Agent"),
        )