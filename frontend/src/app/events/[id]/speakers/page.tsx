import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'
import { Input } from '@/components/ui/input'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'

export default function SpeakersPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Speaker Management</h1>
          <p className="text-muted-foreground">
            Manage speakers, outreach, and session assignments
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export List</Button>
          <Button>Add Speaker</Button>
        </div>
      </div>

      {/* Filters and Search */}
      <Card>
        <CardContent className="pt-6">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <Input placeholder="Search speakers..." />
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Status</SelectItem>
                <SelectItem value="confirmed">Confirmed</SelectItem>
                <SelectItem value="pending">Pending</SelectItem>
                <SelectItem value="declined">Declined</SelectItem>
              </SelectContent>
            </Select>
            <Select>
              <SelectTrigger>
                <SelectValue placeholder="Expertise" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Expertise</SelectItem>
                <SelectItem value="ai">Artificial Intelligence</SelectItem>
                <SelectItem value="ml">Machine Learning</SelectItem>
                <SelectItem value="data">Data Science</SelectItem>
              </SelectContent>
            </Select>
            <Button variant="outline">Clear Filters</Button>
          </div>
        </CardContent>
      </Card>

      {/* Speaker Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold">24</div>
            <div className="text-sm text-muted-foreground">Total Speakers</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-success">18</div>
            <div className="text-sm text-muted-foreground">Confirmed</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-warning">4</div>
            <div className="text-sm text-muted-foreground">Pending</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-destructive">2</div>
            <div className="text-sm text-muted-foreground">Declined</div>
          </CardContent>
        </Card>
      </div>

      {/* Speakers Table */}
      <Card>
        <CardHeader>
          <CardTitle>Speaker Directory</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Speaker</TableHead>
                <TableHead>Expertise</TableHead>
                <TableHead>Session</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Fee</TableHead>
                <TableHead>Actions</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">Dr. Sarah Johnson</div>
                    <div className="text-sm text-muted-foreground">sarah.johnson@ai-research.org</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="secondary">AI Ethics</Badge>
                </TableCell>
                <TableCell>
                  <div className="font-medium">Opening Keynote</div>
                  <div className="text-sm text-muted-foreground">Day 1, 10:00 AM</div>
                </TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>$5,000</TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">Edit</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">Prof. Michael Chen</div>
                    <div className="text-sm text-muted-foreground">mchen@stanford.edu</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="secondary">Machine Learning</Badge>
                </TableCell>
                <TableCell>
                  <div className="font-medium">AI in Healthcare</div>
                  <div className="text-sm text-muted-foreground">Day 1, 2:00 PM</div>
                </TableCell>
                <TableCell>
                  <StatusChip variant="warning">Pending</StatusChip>
                </TableCell>
                <TableCell>$3,500</TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">Edit</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div>
                    <div className="font-medium">Lisa Rodriguez</div>
                    <div className="text-sm text-muted-foreground">lisa@techstartup.com</div>
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant="secondary">Data Science</Badge>
                </TableCell>
                <TableCell>
                  <div className="font-medium">Data Analytics Workshop</div>
                  <div className="text-sm text-muted-foreground">Day 2, 9:00 AM</div>
                </TableCell>
                <TableCell>
                  <StatusChip variant="success">Confirmed</StatusChip>
                </TableCell>
                <TableCell>$2,500</TableCell>
                <TableCell>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline">Edit</Button>
                    <Button size="sm" variant="outline">Contact</Button>
                  </div>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Outreach Campaign */}
      <Card>
        <CardHeader>
          <CardTitle>Outreach Campaign</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Speaker Outreach Campaign</div>
                <div className="text-sm text-muted-foreground">Targeting 15 potential speakers</div>
              </div>
              <StatusChip variant="success">Active</StatusChip>
            </div>
            <div className="grid grid-cols-3 gap-4 text-sm">
              <div>
                <div className="font-medium">Emails Sent</div>
                <div className="text-2xl font-bold text-conference-600">12</div>
              </div>
              <div>
                <div className="font-medium">Responses</div>
                <div className="text-2xl font-bold text-success">8</div>
              </div>
              <div>
                <div className="font-medium">Conversion Rate</div>
                <div className="text-2xl font-bold text-conference-600">67%</div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
