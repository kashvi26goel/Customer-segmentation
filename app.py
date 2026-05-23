import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load your processed files 
data = pd.read_csv(r"C:\\Users\\Hp\Desktop\\Data analysis Projects\\Customer Segmentation\df_enco")  
cluster_avg = pd.read_csv(r"C:\\Users\\Hp\\Desktop\\Data analysis Projects\\Customer Segmentation\\clus_mean")
cluster_lb = {
    0: 'Young Budget Shoppers',
    1: 'Older Budget Enthusiasts',
    2: 'Senior Premium Buyers',
    3: 'Budget Luxury Shoppers',
    4: 'Senior Premium Buyers 1',
    5: 'Affluent Home Improvers'
} 
data['Cluster_Label'] = data['Cluster'].map(cluster_lb)

# --- PHASE 1: Title & Introduction ---
st.set_page_config(layout="wide")
st.title("🛍️ Customer Segmentation Dashboard")
st.markdown("""
    Discover hidden customer patterns, decode shopper behavior,
    and unlock smarter marketing moves using intelligent segmentation.

""", unsafe_allow_html=True)



# --- PHASE 2: Cluster Overview ---
st.header("🔍 Clustering Overview")
st.markdown("""
Using techniques like *KMeans Clustering* and *Principal Component Analysis*, 
we have segmented customers into distinct groups based on their behavior, preferences, and spending patterns.
""")

# --- PHASE 3: Customer Segments Snapshot ---
st.header("👥 Customer Segment Summaries")

# Dictionary containing detailed descriptions
cluster_desc = {
    0: 'Low Spenders & Young Shoppers & Prefer Home & Garden & Mostly Male',
    1: 'Low Spenders & Older Consumers & Prefer Sports',
    2: 'High-Income & Frequent Shoppers & Big Spenders & Older Consumers & Prefer Groceries',
    3: 'Low-Income & High Spenders & Prefer Groceries & Mostly Female',
    4: 'Low-Income & Big Spenders & Older Consumers & Prefer Electronics & Mostly Other',
    5: 'High-Income & Older Consumers & Prefer Home & Garden'
}

cols = st.columns(3)
for i, cluster in enumerate(cluster_avg.index):
    with cols[i % 3]:
        st.subheader(f"Segment {cluster}: {cluster_lb[cluster]}")
        st.markdown(f"*Description:* {cluster_desc[cluster]}")
        st.write(cluster_avg.loc[cluster][['income', 'spending_score', 'purchase_frequency']])
# --- PHASE 4: Cluster Distribution ---
st.header("📊 Cluster Distribution")
cluster_counts = data['Cluster_Label'].value_counts()
fig1 = px.pie(values=cluster_counts.values, names=cluster_counts.index, title="Customer Segment Proportions")
st.plotly_chart(fig1, use_container_width=True)

# --- PHASE 5: PCA Scatter Plot ---
st.header("🧭 2D PCA Scatter Plot")
fig2 = px.scatter(
    data,
    x="PCA1", y="PCA2",
    color="Cluster_Label",
    hover_data=["income", "spending_score", "purchase_frequency"],
    title="Customer Segments Visualized in 2D"
)
st.plotly_chart(fig2, use_container_width=True)

# --- PHASE 6: Segment-wise Key Traits ---
st.header("📌 Segment-wise Traits")

selected_cluster = st.selectbox("Choose a Segment", options=sorted(data['Cluster'].unique()))
selected_means = cluster_avg.loc[selected_cluster]

traits = selected_means[[
    'income', 'spending_score', 'purchase_frequency',
    'last_purchase_amount', 'age_group'
]]
fig3 = px.bar(
    traits,
    title=f"Average Traits for Segment {selected_cluster}: {cluster_lb[selected_cluster]}",
    labels={"value": "Average Value", "index": "Feature"},
    color=traits.values,
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig3, use_container_width=True)

# --- PHASE 6.2: Gender Distribution ---
st.subheader("🔹 Gender Distribution in Selected Segment")

gender_cols = [col for col in data.columns if col.startswith('gender_')]
gender_segment = data[data['Cluster'] == selected_cluster][gender_cols].sum()
gender_segment.index = [col.replace("gender_", "") for col in gender_segment.index]

fig_gender = px.pie(
    names=gender_segment.index,
    values=gender_segment.values,
    title="Gender Split"
)
st.plotly_chart(fig_gender, use_container_width=True)

# --- PHASE 6.3: Preferred Category Distribution ---
st.subheader("🔹 Preferred Product Categories in Selected Segment")

cat_cols = [col for col in data.columns if col.startswith('preferred_category_')]
cat_segment = data[data['Cluster'] == selected_cluster][cat_cols].sum().sort_values(ascending=False)
cat_segment.index = [col.replace("preferred_category_", "") for col in cat_segment.index]

fig_cat = px.bar(
    x=cat_segment.index,
    y=cat_segment.values,
    labels={"x": "Category", "y": "Count"},
    title="Top Preferred Categories",
    color=cat_segment.values,
    color_continuous_scale="Plasma"

)

st.plotly_chart(fig_cat)

# --- PHASE 6.4: Age Distribution ---
st.subheader("🔹 Age Distribution in Selected Segment")
age_group_map = {
    0: "18-25",
    1: "25-45",
    2: "45-60",
    3: "60 and abaove",
    
}
age_segment = data[data['Cluster'] == selected_cluster]['age_group'].map(age_group_map).value_counts()

fig_age_group = px.bar(
    x=age_segment.index,
    y=age_segment.values,
    labels={"x": "Age Group", "y": "Number of Customers"},
    title="Age Group Distribution",
    color=age_segment.index  # Automatically assigns different colors
)

st.plotly_chart(fig_age_group, use_container_width=True)
# --- PHASE 7: Storytelling & Insights ---
st.header("💡 Business Insights")
st.markdown("### What does this mean for marketing and product teams?")

cluster_insight_map = {
    0: "- Engage with youth-centric UX, offer student discounts, and promote budget-friendly Home & Garden essentials tailored for young male shoppers.",
    1: "- Focus on affordable sports gear bundles, senior-friendly navigation, and build loyalty through reward programs for older budget-conscious consumers.",
    2: "- Emphasize high-quality grocery products, offer personalized shopping experiences, premium memberships, and convenient home delivery options for affluent, older frequent buyers.",
    3: "- Promote exclusive grocery deals, flexible payment options, and loyalty perks to appeal to high-spending females from lower-income groups seeking value in essentials.",
    4: "- Target tech-savvy older consumers with premium electronics bundles, subscription-based support services, and easy financing options despite lower income.",
    5: "- Offer high-end Home & Garden improvement solutions, in-home consultations, and personalized shopping journeys for affluent older customers focused on home enhancement."
}

label = cluster_lb[selected_cluster]
insight_text = cluster_insight_map.get(selected_cluster, "- General marketing and personalization strategies.")
st.info(f"*Segment {selected_cluster} ({label})*\n\n{insight_text}")
# --- PHASE 8: Footer ---
st.markdown("---")
st.markdown("Crafted for data-driven decision making and customer insights.")


