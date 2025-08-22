import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { StatusChip } from '@/components/ui/status-chip'

export default function ScheduleBuilderPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold">Schedule Builder</h1>
          <p className="text-muted-foreground">
            Drag and drop sessions to build your conference schedule
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline">Export Schedule</Button>
          <Button>Save Changes</Button>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Session Library */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <span>Session Library</span>
              <Badge variant="secondary">24 Sessions</Badge>
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="p-3 border rounded-lg cursor-move hover:bg-muted/50">
              <div className="font-medium">Opening Keynote</div>
              <div className="text-sm text-muted-foreground">60 min • Main Hall</div>
              <StatusChip variant="success" className="mt-2">Confirmed</StatusChip>
            </div>
            <div className="p-3 border rounded-lg cursor-move hover:bg-muted/50">
              <div className="font-medium">AI in Healthcare</div>
              <div className="text-sm text-muted-foreground">45 min • Room A</div>
              <StatusChip variant="warning" className="mt-2">Pending</StatusChip>
            </div>
            <div className="p-3 border rounded-lg cursor-move hover:bg-muted/50">
              <div className="font-medium">Networking Break</div>
              <div className="text-sm text-muted-foreground">30 min • Lobby</div>
              <StatusChip variant="default" className="mt-2">Scheduled</StatusChip>
            </div>
          </CardContent>
        </Card>

        {/* Schedule Grid */}
        <div className="lg:col-span-2">
          <Card>
            <CardHeader>
              <CardTitle>Conference Schedule</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {/* Day 1 */}
                <div>
                  <h3 className="font-semibold mb-3">Day 1 - October 15, 2024</h3>
                  <div className="grid grid-cols-4 gap-2 text-sm">
                    <div className="font-medium p-2 bg-muted rounded">Time</div>
                    <div className="font-medium p-2 bg-muted rounded">Main Hall</div>
                    <div className="font-medium p-2 bg-muted rounded">Room A</div>
                    <div className="font-medium p-2 bg-muted rounded">Room B</div>
                    
                    <div className="p-2">9:00 AM</div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    
                    <div className="p-2">10:00 AM</div>
                    <div className="p-2 bg-success/10 border border-success/20 rounded">
                      <div className="font-medium">Opening Keynote</div>
                      <div className="text-xs text-muted-foreground">Dr. Sarah Johnson</div>
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                  </div>
                </div>

                {/* Day 2 */}
                <div>
                  <h3 className="font-semibold mb-3">Day 2 - October 16, 2024</h3>
                  <div className="grid grid-cols-4 gap-2 text-sm">
                    <div className="font-medium p-2 bg-muted rounded">Time</div>
                    <div className="font-medium p-2 bg-muted rounded">Main Hall</div>
                    <div className="font-medium p-2 bg-muted rounded">Room A</div>
                    <div className="font-medium p-2 bg-muted rounded">Room B</div>
                    
                    <div className="p-2">9:00 AM</div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                    <div className="p-2 border-2 border-dashed border-muted-foreground/30 rounded min-h-[60px] flex items-center justify-center text-muted-foreground">
                      Drop session here
                    </div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Conflict Detection */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <span>Conflict Detection</span>
            <Badge variant="danger">2 Conflicts</Badge>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            <div className="p-3 border border-destructive/20 bg-destructive/5 rounded-lg">
              <div className="font-medium text-destructive">Speaker Double Booking</div>
              <div className="text-sm text-muted-foreground">
                Dr. Sarah Johnson is scheduled for "AI Ethics" and "Machine Learning Basics" at the same time
              </div>
            </div>
            <div className="p-3 border border-destructive/20 bg-destructive/5 rounded-lg">
              <div className="font-medium text-destructive">Room Capacity Exceeded</div>
              <div className="text-sm text-muted-foreground">
                "Advanced AI Workshop" (120 attendees) exceeds Room A capacity (80 seats)
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
