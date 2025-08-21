import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { EventCard } from '@/components/ui/event-card'
import { mockEvents } from '@/lib/mock-data'

export default function EventsPage() {
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

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Page Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Events</h1>
            <p className="text-gray-600 mt-2">Manage your conference planning projects</p>
          </div>
          <Button className="bg-conference-600 hover:bg-conference-700">
            Create New Event
          </Button>
        </div>

        {/* Filters and Search */}
        <div className="bg-white rounded-lg shadow-sm border p-6 mb-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Status</label>
              <select className="w-full border border-gray-300 rounded-md px-3 py-2">
                <option value="">All Status</option>
                <option value="planning">Planning</option>
                <option value="active">Active</option>
                <option value="completed">Completed</option>
                <option value="cancelled">Cancelled</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">City</label>
              <input 
                type="text" 
                placeholder="Filter by city"
                className="w-full border border-gray-300 rounded-md px-3 py-2"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Date Range</label>
              <input 
                type="date" 
                className="w-full border border-gray-300 rounded-md px-3 py-2"
              />
            </div>
            <div className="flex items-end">
              <Button variant="outline" className="w-full">
                Search
              </Button>
            </div>
          </div>
        </div>

                       {/* Events Grid */}
               <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                 {mockEvents.map((event) => (
                   <EventCard
                     key={event.id}
                     event={event}
                     onViewDetails={(id) => window.location.href = `/events/${id}/timeline`}
                     onEdit={(id) => console.log('Edit event:', id)}
                   />
                 ))}
               </div>

        {/* Empty State */}
        {mockEvents.length === 0 && (
          <div className="text-center py-12">
            <div className="w-16 h-16 bg-conference-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-conference-600 text-2xl">📅</span>
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">No events yet</h3>
            <p className="text-gray-600 mb-6">Create your first conference planning project to get started.</p>
            <Button className="bg-conference-600 hover:bg-conference-700">
              Create Your First Event
            </Button>
          </div>
        )}
      </main>
    </div>
  )
}
