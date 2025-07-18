import os
from crewai import Crew, Task
from agents.design_agent import get_design_agent
from agents.product_agent import get_product_agent, fetch_mock_products
from agents.budget_agent import get_budget_agent
from agents.summary_agent import get_summary_agent
from dotenv import load_dotenv

# Load OpenAI key
load_dotenv()

def run_crew_pipeline(room, style, budget):
    # Get agents
    design_agent = get_design_agent()
    product_agent = get_product_agent()
    budget_agent = get_budget_agent()
    summary_agent = get_summary_agent()

    # Define Tasks
    design_task = Task(
        description=f"Provide layout, color, and furniture placement tips for a {style} {room}.",
        expected_output="Design strategy including key elements, color palette, and layout principles.",
        agent=design_agent
    )

    product_task = Task(
        description=f"List 3–5 product ideas that match the {style} style and {room} type.",
        expected_output="List of product name, estimated price, and use case.",
        agent=product_agent
    )

    budget_task = Task(
        description=f"Review product suggestions and remove or replace any item that exceeds the total budget of ₹{budget}.",
        expected_output="Updated list of items within budget, ensuring diversity.",
        agent=budget_agent
    )

    summary_task = Task(
        description="Summarize everything into a clean, client-friendly design plan with layout tips and product links.",
        expected_output="Final design plan: layout summary + recommended items with price + total cost.",
        agent=summary_agent
    )

    # Create and run the crew
    crew = Crew(
        agents=[design_agent, product_agent, budget_agent, summary_agent],
        tasks=[design_task, product_task, budget_task, summary_task],
        verbose=True
    )

    result = crew.kickoff()
    return result

# For quick terminal testing
if __name__ == "__main__":
    output = run_crew_pipeline("bedroom", "boho", 2000)
    print("\nFinal Output:\n", output)
