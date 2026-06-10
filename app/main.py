from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.profiles import PROFILE, ACTIVE_PROFILE, MODEL_ID

app = FastAPI(title="Model Server", version="1.0.0")

# -------------------------
# GLOBAL STATE
# -------------------------
MODEL_READY = False


# -------------------------
# STARTUP EVENT
# -------------------------
@app.on_event("startup")
def startup():
    global MODEL_READY
    MODEL_READY = True
    print("🚀 Model Server Started Successfully")


# -------------------------
# HEALTH CHECKS (PROD STANDARD)
# -------------------------

# Liveness probe (is app running?)
@app.get("/v1/health/live")
def live():
    return {"status": "alive"}


# Simple health endpoint (used by your test.sh)
@app.get("/health")
def health():
    return {"status": "ok"}


# Readiness probe (is model ready to serve?)
@app.get("/v1/health/ready")
def ready():
    if MODEL_READY:
        return {"status": "ready"}

    return JSONResponse(
        status_code=503,
        content={"status": "loading"}
    )


# -------------------------
# MODEL INFO APIs
# -------------------------

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


# -------------------------
# CHAT / INFERENCE API
# -------------------------
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
