import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'
import { Progress } from '@/components/ui/progress'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { Alert, AlertDescription } from '@/components/ui/alert'

export default function CommandCenterPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Command Center</h1>
          <p className="text-muted-foreground">
            Real-time monitoring and control for event operations
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export Report</Button>
          <Button>Emergency Contact</Button>
        </div>
      </div>

      {/* System Status */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-success">🟢</div>
            <div className="text-sm text-muted-foreground">System Status</div>
            <div className="text-xs text-success mt-1">All systems operational</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-conference-600">342</div>
            <div className="text-sm text-muted-foreground">Attendees Checked In</div>
            <div className="text-xs text-conference-600 mt-1">85% of total</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-warning">3</div>
            <div className="text-sm text-muted-foreground">Active Incidents</div>
            <div className="text-xs text-warning mt-1">2 minor, 1 moderate</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-success">12</div>
            <div className="text-sm text-muted-foreground">Staff On Duty</div>
            <div className="text-xs text-success mt-1">All positions filled</div>
          </CardContent>
        </Card>
      </div>

      {/* Active Incidents */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span>Active Incidents</span>
            <Badge variant="warning">3 Active</Badge>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <Alert>
              <AlertDescription>
                <div className="flex items-center justify-between">
                  <div>
                    <div className="font-medium">AV System Failure - Room A</div>
                    <div className="text-sm text-muted-foreground">
                      Projector not responding, technician dispatched
                    </div>
                  </div>
                  <div className="text-right">
                    <StatusChip variant="warning">In Progress</StatusChip>
                    <div className="text-xs text-muted-foreground">15 min ago</div>
                  </div>
                </div>
              </AlertDescription>
            </Alert>
            
            <Alert>
              <AlertDescription>
                <div className="flex items-center justify-between">
                  <div>
                    <div className="font-medium">Speaker Running Late - Dr. Johnson</div>
                    <div className="text-sm text-muted-foreground">
                      ETA 20 minutes, backup speaker on standby
                    </div>
                  </div>
                  <div className="text-right">
                    <StatusChip variant="warning">Monitoring</StatusChip>
                    <div className="text-xs text-muted-foreground">8 min ago</div>
                  </div>
                </div>
              </AlertDescription>
            </Alert>
            
            <Alert>
              <AlertDescription>
                <div className="flex items-center justify-between">
                  <div>
                    <div className="font-medium">Catering Shortage - Coffee Station</div>
                    <div className="text-sm text-muted-foreground">
                      Running low on coffee, additional supply ordered
                    </div>
                  </div>
                  <div className="text-right">
                    <StatusChip variant="default">Resolved</StatusChip>
                    <div className="text-xs text-muted-foreground">5 min ago</div>
                  </div>
                </div>
              </AlertDescription>
            </Alert>
          </div>
        </CardContent>
      </Card>

      {/* Session Status */}
      <Card>
        <CardHeader>
          <CardTitle>Session Status</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Time</TableHead>
                <TableHead>Session</TableHead>
                <TableHead>Room</TableHead>
                <TableHead>Speaker</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Attendance</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>10:00 AM</TableCell>
                <TableCell>
                  <div className="font-medium">Opening Keynote</div>
                  <div className="text-sm text-muted-foreground">AI Ethics in Practice</div>
                </TableCell>
                <TableCell>Main Hall</TableCell>
                <TableCell>Dr. Sarah Johnson</TableCell>
                <TableCell>
                  <StatusChip variant="success">In Progress</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">245/300</div>
                  <Progress value={82} className="h-1 mt-1" />
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>11:30 AM</TableCell>
                <TableCell>
                  <div className="font-medium">AI in Healthcare</div>
                  <div className="text-sm text-muted-foreground">Breakout Session</div>
                </TableCell>
                <TableCell>Room A</TableCell>
                <TableCell>Prof. Michael Chen</TableCell>
                <TableCell>
                  <StatusChip variant="warning">Delayed</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">--/80</div>
                  <div className="text-xs text-muted-foreground">Not started</div>
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>2:00 PM</TableCell>
                <TableCell>
                  <div className="font-medium">Data Analytics Workshop</div>
                  <div className="text-sm text-muted-foreground">Hands-on Session</div>
                </TableCell>
                <TableCell>Room B</TableCell>
                <TableCell>Lisa Rodriguez</TableCell>
                <TableCell>
                  <StatusChip variant="default">Scheduled</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">--/60</div>
                  <div className="text-xs text-muted-foreground">Not started</div>
                </TableCell>
                <TableCell>
                  <Button size="sm" variant="outline">View</Button>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Staff Assignments */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Staff Assignments</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">John Smith</div>
                  <div className="text-sm text-muted-foreground">AV Technician</div>
                </div>
                <div className="text-right">
                  <StatusChip variant="success">On Duty</StatusChip>
                  <div className="text-xs text-muted-foreground">Room A</div>
                </div>
              </div>
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">Sarah Wilson</div>
                  <div className="text-sm text-muted-foreground">Registration Desk</div>
                </div>
                <div className="text-right">
                  <StatusChip variant="success">On Duty</StatusChip>
                  <div className="text-xs text-muted-foreground">Main Lobby</div>
                </div>
              </div>
              <div className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <div className="font-medium">Mike Chen</div>
                  <div className="text-sm text-muted-foreground">Security</div>
                </div>
                <div className="text-right">
                  <StatusChip variant="success">On Duty</StatusChip>
                  <div className="text-xs text-muted-foreground">Main Entrance</div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-2 gap-3">
              <Button variant="outline" className="h-20 flex-col">
                <span className="text-lg">📢</span>
                <span className="text-sm">Send Announcement</span>
              </Button>
              <Button variant="outline" className="h-20 flex-col">
                <span className="text-lg">📱</span>
                <span className="text-sm">Push Notification</span>
              </Button>
              <Button variant="outline" className="h-20 flex-col">
                <span className="text-lg">🚨</span>
                <span className="text-sm">Emergency Alert</span>
              </Button>
              <Button variant="outline" className="h-20 flex-col">
                <span className="text-lg">📊</span>
                <span className="text-sm">Live Analytics</span>
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Communication Log */}
      <Card>
        <CardHeader>
          <CardTitle>Communication Log</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="flex items-start gap-3 p-3 border rounded-lg">
              <div className="w-2 h-2 bg-success rounded-full mt-2"></div>
              <div className="flex-1">
                <div className="font-medium">System Announcement</div>
                <div className="text-sm text-muted-foreground">
                  Welcome to Tech Conference 2024! Please check in at the registration desk.
                </div>
                <div className="text-xs text-muted-foreground mt-1">2 minutes ago</div>
              </div>
            </div>
            <div className="flex items-start gap-3 p-3 border rounded-lg">
              <div className="w-2 h-2 bg-warning rounded-full mt-2"></div>
              <div className="flex-1">
                <div className="font-medium">Session Update</div>
                <div className="text-sm text-muted-foreground">
                  "AI in Healthcare" session delayed by 15 minutes due to technical issues.
                </div>
                <div className="text-xs text-muted-foreground mt-1">8 minutes ago</div>
              </div>
            </div>
            <div className="flex items-start gap-3 p-3 border rounded-lg">
              <div className="w-2 h-2 bg-conference-600 rounded-full mt-2"></div>
              <div className="flex-1">
                <div className="font-medium">Staff Message</div>
                <div className="text-sm text-muted-foreground">
                  Additional coffee supply has arrived at the main catering station.
                </div>
                <div className="text-xs text-muted-foreground mt-1">12 minutes ago</div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
