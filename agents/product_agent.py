from crewai import Agent
import random

# Rich product mock catalog for recommendation engine
def fetch_mock_products():
    catalog = [
        # BEDROOM - BOHO
        {
            "name": "Boho Rattan Bed Frame",
            "price": 4200,
            "room": "bedroom",
            "style": "boho",
            "link": "#",
            "image": "https://i.pinimg.com/736x/c1/37/aa/c137aa0b21b90512dc58136d4d6a23dc.jpg",
            "description": "Natural wood frame with woven rattan headboard — earthy and airy."
        },
        {
            "name": "Macramé Dreamcatcher",
            "price": 350,
            "room": "bedroom",
            "style": "boho",
            "link": "#",
            "image": "https://tse3.mm.bing.net/th/id/OIP.MBzQe1BlW0dT9aYsOdoS1AHaJQ?rs=1&pid=ImgDetMain&o=7&rm=3",
            "description": "Handcrafted wall art for above the bed."
        },

        # LIVING ROOM - MODERN
        {
            "name": "Sleek Modular Sofa",
            "price": 9500,
            "room": "living room",
            "style": "modern",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/5b/40/89/5b40894d0ce7b5e2993f6d06a5f1173e.jpg",
            "description": "L-shaped couch with neutral tones and minimalist lines."
        },
        {
            "name": "Glass Coffee Table",
            "price": 2700,
            "room": "living room",
            "style": "modern",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/f2/8a/dc/f28adc547973f188884501800ec7183c.jpg",
            "description": "Tempered glass with chrome legs — clean and contemporary."
        },

        # STUDY ROOM - MINIMALIST
        {
            "name": "White Study Desk",
            "price": 2200,
            "room": "study room",
            "style": "minimalist",
            "link": "#",
            "image": "https://i.pinimg.com/736x/50/41/9f/50419f5a54a04b5ee9a3aeeb99da2d1a.jpg",
            "description": "Simple flat-top desk with hidden drawers."
        },
        {
            "name": "Minimal LED Table Lamp",
            "price": 650,
            "room": "study room",
            "style": "minimalist",
            "link": "#",
            "image": "https://i.pinimg.com/736x/54/69/67/546967b016fc83f0f7248e4620f0fbfe.jpg",
            "description": "No-fuss lighting with adjustable brightness."
        },

        # DINING ROOM - SCANDINAVIAN
        {
            "name": "Nordic Wooden Dining Table",
            "price": 6000,
            "room": "dining room",
            "style": "scandinavian",
            "link": "#",
            "image": "https://tse2.mm.bing.net/th/id/OIP.WUuIvhTT-QpgVgk3UhgRzAHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
            "description": "Natural wood table with tapered legs and clean profile."
        },
        {
            "name": "Set of 4 Light Oak Chairs",
            "price": 2800,
            "room": "dining room",
            "style": "scandinavian",
            "link": "#",
            "image": "https://cdn.hibid.com/img.axd?id=7968046767&wid=&rwl=false&p=&ext=&w=0&h=0&t=&lp=&c=true&wt=false&sz=MAX&checksum=r448pBwRC8lxjIjeIt2AX9AO8obpGFAm",
            "description": "Breathable backrest design and soft neutral tones."
        },

        # BEDROOM - JAPANESE STYLE
        {
            "name": "Tatami Floor Mattress",
            "price": 3000,
            "room": "bedroom",
            "style": "japanese style",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/bb/b1/71/bbb1713c6f48c56a439a9e6ca41da6dc.jpg",
            "description": "Foldable and breathable cotton mat for restful sleep."
        },
        {
            "name": "Shoji Paper Divider",
            "price": 1600,
            "room": "bedroom",
            "style": "japanese style",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/7f/4d/5e/7f4d5e7a35e0a1fc85b81a2dae139934.jpg",
            "description": "Elegant sliding-style screen for subtle room separation."
        },

        # LIVING ROOM - VINTAGE
        {
            "name": "Retro Velvet Armchair",
            "price": 2100,
            "room": "living room",
            "style": "vintage",
            "link": "#",
            "image": "https://i.pinimg.com/736x/b6/52/2e/b6522e3324b7968d9612e2328bc678f7.jpg",
            "description": "Old-school comfort with modern polish in velvet."
        },
        {
            "name": "Classic Record Console",
            "price": 3600,
            "room": "living room",
            "style": "vintage",
            "link": "#",
            "image": "https://i.pinimg.com/736x/95/d2/0f/95d20f1be2b80ec0811e7d88d89745a7.jpg",
            "description": "Store your vinyl in retro style with a built-in player shelf."
        },

        # DINING ROOM - JAPANESE STYLE
        {
            "name": "Low Dining Table (Chabudai)",
            "price": 3500,
            "room": "dining room",
            "style": "japanese style",
            "link": "#",
            "image": "https://i.pinimg.com/736x/55/94/57/559457f7e82f03b3c1c76e0291377c2c.jpg",
            "description": "Compact, floor-level wooden table for traditional seating."
        },

        # STUDY ROOM - SCANDINAVIAN
        {
            "name": "Light Wood Study Table",
            "price": 2500,
            "room": "study room",
            "style": "scandinavian",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/20/f9/0d/20f90db26e1f90d706a29f0fed2ae7d2.jpg",
            "description": "Slim and practical table with rounded corners and wood grain finish."
        },

        # BEDROOM - MINIMALIST
        {
            "name": "Platform Bed Frame",
            "price": 3200,
            "room": "bedroom",
            "style": "minimalist",
            "link": "#",
            "image": "https://i.pinimg.com/1200x/50/b2/b1/50b2b1ee6a54dcc2a509464a77d29647.jpg",
            "description": "Solid pine frame with no headboard — just simplicity."
        },

        # DINING ROOM - VINTAGE
        {
            "name": "Vintage Dining Hutch",
            "price": 4800,
            "room": "dining room",
            "style": "vintage",
            "link": "#",
            "image": "https://i.pinimg.com/736x/14/93/91/14939148ab71ad7581da38d3d4103309.jpg",
            "description": "Rustic wood with glass shelves for dishes and collectibles."
        },
    ]
    random.shuffle(catalog)
    return catalog


def get_product_agent():
    return Agent(
        role="Furniture Sourcing Specialist",
        goal="Find relevant furniture items based on the design style and room type",
        backstory=(
            "You're an expert at sourcing stylish yet budget-friendly furniture items that match different room styles. "
            "You help interior designers find practical product suggestions."
        ),
        verbose=True,
        allow_delegation=False
    )
