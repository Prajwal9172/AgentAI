# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task

# # If you want to run a snippet of code before or after the crew starts, 
# # you can use the @before_kickoff and @after_kickoff decorators
# # https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# @CrewBase
# class CrewAgent():
# 	"""CrewAgent crew"""

# 	# Learn more about YAML configuration files here:
# 	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
# 	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
# 	agents_config = 'config/agents.yaml'
# 	tasks_config = 'config/tasks.yaml'

# 	# If you would like to add tools to your agents, you can learn more about it here:
# 	# https://docs.crewai.com/concepts/agents#agent-tools
# 	@agent
# 	def researcher(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['researcher'],
# 			verbose=True
# 		)

# 	@agent
# 	def reporting_analyst(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['reporting_analyst'],
# 			verbose=True
# 		)

# 	# To learn more about structured task outputs, 
# 	# task dependencies, and task callbacks, check out the documentation:
# 	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
# 	@task
# 	def research_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['research_task'],
# 		)

# 	@task
# 	def reporting_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['reporting_task'],
# 			output_file='report.md'
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the CrewAgent crew"""
# 		# To learn how to add knowledge sources to your crew, check out the documentation:
# 		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			process=Process.sequential,
# 			verbose=True,
# 			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
# 		)

from pydantic import BaseModel
from typing import List

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

# 1. Define our JSON schema via Pydantic
class JiraStory(BaseModel):
    title: str
    content: str

class JiraStories(BaseModel):
    stories: List[JiraStory]  # enforces [{"title":"…","content":"…"},…]&#8203;:contentReference[oaicite:4]{index=4}

@CrewBase
class CrewAgent():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # 2. Agents from YAML
    # @agent
    # def researcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['researcher'],
    #         verbose=True
    #     )

    # @agent
    # def reporting_analyst(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reporting_analyst'],
    #         verbose=True
    #     )

    @agent
    def jira_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['jira_agent'],
            verbose=True,
        )  # matches jira_agent in agents.yaml&#8203;:contentReference[oaicite:5]{index=5}

    # 3. Tasks from YAML + structured output
    # @task
    # def research_task(self) -> Task:
    #     return Task(config=self.tasks_config['research_task'])

    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reporting_task'],
    #         output_file='report.md'
    #     )

    @task
    def jira_task(self) -> Task:
        return Task(
            config=self.tasks_config['jira_task'],
            output_json=JiraStories  # validate & parse final JSON :contentReference[oaicite:6]{index=6}
        )

    # 4. Assemble the Crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )  # sequential pipeline of research → report → Jira generation :contentReference[oaicite:7]{index=7}
