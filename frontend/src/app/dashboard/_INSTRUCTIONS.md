# Dashboard Module - TODO

## Overview
The dashboard is the main hub for conference planning activities. It provides an overview of all events, agent status, and key metrics.

## Components to Implement

### 1. Dashboard Layout (`page.tsx`)
- Header with user profile and notifications
- Sidebar navigation to different event sections
- Main content area with overview cards
- Real-time updates via WebSocket

### 2. Overview Cards
- **Events Summary**: Total events, active events, completed events
- **Agent Status**: Number of active agents, pending approvals
- **Budget Overview**: Total budget, spent, remaining
- **Recent Activity**: Latest agent decisions and approvals

### 3. Quick Actions
- Create new event button
- View pending approvals
- Access command center
- Generate reports

### 4. Event List
- Table/grid of all events with status
- Filter by status, date range, agent
- Search functionality
- Quick actions per event

## Data Requirements
- Event data from `/api/v1/events/`
- Agent status from `/api/v1/agents/`
- User permissions and role-based access
- Real-time updates via WebSocket

## Styling Guidelines
- Use conference color palette (conference-600 for primary actions)
- Status chips for event states
- Responsive design for mobile/tablet
- Loading states and error handling

## TODO Checklist
- [ ] Create dashboard layout component
- [ ] Implement overview cards with mock data
- [ ] Add event list with filtering
- [ ] Integrate with API endpoints
- [ ] Add real-time updates
- [ ] Implement responsive design
- [ ] Add loading and error states
