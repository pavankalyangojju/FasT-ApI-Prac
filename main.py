from typing import Optional,List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections

from api.users import router

app = FastAPI(
    title="FasT-ApI-Prac",
    description="B for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Pavan",
        "email": "pavan@gmail.com",
    },
    license_info={
        "name": "MIB",
    }
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

