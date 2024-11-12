from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("A chave de API da OpenAI não foi encontrada. Verifique seu arquivo .env.")

class MyLLM:
    # Definir o modelo LLM usando ChatOpenAI e a chave da API
    gpt_mini              = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=api_key)
    gpt4o_mini            = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=api_key)
    gpt4o_mini_2024_07_18 = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", openai_api_key=api_key)
    gpt_4o_2024_08_06     = ChatOpenAI(model_name="gpt-4o-2024-08-06", openai_api_key=api_key)
    gpt4o                 = ChatOpenAI(model_name="gpt-4o", openai_api_key=api_key)
    gpt_o1                = ChatOpenAI(model_name="o1-preview", openai_api_key=api_key)
    gpt_o1_mini           = ChatOpenAI(model_name="o1-mini", openai_api_key=api_key)
    Ollama_llama_3_1      = ChatOpenAI(model_name="ollama/llama3.1", base_url="http://localhost:1140/openai-8B", openai_api_key=api_key)
