from mcp.server.mcpserver import MCPServer
import requests


mcp = MCPServer("User service")


@mcp.tool()
def register_user(name, age: int):
    """
    Register a new user in the User Service.

    Use this tool when the user wants to create/register a new user.
    """
    response = requests.post(f"http://127.0.0.1:5000/user/register", json={"name": name, "age": age})
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_user(user_id: str):
    """
    Retrieve a user from the User Service by user ID.

    Use this tool when the user wants to look up an existing user.
    """
    response = requests.get(f"http://127.0.0.1:5000/user/{user_id}")
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    mcp.run()
