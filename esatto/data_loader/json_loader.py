from typing import Any
import json

def get_patients_data(filename: str) -> Any:
    with open(filename, 'r') as f:
        return json.load(f)