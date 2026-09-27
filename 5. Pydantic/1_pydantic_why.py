# def insert_patient_data(name: str, age: int):

    # print(name)
    # print(age)

    # print('Inserted into database')

#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError('Age cannot be negative')
#         else:
#             print(name)
#             print(age)
#             print('Inserted into database')
#     else:
#         raise TypeError('Invalid data type')

# def update_patient_data(name: str, age: int):

#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('Inserted into database')
#     else:
#         raise TypeError('Invalid data type')

# insert_patient_data('Juhi', 'Twenty Five')
# insert_patient_data('Juhi', 25)

# Problems

# 1. Type Validation: We have to manually check the data type of each parameter. This can lead to repetitive code and potential errors if we forget to validate a parameter.
# 2. Data Validation: We have to manually check the data values to ensure they are valid. This can be time-consuming and error-prone.

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Patient Name', description='Name of the patient', example=['Juhi', 'Nikhil', 'Sakshi'])]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int = Field(..., gt=0, lt=120)
    weight: float = Field(..., gt=0, strict=True)
    # married: bool = False
    married: Annotated[bool, Field(default=False, description='Marital status of the patient', example=True)]
    # allergies: Optional[List[str]] = None
    # allergies: Optional[List[str]] = Field(max_length=5)
    allergies: Optional[Annotated[List[str], Field(max_length=5, description='List of allergies', example=['dust', 'pollen'])]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedIn_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details) 
    print('Updated')

# patient_info = {'name': 'Juhi', 'age': 25, 'weight': 55.5, 'married': False, 'allergies': ['dust', 'pollen'], 'contact_details': {'email': 'juhisri1248@proton.me', 'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'age': 25, 'weight': 55.5, 'married': False, 'contact_details': {'email': 'juhisri1248@proton.me', 'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'age': 25, 'weight': 55.5, 'contact_details': {'email': 'juhisri1248@proton.me', 'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'email': 'juhisri1248@proton.me', 'age': 25, 'weight': 55.5, 'married': False, 'contact_details': {'phone': '+91 1234567890'}}
patient_info = {'name': 'Juhi', 'email': 'juhisri1248@proton.me', 'linkedIn_url': 'https://www.linkedin.com/in/juhi-sri-1248', 'age': 25, 'weight': 55.5, 'married': False, 'contact_details': {'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'email': 'juhisri1248@proton.me', 'linkedIn_url': 'https://www.linkedin.com/in/juhi-sri-1248', 'age': 25, 'weight': -55.5, 'married': False, 'contact_details': {'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'email': 'juhisri1248', 'age': 25, 'weight': 55.5, 'married': False, 'contact_details': {'phone': '+91 1234567890'}}
# patient_info = {'name': 'Juhi', 'age': "Twenti Five"} # This will raise a validation error because age is not an int

patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)