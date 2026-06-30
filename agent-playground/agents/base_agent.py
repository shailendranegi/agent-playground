from abc import ABC, abstractmethod

class BaseAgent(ABC):

    INTENT = None
    DESCRIPTION = ""
    PHRASES = []

    @abstractmethod
    def handle(self, user_input):
        pass

    def matches(self, user_input):

        text = user_input.lower()

        return any(
            phrase in text
            for phrase in self.PHRASES
        )
