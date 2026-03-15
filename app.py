import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Trend Analyzer", layout="wide")

st.title("Universal Trend Analyzer")

st.write("Type anything to see how trending it is!")

# user input
keyword = st.text_input("Enter a topic (Example: IPL, AI, Python, Virat Kohli)")

if keyword:

    pytrends = TrendReq(hl='en-US', tz=330)

    pytrends.build_payload([keyword], timeframe='today 12-m')

    data = pytrends.interest_over_time()

    if not data.empty:

        data = data.drop(columns=['isPartial'])

        # trend percentage
        trend_percent = data[keyword].mean()

        st.metric(
            "🔥 Trend Percentage",
            f"{trend_percent:.2f}%"
        )

        st.subheader("Trend Over Time")

        fig = px.line(
            data,
            x=data.index,
            y=keyword,
            title=f"{keyword} Trend (Last 12 Months)"
        )

        st.plotly_chart(fig, use_container_width=True)

        max_value = data[keyword].max()
        max_date = data[keyword].idxmax()

        st.success(
            f"Highest interest: {max_value}% on {max_date.date()}"
        )

        st.subheader("Region Interest")

        region = pytrends.interest_by_region()

        if not region.empty:

            region = region.sort_values(by=keyword, ascending=False).head(10)

            fig2 = px.bar(
                region,
                x=region.index,
                y=keyword,
                title="Top Regions Searching This Topic"
            )

            st.plotly_chart(fig2)

    else:
        st.warning("No trend data found")