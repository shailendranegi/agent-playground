from agents.base_agent import BaseAgent
from tools.tool_registry import ToolRegistry


class ManagerAgent(BaseAgent):

    INTENT = "manager"

    def handle(self, user_input):
        if "manager" in user_input.lower():
            tool_name = "manager"

        manager = ToolRegistry.execute(tool_name)
        return (f"Manager Agent: "
                f"Manager is: {manager}")
