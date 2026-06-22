# Agent Playground

A hands-on learning project for understanding modern AI Agent architectures from first principles.

The goal of this project is not to use an agent framework immediately, but to understand the core architectural concepts behind frameworks such as:

* Google ADK
* LangGraph
* OpenAI Agents
* CrewAI
* AutoGen

---

## Current Architecture

```text
User
 ↓
SupervisorAgent
 ↓
Intent Classification
 ↓
AgentRegistry
 ↓
Specialized Agent
 ↓
Tool Selection
 ↓
ToolRegistry
 ↓
Tool
 ↓
Response Formatting
 ↓
Response
```

---

## Project Structure

```text
agent-playground
│
├── main.py
│
├── agents
│   ├── agent_registry.py
│   ├── base_agent.py
│   ├── leave_agent.py
│   ├── salary_agent.py
│   ├── profile_agent.py
│   └── manager_agent.py
│
└── tools
    ├── hr_tools.py
    └── tool_registry.py
```

---

## Concepts Implemented

### Supervisor Agent

Acts as the orchestrator.

Responsibilities:

* Receive user requests
* Determine intent
* Select the appropriate specialized agent
* Delegate execution

Example:

```python
intent = self.classify_intent(user_input)
agent = AgentRegistry.get(intent)
return agent.handle(user_input)
```

---

### Specialized Agents

Each agent owns a specific business domain.

Examples:

* LeaveAgent
* SalaryAgent
* ProfileAgent
* ManagerAgent

Responsibilities:

* Domain-specific logic
* Tool selection
* Response formatting

---

### Tool Registry

Provides a centralized mechanism for tool discovery and execution.

Example:

```python
ToolRegistry.execute("leave_balance")
```

This pattern is similar to:

* ADK Toolsets
* Function Calling
* LangGraph Tool Nodes

---

### BaseAgent Contract

All agents inherit from BaseAgent.

```python
class BaseAgent(ABC):

    @abstractmethod
    def handle(self, user_input):
        pass
```

Benefits:

* Consistent interface
* Extensibility
* Polymorphism

---

### Agent Registry

Central registry responsible for agent discovery.

```python
AgentRegistry.register(LeaveAgent)
```

Benefits:

* Decouples SupervisorAgent from concrete agents
* Easier extension
* Similar to plugin registration patterns

---

## Sample Flow

User Request:

```text
Show my leave history
```

Execution:

```text
SupervisorAgent
 ↓
LeaveAgent
 ↓
ToolRegistry
 ↓
leave_history tool
 ↓
Response
```

Result:

```text
Leave Agent:
[
  "Annual leaves - 5 days",
  "Sick leave - 2 days"
]
```

---

## Learning Roadmap

### Completed

* Intent Classification
* Specialized Agents
* Tool Calling
* Tool Registry
* Agent Registry
* BaseAgent Contract

### Next

* Memory Layer
* Conversation State
* Agent Self Registration
* Dynamic Agent Discovery
* Multi-Agent Collaboration
* LangGraph Implementation
* Google ADK Implementation
* Agent Governance
* Evaluation & Observability

---

## Architecture Mapping

| This Project      | ADK                | LangGraph         |
| ----------------- | ------------------ | ----------------- |
| SupervisorAgent   | root_agent         | Router Node       |
| Specialized Agent | Skill / Agent      | Node              |
| ToolRegistry      | Toolset            | Tool Node         |
| AgentRegistry     | Skill Registration | Node Registration |
| BaseAgent         | Skill Contract     | State Contract    |

---

## Purpose

This repository is a learning playground focused on understanding how modern AI Agent frameworks work internally before adopting framework-specific abstractions.

The emphasis is on architecture, orchestration, tool calling, and extensibility rather than framework-specific APIs.
