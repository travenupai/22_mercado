# crew.py

import os
import openai
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, ScrapeElementFromWebsiteTool
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Set up OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

openai.api_key = api_key

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=api_key)

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
scrape_element_tool = ScrapeElementFromWebsiteTool()

@CrewBase
class VidmarmercadoCrew():
    """Vidmarmercado crew"""

    @agent
    def customer_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_analysis_agent'],
            tools=[search_tool, scrape_tool],
            verbose=True,
            allow_delegation=True,
            allow_interruption=True,
            allow_fallback=True,
            memory=True,
            llm=llm
        )

    @agent
    def market_trends_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_trends_agent'],
            tools=[search_tool, scrape_tool, scrape_element_tool],
            verbose=True,
            allow_delegation=True,
            allow_interruption=True,
            allow_fallback=True,
            memory=True,
            llm=llm
        )

    @agent
    def product_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['product_analysis_agent'],
            tools=[search_tool, scrape_tool, scrape_element_tool],
            verbose=True,
            allow_delegation=True,
            allow_interruption=True,
            allow_fallback=True,
            memory=True,
            llm=llm
        )

    @task
    def customer_feedback_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['customer_feedback_analysis'],
            output_file='customer_feedback_analysis.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 20000}]
        )

    @task
    def market_trends_monitoring(self) -> Task:
        return Task(
            config=self.tasks_config['market_trends_monitoring'],
            output_file='market_trends_monitoring.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 20000}]
        )

    @task
    def product_comparison(self) -> Task:
        return Task(
            config=self.tasks_config['product_comparison'],
            output_file='product_comparison.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 20000}]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Vidmarmercado crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True  # Activate memory
        )
