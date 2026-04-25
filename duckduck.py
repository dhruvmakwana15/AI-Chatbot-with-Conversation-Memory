from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.tools import tool

path= r"C:\Users\dhruv\OneDrive\Desktop\Langchain_model\Chatmodel\.env"
load_dotenv(path)

llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = [DuckDuckGoSearchRun()]
#result=search_tool.invoke("top news in  india")

from langchain_classic.agents import AgentExecutor,create_react_agent,initialize_agent
from langchain_classic import hub

prompt=hub.pull("hwchase17/react")
prompt = prompt.partial(
    instructions="""
Use the following format:

Thought: think step by step
Action: the tool to use (duckduckgo_search)
Action Input: input to the tool
Observation: result of the tool
...
Thought: I now know the final answer
Final Answer: final answer to user
"""
)
agent=create_react_agent(
    llm=model,
    tools=[search_tool[0]],
    prompt=prompt,
)

Agent_Executor=AgentExecutor(
    agent=agent,
    tools=[search_tool[0]],
    verbose=True,
    handle_parsing_errors=True
)
def plan_trip():
    print(" Welcome to Manan Travel Planner \n")

    origin = input("Enter your origin city: ")
    destination = input("Enter your destination city: ")
    budget = input("Enter your budget (in INR or USD): ")
    transport = input("Preferred transport (flight/train/bus/car): ")

    query = f"""
    Plan a personalized {transport} trip from {origin} to {destination}
    within a budget of {budget}.
    Include 3 travel options, hotel suggestions, and a 3-day itinerary.
    """

    response = Agent_Executor.invoke({"input": query})
    print("\n Your Personalized Travel Plan:\n")
    print(response["output"])

if __name__ == "__main__":
    plan_trip()  
