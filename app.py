import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Zomato Growth Intelligence", layout="wide")

# -------------------------
# 🎨 RESPONSIVE UI (MOBILE + DESKTOP)
# -------------------------
st.markdown("""
<style>
body {
    background-color: #ffffff;
}

/* Container spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Headings */
h1, h2, h3 {
    color: #E23744;
}

/* Banner */
.banner {
    background: linear-gradient(90deg, #E23744, #ff6b6b);
    padding: 20px;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 15px;
}

/* Cards */
.card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 14px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* Text */
.small-text {
    font-size: 14px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 📊 LOAD DATA
# -------------------------
df = pd.read_csv("zomato_customer_data.csv")
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# -------------------------
# 🔥 HEADER
# -------------------------
st.markdown("""
<div class="banner">
<h3>"Your margin is my opportunity." – Jeff Bezos</h3>
<p style="font-size:14px;">Food delivery is about demand, behavior, and unit economics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<marquee style="color:#E23744;">
Zomato profitability push • Rising delivery costs • Tier-2 demand growth • Quick commerce competition
</marquee>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# 🖼️ IMAGES GRID (RESPONSIVE)
# -------------------------
st.subheader("📍 Field Observations")

cols = st.columns(3)

images = [
    "image1.jpeg",
    "image2.jpeg",
    "image3.jpeg",
    "image4.jpeg",
    "image5.jpeg",
    "image6.jpeg"
]

for i, img in enumerate(images):
    try:
        with cols[i % 3]:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(Image.open(img), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    except:
        pass

st.markdown("---")

# -------------------------
# 📊 METRICS
# -------------------------
st.subheader("📊 Demand Snapshot")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Order Value", f"₹{round(df['avg_order_value'].mean(),2)}")
col2.metric("Orders/Month", round(df['order_frequency'].mean(),2))
col3.metric("Discount Sensitivity", f"{round(df['discount_sensitivity'].mean()*100,1)}%")

st.markdown("""
<div class="card">
Demand is driven by repeat behavior rather than acquisition — indicating habit-based consumption patterns.
</div>
""", unsafe_allow_html=True)

# -------------------------
# 📈 CHARTS (STACKED FOR MOBILE)
# -------------------------
st.subheader("📈 Demand Distribution")

fig, ax = plt.subplots()
ax.hist(df['avg_order_value'], bins=10)
st.pyplot(fig)

st.subheader("👤 Customer Behavior")

fig2, ax2 = plt.subplots()
ax2.scatter(df['age'], df['order_frequency'])
ax2.set_xlabel("Age")
ax2.set_ylabel("Orders")
st.pyplot(fig2)

# -------------------------
# 🍽️ CUISINE
# -------------------------
st.subheader("🍽️ Cuisine Demand")

st.bar_chart(df['preferredcuisine'].value_counts())

st.markdown("""
<div class="card">
Fast food and biryani dominate — indicating convenience-driven and high-frequency demand segments.
</div>
""", unsafe_allow_html=True)

# -------------------------
# 🚀 STRATEGY
# -------------------------
st.subheader("🚀 Growth Strategy")

st.markdown("""
- Optimize menu conversion  
- Reduce blanket discounting  
- Focus on repeat customers  
- Scale high-performing partners  
""")

st.success("Demand exists. Execution determines growth.")

st.markdown("---")

# -------------------------
# 🧠 DESIGNER NOTE (SMART POSITIONING)
# -------------------------
st.markdown("""
<div class="small-text">

My understanding of food delivery ecosystems has been shaped through a combination of on-ground exposure and structured analysis.  

Across multiple cities, I have observed how restaurants operate — from legacy establishments such as Soam and Aaram Vada Pav in Mumbai to regional formats like Lotus Valley in Madhya Pradesh — focusing on positioning, menu design, and demand behavior.  

These observations extended into understanding how platforms like Zomato and Swiggy influence visibility, pricing, and repeat consumption.  

In parallel, exposure to retail systems provided insight into inventory movement, distributor coordination, and execution at the last mile.  

Formally, during my internship at Volvo Eicher Commercial Vehicles, I worked on forecasting, industry analysis, and cross-functional collaboration — strengthening my ability to approach problems through structured reasoning and data-backed decision-making.  

Together, these experiences reflect a consistent approach: observing systems, identifying growth drivers, and translating them into actionable insights.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# 🔄 EXPERIENCE SELECTOR
# -------------------------
st.subheader("📍 Selected Experiences")

exp = st.selectbox("Explore", [
    "Soam – Mumbai",
    "Aaram Vada Pav – Mumbai",
    "Lotus Valley – Madhya Pradesh",
    "Retail & Supply Chain",
    "VECV Internship"
])

if exp == "Soam – Mumbai":
    st.image("image1.jpeg", use_container_width=True)
    st.write("Legacy restaurant with strong brand recall and consistent demand.")

elif exp == "Aaram Vada Pav – Mumbai":
    st.image("image2.jpeg", use_container_width=True)
    st.write("High-volume fast format optimized for speed and pricing.")

elif exp == "Lotus Valley – Madhya Pradesh":
    st.image("image4.jpeg", use_container_width=True)
    st.write("Regional dining reflecting localized demand and menu positioning.")

elif exp == "Retail & Supply Chain":
    st.image("image6.jpeg", use_container_width=True)
    st.write("Observed inventory flow, distributor coordination, and retail execution.")

elif exp == "VECV Internship":
    st.image("image3.jpeg", use_container_width=True)
    st.write("Worked on forecasting, analysis, and cross-functional coordination.")