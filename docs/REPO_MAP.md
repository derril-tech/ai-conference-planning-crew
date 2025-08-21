# Repository Map - Conference Planning Crew

## Overview
This repository contains the Conference Planning Crew (OrchestrateX) - a multi-agent AI conference planning platform built with Next.js 14 frontend and FastAPI backend.

## Frontend Structure (`/`)

### Core Files
- `package.json` - Frontend dependencies and scripts
- `next.config.js` - Next.js configuration
- `tailwind.config.js` - Tailwind CSS configuration with custom conference color palette
- `tsconfig.json` - TypeScript configuration with path aliases
- `postcss.config.js` - PostCSS configuration

### Source Code (`/src`)
- `/app/` - Next.js 14 App Router pages and layouts
  - `layout.tsx` - Root layout with providers
  - `page.tsx` - Landing page
  - `globals.css` - Global styles with design tokens
- `/components/` - Reusable React components
  - `/ui/` - Base UI components (shadcn/ui style)
    - `button.tsx` - Button component with variants
    - `card.tsx` - Card component
  - `providers.tsx` - Context providers (React Query, etc.)
- `/lib/` - Utility functions and helpers
  - `utils.ts` - Common utilities (cn, formatting, etc.)
- `/types/` - TypeScript type definitions
- `/hooks/` - Custom React hooks
- `/store/` - State management (Zustand stores)

### TODO: Frontend Modules to Implement
- `/app/dashboard/` - Main dashboard page
- `/app/events/` - Event management pages
- `/app/events/[id]/` - Individual event pages
  - `timeline/` - Agent timeline view
  - `venues/` - Venue management
  - `schedule/` - Schedule builder
  - `speakers/` - Speaker CRM
  - `sponsors/` - Sponsor CRM
  - `budget/` - Budget console
  - `registration/` - Registration dashboard
  - `command/` - Command center

## Backend Structure (`/backend`)

### Core Files
- `requirements.txt` - Python dependencies
- `alembic.ini` - Database migration configuration

### Source Code (`/backend/app`)
- `main.py` - FastAPI application entry point
- `/core/` - Core application configuration
  - `config.py` - Application settings (Pydantic)
  - `database.py` - SQLAlchemy 2.0 async database setup
  - `redis.py` - Redis client configuration
- `/api/v1/` - API version 1 endpoints
  - `api.py` - Main API router
  - `/endpoints/` - Individual endpoint modules
    - `health.py` - Health check endpoints
    - `auth.py` - Authentication endpoints
    - `events.py` - Event management endpoints
    - `venues.py` - Venue management endpoints
    - `speakers.py` - Speaker management endpoints
    - `sponsors.py` - Sponsor management endpoints
    - `agents.py` - AI agent orchestration endpoints

### TODO: Backend Modules to Implement
- `/models/` - SQLAlchemy database models
- `/schemas/` - Pydantic request/response schemas
- `/services/` - Business logic services
- `/agents/` - AI agent implementations
  - `venue_scout.py` - Venue scouting agent
  - `speaker_outreach.py` - Speaker outreach agent
  - `sponsorship_manager.py` - Sponsorship management agent
  - `budget_controller.py` - Budget control agent
  - `marketing_ops.py` - Marketing operations agent
  - `attendee_experience.py` - Attendee experience agent
  - `logistics_travel.py` - Logistics and travel agent
  - `risk_compliance.py` - Risk and compliance agent
- `/orchestrator/` - LangGraph workflow orchestration
- `/integrations/` - External service integrations
  - `stripe.py` - Payment processing
  - `sendgrid.py` - Email service
  - `twilio.py` - SMS service
  - `google_calendar.py` - Google Calendar integration
  - `microsoft_graph.py` - Microsoft Graph integration
- `/workers/` - Background task workers
- `/websockets/` - Real-time communication

## Documentation (`/docs`)
- `REPO_MAP.md` - This file (repository structure)
- `API_SPEC.md` - API documentation and specifications
- `CLAUDE.md` - Claude AI collaboration guidelines
- `PROMPT_DECLARATION` - Project requirements and specifications

## Environment Files
- `.env.example` - Environment variables template
- `.env.local` - Local development environment (gitignored)

## Configuration Files
- `.gitignore` - Git ignore rules
- `README.md` - Project overview and setup instructions
- `PROJECT_BRIEF` - Detailed project requirements

## Development Scripts
- `npm run dev` - Start frontend development server
- `npm run build` - Build frontend for production
- `uvicorn backend.app.main:app --reload` - Start backend development server

## Key Technologies
- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, shadcn/ui
- **Backend**: FastAPI, SQLAlchemy 2.0, Pydantic v2, PostgreSQL, Redis
- **AI**: LangGraph, LangChain, OpenAI, Claude
- **Integrations**: Stripe, SendGrid, Twilio, Google APIs, Microsoft Graph
