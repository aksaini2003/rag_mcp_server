from fastmcp import FastMCP 



#we have to paste the link of server and give a name to it 
server=FastMCP.as_proxy(
    "https://rag-demo-server-by-ak.fastmcp.app/mcp",
    name='Demo Rag Server'
)
if __name__=='__main__':
    server.run()