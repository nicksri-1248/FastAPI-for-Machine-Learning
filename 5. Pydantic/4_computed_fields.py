from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float   # kg
    height: float   # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details) 
    print('Updated')

patient_info = {'name': 'Juhi', 'email': 'juhisri1248@icici.com', 'age': 25, 'weight': 55.5, 'height': 1.75, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '+91 1234567890', 'emergency': '+91 9876543210'}}

patient1 = Patient(**patient_info)  # Validation -> Type coercion

# insert_patient_data(patient1)
update_patient_data(patient1)