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
            
            # 5. Execute custom hardware tool to test Sandbox!
            print("\n==== 🛡️ SANDBOX PENETRATION TEST ====")
            
            print("\n1️⃣ Testing Unauthorized Hardware...")
            res1 = await session.call_tool("get_hardware_status", arguments={"hardware_model": "RTX 4090"})
            print(f"  Result: {res1.content[0].text}")
            
            print("\n2️⃣ Testing Authorized System RAM...")
            res2 = await session.call_tool("get_hardware_status", arguments={"hardware_model": "System RAM"})
            print(f"  Result: {res2.content[0].text}")

            print("\n3️⃣ Testing Authorized RTX 3080 Ti...")
            res3 = await session.call_tool("get_hardware_status", arguments={"hardware_model": "RTX 3080 Ti"})
            print(f"  Result: {res3.content[0].text}")

if __name__ == "__main__":
    asyncio.run(run_mcp_test())
