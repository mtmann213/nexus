import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. Setup the Server Parameters
# We tell the client how to 'start' our local hardware server
server_params = StdioServerParameters(
    command="../venv/bin/python",
    args=["nexus_hardware_server.py"],
)

async def run_mcp_test():
    print("📡 Connecting to the MCP Filesystem Server...")
    
    # 2. Establish the 'Bridge' (stdio connection)
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            
            # 3. Perform the Handshake (Initialize)
            await session.initialize()
            print("✅ Handshake Successful! Connection established.")

            # 4. Discover the Tools!
            # Instead of us TELLING the AI what it can do, 
            # the server tells US.
            print("\n🔍 Asking the Librarian for its tools...")
            tools = await session.list_tools()
            
            for tool in tools.tools:
                print(f"  🛠️ Found Tool: {tool.name}")
                print(f"     Description: {tool.description[:60]}...")
            
            # 5. Execute a custom hardware tool!
            print("\n📊 Querying the GPU Status via MCP...")
            result = await session.call_tool("get_gpu_status", arguments={})
            print(f"  Result: {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(run_mcp_test())
