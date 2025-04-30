import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Quantum Portfolio Dashboard 🚀", layout="wide", page_icon="📈")

# ---------- LOAD DATA ----------
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_csv("portfolio_results.csv")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("📂 Upload & Settings")
    uploaded_file = st.file_uploader("Upload your Portfolio CSV", type=["csv"])
    
    risk_tolerance = st.slider("🎯 Select Risk Tolerance", 0.0, 1.0, 0.5, step=0.05)
    
    st.markdown("---")
    menu = st.radio("📑 Navigation", ["🏠 Overview", "📊 Visualizations", "📁 Download Results", "✅ Conclusion"])

# ---------- LOAD PORTFOLIO DATA ----------
df = load_data(uploaded_file)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Calculate growth
growth = (df['Portfolio_Value'].iloc[-1] / df['Portfolio_Value'].iloc[0] - 1) * 100

# ---------- LANDING PAGE ANIMATION ----------
def landing_animation():
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style="font-size: 48px;">🚀 Welcome to the Quantum Portfolio Dashboard</h1>
            <p style="font-size: 20px;">Smarter Investments Powered by Quantum Computing</p>
            <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="400">
        </div>
        """, unsafe_allow_html=True
    )

# ---------- OVERVIEW ----------
if menu == "🏠 Overview":
    landing_animation()
    
    st.markdown("---")
    st.subheader("🔍 Portfolio Snapshot")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📅 Start Date", df['Date'].iloc[0].strftime("%b %d, %Y"))
    col2.metric("💰 Latest Portfolio Value", f"${df['Portfolio_Value'].iloc[-1]:,.2f}")
    col3.metric("📈 Total Growth", f"{growth:.2f}%")
    
    st.success(f"🎯 Risk Tolerance Set to: {risk_tolerance:.2f}")

    st.markdown("""
    ---
    ### 📜 About
    This dashboard visualizes your portfolio growth, stock allocations, and provides custom investment recommendations based on your risk preferences.
    """)

# ---------- VISUALIZATIONS ----------
elif menu == "📊 Visualizations":
    st.title("📊 Portfolio Visualizations")
    
    st.subheader("📈 Portfolio Value Over Time")
    fig_line = px.line(df, x='Date', y='Portfolio_Value', title="Portfolio Growth", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.subheader("📊 Stocks Allocation (Latest Selection)")
    try:
        latest_stocks = eval(df['Selected_Stocks'].iloc[-1])
        if latest_stocks:
            stock_counts = pd.Series(latest_stocks).value_counts()
            fig_bar = px.bar(stock_counts, x=stock_counts.index, y=stock_counts.values, labels={"x": "Stock", "y": "Frequency"}, title="Stock Selection Frequency")
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.warning("No stock selections found.")
    except Exception:
        st.error("Error parsing Selected_Stocks field.")

    st.subheader("📈 Risk vs Return (Sample Simulation)")
    fake_risks = [0.10, 0.15, 0.20, 0.25, 0.30]
    fake_returns = [0.12, 0.18, 0.22, 0.27, 0.35]
    stock_names = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN']
    
    fig_risk_return = px.scatter(
        x=fake_risks, y=fake_returns, text=stock_names,
        labels={'x': 'Risk (Std Deviation)', 'y': 'Expected Return'},
        size=[50]*5, color=stock_names, title="Simulated Risk vs Return"
    )
    fig_risk_return.update_traces(textposition='top center')
    st.plotly_chart(fig_risk_return, use_container_width=True)

    st.subheader("🎯 Personalized Portfolio Recommendation")
    if risk_tolerance < 0.3:
        st.success("🛡️ Low Risk Portfolio Suggested: **MSFT, AAPL**")
    elif risk_tolerance < 0.7:
        st.success("🚀 Moderate Risk Portfolio Suggested: **GOOG, AMZN, AAPL**")
    else:
        st.success("🔥 High Risk Portfolio Suggested: **TSLA, AMZN, GOOG**")

# ---------- DOWNLOAD RESULTS ----------
elif menu == "📁 Download Results":
    st.title("📥 Download Portfolio Data")
    
    st.dataframe(df, use_container_width=True)
    
    st.download_button(
        label="⬇️ Download Full Portfolio CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="quantum_portfolio_results.csv",
        mime="text/csv"
    )

# ---------- CONCLUSION ----------
elif menu == "✅ Conclusion":
    st.title("✅ Final Insights & Next Steps")
    
    st.markdown(f"""
    ### 📈 Final Portfolio Overview
    - Total Growth Achieved: **{growth:.2f}%**
    - Current Portfolio Value: **${df['Portfolio_Value'].iloc[-1]:,.2f}**
    - Stocks Selected: **{', '.join(eval(df['Selected_Stocks'].iloc[-1])) if eval(df['Selected_Stocks'].iloc[-1]) else "No Stocks Selected"}**

    ### 🚀 Recommendations
    - Rebalance your portfolio based on updated risk appetite quarterly.
    - Explore quantum-enhanced optimization for better diversification.
    - Continue monitoring risk-return trade-offs actively.

    ---
    > _"Patience is the key to success in investing."_ – Warren Buffett

    Thank you for using Quantum Portfolio Dashboard! 🌟
    """)

# ---------- FOOTER ----------
st.markdown("""
---
<div style='text-align: center; font-size: 14px;'>
Made with ❤️ using Streamlit, Plotly, and Quantum Optimization 🚀
</div>
""", unsafe_allow_html=True)
