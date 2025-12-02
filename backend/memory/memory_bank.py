class MemoryBank:
    def __init__(self):
        self.history = []

    def add(self, role, text):
        self.history.append({"role": role, "text": text})

    def get_history(self):
        return self.history
