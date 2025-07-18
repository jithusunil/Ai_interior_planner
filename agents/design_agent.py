from crewai import Agent

# Define the design agent
def get_design_agent():
    return Agent(
        role="Interior Design Expert",
        goal="Generate layout and design suggestions for a room based on style",
        backstory=(
            "You're an interior designer who specializes in modern and minimalist room styles. "
            "You know how to optimize small spaces, suggest color palettes, and provide furniture placement advice."
        ),
        verbose=True,
        allow_delegation=False
    )
