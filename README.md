# OrchestrateX - AI Conference Planning Platform

A comprehensive multi-agent AI platform that coordinates specialized agents to design, staff, budget, schedule, promote, and run conferences end-to-end with human oversight and complete audit trails.

## 🏗️ Project Structure

```
orchestratex-conference-planning/
├── frontend/                 # Next.js 14 Frontend Application
│   ├── src/                 # Source code
│   │   ├── app/            # Next.js App Router pages
│   │   ├── components/     # React components
│   │   ├── lib/           # Utility functions
│   │   └── types/         # TypeScript type definitions
│   ├── package.json       # Frontend dependencies
│   ├── next.config.js     # Next.js configuration
│   ├── tailwind.config.js # Tailwind CSS configuration
│   └── README.md          # Frontend documentation
├── backend/                # FastAPI Backend Application
│   ├── app/               # FastAPI application code
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Core functionality
│   │   ├── models/       # Database models
│   │   ├── schemas/      # Pydantic schemas
│   │   └── agents/       # AI agent implementations
│   ├── requirements.txt   # Python dependencies
│   └── README.md         # Backend documentation
├── docs/                  # Project documentation
├── package.json          # Root package.json (monorepo)
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.11+ and pip
- **PostgreSQL** 14+
- **Redis** 6+

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd orchestratex-conference-planning
   ```

2. **Install all dependencies**
   ```bash
   npm run setup
   ```

3. **Set up environment variables**
   ```bash
   # Copy environment files
   cp frontend/env.example frontend/.env.local
   cp backend/env.example backend/.env
   
   # Edit the files with your actual values
   ```

4. **Start the development servers**
   ```bash
   npm run dev
   ```

This will start:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000

## 📚 Documentation

- **[Frontend Documentation](frontend/README.md)** - Next.js setup, components, and development
- **[Backend Documentation](backend/README.md)** - FastAPI setup, API endpoints, and AI agents
- **[API Documentation](docs/API_SPEC.md)** - Complete API specification
- **[Project Brief](PROJECT_BRIEF)** - Detailed project requirements and specifications

## 🛠️ Development

### Available Scripts

```bash
# Development
npm run dev              # Start both frontend and backend
npm run dev:frontend     # Start only frontend
npm run dev:backend      # Start only backend

# Building
npm run build            # Build both frontend and backend
npm run build:frontend   # Build only frontend
npm run build:backend    # Build only backend

# Production
npm run start            # Start both in production mode
npm run start:frontend   # Start only frontend in production
npm run start:backend    # Start only backend in production

# Setup
npm run setup            # Install all dependencies
npm run install:all      # Install all dependencies
```

### Frontend Development

The frontend is built with:
- **Next.js 14** with App Router
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **shadcn/ui** for components
- **React Query** for server state
- **Zustand** for client state

### Backend Development

The backend is built with:
- **FastAPI** for the API framework
- **SQLAlchemy 2.0** for database ORM
- **Pydantic v2** for data validation
- **LangGraph** for AI agent orchestration
- **PostgreSQL** with pgvector for database
- **Redis** for caching and sessions

## 🤖 AI Agents

The platform includes 8 specialized AI agents:

1. **Venue Scout** - Venue research and selection
2. **Speaker Outreach** - Speaker sourcing and communication
3. **Budget Controller** - Financial planning and optimization
4. **Marketing Ops** - Marketing strategy and campaigns
5. **Attendee Experience** - Experience design and optimization
6. **Logistics & Travel** - Logistics coordination
7. **Risk & Compliance** - Risk assessment and compliance
8. **Sponsorship Manager** - Sponsor acquisition and management

## 🔐 Security & Compliance

- **JWT Authentication** with role-based access control
- **GDPR Compliance** with data export and deletion
- **Audit Trails** for all AI agent decisions
- **Rate Limiting** and security headers
- **Data Encryption** in transit and at rest

## 📊 Features

### Conference Planning
- **Event Wizard** - AI-powered event planning from brief to execution
- **Agent Timeline** - Real-time coordination of specialized AI agents
- **Schedule Builder** - Drag-and-drop session scheduling
- **Venue Management** - Venue research and shortlisting
- **Speaker CRM** - Speaker outreach and management
- **Sponsor Management** - Sponsor acquisition and tracking

### Real-time Operations
- **Command Center** - Live event management and incident response
- **Registration Dashboard** - Attendee registration and analytics
- **Budget Console** - Financial tracking and projections
- **Analytics** - Comprehensive event analytics

### AI-Powered Features
- **Multi-agent Orchestration** - Coordinated AI workflows
- **Human-in-the-Loop** - Approval gates for critical decisions
- **RAG Integration** - Grounded decisions with document citations
- **Conflict Detection** - Automatic schedule and resource conflict detection

## 🚀 Deployment

### Frontend Deployment
The frontend can be deployed to:
- **Vercel** (recommended for Next.js)
- **Netlify**
- **AWS Amplify**

### Backend Deployment
The backend can be deployed to:
- **Railway**
- **Render**
- **Heroku**
- **AWS ECS**
- **Google Cloud Run**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [documentation](docs/)
- Review the [API specification](docs/API_SPEC.md)
- Open an issue on GitHub

---

**OrchestrateX** - Revolutionizing conference planning with AI-powered orchestration! 🚀
