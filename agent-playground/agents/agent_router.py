from agents.agent_registry import AgentRegistry


class AgentRouter:

    @staticmethod
    def resolve(user_input):
        for agent in AgentRegistry.get_all_agents():
            if agent.matches(user_input):
                return agent

        return None