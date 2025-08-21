"""
AI Agents Module for OrchestrateX

This module contains all specialized AI agents for event planning and management.
Each agent inherits from BaseAgent and implements specific workflows for their domain.
"""

from .base_agent import BaseAgent
from .venue_scout import VenueScoutAgent
from .speaker_outreach import SpeakerOutreachAgent
from .sponsorship_manager import SponsorshipManagerAgent
from .budget_controller import BudgetControllerAgent
from .marketing_ops import MarketingOpsAgent
from .attendee_experience import AttendeeExperienceAgent
from .logistics_travel import LogisticsTravelAgent
from .risk_compliance import RiskComplianceAgent

__all__ = [
    "BaseAgent",
    "VenueScoutAgent",
    "SpeakerOutreachAgent", 
    "SponsorshipManagerAgent",
    "BudgetControllerAgent",
    "MarketingOpsAgent",
    "AttendeeExperienceAgent",
    "LogisticsTravelAgent",
    "RiskComplianceAgent"
]

# Agent type mapping for easy instantiation
AGENT_TYPES = {
    "venue_scout": VenueScoutAgent,
    "speaker_outreach": SpeakerOutreachAgent,
    "sponsorship_manager": SponsorshipManagerAgent,
    "budget_controller": BudgetControllerAgent,
    "marketing_ops": MarketingOpsAgent,
    "attendee_experience": AttendeeExperienceAgent,
    "logistics_travel": LogisticsTravelAgent,
    "risk_compliance": RiskComplianceAgent
}

def create_agent(agent_type: str, agent_id: str, event_id: str) -> BaseAgent:
    """
    Factory function to create agent instances.
    
    Args:
        agent_type: Type of agent to create
        agent_id: Unique identifier for the agent
        event_id: Event identifier the agent will work on
        
    Returns:
        BaseAgent: Instance of the specified agent type
        
    Raises:
        ValueError: If agent_type is not recognized
    """
    if agent_type not in AGENT_TYPES:
        raise ValueError(f"Unknown agent type: {agent_type}. Available types: {list(AGENT_TYPES.keys())}")
    
    agent_class = AGENT_TYPES[agent_type]
    return agent_class(agent_id, event_id)
