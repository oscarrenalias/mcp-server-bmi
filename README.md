# MCP BMI 

This is a simple MCP server that exposes a tool to calculate the BMI of a person given their weight and height.

Input parameters:
- weight
- height

Response:
- bmi_index: a number representing the BMI index
- bmi_category: a string representing the category, as per the established values:
    - Underweight (Less than 18.5)
    - Healthy Weight (18.5 to less than 25)
    - Overweight (25 to less than 30)
    - Obesity (30 or greater)
    - Class 1 Obesity (30 to less than 35)
    - Class 2 Obesity (35 to less than 40)
    - Class 3 Severe obesity (40 or greater)

# Implementation

Built on Python with FastMCP, packaged as a Docker container and published to the GitHub registry.

## Running the Server

To start the server locally:

```
uv sync
uv run bmi_server.py
```

Or with Docker:

```
docker build -t mcp-bmi .
docker run --rm -it mcp-bmi
```

## Testing

To run the provided test:

```
uv run test_bmi.py
```

# Development

Use the provided DevContainer for a ready-to-go development environment in VS Code.

# Connecting to an LLM

In progress.