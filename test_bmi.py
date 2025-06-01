import asyncio
from fastmcp import Client
from bmi_server import mcp

client = Client(mcp)

async def test_bmi():
    async with client:
        # Test case: 70kg, 1.75m
        response = await client.call_tool("calculate_bmi", {"weight": 70, "height": 1.75})
        result = response[0].text
        assert result == "22.86", f"Unexpected BMI index: {result['bmi_index']}"

        response = await client.call_tool("bmi_category", {"bmi": 22.86})
        result = response[0].text
        assert result == "Healthy Weight", f"Unexpected BMI category: {result['category']}"
        print("Test passed!", result)

if __name__ == "__main__":
    asyncio.run(test_bmi())
