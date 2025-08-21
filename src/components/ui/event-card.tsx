import * as React from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { StatusChip } from "@/components/ui/status-chip"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { Event } from "@/types"
import { formatCurrency, formatDate } from "@/lib/utils"

interface EventCardProps {
  event: Event
  className?: string
  onViewDetails?: (eventId: string) => void
  onEdit?: (eventId: string) => void
}

export function EventCard({ event, className, onViewDetails, onEdit }: EventCardProps) {
  return (
    <Card className={cn("hover:shadow-lg transition-shadow", className)}>
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <CardTitle className="text-lg">{event.name}</CardTitle>
            <CardDescription className="mt-1">
              {event.city} • {formatDate(event.startDate)}
            </CardDescription>
          </div>
          <StatusChip variant={event.status} />
        </div>
      </CardHeader>
      <CardContent>
        <p className="text-gray-600 text-sm mb-4 line-clamp-2">
          {event.description}
        </p>
        
        <div className="grid grid-cols-2 gap-4 text-sm mb-4">
          <div>
            <span className="font-medium">Attendees:</span> {event.briefJson.expectedAttendees}
          </div>
          <div>
            <span className="font-medium">Budget:</span> {formatCurrency(event.budget.total)}
          </div>
        </div>
        
        <div className="flex gap-2">
          <Button 
            variant="outline" 
            size="sm" 
            className="flex-1"
            onClick={() => onViewDetails?.(event.id)}
          >
            View Details
          </Button>
          <Button 
            variant="outline" 
            size="sm" 
            className="flex-1"
            onClick={() => onEdit?.(event.id)}
          >
            Edit
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
