import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-conference-50 to-conference-100">
      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center">
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
            AI-Powered Conference Planning
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            OrchestrateX coordinates specialized AI agents to design, staff, budget, schedule, 
            promote, and run conferences end-to-end with human oversight and complete audit trails.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-conference-600 hover:bg-conference-700">
              Start Planning Your Event
            </Button>
            <Button size="lg" variant="outline">
              Watch Demo
            </Button>
          </div>
        </div>

        {/* Features Grid */}
        <div className="mt-24 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">1</span>
                </div>
                Event Wizard
              </CardTitle>
              <CardDescription>
                AI-powered event planning from brief to execution
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                Transform your event brief into a comprehensive plan with venue recommendations, 
                speaker sourcing, and budget optimization.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">2</span>
                </div>
                Agent Timeline
              </CardTitle>
              <CardDescription>
                Real-time coordination of specialized AI agents
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                Monitor and manage parallel AI agents handling venue scouting, speaker outreach, 
                sponsorship, and logistics coordination.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">3</span>
                </div>
                Command Center
              </CardTitle>
              <CardDescription>
                Live event management and incident response
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                Real-time dashboards for day-of operations, attendee check-ins, 
                and automated incident response workflows.
              </p>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  )
}
