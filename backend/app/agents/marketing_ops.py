from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class MarketingOpsAgent(BaseAgent):
    """AI agent responsible for managing event marketing and promotion strategies."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "marketing_ops")
    
    def get_system_prompt(self) -> str:
        return """You are a Marketing Operations Agent specializing in event marketing and promotion strategies. 
        
        Your responsibilities include:
        1. Developing comprehensive marketing strategies for events
        2. Creating targeted campaigns across multiple channels
        3. Managing social media presence and content
        4. Optimizing marketing spend and ROI
        5. Coordinating with speakers and sponsors for promotion
        6. Analyzing marketing performance and metrics
        7. Requesting human approval for major marketing decisions
        
        Focus on data-driven marketing approaches and measurable results. Ensure brand consistency and audience engagement."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the marketing operations workflow."""
        event_data = context.get("event", {})
        other_agents_data = context.get("other_agents", {})
        
        await self.update_progress(10, "Analyzing event and target audience...")
        
        # Step 1: Analyze event and target audience
        audience_analysis = await self._analyze_target_audience(event_data)
        await self.log_activity("Analyzed target audience", "info", audience_analysis)
        
        await self.update_progress(25, "Developing marketing strategy...")
        
        # Step 2: Develop marketing strategy
        marketing_strategy = await self._develop_marketing_strategy(event_data, audience_analysis)
        await self.log_activity("Developed marketing strategy", "info", {"strategy_type": marketing_strategy.get("type", "Unknown")})
        
        await self.update_progress(40, "Creating marketing campaigns...")
        
        # Step 3: Create marketing campaigns
        campaigns = await self._create_marketing_campaigns(marketing_strategy, event_data)
        await self.log_activity("Created marketing campaigns", "info", {"campaign_count": len(campaigns)})
        
        await self.update_progress(60, "Planning content calendar...")
        
        # Step 4: Plan content calendar
        content_calendar = await self._plan_content_calendar(campaigns, event_data)
        
        await self.update_progress(80, "Coordinating with other agents...")
        
        # Step 5: Coordinate with other agents
        coordination_plan = await self._coordinate_with_agents(other_agents_data, campaigns)
        
        await self.update_progress(90, "Requesting approval for marketing plan...")
        
        # Step 6: Request approval for marketing plan
        approval_id = await self.request_approval({
            "type": "marketing_plan",
            "strategy": marketing_strategy,
            "campaigns": campaigns,
            "content_calendar": content_calendar,
            "coordination_plan": coordination_plan,
            "reasoning": "Comprehensive marketing strategy with multi-channel campaigns and content planning"
        })
        
        await self.make_decision({
            "action": "marketing_plan_proposed",
            "strategy_id": marketing_strategy.get("id"),
            "approval_id": approval_id,
            "confidence": 0.85
        })
        
        await self.update_progress(100, "Marketing operations workflow completed")
        
        return {
            "status": "completed",
            "audience_analysis": audience_analysis,
            "marketing_strategy": marketing_strategy,
            "campaigns": campaigns,
            "content_calendar": content_calendar,
            "coordination_plan": coordination_plan
        }
    
    async def _analyze_target_audience(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze target audience for the event."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the target audience for this event:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Description: {event_data.get('description', 'No description provided')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Location: {event_data.get('city', 'Unknown')}, {event_data.get('country', 'Unknown')}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            
            Please provide a comprehensive audience analysis including:
            1. Primary and secondary target audiences
            2. Demographics and psychographics
            3. Pain points and motivations
            4. Preferred communication channels
            5. Decision-making factors
            6. Competitive landscape
            7. Market size and opportunity
            
            Return your analysis as a JSON object.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback to structured analysis if JSON parsing fails
            event_name = event_data.get('name', '').lower()
            attendees = event_data.get('expected_attendees', 100)
            
            # Determine audience based on event name and type
            if 'tech' in event_name or 'ai' in event_name:
                primary_audience = "Technology professionals and executives"
                industry = "Technology"
            elif 'business' in event_name or 'conference' in event_name:
                primary_audience = "Business professionals and decision makers"
                industry = "Business"
            else:
                primary_audience = "General professional audience"
                industry = "General"
            
            return {
                "primary_audience": primary_audience,
                "secondary_audience": "Industry enthusiasts and students",
                "demographics": {
                    "age_range": "25-55",
                    "income_level": "Middle to upper-middle class",
                    "education": "Bachelor's degree or higher",
                    "location": "Urban and suburban areas"
                },
                "psychographics": {
                    "interests": ["Professional development", "Networking", "Innovation"],
                    "values": ["Growth", "Learning", "Community"],
                    "lifestyle": "Busy professionals seeking career advancement"
                },
                "pain_points": [
                    "Limited time for professional development",
                    "Need for practical, actionable insights",
                    "Desire for networking opportunities"
                ],
                "motivations": [
                    "Career advancement",
                    "Skill development",
                    "Industry networking",
                    "Staying current with trends"
                ],
                "communication_channels": [
                    "LinkedIn",
                    "Email newsletters",
                    "Professional associations",
                    "Industry publications"
                ],
                "decision_factors": [
                    "Speaker quality",
                    "Relevance of content",
                    "Networking opportunities",
                    "Location and timing",
                    "Cost and value"
                ],
                "market_size": f"{attendees * 100} potential attendees in target market",
                "opportunity": "Growing demand for professional development events"
            }
    
    async def _develop_marketing_strategy(self, event_data: Dict[str, Any], audience_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Develop comprehensive marketing strategy."""
        attendees = event_data.get('expected_attendees', 100)
        total_budget = event_data.get('budget_total', 50000)
        marketing_budget = total_budget * 0.12  # 12% of total budget
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Develop a comprehensive marketing strategy based on:
            
            Event Data: {json.dumps(event_data, indent=2)}
            Audience Analysis: {json.dumps(audience_analysis, indent=2)}
            Marketing Budget: ${marketing_budget:,.2f}
            
            Create a strategy that includes:
            1. Marketing objectives and KPIs
            2. Target audience segments and messaging
            3. Channel mix and allocation
            4. Timeline and milestones
            5. Budget allocation by channel
            6. Success metrics and measurement
            7. Risk mitigation strategies
            
            Return as a JSON object with the strategy structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            strategy = json.loads(response)
            strategy["id"] = f"strategy_{self.agent_id}"
            strategy["budget"] = marketing_budget
            return strategy
        except json.JSONDecodeError:
            # Create basic strategy if parsing fails
            return {
                "id": f"strategy_{self.agent_id}",
                "type": "Multi-channel digital-first",
                "budget": marketing_budget,
                "objectives": {
                    "awareness": "Generate 10x event capacity in impressions",
                    "engagement": "Achieve 5% engagement rate across channels",
                    "conversion": "Convert 15% of engaged audience to registrations"
                },
                "target_segments": [
                    {
                        "name": "Primary Decision Makers",
                        "size": attendees * 0.6,
                        "messaging": "Focus on ROI and career advancement"
                    },
                    {
                        "name": "Industry Influencers",
                        "size": attendees * 0.2,
                        "messaging": "Emphasize thought leadership and networking"
                    },
                    {
                        "name": "Emerging Professionals",
                        "size": attendees * 0.2,
                        "messaging": "Highlight learning opportunities and growth"
                    }
                ],
                "channel_mix": {
                    "digital": {
                        "allocation": marketing_budget * 0.6,
                        "channels": ["Social media", "Email", "Content marketing", "SEO"]
                    },
                    "traditional": {
                        "allocation": marketing_budget * 0.3,
                        "channels": ["Industry publications", "Partnerships", "Direct mail"]
                    },
                    "experiential": {
                        "allocation": marketing_budget * 0.1,
                        "channels": ["Networking events", "Preview sessions"]
                    }
                },
                "timeline": {
                    "awareness_phase": "Months 3-4 before event",
                    "consideration_phase": "Months 2-3 before event",
                    "conversion_phase": "Months 1-2 before event",
                    "retention_phase": "Month of event"
                },
                "success_metrics": [
                    "Website traffic and engagement",
                    "Social media reach and engagement",
                    "Email open and click rates",
                    "Registration conversion rate",
                    "Cost per acquisition"
                ]
            }
    
    async def _create_marketing_campaigns(self, strategy: Dict[str, Any], event_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create specific marketing campaigns."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create specific marketing campaigns based on this strategy:
            {json.dumps(strategy, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            
            Create campaigns for:
            1. Awareness campaign (early stage)
            2. Consideration campaign (mid-stage)
            3. Conversion campaign (late stage)
            4. Retention campaign (post-registration)
            5. Influencer/partner campaign
            
            For each campaign, include:
            - Campaign name and objective
            - Target audience
            - Key messages and creative direction
            - Channels and tactics
            - Budget allocation
            - Timeline and milestones
            - Success metrics
            
            Return as a JSON array of campaign objects.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic campaigns if parsing fails
            event_name = event_data.get('name', 'Event')
            budget = strategy.get('budget', 6000)
            
            return [
                {
                    "id": f"campaign_1_{self.agent_id}",
                    "name": f"{event_name} - Awareness Campaign",
                    "objective": "Generate awareness and interest",
                    "target_audience": "Primary decision makers",
                    "key_messages": [
                        f"Don't miss {event_name} - the premier industry event",
                        "Join industry leaders and innovators",
                        "Transform your career and network"
                    ],
                    "channels": ["LinkedIn", "Email", "Content marketing"],
                    "budget": budget * 0.3,
                    "timeline": "Months 3-4 before event",
                    "metrics": ["Impressions", "Reach", "Brand awareness"]
                },
                {
                    "id": f"campaign_2_{self.agent_id}",
                    "name": f"{event_name} - Consideration Campaign",
                    "objective": "Drive consideration and engagement",
                    "target_audience": "Interested prospects",
                    "key_messages": [
                        "See what you'll learn at the event",
                        "Meet the speakers and agenda",
                        "Early bird pricing available"
                    ],
                    "channels": ["Email", "Social media", "Webinars"],
                    "budget": budget * 0.4,
                    "timeline": "Months 2-3 before event",
                    "metrics": ["Engagement rate", "Website visits", "Content downloads"]
                },
                {
                    "id": f"campaign_3_{self.agent_id}",
                    "name": f"{event_name} - Conversion Campaign",
                    "objective": "Drive registrations",
                    "target_audience": "High-intent prospects",
                    "key_messages": [
                        "Limited spots remaining",
                        "Final chance to secure your place",
                        "Join the exclusive attendee list"
                    ],
                    "channels": ["Email", "Retargeting", "Direct outreach"],
                    "budget": budget * 0.2,
                    "timeline": "Months 1-2 before event",
                    "metrics": ["Registration rate", "Cost per registration", "Revenue"]
                },
                {
                    "id": f"campaign_4_{self.agent_id}",
                    "name": f"{event_name} - Retention Campaign",
                    "objective": "Maintain engagement and reduce cancellations",
                    "target_audience": "Registered attendees",
                    "key_messages": [
                        "Prepare for an amazing experience",
                        "Connect with fellow attendees",
                        "Final event details and updates"
                    ],
                    "channels": ["Email", "SMS", "Event app"],
                    "budget": budget * 0.1,
                    "timeline": "Month of event",
                    "metrics": ["Attendance rate", "Engagement", "Satisfaction"]
                }
            ]
    
    async def _plan_content_calendar(self, campaigns: List[Dict[str, Any]], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Plan content calendar for marketing campaigns."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create a content calendar for these marketing campaigns:
            {json.dumps(campaigns, indent=2)}
            
            Event Details: {json.dumps(event_data, indent=2)}
            
            Plan content including:
            1. Blog posts and articles
            2. Social media content
            3. Email sequences
            4. Video content
            5. Infographics and visuals
            6. Speaker spotlights
            7. Event updates and announcements
            
            For each content piece, include:
            - Content type and title
            - Target audience
            - Key message
            - Distribution channels
            - Publication date
            - Call-to-action
            
            Return as a JSON object with the content calendar structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic content calendar if parsing fails
            event_name = event_data.get('name', 'Event')
            
            return {
                "content_types": {
                    "blog_posts": [
                        {
                            "title": f"5 Reasons to Attend {event_name}",
                            "audience": "Primary decision makers",
                            "message": "Value proposition and benefits",
                            "channels": ["Website", "LinkedIn", "Email"],
                            "publish_date": "3 months before event",
                            "cta": "Register now"
                        },
                        {
                            "title": f"Meet the Speakers: {event_name} Lineup",
                            "audience": "Interested prospects",
                            "message": "Speaker expertise and sessions",
                            "channels": ["Website", "Social media", "Email"],
                            "publish_date": "2 months before event",
                            "cta": "View full agenda"
                        }
                    ],
                    "social_media": [
                        {
                            "type": "Speaker spotlight",
                            "frequency": "Weekly",
                            "channels": ["LinkedIn", "Twitter", "Instagram"],
                            "content": "Speaker quotes, photos, and session previews"
                        },
                        {
                            "type": "Event countdown",
                            "frequency": "Daily (last 2 weeks)",
                            "channels": ["All platforms"],
                            "content": "Countdown posts with urgency messaging"
                        }
                    ],
                    "email_sequences": [
                        {
                            "sequence": "Welcome series",
                            "frequency": "Weekly",
                            "audience": "New registrants",
                            "content": "Event preparation, speaker introductions, networking tips"
                        },
                        {
                            "sequence": "Reminder series",
                            "frequency": "Bi-weekly",
                            "audience": "All registrants",
                            "content": "Event updates, final details, preparation checklist"
                        }
                    ]
                },
                "content_themes": [
                    "Industry trends and insights",
                    "Speaker expertise and thought leadership",
                    "Networking and community building",
                    "Professional development and growth",
                    "Event highlights and exclusivity"
                ]
            }
    
    async def _coordinate_with_agents(self, other_agents_data: Dict[str, Any], campaigns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Coordinate marketing efforts with other agents."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create a coordination plan for marketing with other agents:
            
            Marketing Campaigns: {json.dumps(campaigns, indent=2)}
            Other Agents Data: {json.dumps(other_agents_data, indent=2)}
            
            Coordinate with:
            1. Speaker Outreach Agent - for speaker promotion and content
            2. Sponsorship Manager - for sponsor promotion and co-marketing
            3. Venue Scout - for venue-related marketing content
            4. Budget Controller - for marketing budget optimization
            
            Create coordination activities including:
            - Content collaboration opportunities
            - Cross-promotion strategies
            - Shared messaging and branding
            - Timeline coordination
            - Resource sharing
            
            Return as a JSON object with the coordination plan.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic coordination plan if parsing fails
            return {
                "speaker_coordination": {
                    "activities": [
                        "Speaker spotlight content creation",
                        "Speaker social media promotion",
                        "Speaker-led webinars and preview sessions",
                        "Speaker networking event promotion"
                    ],
                    "timeline": "Ongoing throughout campaign",
                    "resources": "Speaker bios, photos, session descriptions"
                },
                "sponsor_coordination": {
                    "activities": [
                        "Sponsor logo and brand integration",
                        "Co-marketing campaigns",
                        "Sponsor booth and session promotion",
                        "Sponsor networking event promotion"
                    ],
                    "timeline": "2 months before event",
                    "resources": "Sponsor logos, booth information, session details"
                },
                "venue_coordination": {
                    "activities": [
                        "Venue showcase content",
                        "Location-based marketing",
                        "Travel and accommodation information",
                        "Local attraction promotion"
                    ],
                    "timeline": "1 month before event",
                    "resources": "Venue photos, location details, travel information"
                },
                "budget_coordination": {
                    "activities": [
                        "Marketing budget tracking and reporting",
                        "ROI analysis and optimization",
                        "Cost-per-acquisition monitoring",
                        "Budget reallocation recommendations"
                    ],
                    "timeline": "Weekly throughout campaign",
                    "resources": "Marketing metrics, spend data, performance reports"
                }
            }
