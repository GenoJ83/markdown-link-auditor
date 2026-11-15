from pydantic import BaseModel
class MarkdownLink(BaseModel):
    file_path: str
    line_number: int
    target_url: str
    is_external: bool
    status: str = 'PENDING'
