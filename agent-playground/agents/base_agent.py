from abc import ABC, abstractmethod

class BaseAgent(ABC):

    INTENT = None

    @abstractmethod
    def handle(self, user_input):
        pass
