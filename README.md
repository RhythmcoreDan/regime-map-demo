Regime Map Demo

A lightweight demonstration of a market regime classifier using trend strength and volatility to categorize market conditions.

This is a simplified, safe, public version of the regime engine used in my full trading system (RhythmCore).

🚀 What This Demo Shows

This demo computes:

Trend Strength
Rolling directional momentum using close-to-close returns.

Volatility
Rolling standard deviation of returns.

Regime Classification
A simple, intuitive map of market states:

Possible Regimes:

TRENDING_BULL

TRENDING_BEAR

TRENDING_BULL_HIGH_VOL

TRENDING_BEAR_HIGH_VOL

CHOPPY_HIGH_VOL

CHOPPY_LOW_VOL

UNKNOWN (insufficient data)

This lets you quickly identify when markets are stable, directional, or chaotic.

📂 Project Structure
regime-map-demo/
│
├── regime_map_demo.py     # Core regime engine
├── run_demo.py            # Demo runner (add this if needed)
├── sample_data.csv        # Candle sample
└── README.md

🧪 How to Run

Make sure you have pandas:

pip install pandas


Then run:

python run_demo.py


(If you want, I can generate run_demo.py for this repo too — just say the word.)

📊 Example Regime Output
2024-01-10 | close=1.1210 | TRENDING_BULL
2024-01-11 | close=1.1225 | TRENDING_BULL_HIGH_VOL
2024-01-12 | close=1.1200 | CHOPPY_LOW_VOL
2024-01-13 | close=1.1195 | CHOPPY_HIGH_VOL
2024-01-14 | close=1.1180 | TRENDING_BEAR

🧠 About This Project

This demo shows a simple version of how I approach:

Regime detection

State classification

Multi-factor analysis

System architecture for trading bots

My full system integrates this with emotional engines, execution layers, and real-time data feeds.

🤝 Collaboration

If you’d like to build custom indicators, trading bots, or regime systems, I’m open to collaboration.
