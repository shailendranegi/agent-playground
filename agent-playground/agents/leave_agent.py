from agents.base_agent import BaseAgent
from tools.tool_registry import ToolRegistry


class LeaveAgent(BaseAgent):

    INTENT = "leave"
    DESCRIPTION = "Handles leave related requests"
    PHRASES = [
        "leave",
        "vacation",
        "holiday"
    ]

    def handle(self, user_input):

        if "history" in user_input.lower():
            tool_name = "leave_history"
        else:
            tool_name = "leave_balance"

        result = ToolRegistry.execute(tool_name)

        return f"Leave Agent: {result}"
