from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class MyLLM():
    
    # Definir o modelo LLM
    gpt_mini              = ChatOpenAI(model_name="gpt-4o-mini")
    gpt4o_mini            = ChatOpenAI(model_name="gpt-4o-mini")
    gpt4o_mini_2024_07_18 = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18")
    gpt_4o_2024_08_06     = ChatOpenAI(model_name="gpt-4o-2024-08-06")
    gpt4o                 = ChatOpenAI(model_name="gpt-4o")
    gpt_o1                = ChatOpenAI(model_name="o1-preview")
    gpt_o1_mini           = ChatOpenAI(model_name="o1-mini")
    Ollama_llama_3_1      = ChatOpenAI(model_name="ollama/llama3.1", base_url="http://localhost:1140/openai-8B")