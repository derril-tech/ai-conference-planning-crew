import * as React from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

interface ActivityItem {
  id: string
  agent: string
  message: string
  timestamp: string
  type: 'info' | 'success' | 'warning' | 'error'
  actions?: {
    label: string
    onClick: () => void
    variant?: 'default' | 'outline' | 'destructive'
  }[]
}

interface ActivityFeedProps {
  title?: string
  description?: string
  activities: ActivityItem[]
  className?: string
  maxHeight?: string
}

export function ActivityFeed({ 
  title = "Activity Feed", 
  description = "Real-time updates from AI agents",
  activities, 
  className,
  maxHeight = "max-h-96"
}: ActivityFeedProps) {
  const getTypeIcon = (type: string) => {
    switch (type) {
      case 'success':
        return '✅'
      case 'warning':
        return '⚠️'
      case 'error':
        return '❌'
      default:
        return 'ℹ️'
    }
  }

  const getTypeColor = (type: string) => {
    switch (type) {
      case 'success':
        return 'bg-success-600'
      case 'warning':
        return 'bg-warning-600'
      case 'error':
        return 'bg-danger-600'
      default:
        return 'bg-conference-600'
    }
  }

  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className={cn("space-y-4 overflow-y-auto", maxHeight)}>
          {activities.map((activity) => (
            <div key={activity.id} className="flex items-start space-x-4 p-4 border rounded-lg">
              <div className="flex-shrink-0">
                <div className={cn(
                  "w-8 h-8 rounded-full flex items-center justify-center",
                  getTypeColor(activity.type)
                )}>
                  <span className="text-white text-sm">
                    {getTypeIcon(activity.type)}
                  </span>
                </div>
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <h3 className="font-medium">{activity.agent}</h3>
                  <span className="text-xs text-gray-500">{activity.timestamp}</span>
                </div>
                <p className="text-sm text-gray-600 mt-1">
                  {activity.message}
                </p>
                {activity.actions && activity.actions.length > 0 && (
                  <div className="mt-3 flex space-x-2">
                    {activity.actions.map((action, index) => (
                      <Button
                        key={index}
                        size="sm"
                        variant={action.variant || "outline"}
                        onClick={action.onClick}
                      >
                        {action.label}
                      </Button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
          
          {activities.length === 0 && (
            <div className="text-center py-8">
              <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-gray-400 text-2xl">📝</span>
              </div>
              <p className="text-gray-500">No activities yet</p>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
