# Backend - Conference Planning Crew

## Overview

The backend is a FastAPI application that provides RESTful APIs for conference planning management, AI agent orchestration, and real-time collaboration. It uses SQLAlchemy 2.0 for database operations and integrates with various AI services and external APIs.

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Database**: PostgreSQL with pgvector extension
- **ORM**: SQLAlchemy 2.0 (async)
- **Validation**: Pydantic v2
- **Authentication**: JWT with refresh tokens
- **Caching**: Redis
- **Background Tasks**: Celery
- **AI**: LangGraph, LangChain, OpenAI, Claude
- **Real-time**: WebSockets
- **Testing**: pytest, pytest-asyncio

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/                # Core configuration and utilities
│   │   ├── config.py        # Application settings
│   │   ├── database.py      # Database configuration
│   │   └── redis.py         # Redis configuration
│   ├── api/                 # API endpoints
│   │   └── v1/             # API version 1
│   │       ├── api.py      # Main API router
│   │       └── endpoints/  # Individual endpoint modules
│   │           ├── health.py
│   │           ├── auth.py
│   │           ├── events.py
│   │           ├── venues.py
│   │           ├── speakers.py
│   │           ├── sponsors.py
│   │           └── agents.py
│   ├── models/              # SQLAlchemy database models (TODO)
│   ├── schemas/             # Pydantic request/response schemas (TODO)
│   ├── services/            # Business logic services (TODO)
│   ├── agents/              # AI agent implementations (TODO)
│   ├── orchestrator/        # LangGraph workflow orchestration (TODO)
│   ├── integrations/        # External service integrations (TODO)
│   ├── workers/             # Background task workers (TODO)
│   └── websockets/          # Real-time communication (TODO)
├── requirements.txt         # Python dependencies
├── alembic.ini             # Database migration configuration (TODO)
└── tests/                  # Test suite (TODO)
```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 14+ with pgvector extension
- Redis 6+
- Virtual environment (recommended)

### Installation

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` with your configuration:
   ```env
   # Database
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/conference_crew
   
   # Redis
   REDIS_URL=redis://localhost:6379
   
   # AI Services
   OPENAI_API_KEY=your-openai-api-key
   ANTHROPIC_API_KEY=your-anthropic-api-key
   
   # Security
   SECRET_KEY=your-secret-key-here
   ```

4. **Set up database**:
   ```bash
   # Create database
   createdb conference_crew
   
   # Enable pgvector extension
   psql conference_crew -c "CREATE EXTENSION IF NOT EXISTS vector;"
   
   # Run migrations (when implemented)
   alembic upgrade head
   ```

5. **Start development server**:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Available Scripts

- `uvicorn app.main:app --reload` - Start development server
- `pytest` - Run tests
- `black .` - Format code
- `isort .` - Sort imports
- `flake8 .` - Lint code
- `mypy .` - Type checking

## API Documentation

### Base URL
- Development: `http://localhost:8000`
- Production: `https://api.conference-planning-crew.com`

### Authentication
The API uses JWT authentication with access and refresh tokens.

**Headers**:
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

### Endpoints

#### Health Check
- `GET /api/v1/health/` - Basic health check
- `GET /api/v1/health/db` - Database health check
- `GET /api/v1/health/redis` - Redis health check

#### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - User logout

#### Events
- `GET /api/v1/events/` - List all events
- `POST /api/v1/events/` - Create new event
- `GET /api/v1/events/{event_id}` - Get event details
- `PUT /api/v1/events/{event_id}` - Update event
- `DELETE /api/v1/events/{event_id}` - Delete event

#### AI Agents
- `GET /api/v1/agents/` - List active agents
- `POST /api/v1/agents/start` - Start agent workflow
- `GET /api/v1/agents/{agent_id}` - Get agent status
- `POST /api/v1/agents/{agent_id}/approve` - Approve agent decision
- `POST /api/v1/agents/{agent_id}/reject` - Reject agent decision

## Development Guidelines

### Code Structure

1. **Models** (`app/models/`) - SQLAlchemy database models
2. **Schemas** (`app/schemas/`) - Pydantic request/response schemas
3. **Services** (`app/services/`) - Business logic
4. **Endpoints** (`app/api/v1/endpoints/`) - API routes
5. **Agents** (`app/agents/`) - AI agent implementations

### Database Models

Use SQLAlchemy 2.0 async patterns:

```python
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid
from datetime import datetime

class Event(Base):
    __tablename__ = "events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    # ... other fields
```

### API Schemas

Use Pydantic v2 for request/response validation:

```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
```

### Error Handling

Use consistent error responses:

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Event not found"
)
```

### Async/Await

All database operations should be async:

```python
async def get_event(event_id: str, db: AsyncSession):
    result = await db.execute(
        select(Event).where(Event.id == event_id)
    )
    return result.scalar_one_or_none()
```

## AI Agent Architecture

### Agent Types

1. **Venue Scout** - Find and evaluate venues
2. **Speaker Outreach** - Recruit and manage speakers
3. **Sponsorship Manager** - Design and sell sponsorship packages
4. **Budget Controller** - Manage and optimize budget
5. **Marketing Ops** - Execute marketing campaigns
6. **Attendee Experience** - Optimize attendee journey
7. **Logistics & Travel** - Coordinate logistics
8. **Risk & Compliance** - Identify and mitigate risks

### LangGraph Workflow

```python
from langgraph import StateGraph, END

# Define state schema
class ConferenceState(TypedDict):
    event_id: str
    brief: dict
    venue_shortlist: List[dict]
    speakers: List[dict]
    # ... other state fields

# Create workflow
workflow = StateGraph(ConferenceState)
workflow.add_node("venue_scout", venue_scout_agent)
workflow.add_node("speaker_outreach", speaker_outreach_agent)
# ... add other agents
```

### Human-in-the-Loop

- Approval gates for critical decisions
- Decision rationale and citations
- Risk assessment and mitigation
- Audit trail for all actions

## Testing

### Unit Tests
```bash
pytest tests/unit/
```

### Integration Tests
```bash
pytest tests/integration/
```

### API Tests
```bash
pytest tests/api/
```

### Test Structure
```
tests/
├── unit/           # Unit tests
├── integration/    # Integration tests
├── api/           # API endpoint tests
├── fixtures/      # Test fixtures
└── conftest.py    # Test configuration
```

## Performance

### Optimization
- Async database operations
- Connection pooling
- Redis caching
- Background task processing
- Efficient query patterns

### Monitoring
- Request/response logging
- Database query performance
- Memory usage tracking
- Error rate monitoring

## Security

### Authentication
- JWT tokens with refresh mechanism
- Role-based access control (RBAC)
- Secure password hashing
- Session management

### Data Protection
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CORS configuration

### API Security
- Rate limiting
- Request size limits
- HTTPS enforcement
- Security headers

## Deployment

### Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `SECRET_KEY` - JWT secret key
- `OPENAI_API_KEY` - OpenAI API key
- `ANTHROPIC_API_KEY` - Anthropic API key

### Production Considerations
- Use production-grade ASGI server (Gunicorn + Uvicorn)
- Set up proper logging
- Configure monitoring and alerting
- Implement health checks
- Set up backup strategies

## Troubleshooting

### Common Issues

1. **Database Connection**
   - Verify PostgreSQL is running
   - Check connection string format
   - Ensure pgvector extension is installed

2. **Redis Connection**
   - Verify Redis is running
   - Check connection string
   - Test with redis-cli

3. **AI Service Integration**
   - Verify API keys are valid
   - Check rate limits
   - Monitor API usage

### Debugging

- Enable debug logging
- Use FastAPI's automatic documentation
- Check application logs
- Monitor database queries

## Contributing

1. Follow PEP 8 style guidelines
2. Add type hints to all functions
3. Write tests for new features
4. Update documentation
5. Use conventional commit messages

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [PostgreSQL](https://www.postgresql.org/docs/)
