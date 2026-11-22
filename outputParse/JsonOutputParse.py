from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b",temperature=0.5)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name , age, and city of a frictional person \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})

print(result)

#prompt = template.format()

#result = model.invoke(prompt)
#print(result.text)

#final_result = parser.parse(result.text)
#print(final_result)