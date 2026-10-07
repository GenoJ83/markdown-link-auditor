import json
def export_broken_links_json(broken: list) -> str:
    return json.dumps(broken, indent=2)
