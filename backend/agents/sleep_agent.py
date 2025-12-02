import google.generativeai as genai

class SleepAgent:
    def __init__(self):
        self.model = "gemini-1.5"

    def handle(self, message):
        prompt = f"User asked: {message}\nPlease provide personalized sleep improvement tips."
        response = genai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=200
        )
        return response.output_text
