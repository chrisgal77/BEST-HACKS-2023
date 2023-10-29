from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel
from best23.models.palm2 import model as palm2_model
from best23.models.translate import model as translator
from best23.models.recommendations.system import model as recommender
from best23.database.handler import database
from PIL import Image
import base64
from pathlib import Path
import io
import os
import difflib


def find_similar_filename(path, target_filename):
    folder_path = Path(path)
    
    best_match = None
    best_match_ratio = 0.0
    
    for file_path in folder_path.iterdir():
        if file_path.is_file():
            filename = file_path.stem
            similarity_ratio = difflib.SequenceMatcher(None, filename, target_filename).ratio()
            
            if similarity_ratio > best_match_ratio:
                best_match = file_path
                best_match_ratio = similarity_ratio
    
    return best_match


def load_image_as_base64(image_path):
    with Image.open(image_path) as img:
        if img.format != "JPEG":
            img = img.convert("RGB")

        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="JPEG")
        img_byte_array = img_byte_array.getvalue()

        base64_image = base64.b64encode(img_byte_array).decode('utf-8')

        return base64_image


ml_models = {}


class Register(BaseModel):
    login: str
    password: str
    name: str
    description: str


class Login(BaseModel):
    login: str
    password: str


class UpdateDescription(BaseModel):
    user_id: str
    description: str


class ProposeTopics(BaseModel):
    user_id: str

class UnregisteredProposePlaces(BaseModel):
    text: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models["palm2"] = palm2_model
    ml_models["translator"] = translator
    ml_models["recommender"] = recommender
    ml_models["database"] = database
    yield
    ml_models.clear() 


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/tell-details")
async def details(
    text: str
):
    translated = ml_models["translator"].translate2english(text)
    eng_summarized = ml_models["palm2"].generate(f"Tell something about this Wroclaw place: {translated}")
    translated = ml_models["translator"].translate2polish(eng_summarized)
    return {"result": translated}


@app.post("/propose-places")
async def propose_places(
    request: ProposeTopics
):
    response = ml_models["recommender"].recommend_for_user(request.user_id)

    final_response = {}
    for category, values in response.items():
        final_response[category] = []

        for name in values:
            final_response[category].append(
                {
                    "name": name,
                    "image": load_image_as_base64(find_similar_filename("/home/mb-pro-kg/best23/data/backup", name))
                }
            )
    
    return final_response


@app.post("/update")
async def update(
    request: UpdateDescription
):
    user_id = ml_models["database"].update_description(
        user_id=request.user_id,
        description=request.description,
    )
    ml_models["recommender"].refresh()
    return {"user_id": user_id}


@app.post("/login")
async def login(
    request: Login
):
    user_id = ml_models["database"].login(
        password=request.password,
        login=request.login,
    )
    ml_models["recommender"].refresh()
    return {"user_id": user_id}


@app.post("/register")
async def register(
    request: Register
):
    user_id = ml_models["database"].register(
        name=request.name,
        login=request.login,
        password=request.password,
        description=request.description
    )
    ml_models["recommender"].refresh()

    return {"user_id": user_id}


@app.post("/propose-places-search")
async def propose_places_search(
    request: UnregisteredProposePlaces
):
    response = ml_models["recommender"].recommend_search(request.text)

    final_response = {}
    for category, values in response.items():
        final_response[category] = []

        for name in values:
            final_response[category].append(
                {
                    "name": name,
                    "image": load_image_as_base64(find_similar_filename("/home/mb-pro-kg/best23/data/backup", name))
                }
            )
    
    return final_response


@app.post("/propose-topic")
async def propose_topic(
    request: ProposeTopics
):
    response = ml_models["recommender"].recommend_users(request.user_id)
    translated = ml_models["translator"].translate2english("\n".join(response["descriptions"]))
    eng_summarized = ml_models["palm2"].generate(f"Propose topic for a discussion that can satisfy people with such interests. PROVICE ONLY TOPIC FOR DISCUSSION! Those are people descriptions: {translated}")
    translated = ml_models["translator"].translate2polish(eng_summarized)
    return {"common_topic": translated, "recommended_users": response["user_names"], "recommended_user_ids": response["similar_users"]}