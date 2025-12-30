# Event Analytics API (AWS + Docker + FastAPI)

A production-style event analytics backend API built with FastAPI, PostgreSQL, and Docker, designed to be deployed on AWS EC2.This service allows clients to:

Create users with API keys

Ingest analytics events

Query aggregated event summaries

Run locally or in production using Docker

### Tech Stack

FastAPI – REST API framework

PostgreSQL – Relational database

SQLAlchemy – ORM

Docker & Docker Compose – Containerization

AWS EC2 – Deployment target

Pytest – Automated testing

## AWS Deployment (EC2):

1. Launch an EC2 instance.
2. Install Docker and Docker Compose.
3. Clone this repository.
4. Create .env file on the server.
5. Run:

```
docker compose up -d --build
```
