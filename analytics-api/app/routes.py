
from fastapi import FastAPI, HTTPException, APIRouter


app = FastAPI()
router = APIRouter()
router = FastAPI.routes()


@router.get()