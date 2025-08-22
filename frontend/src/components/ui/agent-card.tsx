import * as React from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { StatusChip } from "@/components/ui/status-chip"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import { Agent } from "@/types"

interface AgentCardProps {
  agent: Agent
  className?: string
  onViewDetails?: (agentId: string) => void
  onReview?: (agentId: string) => void
}

export function AgentCard({ agent, className, onViewDetails, onReview }: AgentCardProps) {
  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return '✅'
      case 'running':
        return '🔄'
      case 'waiting_approval':
        return '⏳'
      case 'error':
        return '❌'
      default:
        return '⏸️'
    }
  }

  const getAgentIcon = (type: string) => {
    switch (type) {
      case 'venue_scout':
        return '🏢'
      case 'speaker_outreach':
        return '🎤'
      case 'sponsorship_manager':
        return '💼'
      case 'budget_controller':
        return '💰'
      case 'marketing_ops':
        return '📢'
      case 'attendee_experience':
        return '👥'
      case 'logistics_travel':
        return '✈️'
      case 'risk_compliance':
        return '🛡️'
      default:
        return '🤖'
    }
  }

  return (
    <Card className={cn("hover:shadow-lg transition-shadow", className)}>
      <CardHeader className="pb-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-conference-100 rounded-lg flex items-center justify-center">
              <span className="text-conference-600 text-lg">
                {getAgentIcon(agent.type)}
              </span>
            </div>
            <div>
              <CardTitle className="text-lg capitalize">
                {agent.type.replace('_', ' ')}
              </CardTitle>
              <CardDescription className="text-sm">
                {agent.currentTask}
              </CardDescription>
            </div>
          </div>
          <StatusChip 
            variant={agent.status as any} 
            icon={getStatusIcon(agent.status)}
          />
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>Progress</span>
              <span>{agent.progress}%</span>
            </div>
            <Progress value={agent.progress} className="h-2" />
          </div>
          
          <div className="flex justify-between text-sm">
            <span>Decisions Made</span>
            <span className="font-medium">{agent.decisions.length}</span>
          </div>
          
          <div className="flex gap-2">
            <Button 
              variant="outline" 
              size="sm" 
              className="flex-1"
              onClick={() => onViewDetails?.(agent.id)}
            >
              View Details
            </Button>
            {agent.status === 'waiting_approval' && (
              <Button 
                size="sm" 
                className="flex-1 bg-warning-600 hover:bg-warning-700"
                onClick={() => onReview?.(agent.id)}
              >
                Review
              </Button>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
