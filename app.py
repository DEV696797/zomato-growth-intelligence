import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Zomato Growth", layout="centered")

# -------------------------
# 🎨 ZOMATO UI STYLE
# -------------------------
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
.main {
    background-color: white;
}
h1, h2, h3 {
    color: #E23744;
}

/* Card style */
.card {
    background-color: #ffffff;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

/* Zomato banner */
.banner {
    background: linear-gradient(90deg, #E23744, #ff6b6b);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 🔥 HEADER
# -------------------------
st.markdown("""
<div class="banner">
<h2>Food delivery is no longer about logistics — it is about shaping demand and driving unit economics.</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<marquee style="color:#E23744;">
Zomato profitability push • Rising delivery costs • Tier-2 demand growth • Quick commerce competition
</marquee>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# 🖼️ IMAGE CARDS (ZOMATO STYLE)
# -------------------------
st.subheader("📍 Field Observations")

images = [
    "image1.jpeg",
    "image2.jpeg",
    "image3.jpeg",
    "image4.jpeg",
    "image5.jpeg",
    "image6.jpeg"
]

for img in images:
    try:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(Image.open(img), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        pass

st.markdown("---")

# -------------------------
# 📊 LOAD DATA
# -------------------------
try:
    df = pd.read_csv("zomato_customer_data.csv")
except:
    st.error("Dataset missing")

# -------------------------
# 📊 CASE: DEMAND
# -------------------------
st.subheader("📊 Demand Snapshot")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Order Value", f"₹{round(df['avg_order_value'].mean(),2)}")
col2.metric("Orders/Month", round(df['order_frequency'].mean(),2))
col3.metric("Discount %", f"{round(df['discount_used'].mean()*100,1)}%")

st.markdown('<div class="card">Demand is concentrated in repeat users with moderate ticket size, indicating habit-driven consumption.</div>', unsafe_allow_html=True)

# -------------------------
# 📈 VISUAL
# -------------------------
fig, ax = plt.subplots()
ax.hist(df['avg_order_value'], bins=10)
st.pyplot(fig)

# -------------------------
# 👤 CUSTOMER INSIGHT
# -------------------------
st.subheader("👤 Customer Behavior")

fig2, ax2 = plt.subplots()
ax2.scatter(df['age'], df['order_frequency'])
st.pyplot(fig2)

st.markdown('<div class="card">Core users (18–35) drive frequency. Growth lever lies in retention, not acquisition.</div>', unsafe_allow_html=True)

# -------------------------
# 🍽️ RESTAURANTS
# -------------------------
st.subheader("🍽️ Cuisine Demand")

st.bar_chart(df['cuisine'].value_counts())

st.markdown('<div class="card">Fast food & biryani dominate — indicating convenience-driven demand.</div>', unsafe_allow_html=True)

# -------------------------
# 🚀 STRATEGY
# -------------------------
st.subheader("🚀 Growth Strategy")

st.markdown("""
- Improve menu conversion  
- Reduce discount dependency  
- Focus on repeat users  
- Scale top-performing partners  
""")

st.success("Demand exists. Execution drives growth.")

st.markdown("---")

# -------------------------
# 🧠 DESIGNER NOTE
# -------------------------
st.markdown("""
<div style="font-size:14px; line-height:1.7;">

Across multiple cities, I have observed restaurant formats, customer behavior, and consumption patterns — from legacy establishments such as Soam and Aaram Vada Pav in Mumbai to regional formats like Lotus Valley in Madhya Pradesh.  

These observations were analytical, focused on understanding menu structuring, positioning, and the interaction between restaurants and aggregator platforms like Zomato and Swiggy in driving demand.  

In parallel, I examined adjacent retail ecosystems including regulated categories such as pet nutrition (Royal Canin, Pedigree, SmartHeart), gaining insight into inventory movement, distributor networks, and coordination between sales and warehouse operations.  

This is complemented by my internship at Volvo Eicher Commercial Vehicles, where I worked on forecasting, industry analysis, and cross-functional coordination — strengthening my ability to approach business problems through structured and data-backed reasoning.

</div>
""", unsafe_allow_html=True)