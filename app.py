import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import random

st.set_page_config(page_title="Zomato Growth Intelligence", layout="centered")

# -------------------------
# 🎨 ZOMATO UI (RESPONSIVE)
# -------------------------
st.markdown("""
<style>
body {background-color: #ffffff;}
h1, h2, h3 {color: #E23744;}

.banner {
    background: linear-gradient(90deg, #E23744, #ff6b6b);
    padding: 18px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

.card {
    background-color: white;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 12px;
}

.small-text {
    text-align:center;
    color:gray;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 📊 LOAD DATA
# -------------------------
df = pd.read_csv("zomato_customer_data.csv")
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# -------------------------
# 🔥 DYNAMIC HEADER
# -------------------------
avg_order = df['avg_order_value'].mean()
order_freq = df['order_frequency'].mean()
discount = df['discount_sensitivity'].mean()

if discount > 0.8:
    insight = "Demand is heavily price-driven, indicating discount-led conversion."
elif order_freq > 9:
    insight = "High repeat ordering suggests habit-driven consumption."
else:
    insight = "Balanced demand with scope for improving retention and conversion."

quotes = [
    '"Your margin is my opportunity." – Jeff Bezos',
    '"However beautiful the strategy, you should occasionally look at the results." – Winston Churchill',
    '"People don’t buy what you do; they buy why you do it." – Simon Sinek'
]

selected_quote = random.choice(quotes)

st.markdown(f"""
<div class="banner">
<h3>{selected_quote}</h3>
<p style="font-size:13px; margin-top:10px;">📊 Insight: {insight}</p>
</div>
""", unsafe_allow_html=True)

# 📌 Quote context (real credibility)
st.caption("The quote reflects a low-margin, scale-driven strategy used by companies like Amazon to disrupt markets. :contentReference[oaicite:0]{index=0}")

# -------------------------
# 📰 NEWS TICKER
# -------------------------
st.markdown("""
<marquee style="color:#E23744;">
Zomato profitability push • Rising delivery costs • Tier-2 demand growth • Increasing focus on unit economics and retention
</marquee>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# 🖼️ TOP IMAGES
# -------------------------
st.subheader("📍 Field Observations")

image_files = [
    "image1.jpeg",
    "image2.jpeg",
    "image3.jpeg",
    "image4.jpeg",
    "image5.jpeg",
    "image6.jpeg"
]

for img in image_files:
    try:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(Image.open(img), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        pass

st.markdown("""
<div class="small-text">
On-ground exposure across restaurants, cities, and operational systems shaping my understanding of demand and execution.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# 📊 DEMAND METRICS
# -------------------------
st.subheader("📊 Demand Snapshot")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Order Value", f"₹{round(avg_order,2)}")
col2.metric("Orders/Month", round(order_freq,2))
col3.metric("Discount Sensitivity", f"{round(discount*100,1)}%")

st.markdown("""
<div class="card">
Demand is driven by repeat users with moderate ticket size — indicating habit formation rather than one-time acquisition.
</div>
""", unsafe_allow_html=True)

# -------------------------
# 📈 VISUALS
# -------------------------
fig, ax = plt.subplots()
ax.hist(df['avg_order_value'], bins=10)
st.pyplot(fig)

# -------------------------
# 👤 CUSTOMER BEHAVIOR
# -------------------------
st.subheader("👤 Customer Behavior")

fig2, ax2 = plt.subplots()
ax2.scatter(df['age'], df['order_frequency'])
ax2.set_xlabel("Age")
ax2.set_ylabel("Order Frequency")
st.pyplot(fig2)

st.markdown("""
<div class="card">
Core users (18–35) dominate ordering frequency. Retention and repeat behavior are key growth levers.
</div>
""", unsafe_allow_html=True)

# -------------------------
# 🍽️ CUISINE ANALYSIS
# -------------------------
st.subheader("🍽️ Cuisine Demand")

st.bar_chart(df['preferredcuisine'].value_counts())

st.markdown("""
<div class="card">
Fast food and biryani dominate — reflecting convenience-driven, high-satisfaction consumption patterns.
</div>
""", unsafe_allow_html=True)

# -------------------------
# 🚀 STRATEGY
# -------------------------
st.subheader("🚀 Growth Strategy")

st.markdown("""
- Improve menu conversion  
- Reduce blanket discounting  
- Focus on repeat customers  
- Scale top-performing partners  
""")

st.success("Demand exists. Execution determines growth.")

st.markdown("---")

# -------------------------
# 🔄 EXPERIENCE SELECTOR (REVOLVING)
# -------------------------
st.subheader("📍 Selected Experiences")

exp = st.selectbox("Explore", [
    "Soam – Mumbai",
    "Aaram Vada Pav – Mumbai",
    "Lotus Valley – MP",
    "Urban Observations",
    "Retail & Supply Chain",
    "VECV Internship"
])

if exp == "Soam – Mumbai":
    st.image("image1.jpeg", use_container_width=True)
    st.markdown("Consistency-driven legacy dining with strong brand recall and demand stability.")

elif exp == "Aaram Vada Pav – Mumbai":
    st.image("image2.jpeg", use_container_width=True)
    st.markdown("High-volume model optimized for speed, pricing efficiency, and repeat consumption.")

elif exp == "Lotus Valley – MP":
    st.image("image4.jpeg", use_container_width=True)
    st.markdown("Regional format reflecting localized demand and differentiated positioning.")

elif exp == "Urban Observations":
    st.image("image5.jpeg", use_container_width=True)
    st.markdown("Observed demand variation across locations, formats, and customer segments.")

elif exp == "Retail & Supply Chain":
    st.image("image6.jpeg", use_container_width=True)
    st.markdown("Studied inventory flow, distributor dynamics, and execution in regulated product ecosystems.")

elif exp == "VECV Internship":
    st.image("image3.jpeg", use_container_width=True)
    st.markdown("Worked on forecasting, analysis, and cross-functional coordination across departments.")

st.markdown("---")

# -------------------------
# 🧠 DESIGNER NOTE (SUBTLE POSITIONING)
# -------------------------
st.markdown("""
<div style="font-size:14px; line-height:1.7;">

My understanding of demand-driven ecosystems has been shaped through a combination of on-ground observation and structured analysis.  

Across multiple cities, I have examined how restaurants position themselves, design menus, and interact with aggregator platforms in driving visibility and demand — from legacy establishments to high-volume formats.  

In parallel, exposure to adjacent retail systems provided insight into inventory flows, distributor coordination, and execution across operational layers.  

Formally, during my internship at Volvo Eicher Commercial Vehicles (VECV), I worked on forecasting, industry analysis, and cross-functional collaboration — strengthening my ability to approach problems through structured reasoning and stakeholder alignment.  

Together, these experiences reflect a consistent approach: observing systems, identifying drivers of growth, and translating them into actionable insights.

</div>
""", unsafe_allow_html=True)
