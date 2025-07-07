
from typing import TYPE_CHECKING, Optional
from siri.tools import SCHEMAS, SERVERS
from siri.agent import Thread
from siri.agent.settings import generate_instructions

class Siri:

    global SCHEMAS
    global SERVERS
    global API_KEY

    def __init__ (self, model: str, instructions: list[str]):
        self.model = model
        self.client = None
        self.system = generate_instructions(instructions)

    def new_thread (self):
        res = Thread(self.system)
        return res
    
    def start_thread (self, prompt: str):
        res = Thread(self.system)
        res += {"role": "user", "content": prompt}
        return res

    def run_tool_calls (self, tool_calls: list[ToolCall]):
        pass

    def advance_thread (self, thread: Thread):

        if (last_sender := thread[-1]["role"]) != "user":
            raise ValueError(
                f"Last message in thread must be from 'user', received {last_sender}"
            )

        continue_completing = True
        while continue_completing:

            response = self.client.chat.completions.create( # type: ignore
                model=self.model,
                tools=SCHEMAS,
                messages=thread.history,
            ).choices[0].message
            thread += response.to_dict()

            if response.tool_calls:
                tool_results: list[dict[str, str]] = run_tool_calls(tool_calls)
                thread += tool_results

            else:
                continue_completing = False

                
            
        




