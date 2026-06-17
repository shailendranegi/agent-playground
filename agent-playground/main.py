from agents.agent_registry import AgentRegistry


# A supervisor agent acts as an orchestrator. It receives teh request, determines the intent, and delegates execution to the appropriate specilized agent.
# Specialized agents are domain-focused and own their tools, prompts, and business logic.
class SupervisorAgent:

    def classify_intent(self, user_input):
        text = user_input.lower()

        if "leave" in text:
            return "leave"

        if "salary" in text:
            return "salary"

        if "profile" in text:
            return "profile"

        if "manager" in text:
            return "manager"

        return "general"

    def run(self, user_input):
        intent = self.classify_intent(user_input)
        agent = AgentRegistry.get(intent)

        if agent:
            return agent.handle(user_input)

        return "General Agent: I don't understand"

agent = SupervisorAgent()

print(agent.run("Show my leave balance"))
print(agent.run("Show my leave history"))
print(agent.run("Show my salary"))
print(agent.run("Show my profile"))
print(agent.run("Show my manager"))