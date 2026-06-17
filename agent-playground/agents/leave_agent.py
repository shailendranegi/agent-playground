from agents.base_agent import BaseAgent
from tools.hr_tools import HRTools
from tools.tool_registry import ToolRegistry


class LeaveAgent(BaseAgent):
    def handle(self, user_input):

        if "history" in user_input.lower():
            tool_name = "leave_history"
        else:
            tool_name = "leave_balance"

        result = ToolRegistry.execute(tool_name)

        return f"Leave Agent: {result}"
