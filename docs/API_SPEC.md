# API Specification - Conference Planning Crew

## Overview
The Conference Planning Crew API is a RESTful API built with FastAPI that provides endpoints for managing conference planning workflows, AI agent orchestration, and real-time collaboration.

## Base URL
- Development: `http://localhost:8000`
- Production: `https://api.conference-planning-crew.com`

## Authentication
The API uses JWT (JSON Web Tokens) for authentication with access and refresh tokens.

### Headers
```
Authorization: Bearer <access_token>
Content-Type: application/json
```

## API Endpoints

### Health Check
- `GET /api/v1/health/` - Basic health check
- `GET /api/v1/health/db` - Database health check
- `GET /api/v1/health/redis` - Redis health check

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - User logout

### Events
- `GET /api/v1/events/` - List all events
- `POST /api/v1/events/` - Create new event
- `GET /api/v1/events/{event_id}` - Get event details
- `PUT /api/v1/events/{event_id}` - Update event
- `DELETE /api/v1/events/{event_id}` - Delete event

### Venues
- `GET /api/v1/venues/` - List venues
- `POST /api/v1/venues/` - Create venue
- `GET /api/v1/venues/{venue_id}` - Get venue details
- `PUT /api/v1/venues/{venue_id}` - Update venue
- `DELETE /api/v1/venues/{venue_id}` - Delete venue

### Speakers
- `GET /api/v1/speakers/` - List speakers
- `POST /api/v1/speakers/` - Create speaker
- `GET /api/v1/speakers/{speaker_id}` - Get speaker details
- `PUT /api/v1/speakers/{speaker_id}` - Update speaker
- `DELETE /api/v1/speakers/{speaker_id}` - Delete speaker

### Sponsors
- `GET /api/v1/sponsors/` - List sponsors
- `POST /api/v1/sponsors/` - Create sponsor
- `GET /api/v1/sponsors/{sponsor_id}` - Get sponsor details
- `PUT /api/v1/sponsors/{sponsor_id}` - Update sponsor
- `DELETE /api/v1/sponsors/{sponsor_id}` - Delete sponsor

### AI Agents
- `GET /api/v1/agents/` - List active agents
- `POST /api/v1/agents/start` - Start agent workflow
- `GET /api/v1/agents/{agent_id}` - Get agent status
- `POST /api/v1/agents/{agent_id}/approve` - Approve agent decision
- `POST /api/v1/agents/{agent_id}/reject` - Reject agent decision

## Data Models

### Event
```json
{
  "id": "uuid",
  "tenant_id": "uuid",
  "name": "string",
  "description": "string",
  "brief_json": "object",
  "city": "string",
  "venue_pref": "string",
  "start_date": "datetime",
  "end_date": "datetime",
  "status": "enum: planning|active|completed|cancelled",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Venue
```json
{
  "id": "uuid",
  "event_id": "uuid",
  "name": "string",
  "address": "string",
  "capacity": "integer",
  "rooms": "array",
  "cost_cards": "object",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Speaker
```json
{
  "id": "uuid",
  "name": "string",
  "bio": "string",
  "topics": "array",
  "availability": "object",
  "contract_uri": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Sponsor
```json
{
  "id": "uuid",
  "company": "string",
  "tier": "enum: platinum|gold|silver|bronze",
  "packages": "object",
  "deliverables": "object",
  "contract_uri": "string",
  "invoices": "array",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Error Responses
All error responses follow this format:
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object"
  }
}
```

### Common Error Codes
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Validation Error
- `500` - Internal Server Error

## Rate Limiting
- 100 requests per minute per IP
- 1000 requests per hour per user

## WebSocket Endpoints
- `ws://localhost:8000/ws/events/{event_id}` - Real-time event updates
- `ws://localhost:8000/ws/agents/{agent_id}` - Real-time agent status updates

## TODO: Additional Endpoints to Implement
- Session management
- Room management
- Track management
- Attendee management
- Ticket management
- Payment processing
- Budget management
- Task management
- Knowledge base management
- Audit log endpoints
