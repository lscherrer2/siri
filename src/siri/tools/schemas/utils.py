
__all__ = ["Arg", "build_schema"]

class Arg:

    name: str
    dtype: str
    description: str
    required: bool
    enum: list
    
    def __init__ (self,
        name: str,
        dtype: str,
        description: str,
        required: bool = True,
        enum: list = []
    ):
        self.name = name
        self.dtype = dtype
        self.description = description
        self.required = required
        self.enum = enum

    def to_property (self):
        res = {
            "type": self.dtype,
            "description": self.description,
        }
        if self.enum:
            res |= {"enum": self.enum}
        return res


def build_schema (
    name: str,
    description: str,
    args: list[Arg]
) -> dict:
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": {
                    arg.name: arg.to_property() for arg in args
                },
                "required": [arg.name for arg in args if arg.required],
            },
        }
    }
