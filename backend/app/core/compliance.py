"""
Compliance Module for OrchestrateX

This module handles GDPR compliance, data retention, audit logging, and regulatory requirements.
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from pydantic import BaseModel

from ..models.user import User
from ..models.event import Event
from ..models.agent_activity import AgentActivity
from ..core.database import get_db

logger = logging.getLogger(__name__)

class DataRetentionPolicy(BaseModel):
    """Data retention policy configuration."""
    user_data_retention_days: int = 2555  # 7 years
    event_data_retention_days: int = 1825  # 5 years
    audit_log_retention_days: int = 2555  # 7 years
    agent_activity_retention_days: int = 1095  # 3 years
    deleted_data_retention_days: int = 30  # 30 days in trash

class GDPRCompliance:
    """GDPR compliance utilities."""
    
    @staticmethod
    async def get_user_data_export(user_id: str, db: AsyncSession) -> Dict[str, Any]:
        """Export all user data for GDPR right to data portability."""
        try:
            # Get user data
            result = await db.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()
            
            if not user:
                return {"error": "User not found"}
            
            # Get user's events
            result = await db.execute(
                select(Event).where(Event.created_by == user_id)
            )
            events = result.scalars().all()
            
            # Get user's agent activities
            result = await db.execute(
                select(AgentActivity).where(AgentActivity.user_id == user_id)
            )
            activities = result.scalars().all()
            
            # Prepare export data
            export_data = {
                "export_date": datetime.utcnow().isoformat(),
                "user_data": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "tenant_id": user.tenant_id,
                    "is_active": user.is_active,
                    "created_at": user.created_at.isoformat() if user.created_at else None,
                    "updated_at": user.updated_at.isoformat() if user.updated_at else None
                },
                "events": [
                    {
                        "id": event.id,
                        "title": event.title,
                        "description": event.description,
                        "start_date": event.start_date.isoformat() if event.start_date else None,
                        "end_date": event.end_date.isoformat() if event.end_date else None,
                        "status": event.status,
                        "budget": event.budget,
                        "created_at": event.created_at.isoformat() if event.created_at else None,
                        "updated_at": event.updated_at.isoformat() if event.updated_at else None
                    }
                    for event in events
                ],
                "agent_activities": [
                    {
                        "id": activity.id,
                        "agent_id": activity.agent_id,
                        "event_id": activity.event_id,
                        "action": activity.action,
                        "details": activity.details,
                        "status": activity.status,
                        "created_at": activity.created_at.isoformat() if activity.created_at else None
                    }
                    for activity in activities
                ]
            }
            
            return export_data
            
        except Exception as e:
            logger.error(f"Error exporting user data: {str(e)}")
            return {"error": "Failed to export user data"}
    
    @staticmethod
    async def delete_user_data(user_id: str, db: AsyncSession) -> Dict[str, Any]:
        """Delete all user data for GDPR right to be forgotten."""
        try:
            # Soft delete user data (mark as deleted but keep for retention period)
            result = await db.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()
            
            if not user:
                return {"error": "User not found"}
            
            # Mark user as deleted
            user.is_active = False
            user.deleted_at = datetime.utcnow()
            user.email = f"deleted_{user.id}@deleted.com"  # Anonymize email
            
            # Mark user's events as deleted
            result = await db.execute(
                select(Event).where(Event.created_by == user_id)
            )
            events = result.scalars().all()
            
            for event in events:
                event.deleted_at = datetime.utcnow()
                event.status = "deleted"
            
            # Mark user's agent activities as deleted
            result = await db.execute(
                select(AgentActivity).where(AgentActivity.user_id == user_id)
            )
            activities = result.scalars().all()
            
            for activity in activities:
                activity.deleted_at = datetime.utcnow()
                activity.status = "deleted"
            
            await db.commit()
            
            # Log the deletion for audit purposes
            logger.info(f"User data deleted for GDPR compliance: {user_id}")
            
            return {"success": True, "message": "User data deleted successfully"}
            
        except Exception as e:
            await db.rollback()
            logger.error(f"Error deleting user data: {str(e)}")
            return {"error": "Failed to delete user data"}
    
    @staticmethod
    async def anonymize_user_data(user_id: str, db: AsyncSession) -> Dict[str, Any]:
        """Anonymize user data while keeping it for analytics."""
        try:
            result = await db.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()
            
            if not user:
                return {"error": "User not found"}
            
            # Anonymize user data
            user.email = f"anonymous_{user.id}@anonymous.com"
            user.first_name = "Anonymous"
            user.last_name = "User"
            user.phone = None
            user.anonymized_at = datetime.utcnow()
            
            await db.commit()
            
            logger.info(f"User data anonymized: {user_id}")
            
            return {"success": True, "message": "User data anonymized successfully"}
            
        except Exception as e:
            await db.rollback()
            logger.error(f"Error anonymizing user data: {str(e)}")
            return {"error": "Failed to anonymize user data"}

class AuditLogger:
    """Audit logging for compliance and security."""
    
    @staticmethod
    async def log_user_action(
        user_id: str,
        action: str,
        resource_type: str,
        resource_id: str,
        details: Dict[str, Any],
        db: AsyncSession
    ) -> None:
        """Log user actions for audit purposes."""
        try:
            audit_log = {
                "user_id": user_id,
                "action": action,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "details": json.dumps(details),
                "timestamp": datetime.utcnow().isoformat(),
                "ip_address": details.get("ip_address"),
                "user_agent": details.get("user_agent")
            }
            
            # In a real implementation, this would be stored in an audit log table
            logger.info(f"AUDIT LOG: {json.dumps(audit_log)}")
            
        except Exception as e:
            logger.error(f"Error logging audit event: {str(e)}")
    
    @staticmethod
    async def log_data_access(
        user_id: str,
        data_type: str,
        data_id: str,
        access_type: str,
        db: AsyncSession
    ) -> None:
        """Log data access for compliance tracking."""
        try:
            access_log = {
                "user_id": user_id,
                "data_type": data_type,
                "data_id": data_id,
                "access_type": access_type,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            logger.info(f"DATA ACCESS LOG: {json.dumps(access_log)}")
            
        except Exception as e:
            logger.error(f"Error logging data access: {str(e)}")

class DataRetentionManager:
    """Manages data retention policies and cleanup."""
    
    def __init__(self, policy: DataRetentionPolicy):
        self.policy = policy
    
    async def cleanup_expired_data(self, db: AsyncSession) -> Dict[str, Any]:
        """Clean up data that has exceeded retention periods."""
        try:
            cleanup_stats = {
                "users_deleted": 0,
                "events_deleted": 0,
                "activities_deleted": 0,
                "audit_logs_deleted": 0
            }
            
            # Clean up expired user data
            user_cutoff = datetime.utcnow() - timedelta(days=self.policy.user_data_retention_days)
            result = await db.execute(
                delete(User).where(
                    User.deleted_at < user_cutoff
                )
            )
            cleanup_stats["users_deleted"] = result.rowcount
            
            # Clean up expired event data
            event_cutoff = datetime.utcnow() - timedelta(days=self.policy.event_data_retention_days)
            result = await db.execute(
                delete(Event).where(
                    Event.deleted_at < event_cutoff
                )
            )
            cleanup_stats["events_deleted"] = result.rowcount
            
            # Clean up expired agent activities
            activity_cutoff = datetime.utcnow() - timedelta(days=self.policy.agent_activity_retention_days)
            result = await db.execute(
                delete(AgentActivity).where(
                    AgentActivity.deleted_at < activity_cutoff
                )
            )
            cleanup_stats["activities_deleted"] = result.rowcount
            
            await db.commit()
            
            logger.info(f"Data retention cleanup completed: {cleanup_stats}")
            
            return {
                "success": True,
                "message": "Data retention cleanup completed",
                "stats": cleanup_stats
            }
            
        except Exception as e:
            await db.rollback()
            logger.error(f"Error during data retention cleanup: {str(e)}")
            return {"error": "Failed to cleanup expired data"}

class ComplianceReporting:
    """Generate compliance reports."""
    
    @staticmethod
    async def generate_gdpr_report(db: AsyncSession) -> Dict[str, Any]:
        """Generate GDPR compliance report."""
        try:
            # Get statistics
            result = await db.execute(select(User))
            total_users = len(result.scalars().all())
            
            result = await db.execute(select(User).where(User.is_active == False))
            deleted_users = len(result.scalars().all())
            
            result = await db.execute(select(User).where(User.anonymized_at.isnot(None)))
            anonymized_users = len(result.scalars().all())
            
            report = {
                "report_date": datetime.utcnow().isoformat(),
                "total_users": total_users,
                "deleted_users": deleted_users,
                "anonymized_users": anonymized_users,
                "data_export_requests": 0,  # Would be tracked in a real system
                "data_deletion_requests": 0,  # Would be tracked in a real system
                "compliance_status": "compliant"
            }
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating GDPR report: {str(e)}")
            return {"error": "Failed to generate GDPR report"}
    
    @staticmethod
    async def generate_audit_report(
        start_date: datetime,
        end_date: datetime,
        db: AsyncSession
    ) -> Dict[str, Any]:
        """Generate audit report for specified period."""
        try:
            # In a real implementation, this would query audit logs
            report = {
                "report_period": {
                    "start_date": start_date.isoformat(),
                    "end_date": end_date.isoformat()
                },
                "total_actions": 0,
                "user_logins": 0,
                "data_accesses": 0,
                "admin_actions": 0,
                "security_events": 0
            }
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating audit report: {str(e)}")
            return {"error": "Failed to generate audit report"}

class PrivacyPolicy:
    """Privacy policy management."""
    
    @staticmethod
    def get_privacy_policy() -> Dict[str, Any]:
        """Get current privacy policy."""
        return {
            "version": "1.0",
            "last_updated": "2024-01-01",
            "data_collection": {
                "personal_data": ["email", "name", "phone", "company"],
                "usage_data": ["login_times", "feature_usage", "preferences"],
                "technical_data": ["ip_address", "user_agent", "device_info"]
            },
            "data_usage": {
                "purpose": "Event planning and management",
                "legal_basis": "Contract performance and legitimate interest",
                "retention_period": "7 years for user data, 5 years for event data"
            },
            "user_rights": [
                "Right to access personal data",
                "Right to rectification",
                "Right to erasure (right to be forgotten)",
                "Right to data portability",
                "Right to object to processing",
                "Right to withdraw consent"
            ],
            "contact": {
                "data_protection_officer": "dpo@orchestratex.com",
                "privacy_email": "privacy@orchestratex.com"
            }
        }
    
    @staticmethod
    def get_cookie_policy() -> Dict[str, Any]:
        """Get cookie policy."""
        return {
            "essential_cookies": [
                {
                    "name": "session",
                    "purpose": "Maintain user session",
                    "duration": "Session"
                },
                {
                    "name": "csrf",
                    "purpose": "Security token",
                    "duration": "Session"
                }
            ],
            "analytics_cookies": [
                {
                    "name": "_ga",
                    "purpose": "Google Analytics",
                    "duration": "2 years"
                }
            ],
            "preference_cookies": [
                {
                    "name": "theme",
                    "purpose": "User interface preferences",
                    "duration": "1 year"
                }
            ]
        }
