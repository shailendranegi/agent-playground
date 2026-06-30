from agents.base_agent import BaseAgent
from tools.tool_registry import ToolRegistry


class SalaryAgent(BaseAgent):

    INTENT = "salary"
    DESCRIPTION = "Handles salary requests"
    PHRASES = [
        "salary",
        "pay",
        "income"
    ]

    def handle(self, user_input):

        if "salary" in user_input.lower():
            tool_name = "salary"

        salary = ToolRegistry.execute(tool_name)
        return f"Salary Agent: You salary is {salary}"
