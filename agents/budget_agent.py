from crewai import Agent

def get_budget_agent():
    return Agent(
        role="Budget Planner",
        goal="Ensure all suggested furniture items fit within the user's budget",
        backstory=(
            "You're a budget-conscious planner. Your job is to review the product list and filter out any items that "
            "push the total over budget while keeping design intent in mind."
        ),
        verbose=True,
        allow_delegation=False
    )
