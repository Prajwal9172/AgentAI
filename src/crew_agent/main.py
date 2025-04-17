# #!/usr/bin/env python
# import sys
# import warnings

# from datetime import datetime

# from crew_agent.crew import CrewAgent

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs',
#         'current_year': str(datetime.now().year)
#     }
    
#     try:
#         CrewAgent().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         CrewAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         CrewAgent().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         CrewAgent().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")


#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from crew_agent.crew import CrewAgent
from dotenv import load_dotenv
load_dotenv() 

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew on a local markdown file to generate Jira stories.
    Usage: python main.py path/to/spec.md
    """
    # if len(sys.argv) < 2:
    #     raise Exception("Please pass the path to your markdown file.")
    # md_path = sys.argv[1]
    md_path = "prd.md"
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year),
        'markdown_content': md
    }

    try:
        result = CrewAgent().crew().kickoff(inputs=inputs)  # kickoff with Markdown spec&#8203;:contentReference[oaicite:8]{index=8}
        # The final JSON is in result.json_dict
        print(result.json_dict)
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# if __name__ == "__main__":
#     run()
