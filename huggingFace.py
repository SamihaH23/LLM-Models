from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="google/flan-t5-base",
                     model_kwargs={
                         "temperature": 0,
                         "max_length": 64
                     })

prompt = "What are good fitness tips for a beginner?"

print(llm(prompt))
