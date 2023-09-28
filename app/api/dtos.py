from app.core.pydantic_base import BaseModel


class Gene(BaseModel):
    gene_symbol: str
    gene_stable_id: str
    transcript_ids: list[str] | None
