from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}") 
async def read_item_val(item_id: int):
    return{"item_id":item_id}

@app.get("/items/")
async def read_item_val(skip: int = 0, limit: int = 0, q: str= None):
    if q:
        return {"query string": q, "skip": skip, "limit": limit}
    else:
        return {"skip": skip, "limit": limit}
    
@app.get("/users/{user_id}")
async def read_user_val(user_id):
    return {"user_id":user_id}

@app.get("/users/{user_id}/items/")
async def read_user_item(user_id, skip, limit):
    return {"user_id": user_id, "skip": skip, "limit": limit}
        