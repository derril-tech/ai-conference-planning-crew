import { Event, Venue, Speaker, Sponsor, Agent, Task, User } from '@/types'

// Mock Users
export const mockUsers: User[] = [
  {
    id: '1',
    email: 'admin@orchestratex.com',
    name: 'Admin User',
    role: 'admin',
    tenantId: '1',
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  },
  {
    id: '2',
    email: 'producer@orchestratex.com',
    name: 'Event Producer',
    role: 'producer',
    tenantId: '1',
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  }
]

// Mock Events
export const mockEvents: Event[] = [
  {
    id: '1',
    tenantId: '1',
    name: 'Tech Conference 2024',
    description: 'Annual technology conference featuring the latest innovations in AI, cloud computing, and cybersecurity.',
    briefJson: {
      targetAudience: 'Technology professionals, developers, and IT decision makers',
      expectedAttendees: 500,
      theme: 'Innovation and Future of Technology',
      objectives: ['Networking opportunities', 'Knowledge sharing', 'Industry insights'],
      constraints: ['Budget limit of $75,000', 'Must be in San Francisco'],
      preferences: {
        venueType: 'conference center',
        catering: 'required',
        parking: 'preferred'
      }
    },
    city: 'San Francisco',
    venuePref: 'Modern conference center with AV capabilities',
    startDate: '2024-06-15T09:00:00Z',
    endDate: '2024-06-17T18:00:00Z',
    status: 'planning',
    budget: {
      total: 75000,
      currency: 'USD',
      categories: [
        { name: 'Venue', allocated: 25000, spent: 0, remaining: 25000, percentage: 33 },
        { name: 'Catering', allocated: 15000, spent: 0, remaining: 15000, percentage: 20 },
        { name: 'Speakers', allocated: 20000, spent: 0, remaining: 20000, percentage: 27 },
        { name: 'Marketing', allocated: 10000, spent: 0, remaining: 10000, percentage: 13 },
        { name: 'Logistics', allocated: 5000, spent: 0, remaining: 5000, percentage: 7 }
      ],
      revenue: [],
      expenses: [],
      createdAt: '2024-01-01T00:00:00Z',
      updatedAt: '2024-01-01T00:00:00Z'
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  },
  {
    id: '2',
    tenantId: '1',
    name: 'Marketing Summit',
    description: 'B2B marketing conference focused on digital transformation and customer experience.',
    briefJson: {
      targetAudience: 'Marketing professionals and business leaders',
      expectedAttendees: 300,
      theme: 'Digital Marketing Excellence',
      objectives: ['Skill development', 'Industry trends', 'Networking'],
      constraints: ['Budget limit of $45,000', 'Must be in New York'],
      preferences: {
        venueType: 'hotel conference center',
        catering: 'required',
        networking: 'preferred'
      }
    },
    city: 'New York',
    venuePref: 'Upscale hotel with conference facilities',
    startDate: '2024-04-20T09:00:00Z',
    endDate: '2024-04-22T17:00:00Z',
    status: 'active',
    budget: {
      total: 45000,
      currency: 'USD',
      categories: [
        { name: 'Venue', allocated: 18000, spent: 18000, remaining: 0, percentage: 40 },
        { name: 'Catering', allocated: 9000, spent: 9000, remaining: 0, percentage: 20 },
        { name: 'Speakers', allocated: 13500, spent: 13500, remaining: 0, percentage: 30 },
        { name: 'Marketing', allocated: 4500, spent: 4500, remaining: 0, percentage: 10 }
      ],
      revenue: [
        {
          id: '1',
          source: 'Ticket Sales',
          amount: 30000,
          expectedDate: '2024-04-01T00:00:00Z',
          receivedDate: '2024-03-15T00:00:00Z',
          status: 'received'
        }
      ],
      expenses: [
        {
          id: '1',
          category: 'Venue',
          description: 'Conference center rental',
          amount: 18000,
          date: '2024-03-01T00:00:00Z',
          status: 'paid',
          approvedBy: '1'
        }
      ],
      createdAt: '2024-01-01T00:00:00Z',
      updatedAt: '2024-01-01T00:00:00Z'
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  }
]

// Mock Venues
export const mockVenues: Venue[] = [
  {
    id: '1',
    eventId: '1',
    name: 'San Francisco Convention Center',
    address: '123 Main St, San Francisco, CA 94105',
    capacity: 800,
    rooms: [
      {
        id: '1',
        venueId: '1',
        name: 'Grand Ballroom',
        capacity: 500,
        features: ['AV System', 'WiFi', 'Podium'],
        setupOptions: ['Theater', 'Classroom', 'Banquet']
      },
      {
        id: '2',
        venueId: '1',
        name: 'Conference Room A',
        capacity: 100,
        features: ['AV System', 'WiFi'],
        setupOptions: ['Theater', 'Classroom']
      }
    ],
    costCards: [
      {
        category: 'Venue Rental',
        items: [
          {
            name: 'Grand Ballroom (3 days)',
            description: 'Main conference space',
            quantity: 3,
            unitPrice: 5000,
            total: 15000
          },
          {
            name: 'Conference Room A (3 days)',
            description: 'Breakout sessions',
            quantity: 3,
            unitPrice: 2000,
            total: 6000
          }
        ],
        total: 21000,
        currency: 'USD'
      }
    ],
    amenities: ['WiFi', 'AV Equipment', 'Catering Kitchen', 'Parking'],
    contactInfo: {
      name: 'John Smith',
      email: 'john@sfconvention.com',
      phone: '+1-555-0123',
      company: 'SF Convention Center',
      title: 'Sales Manager'
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  }
]

// Mock Speakers
export const mockSpeakers: Speaker[] = [
  {
    id: '1',
    eventId: '1',
    name: 'Dr. Sarah Johnson',
    bio: 'Leading AI researcher with 15+ years experience in machine learning and artificial intelligence.',
    topics: ['Artificial Intelligence', 'Machine Learning', 'Ethics in AI'],
    availability: {
      availableDates: ['2024-06-15', '2024-06-16', '2024-06-17'],
      preferredTimes: ['10:00 AM', '2:00 PM'],
      timezone: 'PST',
      constraints: ['No early morning sessions']
    },
    contractUri: 'https://example.com/contracts/sarah-johnson.pdf',
    travelRequirements: {
      needsAccommodation: true,
      needsTransportation: false,
      dietaryRestrictions: ['Vegetarian'],
      specialRequirements: ['Podium with microphone']
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  },
  {
    id: '2',
    eventId: '1',
    name: 'Michael Chen',
    bio: 'Cloud computing expert and CTO at TechCorp, specializing in scalable infrastructure solutions.',
    topics: ['Cloud Computing', 'DevOps', 'Scalability'],
    availability: {
      availableDates: ['2024-06-15', '2024-06-16'],
      preferredTimes: ['11:00 AM', '3:00 PM'],
      timezone: 'PST',
      constraints: []
    },
    contractUri: 'https://example.com/contracts/michael-chen.pdf',
    travelRequirements: {
      needsAccommodation: false,
      needsTransportation: false,
      dietaryRestrictions: [],
      specialRequirements: ['Projector for demos']
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  }
]

// Mock Sponsors
export const mockSponsors: Sponsor[] = [
  {
    id: '1',
    eventId: '1',
    company: 'TechCorp',
    tier: 'platinum',
    packages: [
      {
        name: 'Platinum Package',
        description: 'Premium sponsorship with maximum visibility',
        value: 25000,
        benefits: [
          'Keynote speaking opportunity',
          'Exhibition booth',
          'Logo on all materials',
          'VIP dinner invitation'
        ],
        inventory: 1,
        sold: 1
      }
    ],
    deliverables: [
      {
        name: 'Logo placement',
        description: 'Place TechCorp logo on all conference materials',
        dueDate: '2024-05-15T00:00:00Z',
        status: 'completed',
        assignedTo: '2'
      }
    ],
    contractUri: 'https://example.com/contracts/techcorp.pdf',
    invoices: [
      {
        id: '1',
        sponsorId: '1',
        amount: 25000,
        currency: 'USD',
        status: 'paid',
        dueDate: '2024-03-01T00:00:00Z',
        paidDate: '2024-02-15T00:00:00Z',
        createdAt: '2024-01-01T00:00:00Z'
      }
    ],
    contactInfo: {
      name: 'Lisa Rodriguez',
      email: 'lisa@techcorp.com',
      phone: '+1-555-0456',
      company: 'TechCorp',
      title: 'Marketing Director'
    },
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-01T00:00:00Z'
  }
]

// Mock Agents
export const mockAgents: Agent[] = [
  {
    id: '1',
    eventId: '1',
    type: 'venue_scout',
    status: 'completed',
    currentTask: 'Venue selection completed',
    progress: 100,
    decisions: [
      {
        id: '1',
        agentId: '1',
        type: 'venue_selection',
        description: 'Selected San Francisco Convention Center as primary venue',
        rationale: 'Best fit for capacity, location, and budget requirements',
        citations: [
          {
            source: 'Venue Database',
            title: 'SF Convention Center Profile',
            url: 'https://example.com/venue/sfcc',
            excerpt: 'Modern facility with 800-person capacity',
            relevance: 'Capacity and amenities match requirements'
          }
        ],
        costDelta: 21000,
        risks: ['Limited availability in June'],
        status: 'approved',
        approvedBy: '1',
        approvedAt: '2024-01-15T00:00:00Z',
        createdAt: '2024-01-10T00:00:00Z'
      }
    ],
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-15T00:00:00Z'
  },
  {
    id: '2',
    eventId: '1',
    type: 'speaker_outreach',
    status: 'waiting_approval',
    currentTask: 'Speaker lineup proposal',
    progress: 75,
    decisions: [
      {
        id: '2',
        agentId: '2',
        type: 'speaker_selection',
        description: 'Proposed speaker lineup with 8 confirmed speakers',
        rationale: 'Diverse expertise covering all major conference topics',
        citations: [
          {
            source: 'Speaker Database',
            title: 'Speaker Profiles and Availability',
            url: 'https://example.com/speakers',
            excerpt: 'Confirmed availability and topic expertise',
            relevance: 'Speakers match conference theme and objectives'
          }
        ],
        costDelta: 15000,
        risks: ['Some speakers may have scheduling conflicts'],
        status: 'pending',
        createdAt: '2024-01-20T00:00:00Z'
      }
    ],
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-20T00:00:00Z'
  }
]

// Mock Tasks
export const mockTasks: Task[] = [
  {
    id: '1',
    eventId: '1',
    title: 'Review venue contracts',
    description: 'Review and approve venue rental contracts for SF Convention Center',
    assignedTo: '1',
    agent: 'venue_scout',
    status: 'completed',
    priority: 'high',
    dueDate: '2024-01-20T00:00:00Z',
    dependencies: [],
    notes: ['Contract reviewed and approved', 'Deposit paid'],
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-15T00:00:00Z'
  },
  {
    id: '2',
    eventId: '1',
    title: 'Approve speaker lineup',
    description: 'Review and approve proposed speaker lineup for Tech Conference 2024',
    assignedTo: '1',
    agent: 'speaker_outreach',
    status: 'review',
    priority: 'high',
    dueDate: '2024-01-25T00:00:00Z',
    dependencies: ['1'],
    notes: ['Waiting for final speaker confirmations'],
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-20T00:00:00Z'
  },
  {
    id: '3',
    eventId: '1',
    title: 'Design marketing materials',
    description: 'Create marketing materials including website, social media, and email campaigns',
    assignedTo: '2',
    agent: 'marketing_ops',
    status: 'in_progress',
    priority: 'medium',
    dueDate: '2024-02-15T00:00:00Z',
    dependencies: ['2'],
    notes: ['Website design in progress', 'Social media strategy approved'],
    createdAt: '2024-01-01T00:00:00Z',
    updatedAt: '2024-01-20T00:00:00Z'
  }
]

// Mock data for charts and analytics
export const mockAnalytics = {
  eventProgress: {
    labels: ['Venue', 'Speakers', 'Sponsors', 'Marketing', 'Logistics'],
    data: [100, 75, 60, 40, 20]
  },
  budgetUtilization: {
    labels: ['Venue', 'Catering', 'Speakers', 'Marketing', 'Logistics'],
    data: [28, 20, 27, 13, 12]
  },
  monthlyEvents: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    data: [2, 3, 4, 2, 5, 3]
  }
}

// Mock notifications
export const mockNotifications = [
  {
    id: '1',
    type: 'approval_required',
    title: 'Speaker lineup approval needed',
    message: 'The Speaker Outreach Agent has proposed a lineup for Tech Conference 2024',
    timestamp: '2024-01-20T10:30:00Z',
    read: false,
    actionUrl: '/events/1/speakers'
  },
  {
    id: '2',
    type: 'task_completed',
    title: 'Venue contract signed',
    message: 'Venue Scout Agent has successfully secured the SF Convention Center',
    timestamp: '2024-01-15T14:20:00Z',
    read: true,
    actionUrl: '/events/1/venues'
  },
  {
    id: '3',
    type: 'budget_alert',
    title: 'Budget threshold reached',
    message: 'Marketing budget has reached 80% of allocated amount',
    timestamp: '2024-01-18T09:15:00Z',
    read: false,
    actionUrl: '/events/1/budget'
  }
]
