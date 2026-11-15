def save_audit_report(path: str, data: str):
    with open(path, 'w') as f: f.write(data)
