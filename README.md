# 🚀 Quantum Portfolio Dashboard

An interactive Streamlit-based dashboard that visualizes quantum-optimized investment portfolios and simulates stock performance based on risk tolerance.

---

## 📌 Features
- Upload your own CSV portfolio file or use the default sample.
- Visualize portfolio growth, stock selections, and risk-return simulations.
- Get personalized investment recommendations based on selected risk tolerance.
- Export full results as CSV for further analysis.

---

## 📂 File Upload Format
Make sure your uploaded CSV contains at least the following columns:
- `Date`
- `Portfolio_Value`
- `Selected_Stocks` (as a Python-style list string, e.g., `['AAPL', 'GOOG']`)

---

## 📊 Tech Stack
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)

---

## ▶️ How to Run
```bash
# Clone the repository
git clone https://github.com/your-username/quantum-portfolio-dashboard.git
cd quantum-portfolio-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
