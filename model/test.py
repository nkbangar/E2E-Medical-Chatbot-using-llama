from langchain_ollama import OllamaLLM
 
llm = OllamaLLM(model="llama2", base_url="http://localhost:11434")
 
response = llm.invoke("Write a short poem about coding")
print(response)