import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
 
 
@st.cache_data
def load_firms():
    rng = np.random.default_rng(3)
    n = 300
    return pd.DataFrame({
        "firm": [f"Firm {i:03d}" for i in range(n)],
        "industry": rng.choice(["Service", "Manufacturing", "Finance"], n),
        "Revenue": rng.integers(100, 1500, n),
        "COGS": rng.integers(100, 1200, n),
    })
 
 
firms = load_firms()
 
st.title("Graph of Gross Margin Components")
st.subheader("Example of interactive drag-and-select to display data from scatter plot.")
st.caption("Drag a box or lasso over the points to list those firms.")
fig = px.scatter(firms, x="COGS", y="Revenue", hover_name="firm")
event = st.plotly_chart(fig, on_select="rerun", selection_mode=("box", "lasso"))
 
rows = event.selection.point_indices
if rows:
    st.dataframe(firms.iloc[rows], hide_index=True)
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


