from fastapi import FastAPI
from routes import character_routes
from routes import nation_routes

app = FastAPI(title="Avatar API")

# Include routes
app.include_router(character_routes.router)
app.include_router(nation_routes.router)