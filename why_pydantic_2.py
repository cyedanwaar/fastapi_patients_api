from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description='Give the name of the patient in less than 50 chars', examples=['anwaar', 'israr'])]
    email: Annotated[EmailStr, Field(default=None)]
    linkedin_url: Annotated[AnyUrl, Field(default=None)]
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)] 
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: list[str] | None = None
    contact_details: dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted into Database")


patient_info = {'name': 'abc', 'age': 23, 'weight': 5, 'married':  True,  'contact_details': {'email': 'abc@gmail.com', 'phone': '12312312312'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
