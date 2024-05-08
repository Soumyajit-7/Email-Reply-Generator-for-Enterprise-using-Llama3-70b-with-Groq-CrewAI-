from crewai import Crew, Agent, Task, Process
from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime
from random import randint
from langchain.tools import tool
import json
import os

import requests
from langchain.tools import tool

import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools

search_tool = DuckDuckGoSearchRun()