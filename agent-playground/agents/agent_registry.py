from agents.leave_agent import LeaveAgent
from agents.manager_agent import ManagerAgent
from agents.profile_agent import ProfileAgent
from agents.salary_agent import SalaryAgent


class AgentRegistry:

    AGENTS = {
        "leave": LeaveAgent(),
        "salary": SalaryAgent(),
        "profile": ProfileAgent(),
        "manager": ManagerAgent()
    }

    @staticmethod
    def get(intent):
        return AgentRegistry.AGENTS.get(intent)

