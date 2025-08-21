# OrchestrateX - Multi-Agent AI Conference Planning Platform

## 🚀 Overview

OrchestrateX is a revolutionary multi-agent AI platform that orchestrates specialized AI agents to plan and manage conferences from concept to completion. Built with modern technologies and enterprise-grade security, it provides a comprehensive solution for event planning automation.

## ✨ Key Features

### 🤖 AI Agent Orchestration
- **8 Specialized AI Agents**: Venue Scout, Speaker Outreach, Sponsorship Manager, Budget Controller, Marketing Ops, Attendee Experience, Logistics & Travel, Risk & Compliance
- **LangGraph Integration**: Advanced workflow orchestration and decision-making
- **Human-in-the-Loop**: Critical decisions require human approval
- **RAG-Powered**: Decisions grounded in documents, emails, and vendor data

### 🛡️ Enterprise Security & Compliance
- **GDPR Compliance**: Complete data subject rights implementation
- **Role-Based Access Control**: Multi-level permission system
- **JWT Authentication**: Secure token-based authentication
- **Data Protection**: Encryption, masking, and retention policies
- **Audit Logging**: Comprehensive activity tracking
- **Rate Limiting**: Protection against abuse and DDoS

### 🎨 Modern Frontend
- **Next.js 14**: App Router with React 18
- **TypeScript**: Full type safety
- **Tailwind CSS**: Modern, responsive design
- **shadcn/ui**: Beautiful, accessible components
- **Real-time Updates**: WebSocket integration
- **Mobile-First**: Responsive design for all devices

### ⚡ High-Performance Backend
- **FastAPI**: Modern, fast Python web framework
- **SQLAlchemy 2.0**: Async ORM with PostgreSQL
- **Redis**: Caching and session management
- **Celery**: Background task processing
- **Pydantic v2**: Data validation and serialization

## 🏗️ Architecture

### Frontend Architecture
```
src/
├── app/                    # Next.js App Router
│   ├── dashboard/         # Main dashboard
│   ├── events/           # Event management
│   ├── command/          # AI agent orchestration
│   ├── analytics/        # Data visualization
│   └── settings/         # User configuration
├── components/           # Reusable UI components
│   ├── ui/              # Base components (shadcn/ui)
│   └── specialized/     # Application-specific components
├── lib/                 # Utilities and helpers
└── types/               # TypeScript type definitions
```

### Backend Architecture
```
backend/
├── app/
│   ├── api/v1/          # REST API endpoints
│   ├── agents/          # AI agent implementations
│   ├── core/            # Core functionality
│   │   ├── security.py  # Authentication & authorization
│   │   ├── compliance.py # GDPR & compliance features
│   │   └── middleware.py # Security middleware
│   ├── models/          # SQLAlchemy models
│   └── schemas/         # Pydantic schemas
├── docs/                # Documentation
└── requirements.txt     # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- PostgreSQL 14+
- Redis 6+

### Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your configuration

# Run database migrations
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

### Environment Configuration
```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost/orchestratex

# Redis
REDIS_URL=redis://localhost:6379

# Security
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=["http://localhost:3000"]

# AI Services
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

## 🔧 Development

### Code Quality
```bash
# Frontend
npm run lint
npm run type-check

# Backend
black backend/
isort backend/
flake8 backend/
mypy backend/
```

### Testing
```bash
# Frontend
npm run test

# Backend
pytest backend/tests/
```

## 📚 Documentation

- **[API Documentation](docs/API_SPEC.md)**: Complete API reference
- **[Security Guide](docs/SECURITY.md)**: Security and compliance details
- **[Repository Map](docs/REPO_MAP.md)**: Project structure overview
- **[Claude Guidelines](docs/CLAUDE.md)**: AI collaboration guidelines

## 🔒 Security Features

### Authentication & Authorization
- JWT-based authentication with refresh tokens
- Role-based access control (Super Admin, Admin, Manager, User)
- Multi-tenant data isolation
- Secure password hashing with bcrypt

### Data Protection
- GDPR compliance with data subject rights
- Automatic data retention and cleanup
- Comprehensive audit logging
- Input sanitization and validation

### API Security
- Rate limiting (100 requests/minute per IP)
- Security headers (CSP, HSTS, XSS Protection)
- CORS configuration
- Request validation and sanitization

## 🤖 AI Agent System

### Specialized Agents
1. **Venue Scout**: Venue research and selection
2. **Speaker Outreach**: Speaker identification and recruitment
3. **Sponsorship Manager**: Sponsor relationship management
4. **Budget Controller**: Financial planning and optimization
5. **Marketing Ops**: Marketing strategy and campaigns
6. **Attendee Experience**: Attendee engagement and satisfaction
7. **Logistics & Travel**: Operational coordination
8. **Risk & Compliance**: Risk assessment and governance

### Workflow Features
- **LangGraph Orchestration**: Advanced workflow management
- **Human Approval**: Critical decision validation
- **RAG Integration**: Document-based decision making
- **Progress Tracking**: Real-time workflow monitoring
- **Activity Logging**: Comprehensive audit trails

## 🎯 Use Cases

### Conference Planning
- **Corporate Events**: Internal company conferences
- **Industry Conferences**: Professional association events
- **Academic Conferences**: Research and educational events
- **Trade Shows**: Commercial exhibitions and fairs

### Event Management
- **Venue Selection**: Automated venue research and comparison
- **Speaker Management**: Speaker identification and coordination
- **Sponsorship**: Revenue generation and sponsor relations
- **Budget Management**: Financial planning and optimization
- **Marketing**: Multi-channel marketing campaigns
- **Logistics**: Travel and operational coordination

## 🔄 Roadmap

### Phase 1: Core Platform ✅
- [x] Multi-agent AI system
- [x] Frontend dashboard
- [x] Backend API
- [x] Database models
- [x] Security & compliance

### Phase 2: Advanced Features
- [ ] Real-time collaboration
- [ ] Advanced analytics
- [ ] Mobile application
- [ ] Third-party integrations

### Phase 3: Enterprise Features
- [ ] Multi-tenant architecture
- [ ] Advanced reporting
- [ ] Custom workflows
- [ ] API marketplace

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/your-org/orchestratex/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/orchestratex/discussions)
- **Email**: support@orchestratex.com

## 🙏 Acknowledgments

- **LangChain**: AI agent framework
- **FastAPI**: Modern Python web framework
- **Next.js**: React framework
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: Beautiful UI components

---

**OrchestrateX** - Revolutionizing conference planning with AI-powered orchestration. 🚀
