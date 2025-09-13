# Here you can interact with the database or any other data source
# to fetch and return the user with the specified ID
async def get_user(user_id: int):
    return {"id": user_id, "name": f"User {user_id}"}

# Here you can interact with the database or any other data source
# to insert the user with the specified payload
# For demonstration purposes, let's assume you're inserting the payload as
# is into the database


async def create_user(payload):
    return {"message": "User created successfully", "req_body": payload}
