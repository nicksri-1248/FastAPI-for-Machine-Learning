from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'Gurgram', 'state': 'Haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Juhi', 'gender': 'Female', 'age': 25, 'address': address_dict}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()

print(temp)
print(type(temp))

temp = patient1.model_dump_json()

print(temp)
print(type(temp))

temp = patient1.model_dump(include=['name', 'gender'])

print(temp)
print(type(temp))

temp = patient1.model_dump(exclude=['name', 'gender'])

print(temp)
print(type(temp))

temp = patient1.model_dump(exclude={'address': {'state'}})

print(temp)
print(type(temp))

patient_dict = {'name': 'Juhi', 'age': 25, 'address': address_dict}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))