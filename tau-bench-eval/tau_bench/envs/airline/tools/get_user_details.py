# Copyright Sierra

import json
from typing import Any, Dict


def get_user_details(data: Dict[str, Any], user_id: str) -> str:
    users = data["users"]
    if user_id in users:
        return json.dumps(users[user_id])
    return "Error: user not found"


get_user_details.__info__ = {
    "type": "function",
    "function": {
        "name": "get_user_details",
        "description": "Get the details of an user.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user id, such as 'sara_doe_496'.",
                },
            },
            "required": ["user_id"],
        },
    },
}
