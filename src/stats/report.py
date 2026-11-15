def compute_audit_summary(total: int, dead: int):
    return {'total_links': total, 'broken_links': dead, 'health_pct': round((total - dead)/total*100, 1) if total else 100}
