// Core domain types for Conference Planning Crew

export interface User {
  id: string
  email: string
  name: string
  role: UserRole
  tenantId: string
  createdAt: string
  updatedAt: string
}

export type UserRole = 'admin' | 'producer' | 'coordinator' | 'finance' | 'sponsor_sales'

export interface Tenant {
  id: string
  name: string
  domain: string
  settings: TenantSettings
  createdAt: string
  updatedAt: string
}

export interface TenantSettings {
  timezone: string
  currency: string
  language: string
  features: string[]
}

export interface Event {
  id: string
  tenantId: string
  name: string
  description: string
  briefJson: EventBrief
  city: string
  venuePref: string
  startDate: string
  endDate: string
  status: EventStatus
  budget: Budget
  createdAt: string
  updatedAt: string
}

export interface EventBrief {
  targetAudience: string
  expectedAttendees: number
  theme: string
  objectives: string[]
  constraints: string[]
  preferences: Record<string, any>
}

export type EventStatus = 'planning' | 'active' | 'completed' | 'cancelled'

export interface Venue {
  id: string
  eventId: string
  name: string
  address: string
  capacity: number
  rooms: Room[]
  costCards: CostCard[]
  amenities: string[]
  contactInfo: ContactInfo
  createdAt: string
  updatedAt: string
}

export interface Room {
  id: string
  venueId: string
  name: string
  capacity: number
  features: string[]
  setupOptions: string[]
}

export interface CostCard {
  category: string
  items: CostItem[]
  total: number
  currency: string
}

export interface CostItem {
  name: string
  description: string
  quantity: number
  unitPrice: number
  total: number
}

export interface Speaker {
  id: string
  eventId: string
  name: string
  bio: string
  topics: string[]
  availability: Availability
  contractUri?: string
  travelRequirements: TravelRequirements
  createdAt: string
  updatedAt: string
}

export interface Availability {
  availableDates: string[]
  preferredTimes: string[]
  timezone: string
  constraints: string[]
}

export interface TravelRequirements {
  needsAccommodation: boolean
  needsTransportation: boolean
  dietaryRestrictions: string[]
  specialRequirements: string[]
}

export interface Sponsor {
  id: string
  eventId: string
  company: string
  tier: SponsorTier
  packages: SponsorPackage[]
  deliverables: Deliverable[]
  contractUri?: string
  invoices: Invoice[]
  contactInfo: ContactInfo
  createdAt: string
  updatedAt: string
}

export type SponsorTier = 'platinum' | 'gold' | 'silver' | 'bronze'

export interface SponsorPackage {
  name: string
  description: string
  value: number
  benefits: string[]
  inventory: number
  sold: number
}

export interface Deliverable {
  name: string
  description: string
  dueDate: string
  status: DeliverableStatus
  assignedTo: string
}

export type DeliverableStatus = 'pending' | 'in_progress' | 'completed' | 'overdue'

export interface Invoice {
  id: string
  sponsorId: string
  amount: number
  currency: string
  status: InvoiceStatus
  dueDate: string
  paidDate?: string
  createdAt: string
}

export type InvoiceStatus = 'draft' | 'sent' | 'paid' | 'overdue' | 'cancelled'

export interface Budget {
  total: number
  currency: string
  categories: BudgetCategory[]
  revenue: Revenue[]
  expenses: Expense[]
  createdAt: string
  updatedAt: string
}

export interface BudgetCategory {
  name: string
  allocated: number
  spent: number
  remaining: number
  percentage: number
}

export interface Revenue {
  id: string
  source: string
  amount: number
  expectedDate: string
  receivedDate?: string
  status: RevenueStatus
}

export type RevenueStatus = 'expected' | 'received' | 'overdue'

export interface Expense {
  id: string
  category: string
  description: string
  amount: number
  date: string
  status: ExpenseStatus
  approvedBy?: string
}

export type ExpenseStatus = 'pending' | 'approved' | 'paid' | 'rejected'

export interface Agent {
  id: string
  eventId: string
  type: AgentType
  status: AgentStatus
  currentTask: string
  progress: number
  decisions: AgentDecision[]
  createdAt: string
  updatedAt: string
}

export type AgentType = 
  | 'venue_scout'
  | 'speaker_outreach'
  | 'sponsorship_manager'
  | 'budget_controller'
  | 'marketing_ops'
  | 'attendee_experience'
  | 'logistics_travel'
  | 'risk_compliance'

export type AgentStatus = 'idle' | 'running' | 'waiting_approval' | 'completed' | 'error'

export interface AgentDecision {
  id: string
  agentId: string
  type: string
  description: string
  rationale: string
  citations: Citation[]
  costDelta: number
  risks: string[]
  status: DecisionStatus
  approvedBy?: string
  approvedAt?: string
  createdAt: string
}

export type DecisionStatus = 'pending' | 'approved' | 'rejected' | 'modified'

export interface Citation {
  source: string
  title: string
  url?: string
  excerpt: string
  relevance: string
}

export interface ContactInfo {
  name: string
  email: string
  phone?: string
  company?: string
  title?: string
}

export interface Task {
  id: string
  eventId: string
  title: string
  description: string
  assignedTo: string
  agent?: AgentType
  status: TaskStatus
  priority: TaskPriority
  dueDate: string
  dependencies: string[]
  notes: string[]
  createdAt: string
  updatedAt: string
}

export type TaskStatus = 'todo' | 'in_progress' | 'review' | 'completed' | 'cancelled'
export type TaskPriority = 'low' | 'medium' | 'high' | 'critical'

export interface AuditLog {
  id: string
  actor: string
  action: string
  targetType: string
  targetId: string
  before: Record<string, any>
  after: Record<string, any>
  timestamp: string
  ipAddress?: string
  userAgent?: string
}

// API Response types
export interface ApiResponse<T> {
  data: T
  message: string
  success: boolean
}

export interface PaginatedResponse<T> {
  data: T[]
  pagination: {
    page: number
    limit: number
    total: number
    totalPages: number
  }
}

export interface ErrorResponse {
  error: {
    code: string
    message: string
    details?: Record<string, any>
  }
}

// Form types
export interface CreateEventForm {
  name: string
  description: string
  city: string
  startDate: string
  endDate: string
  expectedAttendees: number
  budget: number
  brief: EventBrief
}

export interface UpdateEventForm extends Partial<CreateEventForm> {
  status?: EventStatus
}

// Filter and search types
export interface EventFilters {
  status?: EventStatus[]
  city?: string
  dateRange?: {
    start: string
    end: string
  }
  budgetRange?: {
    min: number
    max: number
  }
}

export interface SearchParams {
  query: string
  filters: EventFilters
  sortBy: string
  sortOrder: 'asc' | 'desc'
  page: number
  limit: number
}
