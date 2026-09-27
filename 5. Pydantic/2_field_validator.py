from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')

        return value

    @field_validator('name')
    @classmethod
    def transoform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details) 
    print('Updated')

patient_info = {'name': 'Juhi', 'email': 'juhisri1248@icici.com', 'age': 25, 'weight': 55.5, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '+91 1234567890'}}

patient1 = Patient(**patient_info)  # Validation -> Type coercion

# insert_patient_data(patient1)
update_patient_data(patient1)