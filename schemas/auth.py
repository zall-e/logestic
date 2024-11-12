from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str


class Login(BaseModel):
    access_token: str
    refresh_token: str


class RefreshToken(BaseModel):
    token: str


class AccountActivation(BaseModel):
    target_username: str


class ResetPassword(BaseModel):
    username: str
    new_password: str