from tools.hr_tools import HRTools


class ToolRegistry:
    TOOLS = {
        "leave_balance": HRTools.get_leave_balance,
        "leave_history" : HRTools.get_leave_history,
        "salary": HRTools.get_salary,
        "profile": HRTools.get_profile,
        "manager": HRTools.get_manager
    }

    @staticmethod
    def execute(tool_name):
        tool = ToolRegistry.TOOLS.get(tool_name)

        if tool:
            return tool()

        return "Tool not found"

