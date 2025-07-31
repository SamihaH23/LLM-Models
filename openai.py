from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
prompt = "What are the cities of France?"

result = llm.generate([prompt] * 5)
for cities in result.generations:
  print(cities[0].text.strip())
