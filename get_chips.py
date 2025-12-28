import json
from frozen_dict import FrozenDict


def _load_json() -> dict:
    with open("chips.json", "r") as file:
        data = json.load(file)
    return data


def chip_map() -> dict[FrozenDict[str], str]:
    data: dict = _load_json()
    out = {}
    for k, v in data.items():
        out[FrozenDict.from_string(k)] = v
    return out
