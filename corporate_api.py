import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
DATABASE_PATH = Path("app.db")


@app.get("/users/{user_id}")
def get_user(user_id: int) -> JSONResponse:
    """Fetch a user by ID.

    Args:
        user_id: The ID of the user to fetch.

    Returns:
        A standardized JSON response containing the user, or a not-found error.
    """
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.row_factory = sqlite3.Row
        user = connection.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

    if user is None:
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "data": None,
                "message": "User not found",
            },
        )

    return JSONResponse(
        content={
            "status": "success",
            "data": dict(user),
            "message": "User fetched successfully",
        },
    )