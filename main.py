from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

# Dummy user data
user_data = {
    "jeni": {
        "name": "Jeni Thomas",
        "email": "jeni@gmail.com",
        "phone": "+1-555-1234",
        "address": "123 Apple St, New York, NY",
        "status": "shipped"
    },
    "sam": {
        "name": "Sam Wilson",
        "email": "sam@gmail.com",
        "phone": "+1-555-5678",
        "address": "456 Orange Ave, Los Angeles, CA",
        "status": "pending"
    }
}

@app.get("/users/info")
async def get_user_info(name: str = Query(..., description="User")):
    if name in user_data:
        return user_data[name]
    return JSONResponse(status_code=404, content={"message": "User not found"})
