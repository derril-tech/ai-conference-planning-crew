from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class VenueScoutAgent(BaseAgent):
    """AI agent responsible for finding and evaluating conference venues."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "venue_scout")
    
    def get_system_prompt(self) -> str:
        return """You are a Venue Scout Agent specializing in finding and evaluating conference venues. 
        
        Your responsibilities include:
        1. Analyzing event requirements (location, capacity, budget, dates)
        2. Researching potential venues in the target area
        3. Evaluating venues based on criteria like:
           - Capacity and layout suitability
           - Location and accessibility
           - Available amenities and services
           - Pricing and budget fit
           - Availability for the event dates
        4. Creating detailed venue proposals with pros/cons
        5. Requesting human approval for venue selections
        
        Always provide detailed reasoning for your recommendations and clearly indicate when human approval is needed for major decisions."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the venue scouting workflow."""
        event_data = context.get("event", {})
        
        await self.update_progress(10, "Analyzing event requirements...")
        
        # Step 1: Analyze event requirements
        requirements = await self._analyze_requirements(event_data)
        await self.log_activity("Analyzed event requirements", "info", requirements)
        
        await self.update_progress(25, "Researching potential venues...")
        
        # Step 2: Research potential venues
        venues = await self._research_venues(requirements)
        await self.log_activity(f"Found {len(venues)} potential venues", "info", {"venue_count": len(venues)})
        
        await self.update_progress(50, "Evaluating venues...")
        
        # Step 3: Evaluate venues
        evaluated_venues = await self._evaluate_venues(venues, requirements)
        await self.log_activity("Completed venue evaluation", "info", {"evaluated_count": len(evaluated_venues)})
        
        await self.update_progress(75, "Creating venue proposals...")
        
        # Step 4: Create proposals
        proposals = await self._create_proposals(evaluated_venues)
        
        await self.update_progress(90, "Requesting approval for venue selection...")
        
        # Step 5: Request approval for top venue
        if proposals:
            top_venue = proposals[0]
            approval_id = await self.request_approval({
                "type": "venue_selection",
                "venue": top_venue,
                "all_proposals": proposals,
                "reasoning": top_venue.get("reasoning", "")
            })
            
            await self.make_decision({
                "action": "venue_selection_proposed",
                "venue_id": top_venue.get("id"),
                "approval_id": approval_id,
                "confidence": top_venue.get("score", 0.8)
            })
        
        await self.update_progress(100, "Venue scouting workflow completed")
        
        return {
            "status": "completed",
            "venues_researched": len(venues),
            "proposals_created": len(proposals),
            "top_venue": proposals[0] if proposals else None,
            "all_proposals": proposals
        }
    
    async def _analyze_requirements(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze event requirements for venue selection."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the following event requirements for venue selection:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Location: {event_data.get('city', 'Unknown')}, {event_data.get('country', 'Unknown')}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Budget: ${event_data.get('budget_total', 0):,.2f}
            - Description: {event_data.get('description', 'No description provided')}
            
            Please provide a structured analysis including:
            1. Required venue capacity
            2. Preferred location characteristics
            3. Essential amenities needed
            4. Budget constraints and priorities
            5. Special requirements or considerations
            
            Return your analysis as a JSON object.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback to structured text if JSON parsing fails
            return {
                "capacity_required": event_data.get('expected_attendees', 100),
                "location": event_data.get('city', 'Unknown'),
                "budget_max": event_data.get('budget_total', 0) * 0.3,  # Assume 30% for venue
                "amenities_required": ["WiFi", "AV Equipment", "Catering Space"],
                "special_requirements": []
            }
    
    async def _research_venues(self, requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Research potential venues based on requirements."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Research potential venues based on these requirements:
            {json.dumps(requirements, indent=2)}
            
            For the location {requirements.get('location', 'Unknown')}, find 5-8 potential venues that could meet these requirements.
            
            For each venue, provide:
            - Name and address
            - Capacity
            - Estimated daily rate
            - Available amenities
            - Contact information
            - Availability for the event dates
            
            Return as a JSON array of venue objects.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            venues = json.loads(response)
            return venues if isinstance(venues, list) else []
        except json.JSONDecodeError:
            # Return mock venues if parsing fails
            return self._get_mock_venues(requirements)
    
    async def _evaluate_venues(self, venues: List[Dict[str, Any]], requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Evaluate venues based on requirements and criteria."""
        evaluated_venues = []
        
        for venue in venues:
            messages = [
                SystemMessage(content=self.get_system_prompt()),
                HumanMessage(content=f"""
                Evaluate this venue against the requirements:
                
                Venue: {json.dumps(venue, indent=2)}
                Requirements: {json.dumps(requirements, indent=2)}
                
                Provide an evaluation including:
                1. Overall score (0-100)
                2. Pros and cons
                3. Budget fit assessment
                4. Capacity suitability
                5. Location assessment
                6. Amenities match
                7. Recommendations
                
                Return as a JSON object with these fields.
                """)
            ]
            
            response = await self.get_llm_response(messages)
            
            try:
                evaluation = json.loads(response)
                venue.update(evaluation)
                evaluated_venues.append(venue)
            except json.JSONDecodeError:
                # Add basic evaluation if parsing fails
                venue.update({
                    "score": 70,
                    "pros": ["Available", "Good location"],
                    "cons": ["Limited information"],
                    "recommendation": "Consider for further review"
                })
                evaluated_venues.append(venue)
        
        # Sort by score
        evaluated_venues.sort(key=lambda x: x.get("score", 0), reverse=True)
        
        return evaluated_venues
    
    async def _create_proposals(self, evaluated_venues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create detailed venue proposals."""
        proposals = []
        
        for venue in evaluated_venues[:3]:  # Top 3 venues
            messages = [
                SystemMessage(content=self.get_system_prompt()),
                HumanMessage(content=f"""
                Create a detailed proposal for this venue:
                {json.dumps(venue, indent=2)}
                
                Include:
                1. Executive summary
                2. Detailed venue analysis
                3. Cost breakdown
                4. Risk assessment
                5. Implementation timeline
                6. Final recommendation
                
                Return as a JSON object with these sections.
                """)
            ]
            
            response = await self.get_llm_response(messages)
            
            try:
                proposal = json.loads(response)
                proposal["venue_data"] = venue
                proposals.append(proposal)
            except json.JSONDecodeError:
                # Create basic proposal if parsing fails
                proposal = {
                    "executive_summary": f"Proposal for {venue.get('name', 'Unknown Venue')}",
                    "venue_analysis": venue,
                    "cost_breakdown": {"daily_rate": venue.get("daily_rate", 0)},
                    "risk_assessment": "Standard venue risks apply",
                    "timeline": "Immediate booking recommended",
                    "recommendation": "Proceed with booking",
                    "venue_data": venue
                }
                proposals.append(proposal)
        
        return proposals
    
    def _get_mock_venues(self, requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get mock venues for testing purposes."""
        location = requirements.get("location", "Unknown")
        capacity = requirements.get("capacity_required", 100)
        
        return [
            {
                "id": "venue_1",
                "name": f"{location} Convention Center",
                "address": f"123 Main St, {location}",
                "capacity": capacity + 50,
                "daily_rate": 5000,
                "amenities": ["WiFi", "AV Equipment", "Catering", "Parking"],
                "contact": "venue1@example.com",
                "availability": "Available"
            },
            {
                "id": "venue_2",
                "name": f"{location} Grand Hotel",
                "address": f"456 Oak Ave, {location}",
                "capacity": capacity,
                "daily_rate": 3000,
                "amenities": ["WiFi", "AV Equipment", "Catering", "Accommodation"],
                "contact": "venue2@example.com",
                "availability": "Available"
            },
            {
                "id": "venue_3",
                "name": f"{location} Business Center",
                "address": f"789 Pine St, {location}",
                "capacity": capacity - 20,
                "daily_rate": 2000,
                "amenities": ["WiFi", "AV Equipment"],
                "contact": "venue3@example.com",
                "availability": "Available"
            }
        ]
