"""AgentForge Exercise 06.4 — Industry-Specific Agents (stretch)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-06-4", instruction="You are a Industry-Specific Agents agent.")
    print(f"Exercise 06.4 ready: {agent.name}")

if __name__ == "__main__":
    main()
