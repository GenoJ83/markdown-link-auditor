def is_valid_http_status(status_code: int) -> bool:
    return 200 <= status_code < 400
