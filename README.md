# PyBox Status API

A minimal FastAPI app that shows system uptime, hostname, and current UTC time.

## Endpoints

- `/` – Welcome
- `/status` – Returns JSON with system status

## Run with Docker

```bash
docker build -t pybox-status-api .
docker run -d -p 8080:80 pybox-status-api

