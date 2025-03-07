from pydantic import Field, BaseModel


class DatasetEntry(BaseModel):
    src: str = Field(default="", description="The source of the dataset entry")
    url: str = Field(default="", description="The url of the dataset entry")
    html: str = Field(default="", description="The html of the dataset entry")


class Dataset:
    async def generate_context(self)->DatasetEntry:
        pass
