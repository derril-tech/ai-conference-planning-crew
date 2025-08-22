import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { Progress } from '@/components/ui/progress'

export default function SponsorsPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Sponsor Management</h1>
          <p className="text-muted-foreground">
            Manage sponsors, packages, and revenue tracking
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export Report</Button>
          <Button>Add Sponsor</Button>
        </div>
      </div>

      {/* Revenue Overview */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-success">$125,000</div>
            <div className="text-sm text-muted-foreground">Total Revenue</div>
            <div className="text-xs text-success mt-1">+15% vs target</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold">12</div>
            <div className="text-sm text-muted-foreground">Confirmed Sponsors</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-warning">5</div>
            <div className="text-sm text-muted-foreground">Pending Deals</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-conference-600">83%</div>
            <div className="text-sm text-muted-foreground">Revenue Goal</div>
            <Progress value={83} className="mt-2" />
          </CardContent>
        </Card>
      </div>

      {/* Sponsor Packages */}
      <Card>
        <CardHeader>
          <CardTitle>Sponsorship Packages</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">Platinum Sponsor</h3>
                <Badge variant="conference">$25,000</Badge>
              </div>
              <ul className="text-sm space-y-2 text-muted-foreground">
                <li>• Keynote speaking slot</li>
                <li>• Premium booth space</li>
                <li>• Logo on all materials</li>
                <li>• 10 complimentary tickets</li>
              </ul>
              <div className="mt-4">
                <div className="text-sm text-muted-foreground">3 of 4 sold</div>
                <Progress value={75} className="mt-1" />
              </div>
            </div>
            
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">Gold Sponsor</h3>
                <Badge variant="secondary">$15,000</Badge>
              </div>
              <ul className="text-sm space-y-2 text-muted-foreground">
                <li>• Session speaking slot</li>
                <li>• Standard booth space</li>
                <li>• Logo on website</li>
                <li>• 5 complimentary tickets</li>
              </ul>
              <div className="mt-4">
                <div className="text-sm text-muted-foreground">6 of 8 sold</div>
                <Progress value={75} className="mt-1" />
              </div>
            </div>
            
            <div className="border rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-semibold">Silver Sponsor</h3>
                <Badge variant="outline">$8,000</Badge>
              </div>
              <ul className="text-sm space-y-2 text-muted-foreground">
                <li>• Exhibit booth</li>
                <li>• Logo on materials</li>
                <li>• 2 complimentary tickets</li>
              </ul>
              <div className="mt-4">
                <div className="text-sm text-muted-foreground">3 of 6 sold</div>
                <Progress value={50} className="mt-1" />
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Sponsors Table */}
      <Card>
        <CardHeader>
          <CardTitle>Sponsor Directory</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Company</TableHead>
                <TableHead>Package</TableHead>
                <TableHead>Amount</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Contact</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">TechCorp Solutions</div>
                    <div className="text-sm text-muted-foreground">techcorp.com</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="conference">Platinum</Badge>
                </TableCell>
                <TableCell>$25,000</TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">John Smith</div>
                  <div className="text-xs text-muted-foreground">john@techcorp.com</div>
                </TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">View</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">DataFlow Inc</div>
                    <div className="text-sm text-muted-foreground">dataflow.com</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="secondary">Gold</Badge>
                </TableCell>
                <TableCell>$15,000</TableCell>
                <TableCell>
                  <StatusChip variant="warning">Negotiating</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">Sarah Wilson</div>
                  <div className="text-xs text-muted-foreground">sarah@dataflow.com</div>
                </TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">View</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">AI Startup Labs</div>
                    <div className="text-sm text-muted-foreground">aistartup.com</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="outline">Silver</Badge>
                </TableCell>
                <TableCell>$8,000</TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>
                  <div className="text-sm">Mike Chen</div>
                  <div className="text-xs text-muted-foreground">mike@aistartup.com</div>
                </TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">View</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Deliverables Tracking */}
      <Card>
        <CardHeader>
          <CardTitle>Deliverables Tracking</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 border rounded-lg">
              <div>
                <div className="font-medium">TechCorp Solutions - Logo Files</div>
                <div className="text-sm text-muted-foreground">High-resolution logos for all materials</div>
              </div>
              <StatusChip variant="success">Received</StatusChip>
            </div>
            <div className="flex items-center justify-between p-3 border rounded-lg">
              <div>
                <div className="font-medium">DataFlow Inc - Speaker Bio</div>
                <div className="text-sm text-muted-foreground">Speaker information for session</div>
              </div>
              <StatusChip variant="warning">Pending</StatusChip>
            </div>
            <div className="flex items-center justify-between p-3 border rounded-lg">
              <div>
                <div className="font-medium">AI Startup Labs - Booth Setup</div>
                <div className="text-sm text-muted-foreground">Booth specifications and requirements</div>
              </div>
              <StatusChip variant="default">In Progress</StatusChip>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
