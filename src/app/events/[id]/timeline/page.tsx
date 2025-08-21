import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { mockAgents } from '@/lib/mock-data'

export default function EventTimelinePage({ params }: { params: { id: string } }) {
  return (
    <div>
      {/* Page Header */}
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Agent Timeline</h1>
          <p className="text-gray-600 mt-2">Track AI agent progress and workflow status</p>
        </div>
        <Button className="bg-conference-600 hover:bg-conference-700">
          Start New Workflow
        </Button>
      </div>

      {/* Agent Status Overview */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {mockAgents.map((agent) => (
          <Card key={agent.id} className="hover:shadow-md transition-shadow">
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg capitalize">
                  {agent.type.replace('_', ' ')}
                </CardTitle>
                <div className={`w-3 h-3 rounded-full ${
                  agent.status === 'completed' ? 'bg-success-500' :
                  agent.status === 'running' ? 'bg-conference-500' :
                  agent.status === 'waiting_approval' ? 'bg-warning-500' :
                  'bg-gray-300'
                }`}></div>
              </div>
              <CardDescription className="text-sm">
                {agent.currentTask}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div>
                  <div className="flex justify-between text-sm mb-1">
                    <span>Progress</span>
                    <span>{agent.progress}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-conference-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${agent.progress}%` }}
                    ></div>
                  </div>
                </div>
                <div className="flex justify-between text-sm">
                  <span>Decisions</span>
                  <span className="font-medium">{agent.decisions.length}</span>
                </div>
                <div className="flex gap-2">
                  <Button variant="outline" size="sm" className="flex-1">
                    View Details
                  </Button>
                  {agent.status === 'waiting_approval' && (
                    <Button size="sm" className="flex-1 bg-warning-600 hover:bg-warning-700">
                      Review
                    </Button>
                  )}
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Timeline View */}
      <Card>
        <CardHeader>
          <CardTitle>Workflow Timeline</CardTitle>
          <CardDescription>
            Visual representation of agent dependencies and progress
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-6">
            {/* Timeline Item */}
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-conference-600 rounded-full flex items-center justify-center">
                  <span className="text-white text-sm font-bold">1</span>
                </div>
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-semibold">Venue Scout Agent</h3>
                  <span className="status-chip status-success">Completed</span>
                </div>
                <p className="text-gray-600 mt-1">
                  Found 3 venue options matching requirements. Selected San Francisco Convention Center.
                </p>
                <div className="mt-3 flex items-center space-x-4 text-sm text-gray-500">
                  <span>✅ Approved by Admin</span>
                  <span>💰 $21,000 budget impact</span>
                  <span>📅 2 hours ago</span>
                </div>
              </div>
            </div>

            {/* Timeline Item */}
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-warning-500 rounded-full flex items-center justify-center">
                  <span className="text-white text-sm font-bold">2</span>
                </div>
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-semibold">Speaker Outreach Agent</h3>
                  <span className="status-chip status-warning">Waiting Approval</span>
                </div>
                <p className="text-gray-600 mt-1">
                  Proposed speaker lineup with 8 confirmed speakers. Ready for human review.
                </p>
                <div className="mt-3 flex items-center space-x-4 text-sm text-gray-500">
                  <span>⏳ Pending approval</span>
                  <span>💰 $15,000 budget impact</span>
                  <span>📅 4 hours ago</span>
                </div>
                <div className="mt-3 flex space-x-2">
                  <Button size="sm" className="bg-success-600 hover:bg-success-700">
                    Approve
                  </Button>
                  <Button size="sm" variant="outline">
                    Request Changes
                  </Button>
                </div>
              </div>
            </div>

            {/* Timeline Item */}
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-600 text-sm font-bold">3</span>
                </div>
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-semibold text-gray-400">Sponsorship Manager</h3>
                  <span className="status-chip status-gray">Pending</span>
                </div>
                <p className="text-gray-400 mt-1">
                  Waiting for speaker lineup approval before designing sponsorship packages.
                </p>
                <div className="mt-3 flex items-center space-x-4 text-sm text-gray-400">
                  <span>⏸️ Blocked by speaker approval</span>
                  <span>📅 Not started</span>
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
