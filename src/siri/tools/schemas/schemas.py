from siri.tools.schemas.utils import Arg, build_schema

__all__ = ["SCHEMA_MAP", "SCHEMA_LIST"]

SCHEMA_LIST: list[dict] = [
    build_schema(
        name="set_alarm",
        description="sets an alarm on the user's machine",
        args = [
            Arg(
                name="hour",
                dtype="integer",
                description="hour of the day",
                required=True,
            ),
            Arg(
                name="minute",
                dtype="integer",
                description="minute of the day",
                required=True,
            ),
            Arg(
                name="am_or_pm",
                dtype="string",
                description="determines whether alarm is set for morning or afternoon",
                required=True,
                enum=["am", "pm"]
            )
        ]
    )
]

SCHEMA_MAP: dict[str, dict] = {
    schema["name"]: schema for schema in SCHEMA_LIST
}


