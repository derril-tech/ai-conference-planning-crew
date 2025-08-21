from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from app.core.config import settings
import asyncio
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all AI agents in the conference planning system."""
    
    def __init__(self, agent_id: str, event_id: str, agent_type: str):
        self.agent_id = agent_id
        self.event_id = event_id
        self.agent_type = agent_type
        self.status = "idle"
        self.progress = 0
        self.current_task = ""
        self.decisions: List[Dict[str, Any]] = []
        self.metadata: Dict[str, Any] = {}
        
        # Initialize LLM clients
        self.openai_client = None
        self.anthropic_client = None
        
        if settings.OPENAI_API_KEY:
            self.openai_client = ChatOpenAI(
                model="gpt-4-turbo-preview",
                temperature=0.1,
                api_key=settings.OPENAI_API_KEY
            )
        
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = ChatAnthropic(
                model="claude-3-sonnet-20240229",
                temperature=0.1,
                api_key=settings.ANTHROPIC_API_KEY
            )
    
    @abstractmethod
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent's main workflow. Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        """Get the system prompt for this agent. Must be implemented by subclasses."""
        pass
    
    async def start_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Start the agent workflow with proper status tracking."""
        try:
            self.status = "running"
            self.progress = 0
            self.current_task = "Initializing workflow..."
            
            logger.info(f"Starting {self.agent_type} workflow for event {self.event_id}")
            
            # Execute the main workflow
            result = await self.execute_workflow(context)
            
            self.status = "completed"
            self.progress = 100
            self.current_task = "Workflow completed successfully"
            
            logger.info(f"Completed {self.agent_type} workflow for event {self.event_id}")
            
            return result
            
        except Exception as e:
            self.status = "error"
            self.current_task = f"Error: {str(e)}"
            logger.error(f"Error in {self.agent_type} workflow: {str(e)}")
            raise
    
    async def request_approval(self, approval_data: Dict[str, Any]) -> str:
        """Request human approval for a decision."""
        self.status = "waiting_approval"
        self.current_task = "Waiting for human approval"
        
        # Create approval record
        approval = {
            "id": f"approval_{self.agent_id}_{datetime.utcnow().isoformat()}",
            "agent_id": self.agent_id,
            "event_id": self.event_id,
            "type": f"{self.agent_type}_approval",
            "data": approval_data,
            "created_at": datetime.utcnow().isoformat()
        }
        
        # TODO: Save approval to database
        # await self.save_approval(approval)
        
        logger.info(f"Requesting approval for {self.agent_type} agent")
        
        return approval["id"]
    
    async def make_decision(self, decision_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a decision and record it."""
        decision = {
            "id": f"decision_{self.agent_id}_{datetime.utcnow().isoformat()}",
            "agent_type": self.agent_type,
            "data": decision_data,
            "timestamp": datetime.utcnow().isoformat(),
            "confidence": decision_data.get("confidence", 0.8)
        }
        
        self.decisions.append(decision)
        
        logger.info(f"Made decision in {self.agent_type} agent: {decision['id']}")
        
        return decision
    
    async def update_progress(self, progress: int, task: str):
        """Update the agent's progress and current task."""
        self.progress = max(0, min(100, progress))
        self.current_task = task
        
        logger.debug(f"{self.agent_type} agent progress: {progress}% - {task}")
    
    async def log_activity(self, message: str, activity_type: str = "info", data: Optional[Dict[str, Any]] = None):
        """Log an activity for this agent."""
        activity = {
            "agent_id": self.agent_id,
            "event_id": self.event_id,
            "type": activity_type,
            "message": message,
            "data": data or {},
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # TODO: Save activity to database
        # await self.save_activity(activity)
        
        logger.info(f"{self.agent_type} activity: {message}")
    
    async def get_llm_response(self, messages: List[BaseMessage], use_anthropic: bool = False) -> str:
        """Get a response from the LLM."""
        try:
            if use_anthropic and self.anthropic_client:
                response = await self.anthropic_client.ainvoke(messages)
                return response.content
            elif self.openai_client:
                response = await self.openai_client.ainvoke(messages)
                return response.content
            else:
                raise Exception("No LLM client available")
        except Exception as e:
            logger.error(f"Error getting LLM response: {str(e)}")
            raise
    
    def get_agent_state(self) -> Dict[str, Any]:
        """Get the current state of the agent."""
        return {
            "agent_id": self.agent_id,
            "event_id": self.event_id,
            "agent_type": self.agent_type,
            "status": self.status,
            "progress": self.progress,
            "current_task": self.current_task,
            "decisions": self.decisions,
            "metadata": self.metadata
        }
