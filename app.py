!pip install langchain
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

repo_id ="tiiuae/falcon-7b-instruct"
huggingfacehub_api_token="*************************"
llm= HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                    repo_id=repo_id,
                    model_kwargs={"temperature":0.7,"max_new_tokens":500})
					

template ="""Question: {question}
             Answer: Let's give a detailed answer."""

prompt =PromptTemplate(template=template, input_variables=["question"])

chain=LLMChain(prompt=prompt, llm=llm)

out=chain.run("Who is the father of Turing machine?")
print(out)

out=chain.run("How to create cup of milk tea?")
print(out)
