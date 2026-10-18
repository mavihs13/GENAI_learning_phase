from langchain_huggingface import  ChatHuggingFace , HuggingFacePipeline


llm  = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        temperature = 0.7,
        max_new_tokens = 1024
    )
)

try:
    model = ChatHuggingFace(llm=llm)
    result = model.invoke("explain what is open source model")
    print(result.text)
except Exception as e:
    print("Error:", e)    