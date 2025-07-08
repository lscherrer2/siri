from copy import deepcopy

class Thread:
    def __init__ (
        self,
        system_prompt: str
    ):
        self.history = [{
            "role": "system",
            "content": system_prompt
        }]

    def __getitem__ (self, idx: int):
        return self.history[idx]

    def _add_message (self, message: dict[str, str]):
        this_role = message["role"]
        last_role = self.history[-1]["role"]
        
        match last_role:
            case "system":
                assert this_role == "user"
            case "user":
                assert this_role == "assistant"
            case "tool":
                pass
            case _:
                raise NotImplementedError()

    def __iadd__ (self, message: dict[str, str] | list[dict[str, str]]):
        if isinstance(message, dict):
            self._add_message(message)
        elif isinstance(message, list):
            for msg in message:
                self._add_message(msg)
        else: 
            raise ValueError(
                f"Expected message to be of type `dict` or `list`"
                ", received `{type(message)}`"
            ) 


    def __add__ (self, message: list[dict[str, str]]):
        new_thread = deepcopy(self)
        new_thread += message
        return new_thread
    



