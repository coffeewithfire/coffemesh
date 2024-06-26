from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
async def root(user_id: int = 5):
    return {"user_id": user_id}