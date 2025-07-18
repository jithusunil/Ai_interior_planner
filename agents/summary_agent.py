from crewai import Agent

def get_summary_agent():
    return Agent(
        role="Design Proposal Writer",
        goal="Summarize the design plan with layout tips and product recommendations",
        backstory=(
            "You're skilled at writing client-facing summaries of interior plans. "
            "You can create clean, structured, easy-to-read reports based on other agents' input."
        ),
        verbose=True,
        allow_delegation=False
    )
