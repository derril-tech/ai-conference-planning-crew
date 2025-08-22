import Link from 'next/link'
import { Button } from '@/components/ui/button'

interface EventLayoutProps {
  children: React.ReactNode
  params: { id: string }
}

const eventNavItems = [
  { href: 'timeline', label: 'Timeline', icon: '📊' },
  { href: 'venues', label: 'Venues', icon: '🏢' },
  { href: 'schedule', label: 'Schedule', icon: '📅' },
  { href: 'speakers', label: 'Speakers', icon: '🎤' },
  { href: 'sponsors', label: 'Sponsors', icon: '💼' },
  { href: 'budget', label: 'Budget', icon: '💰' },
  { href: 'registration', label: 'Registration', icon: '🎫' },
  { href: 'command', label: 'Command Center', icon: '🎮' },
]

export default function EventLayout({ children, params }: EventLayoutProps) {
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
              <Link href="/events" className="text-gray-700 hover:text-conference-600">Events</Link>
              <Link href="/dashboard" className="text-gray-700 hover:text-conference-600">Dashboard</Link>
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

      {/* Event Navigation */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between py-4">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Tech Conference 2024</h1>
              <p className="text-gray-600">Event ID: {params.id}</p>
            </div>
            <div className="flex items-center space-x-4">
              <span className="status-chip status-planning">Planning</span>
              <Button variant="outline" size="sm">
                Edit Event
              </Button>
            </div>
          </div>
          
          {/* Navigation Tabs */}
          <nav className="flex space-x-8 overflow-x-auto">
            {eventNavItems.map((item) => (
              <Link
                key={item.href}
                href={`/events/${params.id}/${item.href}`}
                className="flex items-center space-x-2 py-4 px-1 border-b-2 border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300 whitespace-nowrap"
              >
                <span>{item.icon}</span>
                <span className="text-sm font-medium">{item.label}</span>
              </Link>
            ))}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  )
}
