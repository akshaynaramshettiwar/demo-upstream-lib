def parse_packet(raw_data: dict) -> dict:
    return {
        "src": raw_data.get("src"),
        "dst": raw_data.get("dst"),
        "protocol": raw_data.get("protocol")
    }

def validate_rule(rule: str) -> bool:
    return rule.startswith("alert")

# first line
