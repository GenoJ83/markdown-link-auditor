def is_safe_redirect(url: str) -> bool:
    return not url.startswith('file://') and not url.startswith('javascript:')
