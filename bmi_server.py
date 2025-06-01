from fastmcp import FastMCP

mcp = FastMCP("BMI MCP Server")

@mcp.tool()
def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate BMI and return index and category.
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    Returns:
        The BMI index
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)

@mcp.tool()
def bmi_category(bmi: float) -> str:
    """
    Determine BMI category based on the index.
    Args:
        bmi (float): The BMI index
    Returns:
        The BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

from bmi_server import mcp

if __name__ == "__main__":
    mcp.run(transport="stdio")
