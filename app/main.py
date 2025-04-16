from fastapi import FastAPI
from datetime import datetime
import socket
import os
import time

app = FastAPI()

start_time = time.time()

@app.get("/")
def read_root():
    return {"message": "Hello Mr. Val, Welcome to PyBox Status API!"}

@app.get("/status")
def get_status():
    uptime = round(time.time() - start_time, 2)
    return {
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat(),
        "uptime_seconds": uptime,
        "environment": os.getenv("ENVIRONMENT", "dev")
    }
