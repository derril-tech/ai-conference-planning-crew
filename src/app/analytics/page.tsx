import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function AnalyticsPage() {
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
            <h1 className="text-3xl font-bold text-gray-900">Analytics</h1>
            <p className="text-gray-600 mt-2">Comprehensive insights and performance metrics</p>
          </div>
          <div className="flex space-x-4">
            <Button variant="outline">
              Export Report
            </Button>
            <Button className="bg-conference-600 hover:bg-conference-700">
              Generate Insights
            </Button>
          </div>
        </div>

        {/* Key Metrics */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-sm font-medium">Total Events</CardTitle>
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">📅</span>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">24</div>
              <p className="text-xs text-muted-foreground">
                +12% from last month
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-sm font-medium">Total Revenue</CardTitle>
                <div className="w-8 h-8 bg-success-100 rounded-lg flex items-center justify-center">
                  <span className="text-success-600 font-semibold">💰</span>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">$2.4M</div>
              <p className="text-xs text-muted-foreground">
                +8% from last month
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-sm font-medium">Avg. Event Success</CardTitle>
                <div className="w-8 h-8 bg-warning-100 rounded-lg flex items-center justify-center">
                  <span className="text-warning-600 font-semibold">📊</span>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">94%</div>
              <p className="text-xs text-muted-foreground">
                +2% from last month
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-sm font-medium">AI Efficiency</CardTitle>
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">🤖</span>
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">87%</div>
              <p className="text-xs text-muted-foreground">
                +5% from last month
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Charts Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          {/* Revenue Trend */}
          <Card>
            <CardHeader>
              <CardTitle>Revenue Trend</CardTitle>
              <CardDescription>
                Monthly revenue over the last 12 months
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
                <div className="text-center">
                  <div className="w-16 h-16 bg-conference-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-conference-600 text-2xl">📈</span>
                  </div>
                  <p className="text-gray-600">Chart visualization will be implemented</p>
                  <p className="text-sm text-gray-500">Using Recharts library</p>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Event Performance */}
          <Card>
            <CardHeader>
              <CardTitle>Event Performance</CardTitle>
              <CardDescription>
                Success rate by event type
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
                <div className="text-center">
                  <div className="w-16 h-16 bg-success-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-success-600 text-2xl">🎯</span>
                  </div>
                  <p className="text-gray-600">Chart visualization will be implemented</p>
                  <p className="text-sm text-gray-500">Using Recharts library</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Agent Performance */}
        <Card className="mb-8">
          <CardHeader>
            <CardTitle>AI Agent Performance</CardTitle>
            <CardDescription>
              Efficiency and success rates for each AI agent
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
                    <span className="text-conference-600 font-semibold">VS</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Venue Scout</h3>
                    <p className="text-sm text-gray-500">Venue selection and negotiation</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-lg font-semibold">92%</div>
                  <div className="text-sm text-gray-500">Success Rate</div>
                </div>
              </div>

              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
                    <span className="text-conference-600 font-semibold">SO</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Speaker Outreach</h3>
                    <p className="text-sm text-gray-500">Speaker recruitment and scheduling</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-lg font-semibold">88%</div>
                  <div className="text-sm text-gray-500">Success Rate</div>
                </div>
              </div>

              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
                    <span className="text-conference-600 font-semibold">SM</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Sponsorship Manager</h3>
                    <p className="text-sm text-gray-500">Sponsor acquisition and management</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-lg font-semibold">85%</div>
                  <div className="text-sm text-gray-500">Success Rate</div>
                </div>
              </div>

              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
                    <span className="text-conference-600 font-semibold">BC</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Budget Controller</h3>
                    <p className="text-sm text-gray-500">Budget optimization and tracking</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-lg font-semibold">96%</div>
                  <div className="text-sm text-gray-500">Success Rate</div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Insights and Recommendations */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <Card>
            <CardHeader>
              <CardTitle>Key Insights</CardTitle>
              <CardDescription>
                AI-generated insights from your data
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="p-4 bg-conference-50 border border-conference-200 rounded-lg">
                  <h4 className="font-medium text-conference-800 mb-2">Revenue Optimization</h4>
                  <p className="text-sm text-conference-700">
                    Events with early bird pricing show 23% higher revenue. Consider implementing tiered pricing strategies.
                  </p>
                </div>
                <div className="p-4 bg-success-50 border border-success-200 rounded-lg">
                  <h4 className="font-medium text-success-800 mb-2">Agent Performance</h4>
                  <p className="text-sm text-success-700">
                    Venue Scout agent has the highest success rate. Consider applying similar strategies to other agents.
                  </p>
                </div>
                <div className="p-4 bg-warning-50 border border-warning-200 rounded-lg">
                  <h4 className="font-medium text-warning-800 mb-2">Risk Alert</h4>
                  <p className="text-sm text-warning-700">
                    Speaker availability is trending downward. Consider expanding speaker network and backup options.
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Recommendations</CardTitle>
              <CardDescription>
                Actionable recommendations for improvement
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-start space-x-3">
                  <div className="w-6 h-6 bg-conference-600 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span className="text-white text-xs">1</span>
                  </div>
                  <div>
                    <h4 className="font-medium">Optimize Speaker Outreach</h4>
                    <p className="text-sm text-gray-600">
                      Implement automated follow-up sequences to improve speaker response rates.
                    </p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-6 h-6 bg-conference-600 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span className="text-white text-xs">2</span>
                  </div>
                  <div>
                    <h4 className="font-medium">Enhance Budget Tracking</h4>
                    <p className="text-sm text-gray-600">
                      Add real-time budget alerts and automated cost optimization suggestions.
                    </p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="w-6 h-6 bg-conference-600 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                    <span className="text-white text-xs">3</span>
                  </div>
                  <div>
                    <h4 className="font-medium">Expand Venue Network</h4>
                    <p className="text-sm text-gray-600">
                      Add more venue options to increase competition and potentially reduce costs.
                    </p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  )
}
