# 📊 NovaMart Marketing Analytics Dashboard

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://novamart-marketing-dashboard.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**🚀 [Live Dashboard](https://novamart-marketing-dashboard.streamlit.app/) | 📫 [Contact Developer](https://asoundankar.netlify.app/)**

*An interactive marketing analytics platform with 20+ advanced visualizations for data-driven decision making*

</div>

---

## 👨‍💻 Developer

**Created by [Atharva Soundankar](https://asoundankar.netlify.app/)**  
*Masters of AI in Business - Data Visualization Assignment*

Connect with me: [Portfolio](https://asoundankar.netlify.app/) | [GitHub](https://github.com/mercydeez)

---

## 🎯 Overview

This project simulates **2 years (2023-2024)** of marketing data for **NovaMart**, a fictional omnichannel retail company operating across India. The dashboard provides comprehensive insights into campaign performance, customer behavior, product sales, and ML-powered lead scoring.

### ✨ Key Features

- 📈 **Real-time Campaign Analytics** - Track performance across 5+ marketing channels
- 👥 **Customer Intelligence** - Segment analysis with churn prediction
- 🛍️ **Product Performance** - Category-wise sales and profit margins
- 🤖 **ML Model Insights** - Lead scoring with ROC curves and feature importance
- 🗺️ **Geographic Analysis** - State-level performance mapping
- 🔄 **Multi-Touch Attribution** - Compare 5 attribution models

---

## 📊 Dashboard Sections

| Section | Visualizations | Key Insights |
|---------|----------------|--------------|
| **Campaign Performance** | 8 charts | Revenue trends, channel efficiency, CTR analysis |
| **Customer Analytics** | 6 charts | Segmentation, LTV distribution, NPS analysis |
| **Product Insights** | 5 charts | Category sales, profit margins, regional performance |
| **ML Models** | 4 charts | Confusion matrix, ROC curve, feature importance |
| **Geographic Analysis** | 5 charts | State-wise revenue, market penetration, satisfaction |
| **Attribution & Funnel** | 5+ charts | Multi-touch attribution, conversion funnel, journey paths |

**Total:** 33+ Interactive Visualizations

---

## 📁 Dataset Overview

| File | Records | Description |
|------|---------|-------------|
| `campaign_performance.csv` | 5,858 | Daily campaign metrics (impressions, clicks, conversions, spend, revenue) |
| `customer_data.csv` | 5,000 | Customer demographics, behavior, and churn indicators |
| `product_sales.csv` | 1,440 | Hierarchical product sales by category/subcategory |
| `lead_scoring_results.csv` | 2,000 | ML model predictions vs actual conversions |
| `feature_importance.csv` | 11 | Pre-calculated feature importance scores |
| `learning_curve.csv` | 11 | Training/validation scores at different data sizes |
| `geographic_data.csv` | 15 | State-level performance metrics with coordinates |
| `channel_attribution.csv` | 8 | Multi-touch attribution model comparison |
| `funnel_data.csv` | 6 | Marketing funnel stages and conversion rates |
| `customer_journey.csv` | 8 | Multi-touchpoint customer paths |
| `correlation_matrix.csv` | 10×10 | Pre-computed metric correlations |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/mercydeez/novamart-marketing-dashboard.git
cd novamart-marketing-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up project structure**
```
novamart-marketing-dashboard/
├── data/
│   ├── campaign_performance.csv
│   ├── customer_data.csv
│   ├── product_sales.csv
│   ├── lead_scoring_results.csv
│   ├── feature_importance.csv
│   ├── learning_curve.csv
│   ├── geographic_data.csv
│   ├── channel_attribution.csv
│   ├── funnel_data.csv
│   ├── customer_journey.csv
│   └── correlation_matrix.csv
├── app.py
├── requirements.txt
└── README.md
```

4. **Run the dashboard**
```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **Visualization:** Plotly, Plotly Express
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Deployment:** Streamlit Cloud

---

## 📈 Key Business Insights

### Campaign Performance
- 🎆 **Seasonality:** Diwali (Oct-Nov) and Christmas (Dec) show 30-40% revenue boost
- 📅 **Weekend Effects:** Social media performs better on weekends; LinkedIn drops 40%
- 📧 **Channel Patterns:** Email has highest CVR; Google Ads highest volume

### Customer Intelligence
- 💎 **Premium Segment:** 2.5x higher LTV than basic customers
- ⚠️ **Churn Indicators:** Low satisfaction + high support tickets = churn risk
- 📊 **Demographics:** Peak income at age 45-50

### Product Performance
- 📱 **Electronics:** Highest volume in Q4
- 👗 **Fashion:** Highest margins in Q2-Q3
- 🌏 **Regional:** West and South regions outperform

### ML Model Performance
- 🎯 **AUC Score:** ~0.75-0.80 (good predictive performance)
- 🔑 **Top Features:** Webinar attendance and form submissions
- ✅ **Model Status:** Well-calibrated with minimal variance

---

## 📊 Visualization Techniques

<details>
<summary><b>Click to expand full visualization list</b></summary>

- ✅ Bar Charts (Simple, Grouped, Stacked)
- ✅ Line Charts & Area Charts
- ✅ Scatter Plots & Bubble Charts
- ✅ Box Plots & Violin Plots
- ✅ Histograms & Distribution Analysis
- ✅ Heatmaps & Correlation Matrices
- ✅ Treemaps & Sunburst Charts
- ✅ Funnel Charts & Journey Paths
- ✅ Choropleth Maps & Bubble Maps
- ✅ Confusion Matrices & ROC Curves
- ✅ Feature Importance & Learning Curves
- ✅ Pie Charts & Donut Charts

</details>

---

## 🎨 Dashboard Features

### Interactive Filters
- 📅 **Date Range Selector** - Analyze specific time periods
- 🌍 **Region Filter** - Focus on geographical areas
- 📢 **Channel Filter** - Isolate marketing channels

### Real-time Metrics
- 💰 Total Revenue & ROAS
- 🎯 Conversion Rates & CTR
- 👥 Customer Retention & Churn
- 📊 Campaign Performance KPIs

### Advanced Analytics
- 🔄 Multi-touch attribution modeling
- 🧠 ML-powered lead scoring
- 📍 Geographic performance mapping
- 🛒 Customer journey analysis

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Atharva Soundankar**

- 🌐 Portfolio: [asoundankar.netlify.app](https://asoundankar.netlify.app/)
- 💼 GitHub: [@mercydeez](https://github.com/mercydeez)
- 📧 Email: Available on portfolio

---

## 🙏 Acknowledgments

- Dataset designed for Masters of AI in Business program
- Built with Streamlit and Plotly for interactive visualizations
- Inspired by real-world marketing analytics challenges

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

[![GitHub stars](https://img.shields.io/github/stars/mercydeez/novamart-marketing-dashboard?style=social)](https://github.com/mercydeez/novamart-marketing-dashboard/stargazers)

**Made with ❤️ by [Atharva Soundankar](https://asoundankar.netlify.app/)**

</div>
