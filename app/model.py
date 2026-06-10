from app.profiles import MODEL_ID

generator = None

def get_generator():
    global generator

    if generator is None:
        print("Loading model...")

        generator = pipeline(
            task="text-generation",
            model=MODEL_ID
        )

    return generator
