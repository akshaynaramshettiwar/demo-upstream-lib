def parse_packet(raw_data: dict) -> dict:
    return {"src": raw_data.get("sr")}

def validate_rule(rule: str) -> bool:
    return rule.startswith("alert")

