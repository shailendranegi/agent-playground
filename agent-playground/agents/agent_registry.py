from agents.leave_agent import LeaveAgent
from agents.manager_agent import ManagerAgent
from agents.profile_agent import ProfileAgent
from agents.salary_agent import SalaryAgent


class AgentRegistry:

    AGENTS = {}

    @staticmethod
    def register(agent_class):
        AgentRegistry.AGENTS[
            agent_class.INTENT
        ] = agent_class()

        print(
            f"Registered agent: "
            f"{agent_class.INTENT}"
        )

    @staticmethod
    def get(intent):
        return AgentRegistry.AGENTS.get(intent)


AgentRegistry.register(LeaveAgent)
AgentRegistry.register(SalaryAgent)
AgentRegistry.register(ProfileAgent)
AgentRegistry.register(ManagerAgent)
