from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from  typing import Literal


load_dotenv()

parser1 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)



model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.2)

prompt1 = PromptTemplate(
    template = 'Classify the given sentiment of the following feedback into positive, negative  \n{feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={
        "format_instructions": parser2.get_format_instructions()
    }
)

prompt2 = PromptTemplate(
    template = 'Write a polite and appreciative response to this positive feedback: \n{feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write a professional and empathetic response to this negative feedback. Acknowledge the issue and offer help. \n{feedback}',
    input_variables=['feedback']
)

classify_chain = prompt1 | model | parser2
 
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser1),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "No valid sentiment detected")
)

chain = classify_chain | branch_chain

user_feedback = input("Enter your feedback: ")
result = chain.invoke({'feedback': user_feedback})
print(result)
chain.get_graph().print_ascii()