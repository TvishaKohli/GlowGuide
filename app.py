import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# -----------------------
# CONFIG
# -----------------------

st.set_page_config(page_title="GlowGuide", layout="centered")

# -----------------------
# FINAL UI THEME
# -----------------------

st.markdown("""
<style>

/* ── GOOGLE FONT ─────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* ── BACKGROUND — diagonal stripe ───────────── */
.stApp {
    background-color: #1C3A2A;
    background-image: repeating-linear-gradient(
        135deg,
        rgba(255, 255, 255, 0.035) 0px,
        rgba(255, 255, 255, 0.035) 36px,
        transparent                36px,
        transparent                72px
    );
    font-family: 'Inter', 'Segoe UI', sans-serif;
    scroll-behavior: smooth;
}

/* ── GLOBAL TEXT ─────────────────────────────── */
html, body, p, span,
.stMarkdown, .stText, .element-container {
    color: #E8D9B0 !important;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* ── HEADINGS ────────────────────────────────── */
h1 {
    color: #E8D9B0 !important;
    font-weight: 700;
}

h2, h3, h4 {
    color: #7DBB96 !important;
}

/* ── LABELS ──────────────────────────────────── */
label {
    color: #7DBB96 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

/* ══════════════════════════════════════════════ */
/*   SELECT BOX — cream bg + dark forest text    */
/* ══════════════════════════════════════════════ */

/* Trigger button container */
div[data-baseweb="select"] {
    background-color: #F5EFD8 !important;
    border-radius: 10px !important;
    border: 1px solid #7DBB96 !important;
}

/* Every child element inside the trigger */
div[data-baseweb="select"] div,
div[data-baseweb="select"] span,
div[data-baseweb="select"] input,
div[data-baseweb="select"] svg,
div[data-baseweb="select"] p {
    color: #1C3A2A !important;
    background-color: transparent !important;
    fill: #1C3A2A !important;
}

/* ── DROPDOWN POPOVER ────────────────────────── */
[data-baseweb="popover"],
[data-baseweb="menu"],
ul[data-baseweb="menu"],
[role="listbox"],
[data-baseweb="select-dropdown"] {
    background-color: #F5EFD8 !important;
    border: 1px solid #7DBB96 !important;
    border-radius: 10px !important;
}

/* ── DROPDOWN OPTIONS ────────────────────────── */
[role="option"],
li[role="option"],
[data-baseweb="menu"] li,
[data-baseweb="menu"] div {
    background-color: #F5EFD8 !important;
    color: #1C3A2A !important;
}

/* Hover & selected state */
[role="option"]:hover,
li[role="option"]:hover,
[role="option"][aria-selected="true"],
li[aria-selected="true"] {
    background-color: #E8D9B0 !important;
    color: #1C3A2A !important;
}

/* Fallback for plain ul/li */
ul {
    background-color: #F5EFD8 !important;
}
li {
    color: #1C3A2A !important;
}
li:hover {
    background-color: #E8D9B0 !important;
}

/* ── SLIDER ──────────────────────────────────── */
.stSlider > div,
.stSlider [data-testid="stTickBar"] {
    color: #1C3A2A !important;
}

/* ════════════════════════════════════════════════
   BUTTONS — beige accent bg, forest green text
   ════════════════════════════════════════════════ */

/* Base style */
button[kind="primary"],
button[kind="secondary"],
[data-testid="baseButton-primary"],
[data-testid="baseButton-secondary"],
.stButton > button {
    background-color: #E8D9B0 !important;
    color: #1C3A2A !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    border: 1px solid #7DBB96 !important;
    box-shadow: none !important;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

/* Streamlit wraps button text in <p> */
button[kind="primary"] p,
button[kind="secondary"] p,
[data-testid="baseButton-primary"] p,
[data-testid="baseButton-secondary"] p,
.stButton > button p {
    color: #1C3A2A !important;
}

/* Hover */
button[kind="primary"]:hover,
button[kind="secondary"]:hover,
[data-testid="baseButton-primary"]:hover,
[data-testid="baseButton-secondary"]:hover,
.stButton > button:hover {
    background-color: #F5EFD8 !important;
    color: #1C3A2A !important;
    border: 1px solid #7DBB96 !important;
    box-shadow: none !important;
    transform: translateY(-1px);
}

button[kind="primary"]:hover p,
button[kind="secondary"]:hover p,
[data-testid="baseButton-primary"]:hover p,
[data-testid="baseButton-secondary"]:hover p,
.stButton > button:hover p {
    color: #1C3A2A !important;
}

/* Focus / Active */
button[kind="primary"]:focus,  button[kind="primary"]:active,
button[kind="secondary"]:focus, button[kind="secondary"]:active,
[data-testid="baseButton-primary"]:focus,
[data-testid="baseButton-primary"]:active,
[data-testid="baseButton-secondary"]:focus,
[data-testid="baseButton-secondary"]:active,
.stButton > button:focus,
.stButton > button:active {
    background-color: #E8D9B0 !important;
    color: #1C3A2A !important;
    border: 1px solid #7DBB96 !important;
    box-shadow: none !important;
    outline: none !important;
}

button[kind="primary"]:focus p,  button[kind="primary"]:active p,
button[kind="secondary"]:focus p, button[kind="secondary"]:active p,
[data-testid="baseButton-primary"]:focus p,
[data-testid="baseButton-secondary"]:focus p,
.stButton > button:active p {
    color: #1C3A2A !important;
}

/* ── PRODUCT CARD ────────────────────────────── */
.product-card {
    background: #F5EFD8;
    padding: 16px 20px;
    border-radius: 12px;
    border: 1px solid #7DBB96;
    margin-bottom: 12px;
}

.product-card h4,
.product-card p,
.product-card b {
    color: #1C3A2A !important;
}

/* ── VIEW DETAILS LINK-BUTTON ─────────────────── */
.view-details-btn {
    display: inline-block;
    margin-top: 12px;
    padding: 8px 20px;
    background-color: #E8D9B0;
    color: #1C3A2A !important;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    font-family: 'Inter', 'Segoe UI', sans-serif;
    border: 1px solid #7DBB96;
    transition: background-color 0.2s ease, transform 0.1s ease;
}

.view-details-btn:hover {
    background-color: #F5EFD8;
    color: #1C3A2A !important;
    text-decoration: none;
    transform: translateY(-1px);
}

/* ── ALERTS ──────────────────────────────────── */
.stSuccess, .stWarning, .stInfo {
    color: #1C3A2A !important;
}

/* ── AI REPORT CARD ──────────────────────────── */
.ai-report-card {
    background: #E8D9B0;
    border: 1px solid #7DBB96;
    border-radius: 14px;
    padding: 18px 24px;
    color: #1C3A2A !important;
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# LOAD DATA
# -----------------------

data = pd.read_csv("skincare_with_concern.csv")

data["product_type"] = data["product_type"].str.lower()
data["concern"] = data["concern"].str.lower()

# -----------------------
# TITLE
# -----------------------

st.markdown("""
<div style="
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0 2px 0;
">
    <span style="
        display: inline-block;
        font-size: 27px !important;
        font-weight: 700 !important;
        color: #E8D9B0 !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        letter-spacing: 0.5px !important;
    ">GlowGuide</span>
    <span style="
        display: inline-block;
        font-size: 27px !important;
        font-weight: 700 !important;
        color: #E8D9B0 !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        letter-spacing: 0.5px !important;
    ">Personalized results</span>
</div>

<div style="
    text-align: center;
    padding: 64px 0 12px 0;
">
    <p style="
        margin: 0;
        font-size: 36px;
        font-weight: 700;
        color: #E8D9B0;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        line-height: 1.3;
        letter-spacing: -0.5px;
    ">Not sure what your<br>skin needs?</p>
    <p style="
        margin: 14px 0 0 0;
        font-size: 17px;
        font-weight: 400;
        color: #7DBB96;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        line-height: 1.6;
    ">We help you find the right skincare routine based on your skin —<br>no guesswork, no confusion.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------
# INPUTS
# -----------------------

st.markdown("### 🧴 Skin Profile")

concern = st.selectbox("Skin Concern", sorted(data["concern"].unique()))
skin_type = st.selectbox("Skin Type", ["Oily", "Dry", "Combination", "Sensitive", "Normal"])

st.markdown("### 🌿 Lifestyle")

water = st.selectbox("Water Intake", ["Less than 1L", "1-2L", "2-3L", "More than 3L"])
sleep = st.selectbox("Sleep", ["Less than 5 hours", "5-6 hours", "6-8 hours", "More than 8 hours"])
sun = st.selectbox("Sun Exposure", ["Rarely", "Moderately", "Very Often"])
diet = st.selectbox("Diet", ["Balanced", "High Junk Food", "High Sugar", "Healthy"])
stress = st.selectbox("Stress", ["Low", "Moderate", "High"])

st.markdown("### ✨ Preferences")

product_type = st.selectbox("Product Type", sorted(data["product_type"].unique()))

st.markdown("### 💰 Budget")

budget = st.slider("Select Budget (₹)", 100, 5000, 1500)

st.divider()

# -----------------------
# SCORING FUNCTION
# -----------------------

def calculate_score(row):
    score = 0
    if row["concern"] == concern:
        score += 3
    if skin_type.lower() in str(row["clean_ingreds"]).lower():
        score += 1
    if row["price_inr"] <= budget:
        score += 2
    return score

# -----------------------
# BUTTON ACTION
# -----------------------

if st.button("🔍 Get Recommendations"):

    results = data[
        (data["concern"] == concern) &
        (data["product_type"] == product_type) &
        (data["price_inr"] <= budget)
    ].copy()

    if results.empty:
        st.info("Showing best matches (budget relaxed)")
        results = data[
            (data["concern"] == concern) &
            (data["product_type"] == product_type)
        ].copy()

    if results.empty:
        st.info("Showing related products")
        results = data[
            (data["concern"] == concern)
        ].copy()

    results["score"] = results.apply(lambda row: calculate_score(row), axis=1)
    results = results.sort_values(by="score", ascending=False)

    # -----------------------
    # SCROLL TO RESULTS
    # -----------------------

    components.html("""
        <script>
            setTimeout(function() {
                var doc = window.parent.document;
                var container = (
                    doc.querySelector('section.main') ||
                    doc.querySelector('.main')        ||
                    doc.querySelector('[data-testid="stAppViewContainer"]') ||
                    doc.documentElement
                );
                container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
            }, 300);
        </script>
    """, height=1)

    # -----------------------
    # PRODUCTS
    # -----------------------

    st.markdown('<div id="results-anchor"></div>', unsafe_allow_html=True)
    st.markdown("### 🌿 Recommended Products")
    st.success(f"Found {len(results)} suitable products")

    for _, row in results.head(5).iterrows():
        product_url = row.get('product_url', '#')
        if not isinstance(product_url, str) or product_url.strip() == '':
            product_url = '#'

        st.markdown(f"""
            <div class="product-card">
                <h4>{row['product_name'].title()}</h4>
                <p>Best match for your skin</p>
                <b>₹{int(row['price_inr'])}</b><br>
                <a href="{product_url}" target="_blank" class="view-details-btn">🛒 View Details</a>
            </div>
        """, unsafe_allow_html=True)

    st.divider()

    # -----------------------
    # LIFESTYLE
    # -----------------------

    st.markdown("### 💡 Lifestyle Suggestions")

    if water == "Less than 1L":
        st.warning("Increase water intake 💧")
    else:
        st.success("Good hydration")

    if diet in ["High Junk Food", "High Sugar"]:
        st.warning("Reduce junk food 🍟")

    if sleep in ["Less than 5 hours", "5-6 hours"]:
        st.warning("Improve sleep 😴")

    if stress == "High":
        st.warning("Reduce stress")

    if sun == "Very Often":
        st.warning("Use sunscreen")

    st.divider()

    # -----------------------
    # AI REPORT
    # -----------------------

    st.markdown("### 🧠 AI Skin Report")

    report = f"You are experiencing {concern}.\n\n"

    if concern in ["acne", "pigmentation", "dark spots", "wrinkles", "sensitivity"]:
        report = f"It looks like your skin is currently dealing with {concern}.\n\n"

    elif concern in ["dryness", "dehydration"]:
        report = f"Your skin may not be getting enough hydration.\n\n"

    elif concern in ["hydration", "glow", "healthy skin"]:
        report = f"Your skin appears balanced, hydrated, and in good condition.\n\n"

    else:
        report = f"Your skin concern is mainly related to {concern}.\n\n"
        report += "\nFocus on skincare + lifestyle balance."

    report_html = report.replace("\n", "<br>")
    st.markdown(f'<div class="ai-report-card">{report_html}</div>', unsafe_allow_html=True)
