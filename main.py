from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3

app = FastAPI()

DB_NAME = "coffee_logs.db"

class CoffeeLogCreate(BaseModel):
    bean_name: str = Field(min_length=1)
    water_g: int
    dose_g: int
    overall_score: int = Field(ge=1, le=5)

class ScoreUpdate(BaseModel):
    overall_score: int = Field(ge=1, le=5)

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bean_name TEXT NOT NULL,
        water_g INTEGER NOT NULL,
        dose_g INTEGER NOT NULL,
        overall_score INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

init_db()

def get_logs(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT log_id, bean_name, water_g, dose_g, overall_score 
        FROM logs 
        """
    )
    rows = cursor.fetchall()

    logs = []
    
    for row in rows:
        log_id, bean_name, water_g, dose_g, overall_score = row
        logs.append({
            "log_id": log_id,
            "bean_name": bean_name,
            "water_g": water_g,
            "dose_g": dose_g,
            "overall_score": overall_score
        })
    
    return logs

def get_log_by_id(conn, log_id):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT log_id, bean_name, water_g, dose_g, overall_score 
        FROM logs 
        WHERE log_id = ?
        """,
        (log_id,)
    )
    row = cursor.fetchone()
    if row is None:
        return None
    
    log_id, bean_name, water_g, dose_g, overall_score = row
    return {
        "log_id": log_id,
        "bean_name": bean_name,
        "water_g": water_g,
        "dose_g": dose_g,
        "overall_score": overall_score
    }

def create_new_log(conn, bean_name, water_g, dose_g, overall_score):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO logs (bean_name, water_g, dose_g, overall_score)
        VALUES (?, ?, ?, ?)
        """,
        (bean_name, water_g, dose_g, overall_score)
    )
    conn.commit()

    log_id = cursor.lastrowid

    return { 
        "log_id": log_id,
        "bean_name": bean_name,
        "water_g": water_g,
        "dose_g": dose_g,
        "overall_score": overall_score
    }

def update_overall_score(conn, log_id, new_score):
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE logs
        SET overall_score = ?
        WHERE log_id = ?
        """,
        (new_score, log_id)
    )
    conn.commit()
    
    if cursor.rowcount == 0:
        return None
    
    return {
        "log_id": log_id,
        "overall_score": new_score
    }

def delete_log(conn, log_id):
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM logs WHERE log_id = ?
        """,
        (log_id,)
    )
    conn.commit()
    
    if cursor.rowcount == 0:
        return None
    
    return {"message": "Log deleted"}

@app.get("/logs")
def read_logs():
    conn = sqlite3.connect(DB_NAME)
    result = get_logs(conn)
    conn.close()
    return result

@app.get("/logs/{log_id}")
def read_log(log_id: int):
    conn = sqlite3.connect(DB_NAME)
    result = get_log_by_id(conn, log_id)
    conn.close()
    if result is None:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@app.post("/logs")
def create_log(log: CoffeeLogCreate):
    conn = sqlite3.connect(DB_NAME)
    result = create_new_log(
        conn, 
        log.bean_name, 
        log.water_g, 
        log.dose_g, 
        log.overall_score
        )
    conn.close()
    
    return result

@app.put("/logs/{log_id}")
def update_score(log_id: int, score: ScoreUpdate):
    conn = sqlite3.connect(DB_NAME)
    result = update_overall_score(conn, log_id, score.overall_score)
    conn.close()

    if result is None:
        raise HTTPException(status_code=404, detail="Log not found")

    return result

@app.delete("/logs/{log_id}")
def remove_log(log_id: int):
    conn = sqlite3.connect(DB_NAME)
    result = delete_log(conn, log_id)
    conn.close()

    if result is None:
        raise HTTPException(status_code=404, detail="Log not found")

    return result

