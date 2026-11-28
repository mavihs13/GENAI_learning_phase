from langchain_groq import ChatGroq
#from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
load_dotenv()

parser = StrOutputParser()

model1 = ChatGroq(model='openai/gpt-oss-20b')
model2 = ChatGroq(model='openai/gpt-oss-20b')

#model2 = ChatHuggingFace(model='TinyLlama/TinyLlama-1.1B-Chat-v1.0',temperature=0.2)
#model2 = ChatGoogleGenerativeAI(model='gemini-3.8-flash')

prompt1 = PromptTemplate(
    template="Generate the small notes on the given topic \n{topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a simple answer question quize on the notes\n{notes}',
    input_variables=['notes']
)

prompt3 = PromptTemplate(
    template='merger the given notes and quize in one document \n notes->{notes},quize->{quize}',
    input_variables=['notes','quize']
)


notes_chain = prompt1 | model1 | parser


parallel_chain = RunnableParallel({
    'notes': notes_chain,
    'quize': notes_chain | prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

topic = input("Enter your topic:\n")

if not topic.strip():
    print("please enter the valid topic:")
else:
    result = chain.invoke({'topic':topic})
    print(result)    

chain.get_graph().print_ascii();