from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

root_agent = Agent(
    name="cypher_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    instruction="Write the cypher query for the data needed by the user",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="docker",
                args=["run", "--rm", "mcp/neo4j-cypher:latest"],
                env={
                    "NEO4J_URI": "bolt://174.31.71.124",
                    "NEO4J_USERNAME": "neo4j",
                    "NEO4J_PASSWORD": "Bluewhale*123"
                }
            )

        ),
    ],
)
