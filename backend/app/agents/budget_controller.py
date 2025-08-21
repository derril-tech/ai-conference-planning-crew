from typing import Dict, Any, List
from langchain.schema import HumanMessage, SystemMessage
from .base_agent import BaseAgent
import json

class BudgetControllerAgent(BaseAgent):
    """AI agent responsible for managing event budgets and financial planning."""
    
    def __init__(self, agent_id: str, event_id: str):
        super().__init__(agent_id, event_id, "budget_controller")
    
    def get_system_prompt(self) -> str:
        return """You are a Budget Controller Agent specializing in event budget management and financial planning. 
        
        Your responsibilities include:
        1. Analyzing event requirements and creating comprehensive budgets
        2. Tracking expenses and revenue projections
        3. Optimizing budget allocation across different categories
        4. Identifying cost-saving opportunities
        5. Monitoring budget performance and variances
        6. Creating financial reports and forecasts
        7. Requesting human approval for major budget decisions
        
        Always prioritize cost-effectiveness while maintaining event quality. Provide detailed financial analysis and clear recommendations."""
    
    async def execute_workflow(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the budget control workflow."""
        event_data = context.get("event", {})
        other_agents_data = context.get("other_agents", {})
        
        await self.update_progress(10, "Analyzing event requirements...")
        
        # Step 1: Analyze event requirements
        requirements = await self._analyze_budget_requirements(event_data)
        await self.log_activity("Analyzed budget requirements", "info", requirements)
        
        await self.update_progress(25, "Creating initial budget...")
        
        # Step 2: Create initial budget
        initial_budget = await self._create_initial_budget(requirements, event_data)
        await self.log_activity("Created initial budget", "info", {"total_budget": initial_budget.get("total", 0)})
        
        await self.update_progress(40, "Optimizing budget allocation...")
        
        # Step 3: Optimize budget allocation
        optimized_budget = await self._optimize_budget_allocation(initial_budget, other_agents_data)
        await self.log_activity("Optimized budget allocation", "info", {"optimization_savings": initial_budget.get("total", 0) - optimized_budget.get("total", 0)})
        
        await self.update_progress(60, "Creating financial projections...")
        
        # Step 4: Create financial projections
        projections = await self._create_financial_projections(optimized_budget, event_data)
        
        await self.update_progress(80, "Identifying cost-saving opportunities...")
        
        # Step 5: Identify cost-saving opportunities
        cost_savings = await self._identify_cost_savings(optimized_budget)
        
        await self.update_progress(90, "Requesting approval for budget plan...")
        
        # Step 6: Request approval for budget plan
        approval_id = await self.request_approval({
            "type": "budget_plan",
            "optimized_budget": optimized_budget,
            "projections": projections,
            "cost_savings": cost_savings,
            "reasoning": "Comprehensive budget plan with optimizations and cost savings"
        })
        
        await self.make_decision({
            "action": "budget_plan_proposed",
            "budget_id": optimized_budget.get("id"),
            "approval_id": approval_id,
            "confidence": 0.9
        })
        
        await self.update_progress(100, "Budget control workflow completed")
        
        return {
            "status": "completed",
            "initial_budget": initial_budget,
            "optimized_budget": optimized_budget,
            "projections": projections,
            "cost_savings": cost_savings,
            "total_savings": initial_budget.get("total", 0) - optimized_budget.get("total", 0)
        }
    
    async def _analyze_budget_requirements(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze event requirements for budget planning."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Analyze the following event requirements for budget planning:
            
            Event Details:
            - Name: {event_data.get('name', 'Unknown')}
            - Description: {event_data.get('description', 'No description provided')}
            - Expected Attendees: {event_data.get('expected_attendees', 0)}
            - Total Budget: ${event_data.get('budget_total', 0):,.2f}
            - Dates: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            - Location: {event_data.get('city', 'Unknown')}, {event_data.get('country', 'Unknown')}
            
            Please provide a structured analysis including:
            1. Event scale and complexity assessment
            2. Required budget categories
            3. Cost drivers and variables
            4. Revenue potential and sources
            5. Risk factors affecting budget
            6. Industry benchmarks for similar events
            
            Return your analysis as a JSON object.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Fallback to structured text if JSON parsing fails
            attendees = event_data.get('expected_attendees', 100)
            total_budget = event_data.get('budget_total', 50000)
            
            return {
                "event_scale": "Medium" if attendees < 500 else "Large",
                "complexity": "Standard conference",
                "budget_categories": [
                    "Venue & Facilities",
                    "Speakers & Entertainment",
                    "Marketing & Promotion",
                    "Technology & AV",
                    "Catering & Refreshments",
                    "Staffing & Operations",
                    "Contingency"
                ],
                "cost_drivers": ["Attendee count", "Location", "Duration", "Quality level"],
                "revenue_sources": ["Registration fees", "Sponsorships", "Exhibitor fees"],
                "risk_factors": ["Weather", "Economic conditions", "Competition"],
                "industry_benchmarks": {
                    "venue_per_attendee": 50,
                    "speaker_per_attendee": 30,
                    "marketing_per_attendee": 20
                }
            }
    
    async def _create_initial_budget(self, requirements: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create initial budget based on requirements."""
        attendees = event_data.get('expected_attendees', 100)
        total_budget = event_data.get('budget_total', 50000)
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create an initial budget based on these requirements:
            {json.dumps(requirements, indent=2)}
            
            Event Details:
            - Attendees: {attendees}
            - Total Budget: ${total_budget:,.2f}
            - Duration: {event_data.get('start_date', 'Unknown')} to {event_data.get('end_date', 'Unknown')}
            
            Create a detailed budget breakdown including:
            1. Venue & Facilities (30-40% of total)
            2. Speakers & Entertainment (15-25% of total)
            3. Marketing & Promotion (10-15% of total)
            4. Technology & AV (5-10% of total)
            5. Catering & Refreshments (10-15% of total)
            6. Staffing & Operations (5-10% of total)
            7. Contingency (5-10% of total)
            
            For each category, provide:
            - Budget allocation
            - Key cost items
            - Justification
            - Risk factors
            
            Return as a JSON object with the budget structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            budget = json.loads(response)
            budget["id"] = f"budget_{self.agent_id}"
            budget["total"] = total_budget
            return budget
        except json.JSONDecodeError:
            # Create basic budget if parsing fails
            return {
                "id": f"budget_{self.agent_id}",
                "total": total_budget,
                "categories": {
                    "venue_facilities": {
                        "allocation": total_budget * 0.35,
                        "items": ["Venue rental", "Setup/teardown", "Insurance"],
                        "justification": "Primary event space and facilities"
                    },
                    "speakers_entertainment": {
                        "allocation": total_budget * 0.20,
                        "items": ["Speaker fees", "Travel expenses", "Materials"],
                        "justification": "Quality content and engagement"
                    },
                    "marketing_promotion": {
                        "allocation": total_budget * 0.12,
                        "items": ["Digital marketing", "Print materials", "Social media"],
                        "justification": "Event promotion and awareness"
                    },
                    "technology_av": {
                        "allocation": total_budget * 0.08,
                        "items": ["AV equipment", "WiFi", "Streaming services"],
                        "justification": "Technical infrastructure"
                    },
                    "catering_refreshments": {
                        "allocation": total_budget * 0.12,
                        "items": ["Meals", "Coffee breaks", "Special dietary needs"],
                        "justification": "Attendee experience and comfort"
                    },
                    "staffing_operations": {
                        "allocation": total_budget * 0.08,
                        "items": ["Event staff", "Security", "Coordination"],
                        "justification": "Event execution and safety"
                    },
                    "contingency": {
                        "allocation": total_budget * 0.05,
                        "items": ["Emergency fund", "Unforeseen expenses"],
                        "justification": "Risk mitigation and flexibility"
                    }
                }
            }
    
    async def _optimize_budget_allocation(self, initial_budget: Dict[str, Any], other_agents_data: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize budget allocation based on other agents' data."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Optimize this budget allocation based on other agents' data:
            
            Initial Budget: {json.dumps(initial_budget, indent=2)}
            Other Agents Data: {json.dumps(other_agents_data, indent=2)}
            
            Consider:
            1. Venue costs from venue scout
            2. Speaker costs from speaker outreach
            3. Marketing needs from marketing ops
            4. Technology requirements
            5. Cost-saving opportunities
            6. Quality vs. cost trade-offs
            
            Provide an optimized budget that:
            - Maintains event quality
            - Reduces unnecessary costs
            - Reallocates savings to high-impact areas
            - Includes detailed justification for changes
            
            Return as a JSON object with the optimized budget structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            optimized = json.loads(response)
            optimized["id"] = f"optimized_budget_{self.agent_id}"
            optimized["original_total"] = initial_budget.get("total", 0)
            optimized["savings"] = initial_budget.get("total", 0) - optimized.get("total", 0)
            return optimized
        except json.JSONDecodeError:
            # Return original budget with minor optimizations if parsing fails
            optimized = initial_budget.copy()
            optimized["id"] = f"optimized_budget_{self.agent_id}"
            optimized["total"] = initial_budget.get("total", 0) * 0.95  # 5% savings
            optimized["savings"] = initial_budget.get("total", 0) * 0.05
            return optimized
    
    async def _create_financial_projections(self, budget: Dict[str, Any], event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create financial projections and forecasts."""
        attendees = event_data.get('expected_attendees', 100)
        
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Create financial projections for this event:
            
            Budget: {json.dumps(budget, indent=2)}
            Event Data: {json.dumps(event_data, indent=2)}
            
            Provide projections including:
            1. Revenue projections (registration fees, sponsorships, etc.)
            2. Expense forecasts by category
            3. Cash flow projections
            4. Break-even analysis
            5. Profit/loss scenarios
            6. Key financial metrics
            
            Return as a JSON object with the projection structure.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Create basic projections if parsing fails
            total_budget = budget.get("total", 50000)
            registration_fee = 200
            sponsorship_revenue = total_budget * 0.3
            
            return {
                "revenue_projections": {
                    "registration_fees": attendees * registration_fee,
                    "sponsorships": sponsorship_revenue,
                    "exhibitor_fees": total_budget * 0.1,
                    "other_revenue": total_budget * 0.05
                },
                "expense_forecasts": budget.get("categories", {}),
                "cash_flow": {
                    "month_1": -total_budget * 0.3,
                    "month_2": -total_budget * 0.4,
                    "month_3": total_budget * 0.2
                },
                "break_even": {
                    "attendees_needed": int(total_budget / registration_fee),
                    "revenue_needed": total_budget
                },
                "profit_loss": {
                    "best_case": total_budget * 0.2,
                    "likely_case": total_budget * 0.1,
                    "worst_case": -total_budget * 0.1
                }
            }
    
    async def _identify_cost_savings(self, budget: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify potential cost-saving opportunities."""
        messages = [
            SystemMessage(content=self.get_system_prompt()),
            HumanMessage(content=f"""
            Identify cost-saving opportunities for this budget:
            {json.dumps(budget, indent=2)}
            
            Look for:
            1. Negotiation opportunities
            2. Alternative suppliers
            3. Bulk discounts
            4. Technology solutions
            5. Process improvements
            6. Resource sharing
            
            For each opportunity, provide:
            - Description
            - Potential savings
            - Implementation effort
            - Risk assessment
            - Recommendation
            
            Return as a JSON array of cost-saving opportunities.
            """)
        ]
        
        response = await self.get_llm_response(messages)
        
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Return basic cost-saving suggestions if parsing fails
            return [
                {
                    "category": "Venue",
                    "opportunity": "Negotiate multi-day discount",
                    "potential_savings": budget.get("total", 0) * 0.05,
                    "effort": "Medium",
                    "risk": "Low",
                    "recommendation": "Proceed with negotiation"
                },
                {
                    "category": "Technology",
                    "opportunity": "Use virtual meeting tools",
                    "potential_savings": budget.get("total", 0) * 0.02,
                    "effort": "Low",
                    "risk": "Low",
                    "recommendation": "Implement virtual components"
                },
                {
                    "category": "Marketing",
                    "opportunity": "Focus on digital marketing",
                    "potential_savings": budget.get("total", 0) * 0.03,
                    "effort": "Medium",
                    "risk": "Low",
                    "recommendation": "Shift budget to digital channels"
                }
            ]
