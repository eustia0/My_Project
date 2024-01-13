import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="庫存新表(PETER).xlsx",
        engine="openpyxl",
        sheet_name="查詢表",
        skiprows=3,
        usecols="D:AD",
        nrows=20000,
    )
    return df

df = get_data_from_excel()
# st.table(df)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
階段分類 = st.sidebar.multiselect(
    "階段分類:",
    options=df["階段分類"].unique(),
    default=df["階段分類"].unique()
)

舊型體 = st.sidebar.multiselect(
    "舊型體",
    options=df["舊型體"].unique(),
    default=df["舊型體"].unique(),
)

df_selection = df.query(
    "階段分類 == @階段分類 & 舊型體 == @舊型體"
)

# # Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["實際可用數量"].sum())
# average_rating = round(df_selection["Rating"].mean(), 1)
# star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["實際可用數量"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("實際可用數量:")
    st.subheader(f"{total_sales:,}")
# with middle_column:
#     st.subheader("Average Rating:")
#     st.subheader(f"{average_rating} {star_rating}")
# with right_column:
#     st.subheader("Average Sales Per Transaction:")
#     st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = df_selection.groupby(by=["階段分類"])[["實際可用數量"]].sum().sort_values(by="實際可用數量")
fig_product_sales = px.bar(
    sales_by_product_line,
    x="實際可用數量",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Total",
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )


left_column, right_column = st.columns(2)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# st.table(df)