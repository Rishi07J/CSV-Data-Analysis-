import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

def load_dataframe(data):
    return pd.read_csv(data)

def query_agent(df, query):
    llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile")
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type="openai-tools",
        allow_dangerous_code=True
    )
    result = agent.invoke(query)

    # If result is dict with "output" key, return just the output text
    if isinstance(result, dict) and "output" in result:
        return result["output"]
    return result
