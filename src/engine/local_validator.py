import os
def validate_local_link(base_dir: str, current_file: str, link_target: str) -> bool:
    clean_target = link_target.split('#')[0]
    if not clean_target: return True # Same-file anchor
    target_path = os.path.normpath(os.path.join(os.path.dirname(current_file), clean_target))
    return os.path.exists(os.path.join(base_dir, target_path))
