import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
 
 
@st.cache_data
def load_customers():
    rng = np.random.default_rng(3)
    n = 300
    return pd.DataFrame({
        "customer": [f"Customer {i:03d}" for i in range(n)],
        "plan": rng.choice(["Basic", "Pro", "Team"], n),
        "monthly_revenue": rng.gamma(2.0, 150.0, n).round(),
        "active_users": rng.integers(1, 120, n),
    })
 
 
customers = load_customers()
 
st.title("Customers")
st.caption("Drag a box or lasso over the points to list those customers.")
fig = px.scatter(customers, x="active_users", y="monthly_revenue", hover_name="customer")
event = st.plotly_chart(fig, on_select="rerun", selection_mode=("box", "lasso"))
 
rows = event.selection.point_indices
if rows:
    st.dataframe(customers.iloc[rows], hide_index=True)
else:
    st.info("Nothing selected yet.")

st.info(
        "Below is the Python code powering this visualization, read dynamically from Github Repository."
)

try:
    with open(__file__, "r", encoding="utf-8") as f:
       source_code = f.read()
       st.code(source_code, language="python", line_numbers=True)
    except Exception as e:
       st.error(f"Could not read source file automatically: {e}")


