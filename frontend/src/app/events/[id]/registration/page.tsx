import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'
import { Progress } from '@/components/ui/progress'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

export default function RegistrationPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Registration Dashboard</h1>
          <p className="text-muted-foreground">
            Track ticket sales, attendee demographics, and registration funnel
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export Attendees</Button>
          <Button>Manage Tickets</Button>
        </div>
      </div>

      {/* Registration Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-success">342</div>
            <div className="text-sm text-muted-foreground">Total Registrations</div>
            <div className="text-xs text-success mt-1">+12 today</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-conference-600">85%</div>
            <div className="text-sm text-muted-foreground">Capacity Filled</div>
            <Progress value={85} className="mt-2" />
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-warning">$25,000</div>
            <div className="text-sm text-muted-foreground">Ticket Revenue</div>
            <div className="text-xs text-warning mt-1">+$2,500 today</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-destructive">12</div>
            <div className="text-sm text-muted-foreground">Days Until Event</div>
            <div className="text-xs text-destructive mt-1">Registration closes in 5 days</div>
          </CardContent>
        </Card>
      </div>

      {/* Ticket Types */}
      <Card>
        <CardHeader>
          <CardTitle>Ticket Types & Sales</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">VIP Pass</h3>
                <Badge variant="conference">$299</Badge>
              </div>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span>Sold</span>
                  <span className="font-medium">45/50</span>
                </div>
                <Progress value={90} className="h-2" />
                <div className="text-xs text-muted-foreground">
                  Includes premium seating, networking dinner, exclusive workshops
                </div>
              </div>
            </div>
            
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">Regular Pass</h3>
                <Badge variant="secondary">$149</Badge>
              </div>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span>Sold</span>
                  <span className="font-medium">245/300</span>
                </div>
                <Progress value={82} className="h-2" />
                <div className="text-xs text-muted-foreground">
                  Full conference access, lunch included, networking breaks
                </div>
              </div>
            </div>
            
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">Student Pass</h3>
                <Badge variant="outline">$49</Badge>
              </div>
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span>Sold</span>
                  <span className="font-medium">52/100</span>
                </div>
                <Progress value={52} className="h-2" />
                <div className="text-xs text-muted-foreground">
                  Valid student ID required, limited to certain sessions
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Registration Funnel */}
      <Card>
        <CardHeader>
          <CardTitle>Registration Funnel</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Website Visitors</div>
                <div className="text-sm text-muted-foreground">Total unique visitors</div>
              </div>
              <div className="text-right">
                <div className="font-bold">2,450</div>
                <div className="text-sm text-muted-foreground">100%</div>
              </div>
            </div>
            <Progress value={100} className="h-2" />
            
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Started Registration</div>
                <div className="text-sm text-muted-foreground">Began ticket purchase process</div>
              </div>
              <div className="text-right">
                <div className="font-bold">1,230</div>
                <div className="text-sm text-muted-foreground">50%</div>
              </div>
            </div>
            <Progress value={50} className="h-2" />
            
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Completed Registration</div>
                <div className="text-sm text-muted-foreground">Successfully purchased tickets</div>
              </div>
              <div className="text-right">
                <div className="font-bold">342</div>
                <div className="text-sm text-muted-foreground">14%</div>
              </div>
            </div>
            <Progress value={14} className="h-2" />
          </div>
        </CardContent>
      </Card>

      {/* Attendee Demographics */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Attendee Demographics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-sm">Industry</span>
                <div className="text-right">
                  <div className="font-medium">Technology</div>
                  <div className="text-xs text-muted-foreground">45%</div>
                </div>
              </div>
              <Progress value={45} className="h-2" />
              
              <div className="flex items-center justify-between">
                <span className="text-sm">Experience Level</span>
                <div className="text-right">
                  <div className="font-medium">Mid-Level</div>
                  <div className="text-xs text-muted-foreground">38%</div>
                </div>
              </div>
              <Progress value={38} className="h-2" />
              
              <div className="flex items-center justify-between">
                <span className="text-sm">Company Size</span>
                <div className="text-right">
                  <div className="font-medium">Enterprise (1000+)</div>
                  <div className="text-xs text-muted-foreground">52%</div>
                </div>
              </div>
              <Progress value={52} className="h-2" />
              
              <div className="flex items-center justify-between">
                <span className="text-sm">Geographic Region</span>
                <div className="text-right">
                  <div className="font-medium">North America</div>
                  <div className="text-xs text-muted-foreground">67%</div>
                </div>
              </div>
              <Progress value={67} className="h-2" />
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Recent Registrations</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">Sarah Wilson</div>
                  <div className="text-sm text-muted-foreground">sarah.wilson@techcorp.com</div>
                </div>
                <div className="text-right">
                  <Badge variant="conference">VIP Pass</Badge>
                  <div className="text-xs text-muted-foreground">2 hours ago</div>
                </div>
              </div>
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">Mike Chen</div>
                  <div className="text-sm text-muted-foreground">mike.chen@dataflow.com</div>
                </div>
                <div className="text-right">
                  <Badge variant="secondary">Regular Pass</Badge>
                  <div className="text-xs text-muted-foreground">4 hours ago</div>
                </div>
              </div>
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">Lisa Rodriguez</div>
                  <div className="text-sm text-muted-foreground">lisa@aistartup.com</div>
                </div>
                <div className="text-right">
                  <Badge variant="outline">Student Pass</Badge>
                  <div className="text-xs text-muted-foreground">6 hours ago</div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Attendee List */}
      <Card>
        <CardHeader>
          <CardTitle>Attendee Directory</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="mb-4 flex gap-4">
            <Input placeholder="Search attendees..." className="max-w-sm" />
            <Select>
              <SelectTrigger className="w-40">
                <SelectValue placeholder="Ticket Type" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Types</SelectItem>
                <SelectItem value="vip">VIP Pass</SelectItem>
                <SelectItem value="regular">Regular Pass</SelectItem>
                <SelectItem value="student">Student Pass</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Name</TableHead>
                <TableHead>Company</TableHead>
                <TableHead>Ticket Type</TableHead>
                <TableHead>Registration Date</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Sarah Wilson</div>
                  <div className="text-sm text-muted-foreground">sarah.wilson@techcorp.com</div>
                </TableCell>
                <TableCell>TechCorp Solutions</TableCell>
                <TableCell>
                  <Badge variant="conference">VIP Pass</Badge>
                </TableCell>
                <TableCell>2024-01-15</TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Mike Chen</div>
                  <div className="text-sm text-muted-foreground">mike.chen@dataflow.com</div>
                </TableCell>
                <TableCell>DataFlow Inc</TableCell>
                <TableCell>
                  <Badge variant="secondary">Regular Pass</Badge>
                </TableCell>
                <TableCell>2024-01-14</TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Lisa Rodriguez</div>
                  <div className="text-sm text-muted-foreground">lisa@aistartup.com</div>
                </TableCell>
                <TableCell>AI Startup Labs</TableCell>
                <TableCell>
                  <Badge variant="outline">Student Pass</Badge>
                </TableCell>
                <TableCell>2024-01-13</TableCell>
                <TableCell>
                  <StatusChip variant="warning">Pending Verification</StatusChip>
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  )
}
