# Email-Reply-Generator-for-Enterprise-using-Llama3-70b-with-Groq-CrewAI

**Email Response Generator**
=============================================

**Overview**
-----------

This system is designed to categorize incoming emails and generate responses based on the category. The system uses a combination of natural language processing (NLP) and machine learning algorithms to analyze the email content and determine the appropriate response.

**Components**
--------------

### Agents

* **Categorizer Agent**: Analyzes the email content and categorizes it into one of the following categories: price_enquiry, customer_complaint, product_enquiry, customer_feedback, or off_topic.
* **Researcher Agent**: Conducts research to gather information needed to respond to the email.
* **Email Writer Agent**: Writes a response to the email based on the category and research results.

### Tasks

* **Categorize Email**: Categorizes the email content using the Categorizer Agent.
* **Research Info for Email**: Conducts research to gather information needed to respond to the email using the Researcher Agent.
* **Draft Email**: Writes a response to the email based on the category and research results using the Email Writer Agent.

**How it Works**
----------------

1. The system receives an email as input.
2. The Categorizer Agent analyzes the email content and categorizes it into one of the five categories.
3. The Researcher Agent conducts research to gather information needed to respond to the email.
4. The Email Writer Agent writes a response to the email based on the category and research results.
5. The system outputs the response to the email.

**Technical Requirements**
-------------------------

* Python 3.x
* Langchain library
* CrewAI library
* Groq API key
* LLMs and Multi Agent Architecture

**Usage**
-----

1. First clone this Repository: `git clone https://github.com/Soumyajit-7/Email-Reply-Generator-for-Enterprise-using-Llama3-70b-with-Groq-CrewAI-.git`
2. Install the required libraries using pip: `pip install -r requirements.txt`
3. Go to `https://console.groq.com/keys` and generate your api key
4. Set the Groq API key as an environment variable: `$env:GROQ_API_KEY="GROQ_API_KEY"`
5. Run the system using the following command: `python main.py`
6. Enter the email content when prompted.


**Authors**
---------

* Soumyajit Biswas
