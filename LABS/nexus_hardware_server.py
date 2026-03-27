import asyncio
import subprocess
import json
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types

# 1. Initialize the MCP Server
server = Server("nexus-hardware-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available hardware monitoring tools."""
    return [
        types.Tool(
            name="get_hardware_status",
            description="Get real-time VRAM or System RAM usage securely.",
            inputSchema={
                "type": "object",
                "properties": {
                    "hardware_model": {
                        "type": "string",
                        "description": "The target hardware. e.g. 'RTX 3080 Ti' or 'System RAM'"
                    }
                },
                "required": ["hardware_model"]
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Execute the hardware monitor tool inside the Sandbox."""
    
    if name == "get_hardware_status":
        hardware = arguments.get("hardware_model", "") if arguments else ""
        
        # 🛡️ THE SANDBOX (Safe Schema Validation)
        if hardware not in ["RTX 3080 Ti", "System RAM"]:
            return [types.TextContent(type="text", text=f"🛑 Permission Denied: '{hardware}' is restricted and NOT in the Safe Schema.")]
            
        try:
            if hardware == "RTX 3080 Ti":
                cmd = "nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu --format=csv,nounits,noheader"
                result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
                mem_used, mem_total, util = result.split(',')
                status_report = f"🚀 RTX 3080 Ti Status: {mem_used}MB / {mem_total}MB VRAM | {util}% Util"
                
            elif hardware == "System RAM":
                cmd = "free -m | grep Mem"
                result = subprocess.check_output(cmd, shell=True).decode('utf-8').split()
                mem_total = result[1]
                mem_used = result[2]
                status_report = f"💻 System RAM Status: {mem_used}MB / {mem_total}MB Used"

            return [types.TextContent(type="text", text=status_report)]
        except Exception as e:
            return [types.TextContent(type="text", text=f"❌ Error accessing Hardware: {str(e)}")]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    # Run the server using Standard Input/Output (stdio)
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="nexus-hardware-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
