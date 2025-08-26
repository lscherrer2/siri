from ollama import Client as Ollama
from pathlib import Path
import json

INTERNAL_TOOLS_PATH = Path("client/tools.json")

with open(INTERNAL_TOOLS_PATH, "r") as f:
    INTERNAL_TOOLS = json.load(f)["tools"]

with open(INTERNAL_TOOLS_PATH, "r") as f:
    INTERNAL_TOOLS = json.load(f)["tools"]


class Siri:
    SYSTEM: str = (
        "You are Siri on MacOS. Use the tools at your "
        "disposal to carry out the tasks the user gives you."
    )

    def __init__(self):
        self.client = Ollama()

    def new_query(self, query: str):
        thread = [
            {"role": "system", "content": self.SYSTEM},
            {"role": "user", "content": query},
        ]
