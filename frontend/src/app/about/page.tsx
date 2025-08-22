import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-conference-50 to-conference-100">
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
              <Link href="/dashboard" className="text-gray-700 hover:text-conference-600">Dashboard</Link>
              <Link href="/events" className="text-gray-700 hover:text-conference-600">Events</Link>
            </nav>
            <div className="flex items-center space-x-4">
              <Button variant="outline" asChild>
                <Link href="/login">Sign In</Link>
              </Button>
              <Button asChild>
                <Link href="/register">Get Started</Link>
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-16">
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 mb-6">
            About OrchestrateX
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Revolutionizing conference planning through AI-powered automation and human oversight.
          </p>
        </div>

        {/* Mission Section */}
        <div className="mb-16">
          <Card>
            <CardHeader>
              <CardTitle className="text-3xl text-center">Our Mission</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-lg text-gray-700 text-center leading-relaxed">
                OrchestrateX transforms the complex, time-consuming process of conference planning 
                into an efficient, AI-driven workflow. Our platform coordinates specialized AI agents 
                to handle every aspect of event planning while maintaining human oversight and 
                complete transparency.
              </p>
            </CardContent>
          </Card>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">🤖</span>
                </div>
                AI-Powered
              </CardTitle>
              <CardDescription>
                Eight specialized AI agents working in parallel
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                From venue scouting to speaker outreach, our AI agents handle every aspect 
                of conference planning with precision and efficiency.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">👥</span>
                </div>
                Human Oversight
              </CardTitle>
              <CardDescription>
                Approval gates for critical decisions
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                Maintain control with human-in-the-loop approvals for venue selection, 
                speaker lineup, and budget decisions.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <div className="w-8 h-8 bg-conference-100 rounded-lg flex items-center justify-center">
                  <span className="text-conference-600 font-semibold">📊</span>
                </div>
                Real-time Analytics
              </CardTitle>
              <CardDescription>
                Live dashboards and progress tracking
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-gray-600">
                Monitor progress in real-time with comprehensive dashboards and 
                detailed analytics for every aspect of your event.
              </p>
            </CardContent>
          </Card>
        </div>

        {/* CTA Section */}
        <div className="text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Ready to Transform Your Event Planning?
          </h2>
          <p className="text-lg text-gray-600 mb-8">
            Join the future of conference planning with OrchestrateX.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-conference-600 hover:bg-conference-700">
              Start Your Free Trial
            </Button>
            <Button size="lg" variant="outline">
              Schedule a Demo
            </Button>
          </div>
        </div>
      </main>
    </div>
  )
}
