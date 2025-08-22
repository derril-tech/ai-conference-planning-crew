import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const statusChipVariants = cva(
  "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium transition-colors",
  {
    variants: {
      variant: {
        planning: "bg-conference-100 text-conference-800 border border-conference-200",
        active: "bg-success-100 text-success-800 border border-success-200",
        completed: "bg-gray-100 text-gray-800 border border-gray-200",
        cancelled: "bg-danger-100 text-danger-800 border border-danger-200",
        pending: "bg-warning-100 text-warning-800 border border-warning-200",
        running: "bg-conference-100 text-conference-800 border border-conference-200 animate-pulse",
        waiting_approval: "bg-warning-100 text-warning-800 border border-warning-200",
        error: "bg-danger-100 text-danger-800 border border-danger-200",
        success: "bg-success-100 text-success-800 border border-success-200",
        warning: "bg-warning-100 text-warning-800 border border-warning-200",
        danger: "bg-danger-100 text-danger-800 border border-danger-200",
      },
      size: {
        sm: "px-2 py-0.5 text-xs",
        md: "px-2.5 py-0.5 text-xs",
        lg: "px-3 py-1 text-sm",
      },
    },
    defaultVariants: {
      variant: "planning",
      size: "md",
    },
  }
)

export interface StatusChipProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof statusChipVariants> {
  icon?: React.ReactNode
}

const StatusChip = React.forwardRef<HTMLDivElement, StatusChipProps>(
  ({ className, variant, size, icon, children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(statusChipVariants({ variant, size }), className)}
        {...props}
      >
        {icon && <span className="mr-1">{icon}</span>}
        {children}
      </div>
    )
  }
)
StatusChip.displayName = "StatusChip"

export { StatusChip, statusChipVariants }
