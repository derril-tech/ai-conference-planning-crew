# OrchestrateX Project Structure

## 📁 Root Directory

```
orchestratex-conference-planning/
├── 📁 frontend/                 # Next.js 14 Frontend Application
├── 📁 backend/                  # FastAPI Backend Application
├── 📁 docs/                     # Project Documentation
├── 📁 scripts/                  # Setup and Utility Scripts
├── 📄 package.json             # Root package.json (Monorepo)
├── 📄 docker-compose.yml       # Docker Compose Configuration
├── 📄 .gitignore               # Git Ignore Rules
├── 📄 README.md                # Main Project README
├── 📄 PROJECT_BRIEF            # Detailed Project Requirements
├── 📄 PROMPT_DECLARATION       # AI Prompt Engineering Guidelines
└── 📄 env.example              # Root Environment Template
```

## 🎨 Frontend Structure (`frontend/`)

```
frontend/
├── 📁 src/                     # Source Code
│   ├── 📁 app/                # Next.js App Router
│   │   ├── 📁 dashboard/      # Dashboard Pages
│   │   ├── 📁 events/         # Event Management
│   │   │   └── 📁 [id]/       # Dynamic Event Routes
│   │   │       ├── 📁 schedule/    # Schedule Builder
│   │   │       ├── 📁 speakers/    # Speaker Management
│   │   │       ├── 📁 sponsors/    # Sponsor Management
│   │   │       ├── 📁 budget/      # Budget Console
│   │   │       ├── 📁 registration/ # Registration Dashboard
│   │   │       ├── 📁 venues/      # Venue Management
│   │   │       └── 📁 timeline/    # Agent Timeline
│   │   ├── 📁 command/        # Command Center
│   │   ├── 📁 analytics/      # Analytics Dashboard
│   │   ├── 📁 library/        # Knowledge Library
│   │   ├── 📁 settings/       # User Settings
│   │   ├── 📁 about/          # About Page
│   │   ├── 📄 layout.tsx      # Root Layout
│   │   ├── 📄 page.tsx        # Landing Page
│   │   └── 📄 globals.css     # Global Styles
│   ├── 📁 components/         # React Components
│   │   ├── 📁 ui/            # Base UI Components (shadcn/ui)
│   │   │   ├── 📄 button.tsx
│   │   │   ├── 📄 card.tsx
│   │   │   ├── 📄 input.tsx
│   │   │   ├── 📄 table.tsx
│   │   │   ├── 📄 dialog.tsx
│   │   │   ├── 📄 progress.tsx
│   │   │   ├── 📄 badge.tsx
│   │   │   ├── 📄 select.tsx
│   │   │   ├── 📄 alert.tsx
│   │   │   └── 📄 index.ts
│   │   ├── 📁 specialized/   # Application-Specific Components
│   │   │   ├── 📄 agent-card.tsx
│   │   │   ├── 📄 event-card.tsx
│   │   │   ├── 📄 metric-card.tsx
│   │   │   ├── 📄 activity-feed.tsx
│   │   │   ├── 📄 data-table.tsx
│   │   │   └── 📄 status-chip.tsx
│   │   ├── 📄 navigation.tsx  # Navigation Components
│   │   └── 📄 providers.tsx   # React Providers
│   ├── 📁 lib/               # Utility Functions
│   │   ├── 📄 utils.ts       # General Utilities
│   │   └── 📄 mock-data.ts   # Mock Data for Development
│   └── 📁 types/             # TypeScript Type Definitions
│       └── 📄 index.ts       # Main Type Definitions
├── 📄 package.json           # Frontend Dependencies
├── 📄 next.config.js         # Next.js Configuration
├── 📄 tailwind.config.js     # Tailwind CSS Configuration
├── 📄 postcss.config.js      # PostCSS Configuration
├── 📄 tsconfig.json          # TypeScript Configuration
├── 📄 env.example            # Frontend Environment Template
├── 📄 README.md              # Frontend Documentation
└── 📄 Dockerfile             # Frontend Docker Configuration
```

## ⚙️ Backend Structure (`backend/`)

```
backend/
├── 📁 app/                   # FastAPI Application
│   ├── 📁 api/              # API Endpoints
│   │   └── 📁 v1/           # API Version 1
│   │       ├── 📄 api.py    # Main API Router
│   │       └── 📁 endpoints/ # API Endpoints
│   │           ├── 📄 auth.py      # Authentication
│   │           ├── 📄 events.py    # Event Management
│   │           ├── 📄 agents.py    # AI Agent Management
│   │           └── 📄 compliance.py # Compliance & GDPR
│   ├── 📁 core/             # Core Functionality
│   │   ├── 📄 config.py     # Configuration Management
│   │   ├── 📄 database.py   # Database Connection
│   │   ├── 📄 redis.py      # Redis Connection
│   │   ├── 📄 security.py   # Security & Authentication
│   │   ├── 📄 auth.py       # Auth Dependencies
│   │   ├── 📄 middleware.py # Custom Middleware
│   │   └── 📄 compliance.py # GDPR & Compliance
│   ├── 📁 models/           # SQLAlchemy Models
│   │   ├── 📄 __init__.py
│   │   ├── 📄 user.py       # User Model
│   │   ├── 📄 event.py      # Event Model
│   │   ├── 📄 agent.py      # Agent Model
│   │   ├── 📄 approval.py   # Approval Model
│   │   ├── 📄 venue.py      # Venue Model
│   │   ├── 📄 speaker.py    # Speaker Model
│   │   ├── 📄 sponsor.py    # Sponsor Model
│   │   └── 📄 agent_activity.py # Agent Activity Model
│   ├── 📁 schemas/          # Pydantic Schemas
│   │   ├── 📄 __init__.py
│   │   ├── 📄 user.py       # User Schemas
│   │   ├── 📄 event.py      # Event Schemas
│   │   ├── 📄 agent.py      # Agent Schemas
│   │   └── 📄 approval.py   # Approval Schemas
│   ├── 📁 agents/           # AI Agent Implementations
│   │   ├── 📄 __init__.py
│   │   ├── 📄 base_agent.py # Base Agent Class
│   │   ├── 📄 venue_scout.py # Venue Scout Agent
│   │   ├── 📄 speaker_outreach.py # Speaker Outreach Agent
│   │   ├── 📄 budget_controller.py # Budget Controller Agent
│   │   ├── 📄 marketing_ops.py # Marketing Ops Agent
│   │   ├── 📄 attendee_experience.py # Attendee Experience Agent
│   │   ├── 📄 logistics_travel.py # Logistics & Travel Agent
│   │   ├── 📄 risk_compliance.py # Risk & Compliance Agent
│   │   └── 📄 sponsorship_manager.py # Sponsorship Manager Agent
│   └── 📄 main.py           # FastAPI Application Entry Point
├── 📄 requirements.txt      # Python Dependencies
├── 📄 env.example           # Backend Environment Template
├── 📄 README.md             # Backend Documentation
└── 📄 Dockerfile            # Backend Docker Configuration
```

## 📚 Documentation Structure (`docs/`)

```
docs/
├── 📄 API_SPEC.md           # Complete API Specification
├── 📄 SECURITY.md           # Security & Compliance Guide
├── 📄 REPO_MAP.md           # Repository Structure Map
└── 📄 CLAUDE.md             # AI Collaboration Guidelines
```

## 🛠️ Scripts Structure (`scripts/`)

```
scripts/
├── 📄 setup.sh              # Unix/Linux Setup Script
└── 📄 setup.ps1             # Windows PowerShell Setup Script
```

## 🐳 Docker Configuration

```
├── 📄 docker-compose.yml    # Multi-Service Docker Setup
├── 📄 frontend/Dockerfile   # Frontend Container
└── 📄 backend/Dockerfile    # Backend Container
```

## 🔧 Configuration Files

### Root Level
- `package.json` - Monorepo configuration with workspaces
- `docker-compose.yml` - Multi-service container orchestration
- `.gitignore` - Comprehensive ignore rules for both frontend and backend

### Frontend Configuration
- `frontend/package.json` - Next.js dependencies and scripts
- `frontend/next.config.js` - Next.js framework configuration
- `frontend/tailwind.config.js` - Tailwind CSS styling configuration
- `frontend/tsconfig.json` - TypeScript compiler configuration
- `frontend/postcss.config.js` - PostCSS processing configuration

### Backend Configuration
- `backend/requirements.txt` - Python package dependencies
- `backend/app/core/config.py` - Pydantic settings configuration

## 🌐 Environment Configuration

### Frontend Environment (`frontend/env.example`)
- API endpoints and WebSocket URLs
- Authentication configuration
- External service integrations
- Feature flags and debug settings

### Backend Environment (`backend/env.example`)
- Database connection strings
- Redis configuration
- Security keys and algorithms
- AI service API keys
- External service credentials
- Email and storage configuration

## 🚀 Development Workflow

### Local Development
1. **Setup**: Run `npm run setup` or use setup scripts
2. **Environment**: Configure `.env` files
3. **Development**: Run `npm run dev` for both services
4. **Frontend**: http://localhost:3000
5. **Backend**: http://localhost:8000
6. **API Docs**: http://localhost:8000/docs

### Docker Development
1. **Setup**: `docker-compose up -d`
2. **Services**: All services run in containers
3. **Database**: PostgreSQL on port 5432
4. **Cache**: Redis on port 6379

### Production Deployment
- **Frontend**: Deploy to Vercel, Netlify, or AWS Amplify
- **Backend**: Deploy to Railway, Render, or cloud platforms
- **Database**: Managed PostgreSQL service
- **Cache**: Managed Redis service

## 📦 Package Management

### Frontend Dependencies
- **Framework**: Next.js 14 with App Router
- **UI**: React 18, TypeScript, Tailwind CSS
- **Components**: shadcn/ui component library
- **State**: React Query, Zustand
- **Forms**: React Hook Form, Zod validation
- **Charts**: Recharts for data visualization
- **Real-time**: Socket.io client

### Backend Dependencies
- **Framework**: FastAPI with async support
- **Database**: SQLAlchemy 2.0 with async ORM
- **Validation**: Pydantic v2 for data validation
- **AI**: LangChain, LangGraph for agent orchestration
- **Security**: JWT, bcrypt, role-based access control
- **Background Tasks**: Celery with Redis
- **Monitoring**: Comprehensive logging and metrics

## 🔐 Security Architecture

### Authentication & Authorization
- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- Multi-tenant data isolation
- Secure password hashing

### Data Protection
- GDPR compliance implementation
- Data encryption in transit and at rest
- Comprehensive audit logging
- Data retention policies

### API Security
- Rate limiting and DDoS protection
- Security headers (CSP, HSTS, XSS Protection)
- Input validation and sanitization
- CORS configuration

## 🤖 AI Agent System

### Agent Architecture
- **Base Agent**: Abstract base class with common functionality
- **Specialized Agents**: 8 domain-specific AI agents
- **Orchestration**: LangGraph workflow management
- **Human-in-the-Loop**: Approval gates for critical decisions
- **RAG Integration**: Document-grounded decision making

### Agent Responsibilities
1. **Venue Scout**: Venue research and selection
2. **Speaker Outreach**: Speaker identification and recruitment
3. **Budget Controller**: Financial planning and optimization
4. **Marketing Ops**: Marketing strategy and campaigns
5. **Attendee Experience**: Experience design and optimization
6. **Logistics & Travel**: Operational coordination
7. **Risk & Compliance**: Risk assessment and governance
8. **Sponsorship Manager**: Sponsor acquisition and management

This structure provides a clean, organized, and scalable foundation for the OrchestrateX conference planning platform, with clear separation of concerns between frontend and backend, comprehensive documentation, and multiple deployment options.
