from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, ScrapeElementFromWebsiteTool
from vidmarmercado.my_llm import MyLLM
load_dotenv()
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
scrape_element_tool = ScrapeElementFromWebsiteTool()
# from langchain_openai import ChatOpenAI
gpt4o_mini = MyLLM.gpt4o_mini	

# Uncomment the following line to use an example of a custom tool
# from vidmarmercado.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

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
			allow_interruption=True,  # Permite interrupções para reagir rapidamente a mudanças nos produtos dos concorrentes
			allow_fallback=True,      # Permite fallback caso precise de um especialista em tecnologia ou satisfação do cliente
			memory=True,
			llm=gpt4o_mini,
		)

	@agent
	def market_trends_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['market_trends_agent'],
			tools=[search_tool, scrape_tool, scrape_element_tool],
			allow_delegation=True,
			verbose=True,
			llm=gpt4o_mini,
			allow_interruption=True,  # Permite interrupções para reagir rapidamente a mudanças nos produtos dos concorrentes
            allow_fallback=True,      # Permite fallback caso precise de um especialista em tecnologia ou satisfação do cliente
			memory=True  
		)

	@agent
	def product_analysis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['product_analysis_agent'],
			tools=[search_tool, scrape_tool, scrape_element_tool],
			allow_delegation=True,
			verbose=True,
			llm=gpt4o_mini,
			allow_interruption=True,  # Permite interrupções para reagir rapidamente a mudanças nos produtos dos concorrentes
            allow_fallback=True,      # Permite fallback caso precise de um especialista em tecnologia ou satisfação do cliente
			memory=True
		)

	@task
	def customer_feedback_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['customer_feedback_analysis'],
			output_file='customer_feedback_analysis.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 5000}]
		)

	@task
	def market_trends_monitoring(self) -> Task:
		return Task(
			config=self.tasks_config['market_trends_monitoring'],
			output_file='market_trends_monitoring.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 5000}]
		)

	@task
	def product_comparison(self) -> Task:
		return Task(
			config=self.tasks_config['product_comparison'],
			output_file='product_comparison.md',
            guardrails=[{"output_format": "markdown"}, {"max_length": 5000}]
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Vidmarmercado crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=False  # Desativa a memória
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)