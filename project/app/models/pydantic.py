from pydantic import AnyHttpUrl, BaseModel, ConfigDict


class SummaryPayloadSchema(BaseModel):
    model_config = ConfigDict(url_preserve_empty_path=True)
    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str
