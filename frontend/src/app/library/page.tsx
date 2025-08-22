import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function LibraryPage() {
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
            <h1 className="text-3xl font-bold text-gray-900">Knowledge Library</h1>
            <p className="text-gray-600 mt-2">Manage RAG content, vendor documents, and reference materials</p>
          </div>
          <Button className="bg-conference-600 hover:bg-conference-700">
            Upload Document
          </Button>
        </div>

        {/* Library Categories */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <span className="text-2xl">📋</span>
                RFPs & Briefs
              </CardTitle>
              <CardDescription>
                Event briefs and request for proposals
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span>Documents</span>
                  <span className="font-medium">12</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span>Last Updated</span>
                  <span className="text-gray-500">2 days ago</span>
                </div>
                <Button variant="outline" className="w-full">
                  Browse RFPs
                </Button>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <span className="text-2xl">🏢</span>
                Vendor Documents
              </CardTitle>
              <CardDescription>
                Venue contracts, rate cards, and vendor sheets
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span>Documents</span>
                  <span className="font-medium">45</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span>Last Updated</span>
                  <span className="text-gray-500">1 hour ago</span>
                </div>
                <Button variant="outline" className="w-full">
                  Browse Vendors
                </Button>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <span className="text-2xl">📊</span>
                Historical Data
              </CardTitle>
              <CardDescription>
                Past event reports and performance data
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div className="flex justify-between text-sm">
                  <span>Reports</span>
                  <span className="font-medium">28</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span>Last Updated</span>
                  <span className="text-gray-500">1 week ago</span>
                </div>
                <Button variant="outline" className="w-full">
                  Browse Reports
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Recent Documents */}
        <Card>
          <CardHeader>
            <CardTitle>Recent Documents</CardTitle>
            <CardDescription>
              Recently uploaded and updated documents
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
                    <span className="text-conference-600">📄</span>
                  </div>
                  <div>
                    <h3 className="font-medium">SF Convention Center Rate Card 2024</h3>
                    <p className="text-sm text-gray-500">Vendor Document • 2 hours ago</p>
                  </div>
                </div>
                <Button variant="outline" size="sm">
                  View
                </Button>
              </div>

              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-success-100 rounded-lg flex items-center justify-center">
                    <span className="text-success-600">📋</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Tech Conference 2024 Brief</h3>
                    <p className="text-sm text-gray-500">Event Brief • 1 day ago</p>
                  </div>
                </div>
                <Button variant="outline" size="sm">
                  View
                </Button>
              </div>

              <div className="flex items-center justify-between p-4 border rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-10 h-10 bg-warning-100 rounded-lg flex items-center justify-center">
                    <span className="text-warning-600">📊</span>
                  </div>
                  <div>
                    <h3 className="font-medium">Marketing Summit 2023 Postmortem</h3>
                    <p className="text-sm text-gray-500">Historical Report • 3 days ago</p>
                  </div>
                </div>
                <Button variant="outline" size="sm">
                  View
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  )
}
