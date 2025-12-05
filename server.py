#lets make the mcp server which contains a rag tool 

from fastmcp import FastMCP 
from dotenv import load_dotenv 
load_dotenv() 
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.vectorstores import FAISS


server=FastMCP('Rag_server') 


@server.tool 
def rag_tool(query: str)-> dict:
    """This rag tool return the related docs to the given query """
    embedding_model=GoogleGenerativeAIEmbeddings(model='text-embedding-004')
    vector_store=FAISS.load_local('vector-db',embeddings=embedding_model,allow_dangerous_deserialization=True) 
    
    retriever=vector_store.as_retriever(search_type='similarity',kwargs={'k':5
                                                                         })
    #now lets invoke the retriever 
    docs=retriever.invoke(query) 
    #now lets combine the context of differnt docs 
    
    context='\n'.join([doc.page_content for doc in docs]) 
    return {'query':query,'context':context} 


if __name__=='__main__': 
    server.run(transport='http',port=8000,host='0.0.0.0')
    
    #i have check it it is working fine lets connect with our llm_with_chatbot 
    

#for making storing the depenedencise in the requirements.txt in the uv virtual env
# uv pip compile pyproject.toml -o requirements.txt
