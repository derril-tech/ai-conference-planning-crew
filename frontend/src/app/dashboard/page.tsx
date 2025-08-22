import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { MetricCard } from '@/components/ui/metric-card'

// Mock data for demonstration
const mockEvents = [
  {
    id: '1',
    name: 'Tech Conference 2024',
    status: 'planning' as const,
    startDate: '2024-06-15',
    venue: 'Convention Center',
    attendees: 500,
    budget: 75000
  },
  {
    id: '2',
    name: 'Marketing Summit',
    status: 'active' as const,
    startDate: '2024-04-20',
    venue: 'Grand Hotel',
    attendees: 300,
    budget: 45000
  },
  {
    id: '3',
    name: 'AI Workshop Series',
    status: 'completed' as const,
    startDate: '2024-02-10',
    venue: 'Innovation Hub',
    attendees: 150,
    budget: 25000
  }
]

const mockStats = {
  totalEvents: 12,
  activeEvents: 3,
  completedEvents: 8,
  pendingApprovals: 5,
  totalBudget: 450000,
  spentBudget: 320000
}

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <Link href="/" className="text-2xl font-bold text-conference-600">
                  OrchestrateX
                </Link>
              </div>
            </div>
            <nav className="hidden md:flex space-x-8">
              <Link href="/" className="text-gray-700 hover:text-conference-600">Home</Link>
              <Link href="/about" className="text-gray-700 hover:text-conference-600">About</Link>
              <Link href="/events" className="text-gray-700 hover:text-conference-600">Events</Link>
            </nav>
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-600">Welcome, Admin</span>
              <Button variant="outline" size="sm">
                Logout
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Page Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600 mt-2">Overview of your conference planning activities</p>
        </div>

                       {/* Stats Grid */}
               <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                 <MetricCard
                   title="Total Events"
                   value={mockStats.totalEvents}
                   description={`${mockStats.activeEvents} active, ${mockStats.completedEvents} completed`}
                   icon="📅"
                 />
                 <MetricCard
                   title="Pending Approvals"
                   value={mockStats.pendingApprovals}
                   description="Require human review"
                   icon="⏳"
                 />
                 <MetricCard
                   title="Total Budget"
                   value={`$${(mockStats.totalBudget / 1000).toFixed(0)}k`}
                   description={`$${(mockStats.spentBudget / 1000).toFixed(0)}k spent`}
                   icon="💰"
                 />
                 <MetricCard
                   title="AI Agents Active"
                   value="8"
                   description="All agents operational"
                   icon="🤖"
                 />
               </div>

        {/* Quick Actions */}
        <div className="mb-8">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
          <div className="flex flex-wrap gap-4">
            <Button className="bg-conference-600 hover:bg-conference-700">
              Create New Event
            </Button>
            <Button variant="outline">
              View Pending Approvals
            </Button>
            <Button variant="outline">
              Generate Reports
            </Button>
            <Button variant="outline">
              Access Command Center
            </Button>
          </div>
        </div>

        {/* Recent Events */}
        <div className="mb-8">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-semibold text-gray-900">Recent Events</h2>
            <Link href="/events" className="text-conference-600 hover:text-conference-700 text-sm">
              View All Events →
            </Link>
          </div>
          <div className="grid gap-4">
            {mockEvents.map((event) => (
              <Card key={event.id} className="hover:shadow-md transition-shadow">
                <CardContent className="p-6">
                  <div className="flex items-center justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="text-lg font-semibold">{event.name}</h3>
                        <span className={`status-chip status-${event.status}`}>
                          {event.status}
                        </span>
                      </div>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm text-gray-600">
                        <div>
                          <span className="font-medium">Start Date:</span> {new Date(event.startDate).toLocaleDateString()}
                        </div>
                        <div>
                          <span className="font-medium">Venue:</span> {event.venue}
                        </div>
                        <div>
                          <span className="font-medium">Attendees:</span> {event.attendees}
                        </div>
                        <div>
                          <span className="font-medium">Budget:</span> ${(event.budget / 1000).toFixed(0)}k
                        </div>
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <Button variant="outline" size="sm">
                        View Details
                      </Button>
                      <Button variant="outline" size="sm">
                        Edit
                      </Button>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

        {/* Recent Activity */}
        <div>
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Activity</h2>
          <Card>
            <CardContent className="p-6">
              <div className="space-y-4">
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-conference-600 rounded-full"></div>
                  <span className="text-sm text-gray-600">
                    <strong>Venue Scout Agent</strong> found 3 new venue options for Tech Conference 2024
                  </span>
                  <span className="text-xs text-gray-400 ml-auto">2 hours ago</span>
                </div>
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-warning-600 rounded-full"></div>
                  <span className="text-sm text-gray-600">
                    <strong>Speaker Outreach Agent</strong> needs approval for speaker lineup
                  </span>
                  <span className="text-xs text-gray-400 ml-auto">4 hours ago</span>
                </div>
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-success-600 rounded-full"></div>
                  <span className="text-sm text-gray-600">
                    <strong>Budget Controller</strong> completed budget optimization for Marketing Summit
                  </span>
                  <span className="text-xs text-gray-400 ml-auto">1 day ago</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  )
}
