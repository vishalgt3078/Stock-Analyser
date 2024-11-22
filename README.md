# Stock Analysis Tool 📈

A comprehensive Python-based tool for analyzing Indian NSE stocks. This project uses **Yahoo Finance** data to calculate and evaluate key fundamental and technical metrics for a given stock and provides an overall investment score.

---

## Features 🚀

### 1. Fundamental Analysis
- **P/E Ratio**: Price-to-Earnings ratio.
- **P/B Ratio**: Price-to-Book ratio.
- **ROE**: Return on Equity (%).
- **Debt-to-Equity**: Financial leverage ratio.
- **Revenue Growth**: Quarterly growth of revenue (%).

### 2. Technical Analysis
- **SMA Gap**: Percentage difference between 50-day and 200-day Simple Moving Averages.
- **RSI**: Relative Strength Index to assess stock momentum.

### 3. Investment Scoring
- Normalize and weight metrics to calculate a final investment score on a 0-100 scale.
- Interpretation of the score to help make informed investment decisions.

---

## Installation 💻

1. Clone this repository:
   ```bash
   git clone https://github.com/vishalgt3078/Stock-Analyser.git
   cd Stock-Analyser
2. Install the required packages:
   ```bash
   pip install yfinance numpy pandas


## Usage 📊
Run the script:
```bash
python stock_analysis.py
```
- Enter the NSE stock ticker (e.g., RELIANCE for Reliance Industries).
- View the analysis report:
- Fundamental data
- Technical indicators
- Normalized scores
- Final investment score with interpretation

## Sample Output 📜
Enter the NSE stock ticker: TCS

Analyzing TCS...

**=== Stock Analysis Report ===**
- **Ticker: TCS.NS**

*Fundamental Data:*
- P/E Ratio: 30.25
- P/B Ratio: 8.50
- ROE: 25.12%
- Debt-to-Equity: 40.00
- Revenue Growth: 12.15%

*Technical Indicators:*
- SMA Gap (%): 3.20
- RSI: 65.42

*Normalized Scores (0-100, higher is better):*
- P/E Ratio: 73.33
- P/B Ratio: 80.00
- ROE: 83.87
- Debt-to-Equity: 70.00
- Revenue Growth: 85.75
- SMA Gap (%): 90.00
- RSI: 90.00

**Final Investing Score: 81.23/100**

*Interpretation:*
- Strong investment potential
- Company shows good fundamentals and technical strength


# How It Works ⚙️

## Fundamental Data  
- **Yahoo Finance API**: Fetches company financials and metadata.  
- Calculates growth, valuation ratios, and profitability.  

## Technical Data  
- Fetches up to 1 years of historical price data.  
- Computes 50-day and 200-day SMAs and RSI.  

## Score Calculation  
1. Normalizes each metric to a 0-100 scale.  
2. Assigns weights:  
   - **P/E Ratio**: 15%  
   - **P/B Ratio**: 15%  
   - **ROE**: 20%  
   - **Debt-to-Equity**: 10%  
   - **Revenue Growth**: 20%  
   - **SMA Gap**: 10%  
   - **RSI**: 10%  
3. Computes the weighted score.  

---
## Sample Deployed Link 🌐
Check out the deployed version of the project:
`https://vishalgt3078-stock-analyser-app-wnytgr.streamlit.app/`

## Author 👤
Created by Vishal Gupta. Feel free to connect with me on:
- LinkedIn: `https://www.linkedin.com/in/vishal-gupta-146477205/`
## Final Thoughts
This tool is intended for educational and research purposes and should not be used as the sole basis for investment decisions. Always perform your own due diligence or consult with a financial advisor before making investment decisions
