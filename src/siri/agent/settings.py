__all__ = ["generate_instructions", "API_KEY"]

# maybe use dotenv
API_KEY = ""

ASSISTANT_DIRECTIVE = """
You are Siri, helping a user by answering questions or by controlling
their operating system (MacOS). Use the tools available to the best of
your ability to accomplish what the user asks, or respond to their 
questions. Respond with short, to-the-point messages.
""".strip()

def generate_instructions (instructions: list[str]):
    global ASSISTANT_DIRECTIVE

    if not instructions:
        return ASSISTANT_DIRECTIVE

    formatted_instructions = "\n".join([
        f"{i+1}) {instruct}"
        for i, instruct in enumerate(instructions)
    ])
    
    return f"""

{ASSISTANT_DIRECTIVE}

Follow these instructions, that come at the user's request:
{formatted_instructions}
""".strip()

if __name__ == "__main__":
    instructions = [
        "instruction1",
        "instruction2",
        "instruction3",
    ]
    prompt = generate_instructions(instructions)
    print(prompt)


