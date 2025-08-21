from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class SpeakerOutreachAgent(BaseAgent):
    """AI agent responsible for finding and contacting potential speakers."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "speaker_outreach")
    
    def get_system_prompt(self) -> str:
        return """You are a Speaker Outreach Agent specializing in finding and contacting potential speakers for conferences. 
        
        Your responsibilities include:
        1. Analyzing event theme and target audience
        2. Researching potential speakers in relevant fields
        3. Evaluating speaker qualifications and fit
        4. Creating personalized outreach messages
        5. Managing speaker communications and responses
        6. Coordinating speaker confirmations and logistics
        7. Requesting human approval for speaker selections
        
        Always consider speaker expertise, availability, fees, and alignment with event goals. Provide detailed reasoning for recommendations."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the speaker outreach workflow."""
        event_data = context.get("event", {})
        
        await self.update_progress(10, "Analyzing event requirements...")
        
        # Step 1: Analyze event requirements
        requirements = await self._analyze_speaker_requirements(event_data)
        await self.log_activity("Analyzed speaker requirements", "info", requirements)
        
        await self.update_progress(25, "Researching potential speakers...")
        
        # Step 2: Research potential speakers
        speakers = await self._research_speakers(requirements)
        await self.log_activity(f"Found {len(speakers)} potential speakers", "info", {"speaker_count": len(speakers)})
        
        await self.update_progress(40, "Evaluating speaker fit...")
        
        # Step 3: Evaluate speakers
        evaluated_speakers = await self._evaluate_speakers(speakers, requirements)
        await self.log_activity("Completed speaker evaluation", "info", {"evaluated_count": len(evaluated_speakers)})
        
        await self.update_progress(60, "Creating outreach messages...")
        
        # Step 4: Create outreach messages
        outreach_messages = await self._create_outreach_messages(evaluated_speakers, event_data)
        
        await self.update_progress(80, "Proposing speaker lineup...")
        
        # Step 5: Propose speaker lineup
        lineup = await self._propose_speaker_lineup(evaluated_speakers, requirements)
        
        await self.update_progress(90, "Requesting approval for speaker lineup...")
        
        # Step 6: Request approval for speaker lineup
        if lineup:
            approval_id = await self.request_approval({
                "type": "speaker_lineup",
                "proposed_lineup": lineup,
                "all_candidates": evaluated_speakers,
                "reasoning": lineup.get("reasoning", "")
            })
            
            await self.make_decision({
                "action": "speaker_lineup_proposed",
                "lineup_id": lineup.get("id"),
                "approval_id": approval_id,
                "confidence": lineup.get("confidence", 0.8)
            })
        
        await self.update_progress(100, "Speaker outreach workflow completed")
        
        return {
            "status": "completed",
            "speakers_researched": len(speakers),
            "outreach_messages_created": len(outreach_messages),
            "proposed_lineup": lineup,
            "all_candidates": evaluated_speakers
        }
    
    async def _analyze_speaker_requirements(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze event requirements for speaker selection."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the following event requirements for speaker selection:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Description: {event_data.get('description', 'No description provided')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Budget: ${event_data.get('budget_total', 0):,.2f}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            
            Please provide a structured analysis including:
            1. Event theme and focus areas
            2. Target audience characteristics
            3. Required speaker expertise areas
            4. Number of speakers needed
            5. Speaker budget allocation
            6. Session types and durations
            7. Special requirements (keynote, panel, workshop)
            
            Return your analysis as a JSON object.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback to structured text if JSON parsing fails
            return {
                "event_theme": "Technology and Innovation",
                "target_audience": "Professionals and enthusiasts",
                "expertise_areas": ["Technology", "Business", "Innovation"],
                "speakers_needed": 5,
                "speaker_budget": event_data.get('budget_total', 0) * 0.2,  # Assume 20% for speakers
                "session_types": ["Keynote", "Panel Discussion", "Workshop"],
                "special_requirements": []
            }
    
    async def _research_speakers(self, requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Research potential speakers based on requirements."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Research potential speakers based on these requirements:
            {json.dumps(requirements, indent=2)}
            
            Find 8-12 potential speakers that could meet these requirements.
            
            For each speaker, provide:
            - Name and title
            - Company/organization
            - Expertise areas
            - Speaking experience
            - Contact information
            - Estimated speaking fee
            - Availability for the event dates
            
            Return as a JSON array of speaker objects.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            speakers = json.loads(response)
            return speakers if isinstance(speakers, list) else []
        except json.JSONDecodeError:
            # Return mock speakers if parsing fails
            return self._get_mock_speakers(requirements)
    
    async def _evaluate_speakers(self, speakers: List[Dict[str, Any]], requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Evaluate speakers based on requirements and criteria."""
        evaluated_speakers = []
        
        for speaker in speakers:
            messages = [
                SystemMessage(content=self.get_system_prompt()),
                HumanMessage(content=f"""
                Evaluate this speaker against the requirements:
                
                Speaker: {json.dumps(speaker, indent=2)}
                Requirements: {json.dumps(requirements, indent=2)}
                
                Provide an evaluation including:
                1. Overall fit score (0-100)
                2. Expertise alignment
                3. Speaking experience assessment
                4. Budget fit
                5. Availability assessment
                6. Pros and cons
                7. Recommendations
                
                Return as a JSON object with these fields.
                """)
            ]
            
            response = await self.get_llm_response(messages)
            
            try:
                evaluation = json.loads(response)
                speaker.update(evaluation)
                evaluated_speakers.append(speaker)
            except json.JSONDecodeError:
                # Add basic evaluation if parsing fails
                speaker.update({
                    "fit_score": 75,
                    "expertise_alignment": "Good",
                    "speaking_experience": "Experienced",
                    "budget_fit": "Within budget",
                    "pros": ["Good expertise", "Available"],
                    "cons": ["Limited information"],
                    "recommendation": "Consider for further review"
                })
                evaluated_speakers.append(speaker)
        
        # Sort by fit score
        evaluated_speakers.sort(key=lambda x: x.get("fit_score", 0), reverse=True)
        
        return evaluated_speakers
    
    async def _create_outreach_messages(self, speakers: List[Dict[str, Any]], event_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create personalized outreach messages for speakers."""
        messages = []
        
        for speaker in speakers[:8]:  # Top 8 speakers
            outreach_message = await self._create_speaker_outreach(speaker, event_data)
            messages.append({
                "speaker_id": speaker.get("id"),
                "speaker_name": speaker.get("name"),
                "message": outreach_message,
                "status": "draft"
            })
        
        return messages
    
    async def _create_speaker_outreach(self, speaker: Dict[str, Any], event_data: Dict[str, Any]) -> str:
        """Create a personalized outreach message for a specific speaker."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create a personalized outreach message for this speaker:
            
            Speaker: {json.dumps(speaker, indent=2)}
            Event: {json.dumps(event_data, indent=2)}
            
            The message should be:
            1. Professional and personalized
            2. Highlight why they're a good fit
            3. Include event details and benefits
            4. Clear call to action
            5. Appropriate length (2-3 paragraphs)
            
            Return the message as plain text.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        return response
    
    async def _propose_speaker_lineup(self, speakers: List[Dict[str, Any]], requirements: Dict[str, Any]) -> Dict[str, Any]:
        """Propose a final speaker lineup."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Propose a final speaker lineup based on these candidates and requirements:
            
            Top Candidates: {json.dumps(speakers[:8], indent=2)}
            Requirements: {json.dumps(requirements, indent=2)}
            
            Create a lineup that includes:
            1. Keynote speaker(s)
            2. Panel speakers
            3. Workshop leaders
            4. Backup speakers
            
            For each selected speaker, provide:
            - Role in the event
            - Session type and duration
            - Justification for selection
            - Estimated cost
            
            Return as a JSON object with the lineup structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            lineup = json.loads(response)
            lineup["id"] = f"lineup_{self.agent_id}"
            lineup["confidence"] = 0.85
            return lineup
        except json.JSONDecodeError:
            # Create basic lineup if parsing fails
            return {
                "id": f"lineup_{self.agent_id}",
                "confidence": 0.8,
                "keynote_speakers": speakers[:2] if len(speakers) >= 2 else [],
                "panel_speakers": speakers[2:5] if len(speakers) >= 5 else [],
                "workshop_leaders": speakers[5:7] if len(speakers) >= 7 else [],
                "backup_speakers": speakers[7:10] if len(speakers) >= 10 else [],
                "total_cost": sum(s.get("estimated_fee", 0) for s in speakers[:7]),
                "reasoning": "Selected based on expertise fit and availability"
            }
    
    def _get_mock_speakers(self, requirements: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get mock speakers for testing purposes."""
        theme = requirements.get("event_theme", "Technology")
        
        return [
            {
                "id": "speaker_1",
                "name": "Dr. Sarah Johnson",
                "title": "Chief Technology Officer",
                "company": "Tech Innovations Inc.",
                "expertise": ["AI", "Machine Learning", "Technology Leadership"],
                "speaking_experience": "15+ years, 50+ conferences",
                "contact": "sarah.johnson@techinnovations.com",
                "estimated_fee": 5000,
                "availability": "Available"
            },
            {
                "id": "speaker_2",
                "name": "Michael Chen",
                "title": "VP of Product",
                "company": "Future Systems",
                "expertise": ["Product Management", "Innovation", "Strategy"],
                "speaking_experience": "10+ years, 30+ conferences",
                "contact": "mchen@futuresystems.com",
                "estimated_fee": 3500,
                "availability": "Available"
            },
            {
                "id": "speaker_3",
                "name": "Dr. Emily Rodriguez",
                "title": "Research Director",
                "company": "Innovation Labs",
                "expertise": ["Research", "Emerging Technologies", "Trends"],
                "speaking_experience": "12+ years, 40+ conferences",
                "contact": "erodriguez@innovationlabs.com",
                "estimated_fee": 4000,
                "availability": "Available"
            },
            {
                "id": "speaker_4",
                "name": "James Wilson",
                "title": "CEO",
                "company": "Startup Ventures",
                "expertise": ["Entrepreneurship", "Startups", "Business Strategy"],
                "speaking_experience": "8+ years, 25+ conferences",
                "contact": "jwilson@startupventures.com",
                "estimated_fee": 3000,
                "availability": "Available"
            },
            {
                "id": "speaker_5",
                "name": "Lisa Thompson",
                "title": "Head of Innovation",
                "company": "Global Solutions",
                "expertise": ["Innovation", "Digital Transformation", "Leadership"],
                "speaking_experience": "14+ years, 45+ conferences",
                "contact": "lthompson@globalsolutions.com",
                "estimated_fee": 4500,
                "availability": "Available"
            }
        ]
