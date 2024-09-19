from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    descriptions: str | None = None


class STask(STaskAdd):
    id: int

    class Config:
        from_attributes = True

class StaskId(BaseModel):
    ok: bool = True
    task_id: int