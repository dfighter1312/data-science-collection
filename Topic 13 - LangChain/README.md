# Topic 13 - LangChain

## What this repository do?

This is an experimental repository for LangChain, a framework for developing applications powered by language models. I will somehow explore several functionalities of this framework, then extract which kind of applications that I can build using this framework.

As the first step, I have followed the Quickstart in the [documentation](https://python.langchain.com/en/latest/getting_started/getting_started.html), and perform a specific usecase using LangChain, exploratory data analysis.

In the second stage, I will go through mostly all of the [tutorials](https://python.langchain.com/en/latest/getting_started/tutorials.html) given in the documentation to earn a better insight about this framework. Notes are recorded in this README file.

The experiments are done in the `notebooks` folder.

## How to run the repository?

In order to run all the notebooks in this repo, please follow the steps:

### Entering the topic folder

```bash
cd "Topic 13 - LangChain"
```

### (Optional, but recommended) Create a new conda environment

```bash
conda create --name langchain
```

### Install all the packages

```bash
pip install -r requirements.txt
```

### Create `.env` file

Create the file with the content as below:

```bash
TEST_VAR=Found
OPENAI_API_KEY=...
SERPAPI_API_KEY=...
HUGGINGFACEHUB_API_TOKEN=...
PINECONE_API_KEY=...
```

`TEST_VAR` is only used for testing in notebook 1, so you can ignore it. Others are API keys and tokens, where you can get by creating a free account on OpenAI, HuggingFace, SerpAPI and Pinecone. For most notebooks, OpenAI's API Key is required, so if you care only about notebook using LLM but not other APIs, just let it empty.

## Struggle and Derived Tips during implementation

It was fun exploring this framework, even this is still the beta version. The limitation of my notebook is mostly from the restriction of OpenAI's and Pinecone's API, which raise some warnings and errors in notebook no. 8 and no.9.

This is the flow I think easy to understand about LangChain:
- Firstly, get your **Large Language Model (model)** and enter the prompt (see notebook `1`). This is similar to interacting in ChatGPT's UI from OpenAI. The model can be accessed via APIs (and you need to get and enter your `API_KEY` in an `.env` file), or getting from Hugging Face Hub (see notebook `3`).
- After that, we try to understand **prompt template**. If you are using only the PromptTemplate (see notebook `1`), it doesn't seem so different to using an f-string in Python.
- Exploring a more advanced concept of prompt, **few shot prompt template**, where you give the model some examples relating to completing the task. If the number of examples is too many, leading to high number of tokens --> costly, **example selector** will help you to select only a few samples (see notebook `6`).
- Next is **chain**. Similar to a machine learning pipeline, chain enables sequential steps to execute from a prompt to your final answer.
- So far, the LLM cannot remember anything you have entered. That is where **memory** comes to the rescue. Basically, it is just adding your conversation so far at the beginning of your new prompt. To avoid too many tokens, customized memory types such as summarizing the history, filter out the earliest conversation, etc. are available (see notebook `6`).
- If your need can not be resolved by sequential steps from a chain, you can choose to use an **agent** instead. An agent automatically decides which tool to use at every step, execute things using the tool until it gets the final answer. But in specific, it is just a designated prompt that helps the LLM model act like an agent (see notebook `8`).
- A **tool** can be attached in a chain, or an agent. It is customizable giving its name, description (to show the LLM when to use it), and Python implementation (see notebook `9`).
- Several applications of LangChain are explored. 
    - The most common and powerful application is information retrieval, since LLM can only get the information until 2019. LangChain supports **connecting LLM with our own data**, using a combination of **Loader**: from TextLoader, PDFLoader, arxivLoader, ...; **Text Splitter** where we splitted the loaded document into chunks; **Embedding** where we get the numerical representation of every chunk; and **Vector Database** which stores those numerical representations and associated metadata for search (see notebook `3`, `5`, `7`).
    - **Built-in agents** in LangChain are also helpful for exploratory data analysis (see notebook `2`).
    - **Built-in tools** are varied that users can choose which to use (see notebook `1`, `4`).
