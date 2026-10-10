def generate_link_fix_diff(original: str, old_url: str, new_url: str) -> str:
    return original.replace(old_url, new_url)
