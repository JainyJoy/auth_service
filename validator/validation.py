from typing import Optional
from pydantic import BaseModel, constr, Field, validator
import re


class RegistrationPayload(BaseModel):
    first_name: constr(max_length=50) = Field(title="First Name")
    middle_name: Optional[constr(max_length=50)] = Field(title="Middle Name", default=None)
    last_name: Optional[constr(max_length=50)] = Field(title="Last Name", default=None)
    email: constr(max_length=50) = Field(title="Email")
    password: constr(max_length=20) = Field(title="Password")

    @validator('password', pre=True, always=True)
    def _check_password(cls, password: str):
        pattern = r'^(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$'
        if re.match(pattern, password):
            return password
        else:
            raise ValueError("Password must be at least 8 characters long and contain at least one special character")

    @validator('email', pre=True, always=True)
    def _check_email(cls, email: str):
        if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            raise ValueError("Invalid email format")


class LoginPayload(BaseModel):
    email: constr(max_length=50)
    password: constr(max_length=20)
