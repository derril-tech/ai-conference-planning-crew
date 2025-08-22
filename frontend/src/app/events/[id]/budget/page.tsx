import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'
import { Progress } from '@/components/ui/progress'
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'

export default function BudgetPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Budget Console</h1>
          <p className="text-muted-foreground">
            Track expenses, revenue, and financial projections
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export Report</Button>
          <Button>Add Expense</Button>
        </div>
      </div>

      {/* Budget Overview */}
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
            <div className="text-2xl font-bold text-destructive">$85,000</div>
            <div className="text-sm text-muted-foreground">Total Expenses</div>
            <div className="text-xs text-destructive mt-1">+8% vs budget</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-conference-600">$40,000</div>
            <div className="text-sm text-muted-foreground">Net Profit</div>
            <div className="text-xs text-conference-600 mt-1">32% margin</div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="pt-6">
            <div className="text-2xl font-bold text-warning">68%</div>
            <div className="text-sm text-muted-foreground">Budget Used</div>
            <Progress value={68} className="mt-2" />
          </CardContent>
        </Card>
      </div>

      {/* Revenue Breakdown */}
      <Card>
        <CardHeader>
          <CardTitle>Revenue Breakdown</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Sponsorship Revenue</div>
                <div className="text-sm text-muted-foreground">Platinum, Gold, Silver packages</div>
              </div>
              <div className="text-right">
                <div className="font-bold text-success">$95,000</div>
                <div className="text-sm text-muted-foreground">76% of total</div>
              </div>
            </div>
            <Progress value={76} className="h-2" />
            
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Ticket Sales</div>
                <div className="text-sm text-muted-foreground">Early bird, regular, VIP tickets</div>
              </div>
              <div className="text-right">
                <div className="font-bold text-success">$25,000</div>
                <div className="text-sm text-muted-foreground">20% of total</div>
              </div>
            </div>
            <Progress value={20} className="h-2" />
            
            <div className="flex items-center justify-between">
              <div>
                <div className="font-medium">Other Revenue</div>
                <div className="text-sm text-muted-foreground">Workshops, merchandise, etc.</div>
              </div>
              <div className="text-right">
                <div className="font-bold text-success">$5,000</div>
                <div className="text-sm text-muted-foreground">4% of total</div>
              </div>
            </div>
            <Progress value={4} className="h-2" />
          </div>
        </CardContent>
      </Card>

      {/* Expense Categories */}
      <Card>
        <CardHeader>
          <CardTitle>Expense Categories</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Category</TableHead>
                <TableHead>Budgeted</TableHead>
                <TableHead>Actual</TableHead>
                <TableHead>Variance</TableHead>
                <TableHead>Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Venue & Facilities</div>
                  <div className="text-sm text-muted-foreground">Conference center, rooms, AV</div>
                </TableCell>
                <TableCell>$35,000</TableCell>
                <TableCell>$32,000</TableCell>
                <TableCell className="text-success">-$3,000</TableCell>
                <TableCell>
                  <StatusChip variant="success">Under Budget</StatusChip>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Speaker Fees</div>
                  <div className="text-sm text-muted-foreground">Keynotes, sessions, workshops</div>
                </TableCell>
                <TableCell>$25,000</TableCell>
                <TableCell>$28,000</TableCell>
                <TableCell className="text-destructive">+$3,000</TableCell>
                <TableCell>
                  <StatusChip variant="warning">Over Budget</StatusChip>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Marketing & Promotion</div>
                  <div className="text-sm text-muted-foreground">Ads, materials, social media</div>
                </TableCell>
                <TableCell>$15,000</TableCell>
                <TableCell>$12,000</TableCell>
                <TableCell className="text-success">-$3,000</TableCell>
                <TableCell>
                  <StatusChip variant="success">Under Budget</StatusChip>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>
                  <div className="font-medium">Catering & Hospitality</div>
                  <div className="text-sm text-muted-foreground">Food, beverages, breaks</div>
                </TableCell>
                <TableCell>$10,000</TableCell>
                <TableCell>$13,000</TableCell>
                <TableCell className="text-destructive">+$3,000</TableCell>
                <TableCell>
                  <StatusChip variant="warning">Over Budget</StatusChip>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Financial Projections */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Cash Flow Projection</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-sm">Q1 2024</span>
                <div className="text-right">
                  <div className="font-medium">-$15,000</div>
                  <div className="text-xs text-muted-foreground">Initial expenses</div>
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm">Q2 2024</span>
                <div className="text-right">
                  <div className="font-medium">-$25,000</div>
                  <div className="text-xs text-muted-foreground">Venue deposits</div>
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm">Q3 2024</span>
                <div className="text-right">
                  <div className="font-medium text-success">+$40,000</div>
                  <div className="text-xs text-muted-foreground">Sponsorship payments</div>
                </div>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm">Q4 2024</span>
                <div className="text-right">
                  <div className="font-medium text-success">+$125,000</div>
                  <div className="text-xs text-muted-foreground">Event revenue</div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Risk Analysis</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div className="p-3 border border-warning/20 bg-warning/5 rounded-lg">
                <div className="font-medium text-warning">Sponsorship Risk</div>
                <div className="text-sm text-muted-foreground">
                  2 pending sponsor deals worth $30,000
                </div>
              </div>
              <div className="p-3 border border-danger/20 bg-danger/5 rounded-lg">
                <div className="font-medium text-destructive">Cost Overrun Risk</div>
                <div className="text-sm text-muted-foreground">
                  Speaker fees and catering exceeding budget
                </div>
              </div>
              <div className="p-3 border border-success/20 bg-success/5 rounded-lg">
                <div className="font-medium text-success">Revenue Opportunity</div>
                <div className="text-sm text-muted-foreground">
                  High demand for VIP tickets - consider price increase
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Recent Transactions */}
      <Card>
        <CardHeader>
          <CardTitle>Recent Transactions</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Date</TableHead>
                <TableHead>Description</TableHead>
                <TableHead>Category</TableHead>
                <TableHead>Amount</TableHead>
                <TableHead>Type</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow>
                <TableCell>2024-01-15</TableCell>
                <TableCell>TechCorp Solutions - Platinum Sponsorship</TableCell>
                <TableCell>Sponsorship</TableCell>
                <TableCell className="text-success">+$25,000</TableCell>
                <TableCell>
                  <Badge variant="success">Revenue</Badge>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>2024-01-14</TableCell>
                <TableCell>Conference Center - Venue Deposit</TableCell>
                <TableCell>Venue & Facilities</TableCell>
                <TableCell className="text-destructive">-$15,000</TableCell>
                <TableCell>
                  <Badge variant="destructive">Expense</Badge>
                </TableCell>
              </TableRow>
              <TableRow>
                <TableCell>2024-01-13</TableCell>
                <TableCell>Dr. Sarah Johnson - Speaker Fee</TableCell>
                <TableCell>Speaker Fees</TableCell>
                <TableCell className="text-destructive">-$5,000</TableCell>
                <TableCell>
                  <Badge variant="destructive">Expense</Badge>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  )
}
