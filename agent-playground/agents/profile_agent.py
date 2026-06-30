from agents.base_agent import BaseAgent
from tools.hr_tools import HRTools
from tools.tool_registry import ToolRegistry


class ProfileAgent(BaseAgent):

    INTENT = "profile"
    DESCRIPTION = "Handles employee profile"
    PHRASES = [
        "profile",
        "designation"
    ]

    def handle(self, user_input):

        if "profile" in user_input.lower():
            tool_name = "profile"
        else:
            tool_name = "manager"

        result = ToolRegistry.execute(tool_name)

        if isinstance(result, dict):
            return (
                f"Profile Agent: "
                f"{result['name']} - "
                f"{result['role']}"
            )

        return f"Profile Agent: {result}"
