import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Demo App",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Databricks Asset Bundle Demo App")
st.markdown("This is a simple Streamlit app deployed via Databricks Asset Bundles.")

# Create sample data (same as in our notebooks)
st.header("📊 Sample Data")
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = pd.DataFrame(data, columns=["name", "value"])

# Display the data
st.dataframe(df, use_container_width=True)

# Simple chart
st.header("📈 Simple Chart")
st.bar_chart(df.set_index("name"))

# Interactive elements
st.header("🎛️ Interactive Elements")
col1, col2 = st.columns(2)

with col1:
    multiplier = st.slider("Value Multiplier", 1, 10, 2)
    
with col2:
    show_processed = st.checkbox("Show Processed Data", value=True)

if show_processed:
    processed_df = df.copy()
    processed_df["processed_value"] = processed_df["value"] * multiplier
    processed_df["status"] = "processed"
    
    st.subheader("Processed Data")
    st.dataframe(processed_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("*Deployed with Databricks Asset Bundles* 🎯") 