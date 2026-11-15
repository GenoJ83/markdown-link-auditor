from pydantic import BaseModel
class AuditorConfig(BaseModel):
    timeout_seconds: float = 3.0
    check_external: bool = True
    ignore_patterns: list = ['#', 'mailto:']
