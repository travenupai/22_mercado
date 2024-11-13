# Vidmarmercado Crew



Welcome to the Swot Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.


1. PARA CRIAR UM AMBIENTE VIRTUAL .VENV (SE CRIA O VENV NO DIRETÓRIO RAIZ):

## Installation
criar um NOVO projeto:
1. NO GERENCIADOR DE ARQUIVOS:
Crie um diretório na pasta projetos-python e de um número sequencial.

2. NO TERMINAL:

cd 22_mercado
python -m venv .venv
.venv\Scripts\activate
uv pip install crewai

3. ATENCAO: SE VOCÊ CRIA UM NOVO PROJETO OU FLOW OU PIPELINE, DE ESSES COMANDOS:
NO TERMINAL:
crewai create crew vidmarmercado (exemplo)

crewai create crew nome_do_projeto
ou
crewai create flow nome_do_flow
ou
crewai create pipeline nome_do_pipeline


APOS A CRIACAO DO CREWAI, APAGUE O .venv NO 22_MERCADO

cd vidmarmercado

######### PARA O STREAMLIT FUNCIONAR O CREWAI TEM QUE SER VERSAO 0.61.0

PARA ATIVAR UM VENV NO PYTHON 3.11.7

VÁ ATÉ O DIRETÓRIO RAIZ:
C:\projetos-python\22_mercado\vidmarmercado.

ENTAO DE O COMANDO:
C:\Users\Ashram\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv
.venv\Scripts\Activate
python --version
pip install uv
uv pip install crewai==0.61.0 
uv pip install crewai-tools==0.8.3 
pip freeze | Select-String "crewai"


OU O COMANDO PARA O PYTHON 3.12.6:
python.exe -m venv .venv
.venv\Scripts\Activate
python --version
pip install uv
uv pip install crewai
uv pip install crewai-tools
pip freeze | Select-String "crewai"

uv lock
uv sync


NUNCA USE WEBSITE SEARCH TOOL, ISSO CRIA O DB E ESTRAGA TUDO NO STREAMLIT

4. NO TERMINAL AVANÇE PARA O NOVO DIRETORIO CRIADO

cd novo_diretório
feche todas as abas do open editors, cada uma aberta, não deixa atualizar.


AGORA FAÇA TODA A CRIAÇÃO DA CREW E RETORNE
Ensure you have Python >=3.10 <=3.13 installed on your system. 
This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

5. Para rodar o programa:

crewai run      # Para executar o seu projeto principal


6. PARA QUEM JÁ CRIOU O AMBIENTE VIRTUAL E ESTÁ RETORNANDO:
vá para o diretório RAIZ do projeto 

C:\projetos-python\22_mercado\vidmarmercado

.venv\Scripts\activate    

Não há necessidade de repetir crewai install a menos que você tenha mudado o ambiente (criado um novo ambiente virtual) ou atualizado o pyproject.toml.
uv lock e uv sync: Esses comandos só são necessários para atualizar dependências ou se alguma mudança significativa foi feita no pyproject.toml.

Para rodar o programa:

crewai run      # Para executar o seu projeto principal

## 3. Subir um repositório do VSCode para o GitHub

1. No VSCode, abra o terminal integrado (`Ctrl + '`).
2. Navegue até o diretório do seu projeto, caso ainda não esteja nele:
   ```bash
   cd caminho/para/seu/projeto
   ```
3. Inicialize o repositório local do Git, se ainda não foi feito:
   ```bash
   git init
   ```
4. Adicione os arquivos ao repositório:
   ```bash
   git add .
   ```
5. Faça o primeiro commit:
   ```bash
   git commit -m "Primeiro commit"
   ```
6. Conecte seu repositório local ao GitHub. Use a URL do repositório que você criou no GitHub:
   ```bash
   git remote add origin https://github.com/seu-usuario/nome-repositorio.git
   ```
7. Faça o envio (push) do repositório para o GitHub:
   ```bash
   git push -u origin main
   ```

## 4. Atualizar um repositório do VSCode no GitHub

1. Adicione os novos arquivos ou mudanças ao repositório:
   ```bash
   git add .
   ```
2. Faça o commit com uma mensagem que descreva as alterações:
   ```bash
   git commit -m "Descrição das alterações"
   ```
3. Envie as alterações para o GitHub:
   ```bash
   git push origin main
   ```

## 5. Publicar um projeto do GitHub no Streamlit

uv pip install streamlit

streamlit run app.py

0. SE QUISER RODAR NO SEU COMPUTADOR: no terminal:  steamlit run app.py

1. Crie um arquivo **`requirements.txt`** na raiz do projeto, listando todas as bibliotecas usadas no projeto, por exemplo:
requirements.txt
   ```plaintext
crewai==0.76.9                   # Orquestra agentes e tarefas
crewai-tools==0.13.4             # Ferramentas adicionais para CrewAI
python-dotenv==1.0.1             # Carregar variáveis de ambiente do .env
openai==1.54.0                   # API para LLMs da OpenAI (se necessário)
requests==2.32.3                 # Chamadas HTTP (caso precise)
streamlit==1.39.0                # Interface Web
fpdf2==2.8.1                     # Manipulação de PDFs (se necessário)
python-docx==0.8.11              # Geração de arquivos Word

   streamlit
   pandas
   numpy
   ```
2. No site do [Streamlit](https://share.streamlit.io/), faça login.
3. Clique em **New App** para iniciar o processo de "deploy a public app from Github".
4. No campo **Repository**, insira a URL do seu repositório GitHub, por exemplo:
   ```plaintext
   https://github.com/seu-usuario/nome-repositorio
   ```
5. No campo **Branch**, selecione **main**.
6. No campo **Main file path**, insira o caminho do arquivo Python principal que roda o Streamlit, por exemplo:
   ```plaintext
   src/app.py
   ```
7. Clique em **Deploy** para publicar seu app.

## 6. Voltar para uma versão anterior no GitHub usando o VSCode

1. Verifique o histórico de commits com:
   ```bash
   git log
   ```
   Isso mostrará a lista de commits, incluindo os códigos de hash dos commits (identificadores únicos).
   
2. Para voltar para um commit anterior temporariamente, use o comando:
   ```bash
   git checkout <hash-do-commit>
   ```
   Isso permite que você explore o código como ele estava naquele commit.

3. Para voltar permanentemente para um commit anterior, faça um reset:
   ```bash
   git reset --hard <hash-do-commit>
   ```
   **Atenção:** Isso sobrescreverá as mudanças feitas após esse commit. Use com cuidado.

4. Se você já tiver feito um `reset` e precisar atualizar o repositório remoto, faça o push forçado:
   ```bash
   git push --force
   ```

---

## Como apagar o venv:
No terminal:

deactivate

Remove-Item -Recurse -Force .venv

python -m venv .venv

.venv\Scripts\activate

pip install -U pip
pip install uv
pip install crewai
pip install crewai-tools

uv lock
uv sync



### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/sales_offer/config/agents.yaml` to define your agents
- Modify `src/sales_offer/config/tasks.yaml` to define your tasks
- Modify `src/sales_offer/crew.py` to add your own logic, tools and specific args
- Modify `src/sales_offer/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
uv run sales_offer
```

This command initializes the sales-offer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The sales-offer Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the SalesOffer Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


