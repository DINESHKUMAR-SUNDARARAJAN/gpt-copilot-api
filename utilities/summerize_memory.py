from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

def summarize_memory(messages):
    prompt = "Summarize this conversation for future reference:\n\n"
    for m in messages:
        prompt += f"{m.type.upper()}: {m.content}\n"

    summary = llm.invoke([HumanMessage(content=prompt)])
    return summary