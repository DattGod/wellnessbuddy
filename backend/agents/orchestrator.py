import os
import google.generativeai as genai
from memory.memory_bank import MemoryBank
from agents.nutrition_agent import NutritionAgent
from agents.fitness_agent import FitnessAgent
from agents.sleep_agent import SleepAgent

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class Orchestrator:
    def __init__(self):
        self.memory = MemoryBank()
        self.nutrition_agent = NutritionAgent()
        self.fitness_agent = FitnessAgent()
        self.sleep_agent = SleepAgent()
        self.model = "gemini-1.5"

    def run(self, message):
        self.memory.add("user", message)

        if "meal" in message.lower() or "diet" in message.lower():
            reply = self.nutrition_agent.handle(message)
        elif "workout" in message.lower() or "exercise" in message.lower():
            reply = self.fitness_agent.handle(message)
        elif "sleep" in message.lower() or "insomnia" in message.lower():
            reply = self.sleep_agent.handle(message)
        else:
            # General AI response
            history = self.memory.get_history()
            context = "\n".join([f"{h['role']}: {h['text']}" for h in history])

            response = genai.Completion.create(
                model=self.model,
                prompt=f"User: {message}\nConversation history:\n{context}",
                temperature=0.7,
                max_output_tokens=500
            )
            reply = response.output_text

        self.memory.add("bot", reply)
        return reply
