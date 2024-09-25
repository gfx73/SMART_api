import pydantic

class CriteriaResponse(pydantic.BaseModel):
    reason: str
    conclusion: bool


class ResponseFormat(pydantic.BaseModel):
    S: CriteriaResponse
    M: CriteriaResponse
    A: CriteriaResponse
    R: CriteriaResponse
    T: CriteriaResponse