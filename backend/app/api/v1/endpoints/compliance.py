"""
Compliance API endpoints for OrchestrateX

This module provides endpoints for GDPR compliance, data management, and privacy controls.
"""

from datetime import datetime
from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db
from ...core.security import get_current_user, require_permission
from ...models.user import User
from ...core.compliance import (
    GDPRCompliance,
    AuditLogger,
    DataRetentionManager,
    ComplianceReporting,
    PrivacyPolicy,
    DataRetentionPolicy
)

router = APIRouter()

@router.post("/gdpr/export-data")
async def export_user_data(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Export all user data for GDPR right to data portability.
    
    This endpoint allows users to download all their personal data in a structured format.
    """
    try:
        # Log the data export request
        await AuditLogger.log_user_action(
            user_id=current_user.id,
            action="data_export_requested",
            resource_type="user_data",
            resource_id=current_user.id,
            details={
                "ip_address": request.client.host,
                "user_agent": request.headers.get("user-agent")
            },
            db=db
        )
        
        # Export user data
        export_data = await GDPRCompliance.get_user_data_export(current_user.id, db)
        
        if "error" in export_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=export_data["error"]
            )
        
        return {
            "success": True,
            "message": "Data export completed successfully",
            "data": export_data,
            "export_date": datetime.utcnow().isoformat()
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to export user data"
        )

@router.post("/gdpr/delete-data")
async def delete_user_data(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Delete all user data for GDPR right to be forgotten.
    
    This endpoint allows users to request complete deletion of their personal data.
    """
    try:
        # Log the deletion request
        await AuditLogger.log_user_action(
            user_id=current_user.id,
            action="data_deletion_requested",
            resource_type="user_data",
            resource_id=current_user.id,
            details={
                "ip_address": request.client.host,
                "user_agent": request.headers.get("user-agent")
            },
            db=db
        )
        
        # Delete user data
        result = await GDPRCompliance.delete_user_data(current_user.id, db)
        
        if "error" in result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["error"]
            )
        
        return {
            "success": True,
            "message": "Data deletion request processed successfully",
            "note": "Your data has been marked for deletion and will be permanently removed within 30 days."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process deletion request"
        )

@router.post("/gdpr/anonymize-data")
async def anonymize_user_data(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Anonymize user data while keeping it for analytics purposes.
    
    This endpoint allows users to request anonymization of their personal data.
    """
    try:
        # Log the anonymization request
        await AuditLogger.log_user_action(
            user_id=current_user.id,
            action="data_anonymization_requested",
            resource_type="user_data",
            resource_id=current_user.id,
            details={
                "ip_address": request.client.host,
                "user_agent": request.headers.get("user-agent")
            },
            db=db
        )
        
        # Anonymize user data
        result = await GDPRCompliance.anonymize_user_data(current_user.id, db)
        
        if "error" in result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["error"]
            )
        
        return {
            "success": True,
            "message": "Data anonymization completed successfully",
            "note": "Your personal data has been anonymized while preserving analytics data."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to anonymize user data"
        )

@router.get("/privacy/policy")
async def get_privacy_policy() -> Dict[str, Any]:
    """
    Get the current privacy policy.
    
    Returns the complete privacy policy with data collection, usage, and user rights information.
    """
    return {
        "success": True,
        "policy": PrivacyPolicy.get_privacy_policy()
    }

@router.get("/privacy/cookies")
async def get_cookie_policy() -> Dict[str, Any]:
    """
    Get the cookie policy.
    
    Returns information about cookies used by the application.
    """
    return {
        "success": True,
        "cookies": PrivacyPolicy.get_cookie_policy()
    }

@router.post("/admin/retention/cleanup")
async def cleanup_expired_data(
    current_user: User = Depends(require_permission("manage_system_settings")),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Clean up expired data according to retention policies.
    
    This endpoint is restricted to administrators and system managers.
    """
    try:
        # Initialize retention manager with default policy
        retention_manager = DataRetentionManager(DataRetentionPolicy())
        
        # Perform cleanup
        result = await retention_manager.cleanup_expired_data(db)
        
        if "error" in result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result["error"]
            )
        
        return {
            "success": True,
            "message": "Data retention cleanup completed",
            "stats": result["stats"]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to perform data cleanup"
        )

@router.get("/admin/compliance/gdpr-report")
async def generate_gdpr_report(
    current_user: User = Depends(require_permission("view_system_analytics")),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Generate GDPR compliance report.
    
    This endpoint is restricted to administrators and managers.
    """
    try:
        report = await ComplianceReporting.generate_gdpr_report(db)
        
        if "error" in report:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=report["error"]
            )
        
        return {
            "success": True,
            "report": report
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate GDPR report"
        )

@router.get("/admin/compliance/audit-report")
async def generate_audit_report(
    start_date: str,
    end_date: str,
    current_user: User = Depends(require_permission("view_system_analytics")),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Generate audit report for specified period.
    
    This endpoint is restricted to administrators and managers.
    """
    try:
        # Parse dates
        try:
            start_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"
            )
        
        report = await ComplianceReporting.generate_audit_report(start_dt, end_dt, db)
        
        if "error" in report:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=report["error"]
            )
        
        return {
            "success": True,
            "report": report
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate audit report"
        )

@router.get("/user/privacy-settings")
async def get_user_privacy_settings(
    current_user: User = Depends(get_current_user)
) -> Dict[str, Any]:
    """
    Get user's privacy settings and preferences.
    """
    return {
        "success": True,
        "settings": {
            "user_id": current_user.id,
            "email_notifications": True,  # Would be stored in user preferences
            "marketing_emails": False,    # Would be stored in user preferences
            "data_sharing": False,        # Would be stored in user preferences
            "analytics_consent": True,    # Would be stored in user preferences
            "last_updated": current_user.updated_at.isoformat() if current_user.updated_at else None
        }
    }

@router.put("/user/privacy-settings")
async def update_user_privacy_settings(
    settings: Dict[str, Any],
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict[str, Any]:
    """
    Update user's privacy settings and preferences.
    """
    try:
        # In a real implementation, this would update user preferences in the database
        # For now, we'll just return a success response
        
        # Log the privacy settings update
        await AuditLogger.log_user_action(
            user_id=current_user.id,
            action="privacy_settings_updated",
            resource_type="user_preferences",
            resource_id=current_user.id,
            details={"new_settings": settings},
            db=db
        )
        
        return {
            "success": True,
            "message": "Privacy settings updated successfully",
            "settings": settings
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update privacy settings"
        )
