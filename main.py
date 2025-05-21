from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

# Dummy user data keyed by email
user_data = {
    "jeni@gmail.com": {
        "name": "Jeni Thomas",
        "email": "jeni@gmail.com",
        "phone": "+1-555-1234",
        "address": "123 Apple St, New York, NY",
        "status": "shipped"
    },
    "sam@gmail.com": {
        "name": "Sam Wilson",
        "email": "sam@gmail.com",
        "phone": "+1-555-5678",
        "address": "456 Orange Ave, Los Angeles, CA",
        "status": "pending"
    },
    "kane@gmail.com": {
        "name": "Kane Johnson",
        "email": "kane@gmail.com",
        "phone": "+1-555-0000",
        "address": "789 Banana Blvd, Miami, FL",
        "status": "pending"
    }
}

@app.get("/users/info")
async def get_user_info(
    email: str = Query(..., description="User's email address")
):
    key = email.lower()
    if key in user_data:
        return user_data[key]
    raise HTTPException(status_code=404, detail="User not found")
