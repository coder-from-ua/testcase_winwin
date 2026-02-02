# Local Reverse Proxy Demo (Docker Compose)

Tiny web service running behind an nginx reverse proxy with rate limiting and request ID handling.

---

## 1) Prerequisites

Required:
- Docker (20+)
- Docker Compose v2 (`docker compose`)

---

## 2) How to Run

```bash
cp .env.example .env
# edit ENV_NAME if desired
make up
