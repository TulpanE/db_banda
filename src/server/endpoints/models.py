from pydantic import BaseModel


class User(BaseModel):
    id: int
    login: str
    password: str


class User_login(BaseModel):
    login: str


class User_form(BaseModel):
    login: str
    password: str


class Victim(BaseModel):
    id: int
    name: str
    location_id: int
    loss_amount: str
    incident_date: str


class Victim_name(BaseModel):
    name: str


class Staff(BaseModel):
    id: int
    name: str
    surname: str
    post_id: int
    user_id: int


class Staff_name_surname(BaseModel):
    name: str
    surname: str


class Post(BaseModel):
    id: int
    name_dish: str


class Operations(BaseModel):
    id: int
    name: str
    type: str
    success: str


class Operations_update(BaseModel):
    name: str
    type: str


class Security_incident(BaseModel):
    id: int
    safety_inspection_id: int
    description: str
    status: str


class Messages(BaseModel):
    id: int
    content: str
    status: str
    operation_id: int


class Messages_update(BaseModel):
    content: str
    status: str


class Location(BaseModel):
    id: int
    address: str


class Location_update(BaseModel):
    address: str


class FakeWebsites(BaseModel):
    id: int
    url: str
    purpose: str
    victim_count: int
    outcome: str
    operation_id: int


class FakeWebsites_url_purpose(BaseModel):
    url: str
    purpose: str

