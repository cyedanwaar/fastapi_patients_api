from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str] | None = None
    contact_details: dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid email domain")
        return domain_name
    
    @field_validator('name')
    def name_upper(cls, value:str):
        return value.upper()


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted into Database")


patient_info = {'name': 'sBc', 'email': 'abc@icici.com', 'age': 23, 'weight': 5, 'married':  True,  'contact_details': {'email': 'abc@gmail.com', 'phone': '12312312312'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)