# 🌊🔥🌪️🪨 Avatar: The Last Airbender REST API

A simple REST API for exploring data from the Avatar: The Last Airbender universe.
This API is built with Python + FastAPI and uses PostgreSQL as the database.
It exposes read-only endpoints (GET) for nations, factions, characters, bending styles, episodes, animals, weapons, languages, and quotes.

## Features

- Query information about Nations (Fire Nation, Earth Kingdom, etc.)
- Explore Characters and their relationships (factions, bending, languages, weapons, quotes)
- Browse Episodes by season and number
- View Factions and their associated nations
- Discover Animals and their owners
- Get details on Bending styles and which characters use them
- Access Quotes from characters

## Database Schema

The database is structured around the Avatar universe with relational integrity.

### Core Tables
  nations
  factions
  characters
  locations
  episodes
  bending_styles
  animals
  weapons
  languages
  quotes

### Join Tables

character_factions
character_bending
character_weapons
character_languages

## Example Character Table (SQLAlchemy)
```bash
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    nation_id = Column(Integer, ForeignKey("nations.id"))
    date_of_birth = Column(String(30))
    date_of_death = Column(String(30))
    gender = Column(String(20))
    height = Column(Float)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
```

## Getting Started

### Prerequisites
- Python 3.10+
- PostgreSQL
- pip
- Git

### Setup

1. Clone the repository:

  ```bash
  git clone https://github.com/your-username/avatar-last-airbender-api.git
  ```

2. Create the PostgreSQL database:

```bash
CREATE DATABASE avatar_db;

3. Run the schema script to set up tables

4. Configure your database credentials in .env

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/avatar_api
```

5. Creat virtual environment and install dependencies:
   
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   ```

6. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```
   The server will start at http://127.0.0.1:8000

## Example Endpoints
- GET /api/v1/characters -> List all characters (0 - 20)
- GET /api/v1/characters?nationId=4 -> Filter characters by nation
- GET /api/v1/characters?skip=5&limit=10 -> Pagination

### Example Response

```bash
[
  {
    "id": 1,
    "name": "Aang",
    "nation_id": 1,
    "date_of_birth": "12 AG",
    "date_of_death": "153 AG",
    "gender": "Male",
    "height": 1.65,
    "hair_color": "None",
    "eye_color": "Grey"
  },
  ...
]
```

## Tech Stack
- Backend: Python 3.10+, FastAPI
- Database: PostgreSQL
- ORM: SQLAlchemy
- Build Tool: pip

## Licencse
MIT License. Free to use, modify, and share.

