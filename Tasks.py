import json
import os

import requests
from langchain.tools import tool

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools
from Utils import print_agent_output
from Agents import EmailAgents

from Utils import GROQ_LLM

search_tool = DuckDuckGoSearchRun()

categorizer_agent = EmailAgents().make_categorizer_agent()
researcher_agent = EmailAgents().make_researcher_agent()
email_writer_agent = EmailAgents().make_email_writer_agent()


class EmailTasks():
    # Define your tasks with descriptions and expected outputs
    def categorize_email(self, email_content):
        return Task(
            description=f"""Conduct a comprehensive analysis of the email provided and categorize into \
            one of the following categories:
            price_equiry - used when someone is asking for information about pricing \
            customer_complaint - used when someone is complaining about something \
            product_enquiry - used when someone is asking for information about a product feature, benefit or service but not about pricing \\
            customer_feedback - used when someone is giving feedback about a product \
            off_topic when it doesnt relate to any other category \

            EMAIL CONTENT:\n\n {email_content} \n\n
            Output a single cetgory only""",
            expected_output="""A single categtory for the type of email from the types ('price_equiry', 'customer_complaint', 'product_enquiry', 'customer_feedback', 'off_topic') \
            eg:
            'price_enquiry' \
            """,
            output_file=f"email_category.txt",
            agent=categorizer_agent
            )

    def research_info_for_email(self, email_content):
        return Task(
            description=f"""Conduct a comprehensive analysis of the email provided and the category \
            provided and search the web to find info needed to respond to the email

            EMAIL CONTENT:\n\n {email_content} \n\n
            Only provide the info needed DONT try to write the email""",
            expected_output="""A set of bullet points of useful info for the email writer \
            or clear instructions that no useful material was found.""",
            context = [self.categorize_email(email_content)],
            output_file=f"research_info.txt",
            agent=researcher_agent
            )

    def draft_email(self, email_content):
        return Task(
            description=f"""Conduct a comprehensive analysis of the email provided, the category provided\
            and the info provided from the research specialist to write an email. \

            Write a simple, polite and too the point email which will respond to the customer's email. \
            If useful use the info provided from the research specialist in the email. \

            If no useful info was provided from the research specialist the answer politely but don't make up info. \

            EMAIL CONTENT:\n\n {email_content} \n\n
            Output a single cetgory only""",
            expected_output="""A well crafted email for the customer that addresses their issues and concerns""",
            context = [self.categorize_email(email_content), self.research_info_for_email(email_content)],
            agent=email_writer_agent,
            output_file=f"draft_email.txt",
            )