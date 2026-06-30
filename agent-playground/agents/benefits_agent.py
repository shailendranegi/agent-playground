from agents.base_agent import BaseAgent


class BenefitsAgent(BaseAgent):

    INTENT = "benefits"
    DESCRIPTION = "Handles benefits related questions"
    PHRASES = [
        "benefits",
        "insurance",
        "medical"
    ]

    def handle(self, user_input):
        return "Benefits response"