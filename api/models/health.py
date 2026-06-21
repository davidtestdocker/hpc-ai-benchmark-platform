from pydantic import BaseModel


class CheckItem(BaseModel):
    status: str
    value: str


class HealthResponse(BaseModel):
    status: str
    checks: dict[str, CheckItem]
