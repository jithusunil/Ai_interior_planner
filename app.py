import streamlit as st
from main import run_crew_pipeline
from agents.product_agent import fetch_mock_products

# -------------- Setup Page ------------------
st.set_page_config(page_title="AI Interior Design Planner", layout="wide")

# -------------- Theme Toggle ----------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_mode

# Apply dark mode styling
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #121212;
                color: white;
            }
            h1, h3, h4, h5, h6 {
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# -------------- Title ------------------
st.title("🛋️ AI Interior Design Planner")
st.caption("Smart product picks and layout tips for your dream space — all within your budget.")

# -------------- Sidebar ------------------
with st.sidebar:
    st.header("Room Preferences")
    room = st.selectbox("Room Type", ["bedroom", "living room", "study room", "dining room"])
    style = st.selectbox("Style", ["boho", "modern", "minimalist", "scandinavian", "vintage", "japanese style"])
    budget = st.slider("Budget (₹)", 500, 100000, 2000, step=500)
    generate = st.button("Generate Design Plan")

# ---------- Utility: Chunk Display ----------
def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def display_product_grid(products, title, chunk_size=3, start=0, end=None):
    st.markdown(f"### {title}")
    visible_products = products[start:end]
    for chunk in chunk_list(visible_products, chunk_size):
        cols = st.columns(chunk_size)
        for col, item in zip(cols, chunk):
            with col:
                st.markdown(
                    f"""
                    <div style="
                        background-color: {'#333' if dark_mode else '#fff'};
                        border-radius: 12px;
                        padding: 0.8rem;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
                        text-align: center;
                        height: 300px;
                        display: flex;
                        flex-direction: column;
                        justify-content: space-between;
                        color: {'white' if dark_mode else 'black'};
                    ">
                        <img src="{item['image']}" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px;" />
                        <div style="margin-top: 0.5rem;">
                            <h5 style="font-size: 1rem; margin: 0.3rem 0;">{item['name']}</h5>
                            <p style="font-size: 0.9rem; font-weight: bold; margin: 0;">₹{item['price']}</p>
                            <p style="font-size: 0.75rem; opacity: 0.8;">{item['description']}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ----------- Main App Logic ---------------
if generate:
    with st.spinner("Generating your custom design plan..."):
        design_plan = run_crew_pipeline(room, style, budget)
        all_products = fetch_mock_products()

        within_budget = []
        above_budget = []
        total_cost = 0

        for p in all_products:
            if total_cost + p["price"] <= budget:
                within_budget.append(p)
                total_cost += p["price"]
            else:
                above_budget.append(p)

        st.session_state.within = within_budget
        st.session_state.above = above_budget
        st.session_state.load_count = 1

# ----------- Show Results with Load More -------------
if "within" in st.session_state:
    chunk = 3  # items per row
    step = chunk * 2  # products to show per "page"

    st.markdown(f"### 🎯 Recommended Products for ₹{sum([p['price'] for p in st.session_state.within])} (within your ₹{budget} budget)")
    end_index = step * st.session_state.load_count
    display_product_grid(st.session_state.within, "Top Picks", chunk_size=chunk, end=end_index)

    if len(st.session_state.within) > end_index:
        if st.button("⬇️ Load More"):
            st.session_state.load_count += 1

    if st.session_state.above:
        st.markdown("### 💡 Explore More (If You're Open to Stretching Budget Slightly)")
        display_product_grid(st.session_state.above, "Above Budget", chunk_size=chunk, end=step)

    st.markdown("---")
    st.markdown("#### 📝 Why These Products?")
    st.markdown(f"These items are selected for your **{style} {room}**, matching your style and budget while keeping comfort and space-efficiency in mind.")
else:
    st.info("Set your room preferences and click **Generate Design Plan** to get started.")

