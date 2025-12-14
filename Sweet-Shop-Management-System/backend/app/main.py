from fastapi import FastAPI
from .database import Base, engine
from .routers import auth_routes, sweet_routes

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(auth_routes.router)
app.include_router(sweet_routes.router)
