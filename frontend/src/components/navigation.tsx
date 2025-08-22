import Link from 'next/link'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'

interface NavigationProps {
  className?: string
}

export function Navigation({ className }: NavigationProps) {
  return (
    <nav className={`flex items-center space-x-6 ${className}`}>
      <Link href="/" className="text-gray-700 hover:text-conference-600 transition-colors">
        Home
      </Link>
      <Link href="/events" className="text-gray-700 hover:text-conference-600 transition-colors">
        Events
      </Link>
      <Link href="/dashboard" className="text-gray-700 hover:text-conference-600 transition-colors">
        Dashboard
      </Link>
      <Link href="/library" className="text-gray-700 hover:text-conference-600 transition-colors">
        Knowledge Library
      </Link>
      <Link href="/command" className="text-gray-700 hover:text-conference-600 transition-colors">
        Command Center
      </Link>
      <Link href="/analytics" className="text-gray-700 hover:text-conference-600 transition-colors">
        Analytics
      </Link>
      <Link href="/settings" className="text-gray-700 hover:text-conference-600 transition-colors">
        Settings
      </Link>
    </nav>
  )
}

export function MobileNavigation() {
  return (
    <div className="md:hidden">
      <div className="px-2 pt-2 pb-3 space-y-1">
        <Link href="/" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Home
        </Link>
        <Link href="/events" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Events
        </Link>
        <Link href="/dashboard" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Dashboard
        </Link>
        <Link href="/library" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Knowledge Library
        </Link>
        <Link href="/command" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Command Center
        </Link>
        <Link href="/analytics" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Analytics
        </Link>
        <Link href="/settings" className="block px-3 py-2 text-base font-medium text-gray-700 hover:text-conference-600 hover:bg-gray-50 rounded-md">
          Settings
        </Link>
      </div>
    </div>
  )
}

export function Header() {
  return (
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
          
          <div className="hidden md:block">
            <Navigation />
          </div>
          
          <div className="flex items-center space-x-4">
            <div className="hidden md:flex items-center space-x-2">
              <Badge variant="outline">Admin</Badge>
              <span className="text-sm text-gray-600">Welcome, Admin</span>
            </div>
            <Button variant="outline" size="sm">
              Logout
            </Button>
          </div>
        </div>
      </div>
    </header>
  )
}
