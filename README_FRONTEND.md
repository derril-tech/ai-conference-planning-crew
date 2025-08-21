# Frontend - Conference Planning Crew

## Overview

The frontend is a Next.js 14 application built with React 18, TypeScript, and Tailwind CSS. It provides a modern, responsive interface for managing conference planning workflows with AI agent orchestration.

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui components
- **State Management**: Zustand + React Query
- **Forms**: React Hook Form + Zod validation
- **Charts**: Recharts
- **Real-time**: Socket.IO Client
- **Drag & Drop**: React Beautiful DnD

## Project Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx         # Root layout with providers
│   ├── page.tsx           # Landing page
│   ├── about/             # About page
│   ├── dashboard/         # Main dashboard
│   ├── events/            # Event management (TODO)
│   ├── login/             # Authentication (TODO)
│   └── globals.css        # Global styles
├── components/            # Reusable React components
│   ├── ui/               # Base UI components (shadcn/ui)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   └── ...           # More UI components
│   ├── providers.tsx     # Context providers
│   └── ...               # Feature-specific components
├── lib/                  # Utility functions and helpers
│   ├── utils.ts          # Common utilities
│   └── mock-data.ts      # Mock data for development
├── types/                # TypeScript type definitions
│   └── index.ts          # Domain types and interfaces
├── hooks/                # Custom React hooks (TODO)
├── store/                # Zustand stores (TODO)
└── utils/                # Additional utilities (TODO)
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Backend API running (see README_BACKEND.md)

### Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Set up environment variables**:
   ```bash
   cp env.example .env.local
   ```
   
   Edit `.env.local` with your configuration:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   NEXT_PUBLIC_WS_URL=ws://localhost:8000
   ```

3. **Start development server**:
   ```bash
   npm run dev
   ```

The application will be available at `http://localhost:3000`

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript check

## Development Guidelines

### Component Structure

Components follow a hierarchical structure:

1. **UI Components** (`src/components/ui/`) - Base components from shadcn/ui
2. **Feature Components** (`src/components/`) - Business logic components
3. **Page Components** (`src/app/`) - Next.js pages

### Styling

- Use Tailwind CSS classes for styling
- Follow the conference color palette:
  - Primary: `conference-600` (#0ea5e9)
  - Success: `success-500` (#22c55e)
  - Warning: `warning-500` (#f59e0b)
  - Danger: `danger-500` (#ef4444)

### State Management

- **Local State**: React useState/useReducer
- **Server State**: React Query for API data
- **Global State**: Zustand for app-wide state
- **Form State**: React Hook Form

### TypeScript

- All components must be typed
- Use interfaces from `src/types/index.ts`
- Avoid `any` types - use proper typing

### API Integration

- API calls use React Query for caching and state management
- Base URL configured in environment variables
- Error handling with proper user feedback

## Key Features

### 1. Dashboard
- Overview of all events and agent status
- Quick actions and recent activity
- Real-time updates via WebSocket

### 2. Event Management
- Create and manage events
- View event details and progress
- Agent timeline and decision tracking

### 3. AI Agent Interface
- Monitor agent status and progress
- Review and approve agent decisions
- Human-in-the-loop workflow

### 4. Real-time Updates
- WebSocket integration for live updates
- Agent status changes
- Approval notifications

## Design System

### Color Palette
```css
/* Conference Blue */
conference-50: #f0f9ff
conference-600: #0ea5e9
conference-900: #0c4a6e

/* Status Colors */
success-500: #22c55e
warning-500: #f59e0b
danger-500: #ef4444
```

### Components
- **Button**: Multiple variants (default, outline, secondary, etc.)
- **Card**: Content containers with header, content, footer
- **Status Chips**: For event and task status
- **Forms**: Consistent form styling and validation

### Responsive Design
- Mobile-first approach
- Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)
- Flexible layouts that adapt to screen size

## Testing

### Unit Tests
```bash
npm run test
```

### E2E Tests
```bash
npm run test:e2e
```

## Performance

### Optimization
- Next.js Image component for optimized images
- Code splitting with dynamic imports
- React Query for efficient data fetching
- Tailwind CSS purging for smaller bundle size

### Monitoring
- Core Web Vitals tracking
- Performance budgets
- Bundle size monitoring

## Deployment

### Vercel (Recommended)
1. Connect repository to Vercel
2. Set environment variables
3. Deploy automatically on push to main

### Other Platforms
- Build: `npm run build`
- Start: `npm run start`
- Set environment variables for production

## Troubleshooting

### Common Issues

1. **Build Errors**
   - Check TypeScript errors: `npm run type-check`
   - Verify all imports are correct

2. **API Connection**
   - Ensure backend is running
   - Check `NEXT_PUBLIC_API_URL` in environment

3. **Styling Issues**
   - Verify Tailwind CSS is properly configured
   - Check for conflicting CSS

### Development Tips

- Use React DevTools for debugging
- Enable TypeScript strict mode
- Follow ESLint rules
- Use Prettier for code formatting

## Contributing

1. Follow the established code style
2. Add TypeScript types for new features
3. Include proper error handling
4. Test on multiple screen sizes
5. Update documentation as needed

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [shadcn/ui](https://ui.shadcn.com/)
- [React Query](https://tanstack.com/query/latest)
- [Zustand](https://github.com/pmndrs/zustand)
