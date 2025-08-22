import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { AgentCard } from '@/components/ui/agent-card'
import { ActivityFeed } from '@/components/ui/activity-feed'
import { MetricCard } from '@/components/ui/metric-card'
import { mockAgents } from '@/lib/mock-data'

export default function CommandCenterPage() {
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

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Page Header */}
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Command Center</h1>
            <p className="text-gray-600 mt-2">Monitor and control AI agent workflows in real-time</p>
          </div>
          <div className="flex space-x-4">
            <Button variant="outline">
              View Logs
            </Button>
            <Button className="bg-conference-600 hover:bg-conference-700">
              Start New Workflow
            </Button>
          </div>
        </div>

                 {/* System Status */}
         <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
           <MetricCard
             title="Active Agents"
             value="8"
             description="All agents operational"
             icon="🤖"
           />
           <MetricCard
             title="Pending Decisions"
             value="3"
             description="Require human review"
             icon="⏳"
           />
           <MetricCard
             title="Active Workflows"
             value="5"
             description="Running concurrently"
             icon="🔄"
           />
           <MetricCard
             title="System Health"
             value="98%"
             description="Optimal performance"
             icon="💚"
           />
         </div>

                 {/* Agent Grid */}
         <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
           {mockAgents.map((agent) => (
             <AgentCard
               key={agent.id}
               agent={agent}
               onViewDetails={(id) => console.log('View agent details:', id)}
               onReview={(id) => console.log('Review agent:', id)}
             />
           ))}
         </div>

                 {/* Real-time Activity Feed */}
         <ActivityFeed
           activities={[
             {
               id: '1',
               agent: 'Venue Scout Agent',
               message: 'Found 3 new venue options matching requirements. Ready for human review.',
               timestamp: '2 minutes ago',
               type: 'info',
               actions: [
                 { label: 'Approve', onClick: () => console.log('Approve venue'), variant: 'default' },
                 { label: 'Request Changes', onClick: () => console.log('Request changes'), variant: 'outline' }
               ]
             },
             {
               id: '2',
               agent: 'Budget Controller',
               message: 'Completed budget optimization for Marketing Summit. Saved $12,000.',
               timestamp: '5 minutes ago',
               type: 'success'
             },
             {
               id: '3',
               agent: 'Speaker Outreach Agent',
               message: 'Encountered scheduling conflict with keynote speaker. Requires manual intervention.',
               timestamp: '8 minutes ago',
               type: 'warning',
               actions: [
                 { label: 'Resolve Conflict', onClick: () => console.log('Resolve conflict'), variant: 'outline' }
               ]
             },
             {
               id: '4',
               agent: 'Sponsorship Manager',
               message: 'Generated sponsorship packages based on speaker lineup. Ready for distribution.',
               timestamp: '12 minutes ago',
               type: 'info'
             }
           ]}
         />

        {/* Quick Actions */}
        <div className="mt-8">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Actions</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Button variant="outline" className="h-20 flex flex-col items-center justify-center">
              <span className="text-2xl mb-2">🚀</span>
              <span>Launch New Workflow</span>
            </Button>
            <Button variant="outline" className="h-20 flex flex-col items-center justify-center">
              <span className="text-2xl mb-2">📊</span>
              <span>View Analytics</span>
            </Button>
            <Button variant="outline" className="h-20 flex flex-col items-center justify-center">
              <span className="text-2xl mb-2">⚙️</span>
              <span>Agent Settings</span>
            </Button>
          </div>
        </div>
      </main>
    </div>
  )
}
