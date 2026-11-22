
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Initialize LLM
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Define output structure
class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(description="The age of the person")
    city: str = Field(description="The city where the person lives")

# Create parser
parser = PydanticOutputParser(pydantic_object=Person)

# Create prompt template
template = PromptTemplate(
    template="""
    Generate details of a {person_type} person.

    {format_instructions}
    """,
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


#-----without chain-----------------

# Generate prompt
prompt = template.invoke({'person_type': 'Indian'})
print(prompt)

# Get LLM response
response = model.invoke(prompt)

# Parse response
final_result = parser.parse(response.content)

print(final_result)
print(type(final_result))


#-----with chain-----------------

chain = template | model | parser
result = chain.invoke({'person_type': 'Indian'})
print(result)