import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI()
DATABASE_PATH = Path("app.db")


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int | str]:
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        connection.row_factory = sqlite3.Row
        user = connection.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(user)