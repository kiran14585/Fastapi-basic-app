from pydantic import  Field,BaseModel


class Addition(BaseModel):
    number1 : int = Field(...,description="Enter number 1")
    number2 : int = Field(...,description="Enter number 2")
    





