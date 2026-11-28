from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a detail notes on {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="generate a 5 line summary on the following \n {text}",
    input_variables=['text']
)

model = ChatGroq(model='openai/gpt-oss-20b',temperature=0.2)

chain = prompt1 | model | parser | prompt2 | model | parser

topic = input("Enter your topic:\n")

if not topic.strip():
    print("please enter valid topic")
else:    
  result = chain.invoke({'topic':'Generative AI'})
  print("======Final Summary=======")

print(result)

chain.get_graph().print_ascii();



