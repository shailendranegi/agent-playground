from agents.agent_registry import AgentRegistry
from agents.agent_router import AgentRouter


# A supervisor agent acts as an orchestrator. It receives teh request, determines the intent, and delegates execution to the appropriate specilized agent.
# Specialized agents are domain-focused and own their tools, prompts, and business logic.
class SupervisorAgent:

    def run(self, user_input):

        agent = AgentRouter.resolve(user_input)

        if agent:
            return agent.handle(user_input)

        return "General Agent: I don't understand"

agent = SupervisorAgent()

print(agent.run("Show my leave balance"))
print(agent.run("Show my leave history"))
print(agent.run("Show my salary"))
print(agent.run("Show my profile"))
print(agent.run("Show my manager"))
print(agent.run("My name is Shailendra"))
print(agent.run("What is my name"))
print(agent.run("My favorite color is blue"))
print(agent.run("What is my favorite color"))
print(AgentRegistry.list_intents())
print(AgentRegistry.list_agents())
print(AgentRegistry.list_registered_agents())
print(agent.run("benefits"))
