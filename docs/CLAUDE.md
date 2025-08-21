# CLAUDE.md — Collaboration & Editing Guidelines

This document is Claude's onboarding guide for the Conference Planning Crew project.  
It defines the **purpose of the project, coding conventions, editing rules, and collaboration workflow**.  
Claude should always respect these boundaries when generating code.

---

## 📌 Project Overview
- **Name:** Conference Planning Crew (OrchestrateX)
- **Purpose:** Multi-agent AI conference planning platform that coordinates specialized AI agents to design, staff, budget, schedule, promote, and run conferences end-to-end with human-in-the-loop approvals and complete audit trails.
- **Target Users:** Event planners, conference organizers, corporate event managers, venues, sponsors
- **Goals:** Automate conference planning workflows, provide human oversight, enable real-time collaboration, generate comprehensive audit trails
- **Tech Stack:**  
  - Frontend: Next.js 14 + React 18 + TypeScript + Tailwind CSS + shadcn/ui
  - Backend: FastAPI + SQLAlchemy 2.0 + Pydantic v2 + PostgreSQL + Redis
  - AI: LangGraph + LangChain + OpenAI + Claude
  - Services: Stripe, SendGrid, Twilio, Google/Microsoft APIs

---

## 📂 Folder & File Structure
- **src/** → Frontend code (Next.js App Router, React components, utilities)
- **backend/** → API, models, services, database, AI agents
- **docs/** → Specs (`REPO_MAP.md`, `API_SPEC.md`, `PROMPT_DECLARATION`, `CLAUDE.md`)

### Editable by Claude
- `src/**/*` (except `_INSTRUCTIONS.md`)  
- `backend/app/**/*` (except migrations unless asked)  
- Tests in `src/__tests__/` and `backend/tests/`  

### Do Not Touch
- Lockfiles (`package-lock.json`, `poetry.lock`, etc.)  
- Configuration files (`package.json`, `next.config.js`, `tailwind.config.js`, etc.)
- Documentation files (`docs/*`, `README.md`, `PROJECT_BRIEF`)
- This file (`CLAUDE.md`)  

---

## 🎨 Coding Conventions
- **Languages:** TypeScript (frontend), Python (backend)  
- **Style Guides:**  
  - Frontend: ESLint + Prettier (Next.js defaults)
  - Backend: Black + isort + flake8 (PEP8)  
- **Naming:**  
  - Components: `PascalCase`  
  - Variables: `camelCase` (TS), `snake_case` (Python)  
  - Files: `kebab-case` for pages, `PascalCase` for components
- **Commenting:**  
  - Document public components, functions, and non-obvious logic  
  - Use `// TODO:` or `# TODO:` for clear tasks  
  - Add JSDoc comments for complex functions

---

## 🎨 Design System
- **Color Palette:** Conference Blue (`conference-600`), Success Green, Warning Orange, Danger Red
- **Components:** shadcn/ui base components with custom variants
- **Typography:** Inter font family
- **Spacing:** Tailwind CSS spacing scale
- **Responsive:** Mobile-first design approach
- **Accessibility:** WCAG 2.1 AA compliance

---

## 🤝 AI Collaboration Rules
- Always respond with **full file rewrites** if >30 lines are changed.  
- Keep responses **concise in explanation, complete in code**.  
- Never remove error handling, logging, or comments unless replacing them with better versions.  
- Preserve imports and typing.  
- If ambiguity arises:  
  1. Ask up to **2 clarifying questions**  
  2. If unanswered, proceed with best guess and note assumptions
- **Always include proper TypeScript types and Python type hints**
- **Implement proper error handling and loading states**

---

## ✍️ Editing Rules
- **Editable Files:** All app source code under `src/` and `backend/app/`  
- **Avoid:** configuration files, documentation, auto-generated files
- **Format of Responses:**  
  - Full file rewrites for large changes  
  - Patches (with clear diff context) for small fixes  
- **Error Handling:** must remain in place at all times  
- **TypeScript:** Always use proper types, avoid `any`
- **Python:** Use type hints, async/await patterns

---

## 📦 Project Dependencies
- **Frontend:** Next.js 14, React 18, TypeScript, Tailwind CSS, shadcn/ui, React Query, Zustand
- **Backend:** FastAPI, SQLAlchemy 2.0, Pydantic v2, PostgreSQL, Redis, LangGraph, LangChain
- **AI Services:** OpenAI, Claude, pgvector
- **External APIs:** Stripe, SendGrid, Twilio, Google Calendar, Microsoft Graph
- **Environment:**  
  - Variables in `env.example` must be respected  
  - Secrets should never be hardcoded  

---

## 🛠️ Workflow & Tools
- **Run locally:**  
  - Frontend: `npm run dev`  
  - Backend: `uvicorn backend.app.main:app --reload`  
- **FE ↔ BE boundary:** REST JSON via `/api/v1/*`  
- **Testing:**  
  - Frontend: Jest + React Testing Library
  - Backend: Pytest + pytest-asyncio
- **Database:** PostgreSQL with pgvector extension
- **Deployment:** Vercel (FE) + Render/DigitalOcean (BE)

---

## 📚 Contextual Knowledge

### Conference Planning Domain
- **Events:** Have phases (planning, active, completed), require venues, speakers, sponsors
- **Venues:** Need capacity, amenities, cost analysis, room configurations
- **Speakers:** Require bios, availability, contracts, travel arrangements
- **Sponsors:** Have tiers (platinum, gold, silver, bronze), packages, deliverables
- **Budget:** Track revenue vs expenses, optimize allocation
- **Logistics:** Staffing, vendors, materials, travel coordination

### AI Agent Workflows
- **8 Specialized Agents:** Venue Scout, Speaker Outreach, Sponsorship Manager, Budget Controller, Marketing Ops, Attendee Experience, Logistics & Travel, Risk & Compliance
- **LangGraph Orchestration:** Parallel execution with dependencies
- **Human-in-the-Loop:** Approval gates for critical decisions
- **Structured Outputs:** All decisions include rationale, citations, cost impact
- **Real-time Updates:** WebSocket connections for live status

### Business Rules
- **Multi-tenant:** Role-based access control (admin, producer, coordinator, finance, sponsor_sales)
- **Audit Trail:** All actions and decisions logged with timestamps
- **GDPR Compliance:** Attendee data protection and consent management
- **PCI Compliance:** Secure payment processing via Stripe
- **Data Retention:** Configurable retention policies

---

## ✅ Examples

**Good Answer Example**
```tsx
// Good: Full file rewrite, proper types, error handling, loading states
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface Event {
  id: string;
  name: string;
  status: 'planning' | 'active' | 'completed';
  startDate: string;
  venue?: string;
}

interface EventListProps {
  onEventSelect: (eventId: string) => void;
}

export default function EventList({ onEventSelect }: EventListProps) {
  const [events, setEvents] = useState<Event[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await fetch('/api/v1/events/');
        if (!response.ok) throw new Error('Failed to fetch events');
        const data = await response.json();
        setEvents(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    fetchEvents();
  }, []);

  if (loading) return <div className="flex justify-center p-8">Loading events...</div>;
  if (error) return <div className="text-red-600 p-4">Error: {error}</div>;

  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
      {events.map((event) => (
        <Card key={event.id} className="hover:shadow-md transition-shadow">
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <span>{event.name}</span>
              <span className={`status-chip status-${event.status}`}>
                {event.status}
              </span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-gray-600 mb-4">
              Start Date: {new Date(event.startDate).toLocaleDateString()}
            </p>
            {event.venue && (
              <p className="text-sm text-gray-600 mb-4">Venue: {event.venue}</p>
            )}
            <Button 
              onClick={() => onEventSelect(event.id)}
              className="w-full bg-conference-600 hover:bg-conference-700"
            >
              View Details
            </Button>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
```

**Bad Answer Example**
```tsx
// Bad: No types, no error handling, no loading states, poor styling
function EventList(props) {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('/api/v1/events/')
      .then(res => res.json())
      .then(setEvents);
  }, []);

  return (
    <div>
      {events.map(event => (
        <div key={event.id}>
          <h3>{event.name}</h3>
          <button onClick={() => props.onEventSelect(event.id)}>
            View
          </button>
        </div>
      ))}
    </div>
  );
}
```

---

## 🔧 Development Guidelines

### Frontend Development
- Use Next.js 14 App Router patterns
- Implement responsive design with Tailwind CSS
- Add proper loading and error states
- Use React Query for data fetching
- Implement proper TypeScript types
- Follow accessibility guidelines

### Backend Development
- Use FastAPI async/await patterns
- Implement proper Pydantic validation
- Use SQLAlchemy 2.0 async ORM
- Add comprehensive error handling
- Include proper authentication/authorization
- Add audit logging for all actions

### AI Agent Development
- Define clear agent responsibilities
- Implement structured outputs with citations
- Add human approval gates
- Include comprehensive logging
- Test with various scenarios
- Ensure deterministic behavior

---

## 🚀 Next Steps
1. Implement database models and migrations
2. Create AI agent implementations
3. Build frontend dashboard and event management
4. Add real-time WebSocket updates
5. Implement external API integrations
6. Add comprehensive testing
7. Deploy to production environment


