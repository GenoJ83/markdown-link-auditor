def format_error_table(errors: list) -> str:
    return '\n'.join(f'{e["file"]}:{e["line"]} -> {e["url"]} (DEAD)' for e in errors)
