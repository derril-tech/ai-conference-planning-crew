from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class LogisticsTravelAgent(BaseAgent):
    """AI agent responsible for managing event logistics, travel arrangements, and operational coordination."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "logistics_travel")
    
    def get_system_prompt(self) -> str:
        return """You are a Logistics & Travel Agent specializing in event logistics management and travel coordination. 
        
        Your responsibilities include:
        1. Planning and coordinating event logistics and operations
        2. Managing travel arrangements for speakers and attendees
        3. Coordinating vendor services and equipment
        4. Creating run-of-show and operational plans
        5. Managing on-site logistics and incident response
        6. Coordinating with venue and service providers
        7. Requesting human approval for major logistics decisions
        
        Focus on operational excellence, risk mitigation, and seamless event execution. Prioritize safety, efficiency, and attendee experience."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the logistics and travel workflow."""
        event_data = context.get("event", {})
        other_agents_data = context.get("other_agents", {})
        
        await self.update_progress(10, "Analyzing logistics requirements...")
        
        # Step 1: Analyze logistics requirements
        logistics_analysis = await self._analyze_logistics_requirements(event_data)
        await self.log_activity("Analyzed logistics requirements", "info", logistics_analysis)
        
        await self.update_progress(25, "Planning travel arrangements...")
        
        # Step 2: Plan travel arrangements
        travel_plan = await self._plan_travel_arrangements(event_data, other_agents_data)
        await self.log_activity("Planned travel arrangements", "info", {"travel_plan_id": travel_plan.get("id", "Unknown")})
        
        await self.update_progress(40, "Coordinating vendor services...")
        
        # Step 3: Coordinate vendor services
        vendor_coordination = await self._coordinate_vendor_services(logistics_analysis, event_data)
        await self.log_activity("Coordinated vendor services", "info", {"vendor_count": len(vendor_coordination.get("vendors", []))})
        
        await self.update_progress(60, "Creating operational plans...")
        
        # Step 4: Create operational plans
        operational_plans = await self._create_operational_plans(logistics_analysis, travel_plan, vendor_coordination)
        
        await self.update_progress(80, "Planning incident response...")
        
        # Step 5: Plan incident response
        incident_response = await self._plan_incident_response(operational_plans, event_data)
        
        await self.update_progress(90, "Requesting approval for logistics plan...")
        
        # Step 6: Request approval for logistics plan
        approval_id = await self.request_approval({
            "type": "logistics_plan",
            "logistics_analysis": logistics_analysis,
            "travel_plan": travel_plan,
            "vendor_coordination": vendor_coordination,
            "operational_plans": operational_plans,
            "incident_response": incident_response,
            "reasoning": "Comprehensive logistics and travel plan with operational coordination and incident response"
        })
        
        await self.make_decision({
            "action": "logistics_plan_proposed",
            "logistics_id": logistics_analysis.get("id"),
            "approval_id": approval_id,
            "confidence": 0.87
        })
        
        await self.update_progress(100, "Logistics and travel workflow completed")
        
        return {
            "status": "completed",
            "logistics_analysis": logistics_analysis,
            "travel_plan": travel_plan,
            "vendor_coordination": vendor_coordination,
            "operational_plans": operational_plans,
            "incident_response": incident_response
        }
    
    async def _analyze_logistics_requirements(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze logistics requirements for the event."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the logistics requirements for this event:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Description: {event_data.get('description', 'No description provided')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Location: {event_data.get('city', 'Unknown')}, {event_data.get('country', 'Unknown')}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            - Venue: {event_data.get('venue_name', 'Unknown')}
            
            Please provide a comprehensive logistics analysis including:
            1. Venue and facility requirements
            2. Equipment and technology needs
            3. Staffing and personnel requirements
            4. Transportation and parking needs
            5. Catering and hospitality logistics
            6. Security and safety requirements
            7. Communication and coordination needs
            8. Risk factors and contingency planning
            
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
            
            # Determine logistics complexity based on event characteristics
            if attendees > 500:
                complexity = "High"
                staffing_needs = "Large team with specialized roles"
            elif attendees > 200:
                complexity = "Medium"
                staffing_needs = "Moderate team with key roles"
            else:
                complexity = "Low"
                staffing_needs = "Small team with general roles"
            
            return {
                "id": f"logistics_{self.agent_id}",
                "complexity_level": complexity,
                "venue_requirements": {
                    "capacity": attendees,
                    "rooms_needed": max(3, attendees // 50),
                    "setup_time": "4-6 hours",
                    "teardown_time": "2-3 hours",
                    "accessibility": "Full accessibility compliance required"
                },
                "equipment_needs": {
                    "av_equipment": ["Projectors", "Screens", "Sound system", "Microphones", "Lighting"],
                    "technology": ["WiFi infrastructure", "Charging stations", "Registration system", "Mobile app support"],
                    "furniture": ["Chairs", "Tables", "Podiums", "Signage", "Registration desks"],
                    "specialized": ["Streaming equipment", "Recording devices", "Translation equipment"]
                },
                "staffing_requirements": {
                    "event_coordinator": 1,
                    "av_technicians": max(1, attendees // 200),
                    "registration_staff": max(2, attendees // 100),
                    "security_personnel": max(1, attendees // 300),
                    "catering_staff": "Provided by vendor",
                    "volunteers": max(5, attendees // 50)
                },
                "transportation_needs": {
                    "parking": f"Space for {attendees} vehicles",
                    "shuttle_service": attendees > 200,
                    "public_transport": "Information and directions",
                    "accessibility_transport": "Wheelchair accessible options"
                },
                "catering_logistics": {
                    "meal_service": ["Breakfast", "Lunch", "Coffee breaks"],
                    "dietary_accommodations": ["Vegetarian", "Vegan", "Gluten-free", "Allergen-free"],
                    "service_staff": "Coordinated with catering vendor",
                    "timing": "Aligned with event schedule"
                },
                "security_requirements": {
                    "access_control": "Registration check-in system",
                    "emergency_procedures": "Evacuation plans and emergency contacts",
                    "medical_support": "First aid station and medical personnel",
                    "incident_response": "Designated response team"
                },
                "communication_needs": {
                    "internal_communication": ["Radios", "Mobile phones", "Digital platforms"],
                    "attendee_communication": ["Announcements", "Digital displays", "Mobile app"],
                    "emergency_communication": ["Emergency alerts", "SMS notifications", "Public address system"]
                },
                "risk_factors": [
                    "Weather-related disruptions",
                    "Technical equipment failures",
                    "Staffing shortages",
                    "Transportation delays",
                    "Security incidents",
                    "Health emergencies"
                ],
                "contingency_plans": [
                    "Backup venue options",
                    "Equipment redundancy",
                    "Staff backup plans",
                    "Alternative transportation",
                    "Emergency response procedures"
                ]
            }
    
    async def _plan_travel_arrangements(self, event_data: Dict[str, Any], other_agents_data: Dict[str, Any]) -> Dict[str, Any]:
        """Plan travel arrangements for speakers and attendees."""
        attendees = event_data.get('expected_attendees', 100)
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Plan travel arrangements based on:
            
            Event Data: {json.dumps(event_data, indent=2)}
            Other Agents Data: {json.dumps(other_agents_data, indent=2)}
            Expected Attendees: {attendees}
            
            Create travel arrangements including:
            1. Speaker travel coordination
            2. Attendee travel information
            3. Hotel accommodations
            4. Transportation services
            5. Travel documentation
            6. Cost management
            7. Contingency planning
            
            Consider coordination with:
            - Speaker Outreach Agent (for speaker travel needs)
            - Venue Scout (for venue location and accessibility)
            - Budget Controller (for travel cost management)
            
            Return as a JSON object with the travel plan structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            travel_plan = json.loads(response)
            travel_plan["id"] = f"travel_{self.agent_id}"
            return travel_plan
        except json.JSONDecodeError:
            # Create basic travel plan if parsing fails
            return {
                "id": f"travel_{self.agent_id}",
                "speaker_travel": {
                    "coordination": "Direct coordination with speakers",
                    "arrangements": [
                        "Flight bookings (economy/business based on speaker tier)",
                        "Hotel accommodations (3-4 star properties)",
                        "Ground transportation (airport transfers, local travel)",
                        "Travel insurance coverage",
                        "Visa assistance (if international)"
                    ],
                    "timing": "Booked 2-3 months in advance",
                    "cost_management": "Negotiated rates and group discounts"
                },
                "attendee_travel": {
                    "information_provided": [
                        "Venue location and directions",
                        "Public transportation options",
                        "Parking information",
                        "Hotel recommendations",
                        "Local attractions and dining"
                    ],
                    "accommodation_blocks": [
                        {
                            "hotel_name": "Event Hotel Block",
                            "room_types": ["Standard", "Deluxe", "Suite"],
                            "rates": "Negotiated group rates",
                            "booking_deadline": "1 month before event",
                            "cancellation_policy": "Flexible cancellation"
                        }
                    ],
                    "transportation_services": [
                        "Airport shuttle service (if needed)",
                        "Local taxi and rideshare information",
                        "Public transportation passes",
                        "Walking directions and maps"
                    ]
                },
                "travel_documentation": {
                    "speakers": [
                        "Travel itineraries",
                        "Hotel confirmations",
                        "Transportation vouchers",
                        "Emergency contact information"
                    ],
                    "attendees": [
                        "Travel information packet",
                        "Venue directions",
                        "Local transportation guide",
                        "Emergency contact information"
                    ]
                },
                "cost_management": {
                    "speaker_travel_budget": "Allocated per speaker tier",
                    "attendee_subsidies": "Limited subsidies for key attendees",
                    "group_discounts": "Negotiated with airlines and hotels",
                    "travel_insurance": "Comprehensive coverage for speakers"
                },
                "contingency_planning": {
                    "flight_delays": "Backup travel options and communication",
                    "weather_disruptions": "Alternative travel routes and timing",
                    "accommodation_issues": "Backup hotel options",
                    "emergency_support": "24/7 travel support hotline"
                }
            }
    
    async def _coordinate_vendor_services(self, logistics_analysis: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate vendor services and equipment."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Coordinate vendor services based on this logistics analysis:
            {json.dumps(logistics_analysis, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            
            Coordinate vendor services including:
            1. AV and technology vendors
            2. Catering services
            3. Furniture and equipment rental
            4. Security services
            5. Transportation services
            6. Staffing agencies
            7. Insurance providers
            
            For each vendor, include:
            - Vendor selection criteria
            - Service requirements and specifications
            - Contract terms and conditions
            - Quality assurance measures
            - Backup vendor options
            - Cost management strategies
            
            Return as a JSON object with the vendor coordination structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic vendor coordination if parsing fails
            attendees = event_data.get('expected_attendees', 100)
            
            return {
                "vendors": [
                    {
                        "type": "AV and Technology",
                        "services": ["Sound system", "Projectors", "Lighting", "WiFi", "Streaming equipment"],
                        "selection_criteria": ["Experience", "Equipment quality", "Technical support", "Cost"],
                        "contract_terms": "Service agreement with performance guarantees",
                        "backup_options": "Secondary AV vendor on standby",
                        "quality_assurance": "Pre-event testing and rehearsal"
                    },
                    {
                        "type": "Catering Services",
                        "services": ["Meals", "Coffee breaks", "Special dietary options"],
                        "selection_criteria": ["Food quality", "Service reliability", "Dietary accommodation", "Cost"],
                        "contract_terms": "Fixed menu with dietary options",
                        "backup_options": "Alternative catering vendor",
                        "quality_assurance": "Menu tasting and service rehearsal"
                    },
                    {
                        "type": "Furniture and Equipment",
                        "services": ["Chairs", "Tables", "Podiums", "Signage"],
                        "selection_criteria": ["Quality", "Availability", "Delivery reliability", "Cost"],
                        "contract_terms": "Rental agreement with delivery timeline",
                        "backup_options": "Multiple rental companies",
                        "quality_assurance": "Equipment inspection upon delivery"
                    },
                    {
                        "type": "Security Services",
                        "services": ["Access control", "Emergency response", "Crowd management"],
                        "selection_criteria": ["Licensed personnel", "Experience", "Response time", "Cost"],
                        "contract_terms": "Security service agreement",
                        "backup_options": "Additional security personnel",
                        "quality_assurance": "Security briefing and emergency procedures"
                    },
                    {
                        "type": "Transportation Services",
                        "services": ["Airport transfers", "Local transportation", "Parking management"],
                        "selection_criteria": ["Vehicle quality", "Driver professionalism", "Reliability", "Cost"],
                        "contract_terms": "Transportation service agreement",
                        "backup_options": "Multiple transportation providers",
                        "quality_assurance": "Driver briefing and route planning"
                    }
                ],
                "coordination_timeline": {
                    "vendor_selection": "3-4 months before event",
                    "contract_negotiation": "2-3 months before event",
                    "service_confirmation": "1 month before event",
                    "final_coordination": "1 week before event"
                },
                "quality_management": {
                    "vendor_meetings": "Regular coordination meetings",
                    "service_rehearsals": "Pre-event testing and rehearsal",
                    "performance_monitoring": "Real-time service quality monitoring",
                    "feedback_collection": "Post-event vendor evaluation"
                },
                "cost_management": {
                    "competitive_bidding": "Multiple vendor quotes",
                    "negotiated_rates": "Volume discounts and package deals",
                    "cost_tracking": "Real-time cost monitoring and reporting",
                    "budget_controls": "Approval process for additional costs"
                }
            }
    
    async def _create_operational_plans(self, logistics_analysis: Dict[str, Any], travel_plan: Dict[str, Any], vendor_coordination: Dict[str, Any]) -> Dict[str, Any]:
        """Create operational plans for event execution."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create operational plans based on:
            
            Logistics Analysis: {json.dumps(logistics_analysis, indent=2)}
            Travel Plan: {json.dumps(travel_plan, indent=2)}
            Vendor Coordination: {json.dumps(vendor_coordination, indent=2)}
            
            Create operational plans including:
            1. Run-of-show schedule
            2. Staffing schedules and assignments
            3. Equipment setup and teardown
            4. Vendor coordination timeline
            5. Communication protocols
            6. Quality control procedures
            7. Performance monitoring
            
            For each plan, include:
            - Detailed timeline and milestones
            - Responsibility assignments
            - Quality checkpoints
            - Communication protocols
            - Success metrics
            
            Return as a JSON object with the operational plans structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic operational plans if parsing fails
            return {
                "run_of_show": {
                    "pre_event_day": {
                        "timeline": [
                            "8:00 AM - Vendor setup begins",
                            "10:00 AM - Equipment testing",
                            "2:00 PM - Staff briefing",
                            "4:00 PM - Final walkthrough",
                            "6:00 PM - Setup completion"
                        ],
                        "responsibilities": {
                            "event_coordinator": "Overall coordination",
                            "av_technicians": "Equipment setup and testing",
                            "vendor_coordinator": "Vendor management",
                            "security": "Access control setup"
                        }
                    },
                    "event_day_1": {
                        "timeline": [
                            "6:00 AM - Staff arrival",
                            "7:00 AM - Final preparations",
                            "8:00 AM - Registration opens",
                            "9:00 AM - Event begins",
                            "5:00 PM - Day 1 concludes"
                        ],
                        "responsibilities": {
                            "registration_staff": "Attendee check-in",
                            "av_technicians": "Technical support",
                            "catering_staff": "Meal service",
                            "security": "Crowd management"
                        }
                    },
                    "event_day_2": {
                        "timeline": [
                            "7:00 AM - Staff arrival",
                            "8:00 AM - Event continues",
                            "5:00 PM - Event concludes",
                            "6:00 PM - Teardown begins"
                        ],
                        "responsibilities": {
                            "all_staff": "Event execution",
                            "teardown_crew": "Equipment removal",
                            "cleanup_crew": "Venue cleanup"
                        }
                    }
                },
                "staffing_schedule": {
                    "roles_and_shifts": [
                        {
                            "role": "Event Coordinator",
                            "shifts": ["Full event duration"],
                            "responsibilities": ["Overall coordination", "Issue resolution", "Vendor management"]
                        },
                        {
                            "role": "AV Technicians",
                            "shifts": ["Setup day", "Event days"],
                            "responsibilities": ["Equipment operation", "Technical support", "Troubleshooting"]
                        },
                        {
                            "role": "Registration Staff",
                            "shifts": ["Event days"],
                            "responsibilities": ["Attendee check-in", "Information desk", "Support"]
                        }
                    ],
                    "training": "Pre-event staff training and briefing",
                    "supervision": "On-site supervision and support"
                },
                "equipment_management": {
                    "setup_timeline": "4-6 hours before event",
                    "testing_procedures": "Comprehensive equipment testing",
                    "backup_equipment": "Critical equipment redundancy",
                    "teardown_procedures": "Organized equipment removal"
                },
                "communication_protocols": {
                    "internal_communication": ["Radios", "Mobile phones", "Digital platforms"],
                    "emergency_communication": ["Emergency alerts", "SMS notifications"],
                    "attendee_communication": ["Announcements", "Digital displays"],
                    "vendor_communication": "Dedicated vendor coordinator"
                },
                "quality_control": {
                    "pre_event_checks": "Comprehensive venue and equipment inspection",
                    "during_event_monitoring": "Real-time quality monitoring",
                    "post_event_evaluation": "Comprehensive event evaluation",
                    "feedback_collection": "Staff and attendee feedback"
                }
            }
    
    async def _plan_incident_response(self, operational_plans: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Plan incident response and emergency procedures."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Plan incident response based on these operational plans:
            {json.dumps(operational_plans, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            
            Create incident response plans including:
            1. Emergency procedures and protocols
            2. Incident classification and response levels
            3. Communication protocols for emergencies
            4. Medical and safety response
            5. Technical incident response
            6. Weather and natural disaster response
            7. Security incident response
            8. Recovery and business continuity
            
            For each incident type, include:
            - Response procedures
            - Communication protocols
            - Escalation procedures
            - Recovery procedures
            - Prevention measures
            
            Return as a JSON object with the incident response structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic incident response if parsing fails
            return {
                "emergency_procedures": {
                    "evacuation_plan": {
                        "triggers": ["Fire alarm", "Severe weather", "Security threat"],
                        "procedures": ["Clear announcement", "Orderly evacuation", "Assembly point"],
                        "communication": ["Public address system", "Staff guidance", "Emergency services"]
                    },
                    "medical_emergency": {
                        "response": ["First aid", "Emergency services call", "Medical personnel"],
                        "communication": ["Designated medical contact", "Emergency services", "Event coordinator"],
                        "documentation": ["Incident report", "Medical records", "Follow-up"]
                    }
                },
                "incident_classification": {
                    "level_1": {
                        "description": "Minor incidents",
                        "examples": ["Equipment malfunction", "Minor injury", "Weather delay"],
                        "response": "On-site staff response",
                        "escalation": "Event coordinator notification"
                    },
                    "level_2": {
                        "description": "Moderate incidents",
                        "examples": ["Major equipment failure", "Medical emergency", "Security concern"],
                        "response": "Coordinated team response",
                        "escalation": "Management notification"
                    },
                    "level_3": {
                        "description": "Major incidents",
                        "examples": ["Evacuation required", "Severe weather", "Security threat"],
                        "response": "Emergency services response",
                        "escalation": "Senior management and authorities"
                    }
                },
                "technical_incidents": {
                    "av_failure": {
                        "response": ["Backup equipment", "Technical support", "Alternative presentation"],
                        "communication": ["Speaker notification", "Attendee announcement", "Technical team"]
                    },
                    "power_outage": {
                        "response": ["Backup power", "Emergency lighting", "Venue assessment"],
                        "communication": ["Venue management", "Attendee notification", "Emergency services"]
                    },
                    "internet_failure": {
                        "response": ["Backup connectivity", "Offline alternatives", "Technical support"],
                        "communication": ["IT team", "Attendee notification", "Vendor coordination"]
                    }
                },
                "weather_response": {
                    "severe_weather": {
                        "monitoring": "Weather service alerts",
                        "response": ["Indoor alternatives", "Schedule adjustment", "Communication"],
                        "communication": ["Attendee notification", "Venue coordination", "Emergency services"]
                    },
                    "transportation_disruption": {
                        "response": ["Alternative transportation", "Schedule adjustment", "Communication"],
                        "communication": ["Transportation providers", "Attendee notification", "Venue coordination"]
                    }
                },
                "security_incidents": {
                    "unauthorized_access": {
                        "response": ["Security intervention", "Access control", "Authority notification"],
                        "communication": ["Security team", "Event coordinator", "Authorities if needed"]
                    },
                    "suspicious_activity": {
                        "response": ["Security assessment", "Investigation", "Preventive measures"],
                        "communication": ["Security team", "Event coordinator", "Authorities if needed"]
                    }
                },
                "recovery_procedures": {
                    "incident_documentation": "Comprehensive incident reporting",
                    "follow_up_actions": "Corrective and preventive measures",
                    "communication": "Stakeholder notification and updates",
                    "lessons_learned": "Process improvement and training"
                },
                "prevention_measures": [
                    "Pre-event risk assessment",
                    "Staff training and certification",
                    "Equipment maintenance and testing",
                    "Vendor qualification and monitoring",
                    "Regular safety inspections"
                ]
            }
