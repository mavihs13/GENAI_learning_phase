
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)

load_dotenv()

# Step 1: Initialize the LLM
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5
)

# Step 2: Define the output schema
schema = [
    ResponseSchema(
        name="fact_1",
        description="First fact about the topic"
    ),
    ResponseSchema(
        name="fact_2",
        description="Second fact about the topic"
    ),
    ResponseSchema(
        name="fact_3",
        description="Third fact about the topic"
    )
]

# Step 3: Create the output parser
parser = StructuredOutputParser.from_response_schemas(schema)

# Step 4: Create the prompt template
template = PromptTemplate(
    template="Give me 3 facts about {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


#----------Without Chain-----------------

# Step 5: Generate the prompt
prompt = template.invoke({
    "topic": "Artificial Intelligence"
})

# Step 6: Get response from LLM
response = model.invoke(prompt)

# Step 7: Parse the structured response
result = parser.parse(response.content)

print(result)

#---------With Chain-----------------

chain = template | model | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)
