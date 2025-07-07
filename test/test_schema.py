import sys
from pathlib import Path

module_path = Path(__file__).parent.parent/"src"
sys.path.append(module_path.__str__())
verbose = "--verbose" in sys.argv

from typing import TYPE_CHECKING

if verbose or TYPE_CHECKING:
    import json


from unittest import TestCase, main
from siri.tools.schemas.utils import Arg, build_schema # type: ignore

class TestSchema (TestCase):

    def test_arg_init (self):
        arg = Arg(
            name="test_argument",
            dtype="string",
            description="test_description",
            required=True,
            enum=["yes", "no", "maybe"]
        )
        self.assertEqual(arg.name, "test_argument")
        self.assertEqual(arg.dtype, "string")
        self.assertEqual(arg.description, "test_description")
        self.assertEqual(arg.required, True)
        self.assertEqual(arg.enum, ["yes", "no", "maybe"])
        self.assertTrue(arg.required)

    def test_arg_to_property (self):
        arg = Arg(
            name="test_argument",
            dtype="string",
            description="test_description",
            required=False,
            enum=["yes", "no", "maybe"]
        )
        prop = arg.to_property()

    def test_build_schema (self):
        arg1 = Arg(
            name="arg1",
            dtype="int",
            description="desc1",
            required=True,
            enum=[1, 2, 3]
        )
        arg2 = Arg(
            name="arg2",
            dtype="float",
            description="desc2",
            required=False,
            enum=[0.5, 0.6, 0.7]
        )
        schema = build_schema(
            name="schema",
            description="desc",
            args=[arg1, arg2]

        )

        self.assertEqual(
            schema,
            {
                "type": "function",
                "function": {
                    "name": "schema",
                    "description": "desc",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "arg1": {
                                "type": "int",
                                "description": "desc1",
                                "enum": [1, 2, 3]
                            },
                            "arg2": {
                                "type": "float",
                                "description": "desc2",
                                "enum": [0.5, 0.6, 0.7]
                            }
                        },
                        "required": ["arg1"]
                    },
                }
            },
        )

        if verbose:
            print(
                f"schema from build_schema:\n",
                json.dumps(schema, indent=4) # type: ignore
            )
        
if __name__ == "__main__":
    main()
        




