from agents.base_agent import BaseAgent
from tools.hr_tools import HRTools
from tools.tool_registry import ToolRegistry


class SalaryAgent(BaseAgent):
    def handle(self, user_input):
        if "salary" in user_input.lower():
            tool_name = "salary"

        salary = ToolRegistry.execute(tool_name)
        return f"Salary Agent: You salary is {salary}"
