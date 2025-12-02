import google.generativeai as genai

class NutritionAgent:
    def __init__(self):
        self.model = "gemini-1.5"

    def handle(self, message):
        prompt = f"User asked: {message}\nPlease provide a healthy meal plan recommendation."
        response = genai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=300
        )
        return response.output_text
