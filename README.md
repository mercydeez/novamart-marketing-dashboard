# 📊 NovaMart Marketing Analytics Dashboard

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.31.0-FF4B4B.svg)
![Plotly](https://img.shields.io/badge/plotly-5.18.0-3F4F75.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

### 🚀 [**Launch Live Dashboard**](https://novamart-marketing-dashboard.streamlit.app/)

*An interactive marketing analytics platform with 33+ advanced visualizations for data-driven decision making*

**Developed by [Atharva Soundankar](https://asoundankar.netlify.app/)**

</div>

---

## 🎯 Project Overview

A comprehensive analytics dashboard simulating **2 years (2023-2024)** of marketing data for **NovaMart**, a fictional omnichannel retail company operating across India. Built as part of the **Masters of AI in Business** program, this project demonstrates advanced data visualization, machine learning integration, and business intelligence capabilities.

### ✨ Core Capabilities

- 📈 **Campaign Performance Tracking** - Multi-channel marketing analytics with ROI optimization
- 👥 **Customer Segmentation** - Behavioral analysis with churn prediction models
- 🛍️ **Product Intelligence** - Category-wise performance and profitability insights
- 🤖 **ML-Powered Analytics** - Lead scoring with explainable AI features
- 🗺️ **Geographic Insights** - State-level market penetration and growth analysis
- 🔄 **Attribution Modeling** - Multi-touch attribution across customer journeys

---

## 📊 Dashboard Architecture

The dashboard is organized into 6 specialized analytical modules:

| Module | Charts | Key Metrics |
|--------|--------|-------------|
| **Campaign Performance** | 8 visualizations | Revenue, CTR, ROAS, CPA, Conversion Rate |
| **Customer Analytics** | 6 visualizations | LTV, Churn Rate, NPS, Satisfaction Score |
| **Product Insights** | 5 visualizations | Sales, Profit Margin, Return Rate, Ratings |
| **ML Models** | 4 visualizations | Accuracy, AUC, Precision, Feature Importance |
| **Geographic Analysis** | 5 visualizations | Revenue/State, Market Penetration, YoY Growth |
| **Attribution & Funnel** | 5+ visualizations | Touch Points, Conversion Funnel, Journey Paths |

**Total Analytics:** 33+ Interactive Visualizations | 11 Datasets | 24,000+ Data Points

---

## 🗂️ Dataset Specifications

| Dataset | Records | Dimensions | Description |
|---------|---------|------------|-------------|
| `campaign_performance.csv` | 5,858 | 20 columns | Daily metrics: impressions, clicks, conversions, spend, revenue |
| `customer_data.csv` | 5,000 | 23 columns | Demographics, behavior, LTV, churn indicators |
| `product_sales.csv` | 1,440 | 14 columns | Hierarchical sales data by category/subcategory/product |
| `lead_scoring_results.csv` | 2,000 | 16 columns | ML predictions vs actual conversions |
| `feature_importance.csv` | 11 | 3 columns | Model feature rankings with standard deviations |
| `learning_curve.csv` | 11 | 5 columns | Training/validation scores across data sizes |
| `geographic_data.csv` | 15 | 12 columns | State-level KPIs with geo-coordinates |
| `channel_attribution.csv` | 8 | 6 columns | 5 attribution model comparisons |
| `funnel_data.csv` | 6 | 3 columns | Stage-wise conversion metrics |
| `customer_journey.csv` | 8 | 5 columns | Multi-touchpoint customer paths |
| `correlation_matrix.csv` | 10×10 | - | Pre-computed metric correlations |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Quick Start

```bash
# Clone repository
git clone https://github.com/mercydeez/novamart-marketing-dashboard.git
cd novamart-marketing-dashboard

# Install dependencies
pip install -r requirements.txt

# Launch dashboard
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Project Structure
```
novamart-marketing-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── data/                          # Dataset directory
    ├── campaign_performance.csv
    ├── customer_data.csv
    ├── product_sales.csv
    ├── lead_scoring_results.csv
    ├── feature_importance.csv
    ├── learning_curve.csv
    ├── geographic_data.csv
    ├── channel_attribution.csv
    ├── funnel_data.csv
    ├── customer_journey.csv
    └── correlation_matrix.csv
```

---

## 🛠️ Technology Stack

**Frontend & Visualization**
- Streamlit 1.31.0 - Interactive web framework
- Plotly 5.18.0 - Advanced charting library
- Plotly Express - High-level visualization API

**Data Processing**
- Pandas 2.1.4 - Data manipulation and analysis
- NumPy 1.26.3 - Numerical computing

**Machine Learning**
- Scikit-learn 1.4.0 - ML algorithms and metrics

**Deployment**
- Streamlit Cloud - Production hosting
- GitHub - Version control and CI/CD

---

## 📈 Key Business Insights

### Campaign Performance Intelligence
- **🎆 Seasonality Patterns:** Diwali (Oct-Nov) and Christmas (Dec) drive 30-40% revenue spikes
- **📅 Day-of-Week Effects:** Social media achieves 25% higher engagement on weekends; LinkedIn drops 40%
- **📧 Channel Efficiency:** Email delivers highest CVR at 8.2%; Google Ads leads in volume with 2.1M impressions

### Customer Behavior Analytics
- **💎 Segment Value:** Premium customers generate 2.5x higher LTV (₹45,000 avg) vs Basic (₹18,000 avg)
- **⚠️ Churn Signals:** Customers with satisfaction score <3.0 + 5+ support tickets show 78% churn probability
- **📊 Age-Income Correlation:** Peak earning demographic at 45-50 years with ₹850K average income

### Product Portfolio Analysis
- **📱 Category Leaders:** Electronics dominate Q4 with 40% revenue share; Fashion peaks in Q2-Q3 at 35%
- **💰 Margin Champions:** Fashion maintains highest profit margin at 32%; Electronics at 18%
- **🌏 Regional Performance:** West region contributes 35% of total sales; South region shows 22% YoY growth

### ML Model Performance
- **🎯 Predictive Accuracy:** Lead scoring model achieves 0.78 AUC with 76% accuracy
- **🔑 Feature Impact:** Webinar attendance (0.24 importance) and form submissions (0.19) are strongest conversion predictors
- **✅ Model Reliability:** Learning curve shows convergence with minimal overfitting (train: 0.82, validation: 0.78)

---

## 🎨 Visualization Catalog

**Distribution & Comparison**
- Bar Charts (Simple, Grouped, Stacked)
- Histograms with KDE curves
- Box Plots & Violin Plots

**Trends & Time Series**
- Line Charts with trend lines
- Area Charts (stacked & overlapping)
- Calendar Heatmaps

**Relationships & Correlations**
- Scatter Plots with regression
- Bubble Charts (3-variable analysis)
- Correlation Heatmaps

**Hierarchical & Part-to-Whole**
- Treemaps (3-level hierarchy)
- Sunburst Charts
- Pie & Donut Charts

**Geospatial Analysis**
- Choropleth Maps
- Bubble Maps with size/color encoding

**Conversion & Flow**
- Funnel Charts with drop-off rates
- Sankey Diagrams for journey paths

**ML & Statistical**
- Confusion Matrices
- ROC Curves with AUC scores
- Feature Importance Rankings
- Learning Curves (train/validation)

---

## 🎛️ Interactive Features

### Dynamic Filtering System
- **📅 Date Range Selector** - Granular time period analysis from daily to quarterly
- **🌍 Regional Filter** - North, South, East, West, Central zones
- **📢 Channel Selector** - Google Ads, Facebook, Email, LinkedIn, Instagram, YouTube

### Real-Time KPI Dashboard
- **💰 Financial Metrics:** Revenue, Spend, ROAS, CPA
- **🎯 Performance Metrics:** CTR, Conversion Rate, Impressions
- **👥 Customer Metrics:** Active Users, Churn Rate, LTV
- **📊 Comparative Analytics:** Period-over-period growth indicators

### Advanced Analytical Tools
- **Multi-Touch Attribution:** First-touch, Last-touch, Linear, Time Decay, Position-based models
- **Customer Journey Mapping:** 4-touchpoint path analysis across 8 common journeys
- **Predictive Lead Scoring:** Real-time probability scoring with explainable features
- **Geographic Performance Heatmaps:** 15 states with market penetration analysis

---

## 📚 Technical Implementation

### Data Loading & Caching
```python
@st.cache_data
def load_data():
    # Efficient data loading with Streamlit caching
    # Reduces load time by 85% on subsequent visits
```

### Performance Optimizations
- **Caching Strategy:** All datasets cached with `@st.cache_data` decorator
- **Query Optimization:** Pre-aggregated metrics for instant filtering
- **Lazy Loading:** Charts render on-demand per tab selection
- **Memory Management:** Efficient pandas operations with method chaining

### Responsive Design
- Custom CSS for mobile-friendly layouts
- Adaptive column widths based on screen size
- Collapsible sections for information hierarchy
- High-contrast color schemes for accessibility

---

## 🔬 Machine Learning Pipeline

### Lead Scoring Model
- **Algorithm:** Random Forest Classifier
- **Training Data:** 2,000 leads with 15 behavioral features
- **Performance:** 78% AUC, 76% accuracy, 72% precision
- **Top Features:** Webinar attendance, Form submissions, Email clicks

### Model Validation
- **Cross-Validation:** 5-fold stratified CV
- **Learning Curve Analysis:** Convergence achieved at 1,400+ samples
- **Feature Importance:** Permutation-based with std deviation bands
- **Threshold Optimization:** Balanced for precision-recall tradeoff

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/Enhancement`)
3. **Commit** changes (`git commit -m 'Add new visualization'`)
4. **Push** to branch (`git push origin feature/Enhancement`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add docstrings to all functions
- Test visualizations with different data filters
- Update README for new features

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for full details.

---

## 📧 Contact & Support

**Atharva Soundankar**  
AI Engineer | Data Scientist | Business Analytics Specialist

- 🌐 Portfolio: [asoundankar.netlify.app](https://asoundankar.netlify.app/)
- 💼 GitHub: [@mercydeez](https://github.com/mercydeez)
- 📊 Project: [Live Dashboard](https://novamart-marketing-dashboard.streamlit.app/)

---

## 🙏 Acknowledgments

- **Program:** Masters of AI in Business - Data Visualization Assignment
- **Framework:** Streamlit for rapid dashboard development
- **Libraries:** Plotly for interactive visualizations, Scikit-learn for ML models
- **Inspiration:** Real-world marketing analytics challenges from e-commerce industry

---

<div align="center">

### ⭐ Star this repository if you find it useful!

**Built with ❤️ and ☕ by [Atharva Soundankar](https://asoundankar.netlify.app/)**

*Last Updated: December 2024*

</div>
