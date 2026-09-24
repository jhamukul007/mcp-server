# User Service MCP Server

A simple FastAPI + MCP server implementation that provides user registration and user retrieval through Claude Desktop.

## Project Structure

```text
mcp-server/
├── apis/
│   └── user_controller.py
├── mcps/
│   └── user_mcp.py
├── models/
│   └── user.py
├── main.py
├── pyproject.toml
└── README.md
```

## Prerequisites

- Python 3.10+
- uv
- Claude Desktop

Install dependencies:

```bash
uv sync
```

## Run the FastAPI Server

Start the API server:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 5000 --reload
```

The API server will be available at:

```text
http://127.0.0.1:5000
```

Swagger UI:

```text
http://127.0.0.1:5000/docs
```

## Run the MCP Server

In a separate terminal:

```bash
uv run python mcps/user_mcp.py
```

The MCP server exposes the following tools:

### Register User

```text
register_user(name, age)
```

### Get User

```text
get_user(user_id)
```

## Configure Claude Desktop

Add the MCP server to your Claude Desktop configuration.

On macOS, the configuration file is:

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

Add:

```json
{
  "mcpServers": {
    "user-service": {
      "command": "/Users/mukul/.local/bin/uv",
      "args": [
        "run",
        "--directory",
        "<full-qualified-path-to-mcp-project>",
        "python",
        "mcps/user_mcp.py"
      ]
    }
  }
}
```

Replace:

```text
<full-qualified-path-to-mcp-project>
```

with the absolute path of your MCP project.

For example:

```json
{
  "mcpServers": {
    "user-service": {
      "command": "/Users/mukul/.local/bin/uv",
      "args": [
        "run",
        "--directory",
        "/Users/mukul/Projects/mcp-server",
        "python",
        "mcps/user_mcp.py"
      ]
    }
  }
}
```

Restart Claude Desktop after updating the configuration.

## How to Use

Make sure the FastAPI server is running:

```bash
uv run uvicorn main:app --host 127.0.0.1 --port 5000 --reload
```

Claude Desktop will start the MCP server automatically using the configured MCP server.

Open Claude Desktop and use natural-language prompts.

### Register a User

```text
Register a user having name as Virat Kohli and age 38
```

Claude will use the `register_user` MCP tool.

### Register Another User

```text
Register user with name Bruno and age 50
```

### Get a User

```text
Get user with the id 8fcca025-a712-46b3-82b6-adb800bc550f
```

Claude will use the `get_user` MCP tool.

## Available APIs

### Register User

```http
POST /user
```

Example request:

```json
{
  "name": "Virat Kohli",
  "age": 38
}
```

### Get User

```http
GET /user/{user_id}
```

Example:

```text
GET /user/8fcca025-a712-46b3-82b6-adb800bc550f
```

## Architecture

```text
                    Claude Desktop
                          |
                          | MCP
                          v
                  +-------------------+
                  |    MCP Server     |
                  |                   |
                  | register_user()   |
                  | get_user()        |
                  +---------+---------+
                            |
                            | HTTP
                            v
                  +-------------------+
                  |     FastAPI       |
                  |                   |
                  | POST /user        |
                  | GET /user/{id}    |
                  +---------+---------+
                            |
                            v
                       User Storage
```

## Request Flow

### Register User

```text
User
 |
 | "Register Virat Kohli, age 38"
 v
Claude Desktop
 |
 | register_user(name, age)
 v
MCP Server
 |
 | POST /user
 v
FastAPI
 |
 v
User Storage
```

### Get User

```text
User
 |
 | "Get user with ID ..."
 v
Claude Desktop
 |
 | get_user(user_id)
 v
MCP Server
 |
 | GET /user/{id}
 v
FastAPI
 |
 v
User Storage
```
