import streamlit as st
from src.fundamentals import fetch_fundamental_data
from src.technicals import calculate_technical_indicators
from src.scoring import calculate_score

# Title and Intro
st.title("📊 Stock Analyzer 🚀")
st.markdown("""
Welcome to the **Stock Analyzer**! This tool will help you evaluate a stock's fundamentals, technicals, and provide a final investment score. Simply enter the **NSE stock ticker** below and click **Analyze**. 💡
""")

# Input for Stock Ticker
ticker = st.text_input("Enter NSE stock ticker:", "").strip().upper()

# Analyze Button
if st.button("🔍 Analyze"):
    if not ticker:
        st.error("❗ Please enter a valid ticker symbol to analyze.")
    else:
        st.info(f"📈 Analyzing {ticker}... Please wait while we gather the data!")

        # Fetch Data
        fundamental = fetch_fundamental_data(ticker)
        technical = calculate_technical_indicators(ticker)
        score, normalized = calculate_score(fundamental, technical)
        
        # Displaying Fundamental Analysis
        st.subheader("📊 **Fundamental Analysis**")
        if fundamental:
            st.write(fundamental)
        else:
            st.warning("⚠️ No fundamental data available for this ticker.")

        # Displaying Technical Analysis
        st.subheader("📈 **Technical Analysis**")
        if technical:
            st.write(technical)
        else:
            st.warning("⚠️ No technical data available for this ticker.")
        
        # Displaying Normalized Scores
        st.subheader("💯 **Normalized Scores (0-100, higher is better)**")
        if normalized:
            st.write(normalized)
        else:
            st.warning("⚠️ Unable to calculate normalized scores for this ticker.")
        
        # Displaying Final Score
        st.subheader(f"🏆 **Final Investing Score**: {score:.2f}/100")
        
        # Interpretation of Score
        if score >= 70:
            st.success("🎉 **Strong investment potential!** The company shows good fundamentals and technical strength.")
        elif score >= 50:
            st.warning("⚠️ **Moderate investment potential.** Consider further research before making an investment decision.")
        else:
            st.error("❌ **Exercise caution.** The company shows weak metrics in multiple areas.")
        
        st.markdown("""
        ⚠️ **Disclaimer**: This analysis is based on publicly available data and should be used as one of many tools in your investment decision-making process.
        """)

# Footer (Optional)
st.markdown("""
#### Created with ❤️ by Vishal Gupta
""")
