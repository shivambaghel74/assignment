from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.profiles import (
    PROFILE,
    ACTIVE_PROFILE,
    MODEL_ID
)

app = FastAPI()

MODEL_READY = False


@app.on_event("startup")
def startup():
    global MODEL_READY
    MODEL_READY = True


@app.get("/v1/health/live")
def live():
    return {"status": "alive"}


@app.get("/v1/health/ready")
def ready():

    if MODEL_READY:
        return {"status": "ready"}

    return JSONResponse(
        status_code=503,
        content={"status": "loading"}
    )


@app.get("/v1/models")
def models():

    return {
        "object": "list",
        "data": [
            {
                "id": MODEL_ID,
                "object": "model"
            }
        ]
    }


@app.get("/v1/profiles")
def profiles():

    return {
        "active_profile": PROFILE,
        "parameters": ACTIVE_PROFILE
    }


@app.post("/v1/chat/completions")
def chat(request: dict):

    prompt = ""

    if "messages" in request and len(request["messages"]) > 0:
        prompt = request["messages"][-1].get("content", "")

    return {
        "id": "chatcmpl-test",
        "object": "chat.completion",
        "model": MODEL_ID,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": f"Mock response for: {prompt}"
                },
                "finish_reason": "stop"
            }
        ]
    }
