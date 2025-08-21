from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class AttendeeExperienceAgent(BaseAgent):
    """AI agent responsible for managing attendee engagement and satisfaction."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "attendee_experience")
    
    def get_system_prompt(self) -> str:
        return """You are an Attendee Experience Agent specializing in creating exceptional event experiences and managing attendee satisfaction. 
        
        Your responsibilities include:
        1. Designing engaging attendee experiences and activities
        2. Managing registration and onboarding processes
        3. Creating networking opportunities and matchmaking
        4. Coordinating catering and hospitality services
        5. Managing attendee communications and support
        6. Collecting and analyzing attendee feedback
        7. Requesting human approval for major experience decisions
        
        Focus on creating memorable, valuable experiences that exceed attendee expectations. Prioritize personalization and engagement."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the attendee experience workflow."""
        event_data = context.get("event", {})
        other_agents_data = context.get("other_agents", {})
        
        await self.update_progress(10, "Analyzing attendee needs and preferences...")
        
        # Step 1: Analyze attendee needs and preferences
        attendee_analysis = await self._analyze_attendee_needs(event_data)
        await self.log_activity("Analyzed attendee needs", "info", attendee_analysis)
        
        await self.update_progress(25, "Designing attendee experience...")
        
        # Step 2: Design attendee experience
        experience_design = await self._design_attendee_experience(event_data, attendee_analysis)
        await self.log_activity("Designed attendee experience", "info", {"experience_type": experience_design.get("type", "Unknown")})
        
        await self.update_progress(40, "Planning networking activities...")
        
        # Step 3: Plan networking activities
        networking_plan = await self._plan_networking_activities(experience_design, event_data)
        await self.log_activity("Planned networking activities", "info", {"activity_count": len(networking_plan.get("activities", []))})
        
        await self.update_progress(60, "Coordinating hospitality services...")
        
        # Step 4: Coordinate hospitality services
        hospitality_plan = await self._coordinate_hospitality_services(experience_design, other_agents_data)
        
        await self.update_progress(80, "Creating communication strategy...")
        
        # Step 5: Create communication strategy
        communication_strategy = await self._create_communication_strategy(experience_design, event_data)
        
        await self.update_progress(90, "Requesting approval for experience plan...")
        
        # Step 6: Request approval for experience plan
        approval_id = await self.request_approval({
            "type": "attendee_experience_plan",
            "experience_design": experience_design,
            "networking_plan": networking_plan,
            "hospitality_plan": hospitality_plan,
            "communication_strategy": communication_strategy,
            "reasoning": "Comprehensive attendee experience design with networking, hospitality, and communication strategies"
        })
        
        await self.make_decision({
            "action": "experience_plan_proposed",
            "experience_id": experience_design.get("id"),
            "approval_id": approval_id,
            "confidence": 0.88
        })
        
        await self.update_progress(100, "Attendee experience workflow completed")
        
        return {
            "status": "completed",
            "attendee_analysis": attendee_analysis,
            "experience_design": experience_design,
            "networking_plan": networking_plan,
            "hospitality_plan": hospitality_plan,
            "communication_strategy": communication_strategy
        }
    
    async def _analyze_attendee_needs(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze attendee needs and preferences."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the attendee needs and preferences for this event:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Description: {event_data.get('description', 'No description provided')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Location: {event_data.get('city', 'Unknown')}, {event_data.get('country', 'Unknown')}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            - Duration: Calculate from start to end date
            
            Please provide a comprehensive attendee analysis including:
            1. Attendee personas and segments
            2. Primary goals and objectives
            3. Preferred learning styles and formats
            4. Networking preferences and needs
            5. Dietary and accessibility requirements
            6. Communication preferences
            7. Pain points and concerns
            8. Success metrics for attendees
            
            Return your analysis as a JSON object.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback to structured analysis if JSON parsing fails
            attendees = event_data.get('expected_attendees', 100)
            event_name = event_data.get('name', '').lower()
            
            # Determine attendee types based on event characteristics
            if 'tech' in event_name or 'ai' in event_name:
                primary_goal = "Learn about latest technology trends and innovations"
                learning_style = "Hands-on workshops and technical sessions"
            elif 'business' in event_name or 'conference' in event_name:
                primary_goal = "Gain business insights and professional development"
                learning_style = "Keynote presentations and panel discussions"
            else:
                primary_goal = "Professional development and networking"
                learning_style = "Mixed format with presentations and interactive sessions"
            
            return {
                "attendee_segments": [
                    {
                        "name": "Industry Leaders",
                        "percentage": 20,
                        "goals": ["Thought leadership", "Networking", "Industry insights"],
                        "preferences": ["VIP experiences", "Exclusive networking", "High-level content"]
                    },
                    {
                        "name": "Mid-level Professionals",
                        "percentage": 50,
                        "goals": ["Skill development", "Career advancement", "Networking"],
                        "preferences": ["Practical sessions", "Peer networking", "Mentorship opportunities"]
                    },
                    {
                        "name": "Emerging Professionals",
                        "percentage": 30,
                        "goals": ["Learning", "Networking", "Career exploration"],
                        "preferences": ["Interactive sessions", "Mentorship", "Career guidance"]
                    }
                ],
                "primary_goals": [
                    primary_goal,
                    "Networking and relationship building",
                    "Professional development and skill enhancement",
                    "Industry insights and trend analysis"
                ],
                "learning_preferences": {
                    "formats": ["Keynotes", "Breakout sessions", "Workshops", "Panel discussions"],
                    "styles": learning_style,
                    "interaction_level": "High engagement and participation"
                },
                "networking_needs": [
                    "Structured networking sessions",
                    "Industry-specific meetups",
                    "Mentorship matching",
                    "Social events and activities"
                ],
                "dietary_requirements": {
                    "vegetarian": 15,
                    "vegan": 5,
                    "gluten_free": 8,
                    "dairy_free": 6,
                    "other_allergies": 3
                },
                "accessibility_needs": [
                    "Wheelchair accessibility",
                    "Hearing assistance",
                    "Visual assistance",
                    "Quiet spaces",
                    "Mobility support"
                ],
                "communication_preferences": [
                    "Email updates",
                    "Mobile app notifications",
                    "Social media updates",
                    "SMS reminders"
                ],
                "pain_points": [
                    "Limited networking time",
                    "Information overload",
                    "Scheduling conflicts",
                    "Technical difficulties",
                    "Poor venue logistics"
                ],
                "success_metrics": [
                    "Learning satisfaction score",
                    "Networking connections made",
                    "Knowledge retention",
                    "Future event attendance",
                    "Recommendation likelihood"
                ]
            }
    
    async def _design_attendee_experience(self, event_data: Dict[str, Any], attendee_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Design comprehensive attendee experience."""
        attendees = event_data.get('expected_attendees', 100)
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Design a comprehensive attendee experience based on:
            
            Event Data: {json.dumps(event_data, indent=2)}
            Attendee Analysis: {json.dumps(attendee_analysis, indent=2)}
            Expected Attendees: {attendees}
            
            Create an experience design that includes:
            1. Pre-event engagement activities
            2. On-site experience flow
            3. Learning and development opportunities
            4. Networking and social activities
            5. Technology and digital tools
            6. Personalization and customization
            7. Post-event engagement
            8. Success measurement and feedback
            
            Return as a JSON object with the experience design structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            design = json.loads(response)
            design["id"] = f"experience_{self.agent_id}"
            return design
        except json.JSONDecodeError:
            # Create basic experience design if parsing fails
            return {
                "id": f"experience_{self.agent_id}",
                "type": "Engaging and interactive conference experience",
                "phases": {
                    "pre_event": {
                        "duration": "2-4 weeks before event",
                        "activities": [
                            "Welcome email series",
                            "Attendee profile creation",
                            "Networking introductions",
                            "Session preferences survey",
                            "Pre-event webinars"
                        ]
                    },
                    "on_site": {
                        "duration": "Event duration",
                        "activities": [
                            "Welcome reception",
                            "Interactive sessions",
                            "Structured networking",
                            "Social events",
                            "Wellness activities"
                        ]
                    },
                    "post_event": {
                        "duration": "2-4 weeks after event",
                        "activities": [
                            "Feedback collection",
                            "Content sharing",
                            "Networking follow-up",
                            "Community building",
                            "Future event planning"
                        ]
                    }
                },
                "learning_experience": {
                    "formats": [
                        "Keynote presentations",
                        "Interactive workshops",
                        "Panel discussions",
                        "Roundtable sessions",
                        "Hands-on labs"
                    ],
                    "personalization": [
                        "Track-based learning paths",
                        "Skill level matching",
                        "Interest-based recommendations",
                        "Custom schedules"
                    ]
                },
                "networking_experience": {
                    "structured_activities": [
                        "Speed networking",
                        "Industry meetups",
                        "Mentorship sessions",
                        "Peer learning groups"
                    ],
                    "social_activities": [
                        "Welcome reception",
                        "Networking breaks",
                        "Evening social events",
                        "Wellness activities"
                    ]
                },
                "technology_tools": [
                    "Event mobile app",
                    "Networking platform",
                    "Session feedback system",
                    "Digital content library",
                    "Virtual networking rooms"
                ],
                "personalization_features": [
                    "Customized schedules",
                    "Interest-based recommendations",
                    "Networking suggestions",
                    "Content preferences",
                    "Accessibility accommodations"
                ]
            }
    
    async def _plan_networking_activities(self, experience_design: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Plan networking activities and opportunities."""
        attendees = event_data.get('expected_attendees', 100)
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Plan networking activities based on this experience design:
            {json.dumps(experience_design, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            Expected Attendees: {attendees}
            
            Create networking activities including:
            1. Structured networking sessions
            2. Industry-specific meetups
            3. Mentorship and coaching opportunities
            4. Social and relationship-building activities
            5. Technology-enabled networking
            6. Follow-up and relationship maintenance
            
            For each activity, include:
            - Activity name and description
            - Target audience and group size
            - Duration and timing
            - Format and structure
            - Success metrics
            - Technology requirements
            
            Return as a JSON object with the networking plan structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic networking plan if parsing fails
            return {
                "structured_sessions": [
                    {
                        "name": "Speed Networking",
                        "description": "Quick introductions and connections",
                        "audience": "All attendees",
                        "group_size": 20,
                        "duration": "45 minutes",
                        "format": "Rotating pairs",
                        "timing": "Day 1 morning",
                        "metrics": ["Connections made", "Follow-up rate", "Satisfaction score"]
                    },
                    {
                        "name": "Industry Roundtables",
                        "description": "Deep-dive discussions by industry",
                        "audience": "Industry-specific groups",
                        "group_size": 8,
                        "duration": "60 minutes",
                        "format": "Facilitated discussion",
                        "timing": "Day 1 afternoon",
                        "metrics": ["Engagement level", "Knowledge sharing", "Relationship building"]
                    }
                ],
                "mentorship_activities": [
                    {
                        "name": "Mentor-Mentee Matching",
                        "description": "Structured mentorship sessions",
                        "audience": "Emerging professionals + leaders",
                        "group_size": "1:1 or small groups",
                        "duration": "30 minutes",
                        "format": "Guided conversations",
                        "timing": "Day 2",
                        "metrics": ["Mentorship satisfaction", "Follow-up meetings", "Career impact"]
                    }
                ],
                "social_activities": [
                    {
                        "name": "Welcome Reception",
                        "description": "Casual networking and socializing",
                        "audience": "All attendees",
                        "group_size": "Open",
                        "duration": "90 minutes",
                        "format": "Cocktail reception",
                        "timing": "Day 1 evening",
                        "metrics": ["Attendance", "Engagement", "Social connections"]
                    },
                    {
                        "name": "Networking Breaks",
                        "description": "Structured breaks for connections",
                        "audience": "All attendees",
                        "group_size": "Open",
                        "duration": "30 minutes",
                        "format": "Facilitated networking",
                        "timing": "Between sessions",
                        "metrics": ["Participation", "Connections made", "Satisfaction"]
                    }
                ],
                "technology_enabled": [
                    {
                        "name": "Digital Networking Platform",
                        "description": "AI-powered connection suggestions",
                        "features": ["Profile matching", "Interest-based suggestions", "Meeting scheduling"],
                        "timing": "Pre-event through post-event",
                        "metrics": ["Platform usage", "Connection success rate", "User satisfaction"]
                    }
                ]
            }
    
    async def _coordinate_hospitality_services(self, experience_design: Dict[str, Any], other_agents_data: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate hospitality and catering services."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Coordinate hospitality services based on this experience design:
            {json.dumps(experience_design, indent=2)}
            
            Other Agents Data: {json.dumps(other_agents_data, indent=2)}
            
            Plan hospitality services including:
            1. Catering and refreshments
            2. Dietary accommodations
            3. Accessibility services
            4. Comfort and wellness amenities
            5. Technology support
            6. Staffing and service coordination
            
            Consider coordination with:
            - Venue Scout (for venue capabilities)
            - Budget Controller (for cost management)
            - Logistics Agent (for service delivery)
            
            Return as a JSON object with the hospitality plan structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic hospitality plan if parsing fails
            return {
                "catering_services": {
                    "meals": [
                        {
                            "type": "Welcome breakfast",
                            "dietary_options": ["Standard", "Vegetarian", "Vegan", "Gluten-free"],
                            "timing": "Day 1 morning",
                            "special_requirements": ["Allergen labeling", "Nutritional information"]
                        },
                        {
                            "type": "Networking lunch",
                            "dietary_options": ["Standard", "Vegetarian", "Vegan", "Gluten-free"],
                            "timing": "Day 1 and 2 lunch",
                            "special_requirements": ["Allergen labeling", "Nutritional information"]
                        },
                        {
                            "type": "Coffee breaks",
                            "options": ["Coffee", "Tea", "Water", "Snacks"],
                            "timing": "Between sessions",
                            "special_requirements": ["Dairy alternatives", "Sugar-free options"]
                        }
                    ],
                    "dietary_accommodations": {
                        "vegetarian": "Available at all meals",
                        "vegan": "Available at all meals",
                        "gluten_free": "Available at all meals",
                        "dairy_free": "Available at all meals",
                        "nut_free": "Available at all meals"
                    }
                },
                "accessibility_services": {
                    "mobility": ["Wheelchair accessible venues", "Mobility assistance", "Accessible seating"],
                    "hearing": ["Hearing assistance devices", "Sign language interpreters", "Captioning services"],
                    "visual": ["Large print materials", "Braille materials", "Visual assistance"],
                    "cognitive": ["Quiet spaces", "Clear signage", "Simple instructions"]
                },
                "wellness_amenities": [
                    "Quiet rooms for breaks",
                    "Wellness activities (yoga, meditation)",
                    "Hydration stations",
                    "Comfortable seating areas",
                    "Natural lighting and ventilation"
                ],
                "technology_support": [
                    "WiFi access",
                    "Charging stations",
                    "Technical support desk",
                    "App assistance",
                    "Digital wayfinding"
                ],
                "staffing": {
                    "registration_desk": "Friendly and helpful staff",
                    "information_desk": "Knowledgeable event guides",
                    "technical_support": "IT specialists",
                    "accessibility_support": "Trained accessibility assistants"
                }
            }
    
    async def _create_communication_strategy(self, experience_design: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create communication strategy for attendees."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create a communication strategy for attendees based on this experience design:
            {json.dumps(experience_design, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            
            Develop a communication strategy including:
            1. Pre-event communications
            2. On-site communications
            3. Post-event communications
            4. Emergency and urgent communications
            5. Personalization and segmentation
            6. Multi-channel approach
            7. Feedback and response mechanisms
            
            For each communication type, include:
            - Purpose and objectives
            - Target audience
            - Timing and frequency
            - Channels and formats
            - Content themes
            - Success metrics
            
            Return as a JSON object with the communication strategy structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic communication strategy if parsing fails
            return {
                "pre_event_communications": {
                    "welcome_series": {
                        "purpose": "Build excitement and prepare attendees",
                        "audience": "All registered attendees",
                        "timing": "2-4 weeks before event",
                        "frequency": "Weekly",
                        "channels": ["Email", "Mobile app"],
                        "content": ["Event overview", "Speaker introductions", "Networking tips", "Logistics information"]
                    },
                    "personalized_updates": {
                        "purpose": "Provide personalized information",
                        "audience": "Segmented by interests and preferences",
                        "timing": "1-2 weeks before event",
                        "frequency": "As needed",
                        "channels": ["Email", "Mobile app"],
                        "content": ["Custom schedules", "Interest-based recommendations", "Networking suggestions"]
                    }
                },
                "on_site_communications": {
                    "daily_updates": {
                        "purpose": "Keep attendees informed and engaged",
                        "audience": "All attendees",
                        "timing": "Daily during event",
                        "frequency": "Daily",
                        "channels": ["Mobile app", "Digital displays", "Announcements"],
                        "content": ["Daily schedule", "Weather updates", "Special announcements", "Networking opportunities"]
                    },
                    "real_time_alerts": {
                        "purpose": "Urgent communications and updates",
                        "audience": "All attendees",
                        "timing": "As needed",
                        "frequency": "Immediate",
                        "channels": ["Mobile app push notifications", "SMS", "Announcements"],
                        "content": ["Schedule changes", "Emergency information", "Important updates"]
                    }
                },
                "post_event_communications": {
                    "feedback_collection": {
                        "purpose": "Gather attendee feedback and insights",
                        "audience": "All attendees",
                        "timing": "Immediately after event",
                        "frequency": "Once",
                        "channels": ["Email", "Mobile app"],
                        "content": ["Event feedback survey", "Session ratings", "Networking feedback", "Suggestions for improvement"]
                    },
                    "content_sharing": {
                        "purpose": "Share event content and maintain engagement",
                        "audience": "All attendees",
                        "timing": "1-2 weeks after event",
                        "frequency": "Weekly for 4 weeks",
                        "channels": ["Email", "Mobile app", "Social media"],
                        "content": ["Session recordings", "Presentation slides", "Photo galleries", "Networking follow-ups"]
                    }
                },
                "personalization": {
                    "segmentation": ["By role", "By industry", "By interests", "By experience level"],
                    "customization": ["Personalized schedules", "Interest-based content", "Networking suggestions", "Custom communications"]
                },
                "channels": {
                    "primary": ["Email", "Mobile app"],
                    "secondary": ["SMS", "Social media", "Digital displays"],
                    "emergency": ["Push notifications", "SMS", "Announcements"]
                },
                "success_metrics": [
                    "Communication open rates",
                    "Engagement with content",
                    "Feedback response rates",
                    "Attendee satisfaction with communications",
                    "Information retention and action"
                ]
            }
