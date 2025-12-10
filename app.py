import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
import os

# Page configuration
st.set_page_config(
    page_title="NovaMart Marketing Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
    }
    .insight-box {
        background-color: #e8f1ff;  /* stronger contrast than plain white */
        padding: 1rem 1.2rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        color: #1f2933;            /* darker text for readability */
        box-shadow: 0 2px 4px rgba(15, 23, 42, 0.08);
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    """Load all datasets with error handling"""
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        campaign = pd.read_csv(os.path.join(BASE_DIR, 'data', 'campaign_performance.csv'))
        campaign['date'] = pd.to_datetime(campaign['date'])
        
        customer = pd.read_csv(os.path.join(BASE_DIR, 'data', 'customer_data.csv'))
        product = pd.read_csv(os.path.join(BASE_DIR, 'data', 'product_sales.csv'))
        lead_scoring = pd.read_csv(os.path.join(BASE_DIR, 'data', 'lead_scoring_results.csv'))
        feature_importance = pd.read_csv(os.path.join(BASE_DIR, 'data', 'feature_importance.csv'))
        learning_curve = pd.read_csv(os.path.join(BASE_DIR, 'data', 'learning_curve.csv'))
        geographic = pd.read_csv(os.path.join(BASE_DIR, 'data', 'geographic_data.csv'))
        attribution = pd.read_csv(os.path.join(BASE_DIR, 'data', 'channel_attribution.csv'))
        funnel = pd.read_csv(os.path.join(BASE_DIR, 'data', 'funnel_data.csv'))
        journey = pd.read_csv(os.path.join(BASE_DIR, 'data', 'customer_journey.csv'))
        correlation = pd.read_csv(os.path.join(BASE_DIR, 'data', 'correlation_matrix.csv'))
        
        return {
            'campaign': campaign,
            'customer': customer,
            'product': product,
            'lead_scoring': lead_scoring,
            'feature_importance': feature_importance,
            'learning_curve': learning_curve,
            'geographic': geographic,
            'attribution': attribution,
            'funnel': funnel,
            'journey': journey,
            'correlation': correlation
        }
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load data
data = load_data()

if data is None:
    st.stop()

# Sidebar (updated – no image, clean header + link)
st.sidebar.markdown("""
<div style='text-align:center; padding:10px 0;'>
    <h2 style='color:#1f77b4; margin-bottom:0;'>NovaMart</h2>
    <p style='color:#4a5568; font-size:13px; margin-top:2px;'>
        Marketing Analytics Dashboard
    </p>
    <p style='font-size:12px; margin-top:6px;'>
        <a href="https://github.com/mercydeez/novamart-marketing-dashboard" 
           target="_blank" 
           style="color:#3182ce; text-decoration:none;">
            View project on GitHub ↗
        </a>
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🎯 Dashboard Controls")

# Date filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(data['campaign']['date'].min(), data['campaign']['date'].max()),
    min_value=data['campaign']['date'].min(),
    max_value=data['campaign']['date'].max()
)

# Region filter
regions = ['All'] + list(data['campaign']['region'].unique())
selected_region = st.sidebar.selectbox("Select Region", regions)

# Channel filter
channels = ['All'] + list(data['campaign']['channel'].unique())
selected_channel = st.sidebar.selectbox("Select Channel", channels)

# Apply filters
filtered_campaign = data['campaign'].copy()
if selected_region != 'All':
    filtered_campaign = filtered_campaign[filtered_campaign['region'] == selected_region]
if selected_channel != 'All':
    filtered_campaign = filtered_campaign[filtered_campaign['channel'] == selected_channel]

# Main header
st.markdown('<p class="main-header">📊 NovaMart Marketing Analytics Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Comprehensive Marketing Performance & Customer Intelligence Platform</p>', unsafe_allow_html=True)

# Key Metrics
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Revenue", f"₹{filtered_campaign['revenue'].sum()/1e6:.2f}M", 
              f"{filtered_campaign['revenue'].sum()/data['campaign']['revenue'].sum()*100:.1f}%")
with col2:
    st.metric("Total Conversions", f"{filtered_campaign['conversions'].sum():,}", 
              f"{filtered_campaign['conversion_rate'].mean():.2f}% CVR")
with col3:
    st.metric("Total Spend", f"₹{filtered_campaign['spend'].sum()/1e6:.2f}M",
              f"{filtered_campaign['roas'].mean():.2f}x ROAS")
with col4:
    st.metric("Avg CTR", f"{filtered_campaign['ctr'].mean():.2f}%",
              f"↑ {(filtered_campaign['ctr'].mean() - 2.5):.2f}%")
with col5:
    st.metric("Active Customers", f"{len(data['customer']):,}",
              f"{(1-data['customer']['is_churned'].mean())*100:.1f}% Retention")

st.markdown("---")

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Campaign Performance", 
    "👥 Customer Analytics", 
    "🛍️ Product Insights",
    "🤖 ML Models",
    "🗺️ Geographic Analysis",
    "🔄 Attribution & Funnel"
])

# TAB 1: CAMPAIGN PERFORMANCE
with tab1:
    st.header("📈 Campaign Performance Analysis")
    
    # Revenue by Channel - Bar Chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue by Channel")
        channel_revenue = filtered_campaign.groupby('channel')['revenue'].sum().reset_index()
        channel_revenue = channel_revenue.sort_values('revenue', ascending=False)
        fig = px.bar(channel_revenue, x='channel', y='revenue', 
                     color='revenue', color_continuous_scale='Blues',
                     labels={'revenue': 'Revenue (₹)', 'channel': 'Marketing Channel'})
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
        <div class="insight-box">
        <b>💡 Insight:</b> {channel_revenue.iloc[0]['channel']} is the top-performing channel 
        with ₹{channel_revenue.iloc[0]['revenue']/1e6:.2f}M in revenue.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Revenue by Campaign Type")
        type_revenue = filtered_campaign.groupby('campaign_type')['revenue'].sum().reset_index()
        fig = px.bar(type_revenue, x='campaign_type', y='revenue',
                     color='campaign_type', color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Grouped Bar Chart - Region x Quarter
    st.subheader("Regional Performance by Quarter")
    region_quarter = filtered_campaign.groupby(['region', 'quarter'])['revenue'].sum().reset_index()
    fig = px.bar(region_quarter, x='region', y='revenue', color='quarter',
                 barmode='group', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Line Chart - Daily Revenue Trend
    st.subheader("Daily Revenue Trend")
    daily_revenue = filtered_campaign.groupby('date')['revenue'].sum().reset_index()
    fig = px.line(daily_revenue, x='date', y='revenue', 
                  labels={'revenue': 'Revenue (₹)', 'date': 'Date'})
    fig.update_traces(line_color='#1f77b4', line_width=2)
    fig.update_layout(height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)
    
    # Area Chart - Conversions by Channel over Time
    st.subheader("Conversions by Channel Over Time")
    channel_time = filtered_campaign.groupby(['date', 'channel'])['conversions'].sum().reset_index()
    fig = px.area(channel_time, x='date', y='conversions', color='channel',
                  color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)
    
    # Stacked Bar - Monthly Spend by Campaign Type
    st.subheader("Monthly Spend by Campaign Type")
    monthly_spend = filtered_campaign.groupby(['month', 'campaign_type'])['spend'].sum().reset_index()
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_spend['month'] = pd.Categorical(monthly_spend['month'], categories=month_order, ordered=True)
    monthly_spend = monthly_spend.sort_values('month')
    fig = px.bar(monthly_spend, x='month', y='spend', color='campaign_type',
                 barmode='stack', color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Bubble Chart - CTR vs Conversion Rate vs Spend
    st.subheader("Campaign Efficiency: CTR vs Conversion Rate (Bubble Size = Spend)")
    campaign_agg = filtered_campaign.groupby('campaign_type').agg({
        'ctr': 'mean',
        'conversion_rate': 'mean',
        'spend': 'sum',
        'roas': 'mean'
    }).reset_index()
    fig = px.scatter(campaign_agg, x='ctr', y='conversion_rate', 
                     size='spend', color='campaign_type', hover_data=['roas'],
                     labels={'ctr': 'Click-Through Rate (%)', 
                            'conversion_rate': 'Conversion Rate (%)',
                            'spend': 'Total Spend (₹)'},
                     size_max=60)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: CUSTOMER ANALYTICS
with tab2:
    st.header("👥 Customer Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogram - Age Distribution
        st.subheader("Customer Age Distribution")
        fig = px.histogram(data['customer'], x='age', nbins=30,
                          color_discrete_sequence=['#636EFA'])
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Pie Chart - Customer Segments
        st.subheader("Customer Segment Distribution")
        segment_dist = data['customer']['customer_segment'].value_counts().reset_index()
        segment_dist.columns = ['segment', 'count']
        fig = px.pie(segment_dist, values='count', names='segment',
                    color_discrete_sequence=px.colors.qualitative.Set2,
                    hole=0.4)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Box Plot - Lifetime Value by Segment
    st.subheader("Lifetime Value Distribution by Customer Segment")
    fig = px.box(data['customer'], x='customer_segment', y='lifetime_value',
                 color='customer_segment', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class="insight-box">
    <b>💡 Key Finding:</b> Premium customers have an average LTV of 
    ₹{data['customer'][data['customer']['customer_segment']=='Premium']['lifetime_value'].mean():,.0f}, 
    which is 2.5x higher than Basic customers.
    </div>
    """, unsafe_allow_html=True)
    
    # Violin Plot - Satisfaction Score by NPS Category
    st.subheader("Satisfaction Score Distribution by NPS Category")
    fig = px.violin(data['customer'], x='nps_category', y='satisfaction_score',
                    color='nps_category', box=True,
                    color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Scatter Plot - Income vs Lifetime Value
    st.subheader("Income vs Lifetime Value (colored by Customer Segment)")
    fig = px.scatter(data['customer'], x='income', y='lifetime_value',
                    color='customer_segment', size='total_purchases',
                    hover_data=['age', 'tenure_months'],
                    color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Sunburst - Region > City Tier > Customer Segment
    st.subheader("Customer Hierarchy: Region → City Tier → Segment")
    customer_hierarchy = data['customer'].groupby(['region', 'city_tier', 'customer_segment']).size().reset_index(name='count')
    fig = px.sunburst(customer_hierarchy, path=['region', 'city_tier', 'customer_segment'],
                     values='count', color='count',
                     color_continuous_scale='Blues')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: PRODUCT INSIGHTS
with tab3:
    st.header("🛍️ Product Sales Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar Chart - Category Performance
        st.subheader("Sales by Product Category")
        category_sales = data['product'].groupby('category')['sales'].sum().reset_index()
        category_sales = category_sales.sort_values('sales', ascending=False)
        fig = px.bar(category_sales, x='category', y='sales',
                    color='sales', color_continuous_scale='Greens')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Bar Chart - Profit Margin by Category
        st.subheader("Average Profit Margin by Category")
        margin_data = data['product'].groupby('category')['profit_margin'].mean().reset_index()
        fig = px.bar(margin_data, x='category', y='profit_margin',
                    color='profit_margin', color_continuous_scale='RdYlGn')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Treemap - Category > Subcategory > Product
    st.subheader("Product Sales Treemap")
    product_tree = data['product'].groupby(['category', 'subcategory', 'product_name'])['sales'].sum().reset_index()
    product_tree = product_tree.nlargest(100, 'sales')  # Top 100 for performance
    fig = px.treemap(product_tree, path=['category', 'subcategory', 'product_name'],
                    values='sales', color='sales',
                    color_continuous_scale='Viridis')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Quarterly Sales Trend
    st.subheader("Quarterly Sales Trend by Category")
    quarterly_sales = data['product'].groupby(['quarter', 'category'])['sales'].sum().reset_index()
    fig = px.line(quarterly_sales, x='quarter', y='sales', color='category',
                 markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Regional Performance
    st.subheader("Regional Product Performance")
    regional_sales = data['product'].groupby(['region', 'category'])['sales'].sum().reset_index()
    fig = px.bar(regional_sales, x='region', y='sales', color='category',
                barmode='group', color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# TAB 4: ML MODELS
with tab4:
    st.header("🤖 Machine Learning Model Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Confusion Matrix
        st.subheader("Lead Scoring: Confusion Matrix")
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(data['lead_scoring']['actual_converted'], 
                            data['lead_scoring']['predicted_class'])
        
        fig = go.Figure(data=go.Heatmap(
            z=cm,
            x=['Predicted 0', 'Predicted 1'],
            y=['Actual 0', 'Actual 1'],
            colorscale='Blues',
            text=cm,
            texttemplate='%{text}',
            textfont={"size": 20}
        ))
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
        st.info(f"**Model Accuracy:** {accuracy*100:.2f}%")
    
    with col2:
        # ROC Curve
        st.subheader("ROC Curve")
        from sklearn.metrics import roc_curve, auc
        fpr, tpr, _ = roc_curve(data['lead_scoring']['actual_converted'], 
                               data['lead_scoring']['predicted_probability'])
        roc_auc = auc(fpr, tpr)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fpr, y=tpr, name=f'ROC (AUC = {roc_auc:.3f})',
                                line=dict(color='#1f77b4', width=3)))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], name='Random',
                                line=dict(color='gray', dash='dash')))
        fig.update_layout(xaxis_title='False Positive Rate',
                         yaxis_title='True Positive Rate',
                         height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"**AUC Score:** {roc_auc:.3f} - Good predictive performance!")
    
    # Feature Importance
    st.subheader("Feature Importance Analysis")
    feature_df = data['feature_importance'].sort_values('importance', ascending=False)
    fig = px.bar(feature_df, x='importance', y='feature', orientation='h',
                color='importance', color_continuous_scale='Reds',
                error_x='importance_std')
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
    <div class="insight-box">
    <b>🎯 Top Predictors:</b> {feature_df.iloc[0]['feature']} and {feature_df.iloc[1]['feature']} 
    are the strongest indicators of lead conversion.
    </div>
    """, unsafe_allow_html=True)
    
    # Learning Curve
    st.subheader("Model Learning Curve")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['learning_curve']['training_size'], 
                            y=data['learning_curve']['train_score'],
                            name='Training Score', mode='lines+markers',
                            line=dict(color='#1f77b4', width=3)))
    fig.add_trace(go.Scatter(x=data['learning_curve']['training_size'], 
                            y=data['learning_curve']['validation_score'],
                            name='Validation Score', mode='lines+markers',
                            line=dict(color='#ff7f0e', width=3)))
    fig.update_layout(xaxis_title='Training Size',
                     yaxis_title='Score',
                     height=400, hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

# TAB 5: GEOGRAPHIC ANALYSIS
with tab5:
    st.header("🗺️ Geographic Performance Analysis")
    
    # Choropleth Map
    st.subheader("Revenue by State (Choropleth Map)")
    fig = px.scatter_geo(data['geographic'],
                        lat='latitude', lon='longitude',
                        size='total_revenue',
                        color='revenue_per_customer',
                        hover_name='state',
                        hover_data=['total_customers', 'store_count', 'customer_satisfaction'],
                        color_continuous_scale='Viridis',
                        size_max=50)
    fig.update_geos(scope='asia', showcountries=True)
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Top States by Revenue
        st.subheader("Top 10 States by Revenue")
        top_states = data['geographic'].nlargest(10, 'total_revenue')
        fig = px.bar(top_states, x='state', y='total_revenue',
                    color='total_revenue', color_continuous_scale='Blues')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # YoY Growth by Region
        st.subheader("Year-over-Year Growth by Region")
        regional_growth = data['geographic'].groupby('region')['yoy_growth'].mean().reset_index()
        fig = px.bar(regional_growth, x='region', y='yoy_growth',
                    color='yoy_growth', color_continuous_scale='RdYlGn')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Bubble Map - Store Count vs Satisfaction
    st.subheader("Store Distribution & Customer Satisfaction")
    fig = px.scatter_geo(data['geographic'],
                        lat='latitude', lon='longitude',
                        size='store_count',
                        color='customer_satisfaction',
                        hover_name='state',
                        hover_data=['total_customers', 'market_penetration'],
                        color_continuous_scale='RdYlGn',
                        size_max=40)
    fig.update_geos(scope='asia')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Market Penetration Analysis
    st.subheader("Market Penetration vs Customer Satisfaction")
    fig = px.scatter(data['geographic'], x='market_penetration', y='customer_satisfaction',
                    size='total_customers', color='region', hover_name='state',
                    labels={'market_penetration': 'Market Penetration (%)',
                           'customer_satisfaction': 'Customer Satisfaction'},
                    color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# TAB 6: ATTRIBUTION & FUNNEL
with tab6:
    st.header("🔄 Attribution Models & Conversion Funnel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Multi-Touch Attribution Models
        st.subheader("Channel Attribution Comparison")
        attribution_melted = data['attribution'].melt(id_vars=['channel'], 
                                                      var_name='model', 
                                                      value_name='conversions')
        fig = px.bar(attribution_melted, x='channel', y='conversions', 
                    color='model', barmode='group',
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Attribution Donut Chart - Last Touch Model
        st.subheader("Last Touch Attribution")
        fig = px.pie(data['attribution'], values='last_touch', names='channel',
                    hole=0.5, color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Conversion Funnel
    st.subheader("Marketing Conversion Funnel")
    fig = go.Figure(go.Funnel(
        y=data['funnel']['stage'],
        x=data['funnel']['visitors'],
        textposition="inside",
        textinfo="value+percent initial",
        marker={"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"]}
    ))
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # Funnel Conversion Rates
    col1, col2, col3 = st.columns(3)
    for idx, row in data['funnel'].iterrows():
        if idx < 3:
            with col1:
                st.metric(row['stage'], f"{row['visitors']:,}", 
                         f"{row['conversion_rate']:.1f}%" if pd.notna(row['conversion_rate']) else "")
        elif idx < 6:
            with col2:
                st.metric(row['stage'], f"{row['visitors']:,}", 
                         f"{row['conversion_rate']:.1f}%" if pd.notna(row['conversion_rate']) else "")
    
    # Customer Journey Analysis
    st.subheader("Customer Journey Paths")
    journey_data = data['journey'].copy()
    journey_data['path'] = (journey_data['touchpoint_1'] + ' → ' + 
                           journey_data['touchpoint_2'] + ' → ' + 
                           journey_data['touchpoint_3'] + ' → ' + 
                           journey_data['touchpoint_4'])
    journey_data = journey_data.sort_values('customer_count', ascending=False)
    
    fig = px.bar(journey_data, x='customer_count', y='path', orientation='h',
                color='customer_count', color_continuous_scale='Teal')
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation Heatmap
    st.subheader("Marketing Metrics Correlation Matrix")
    corr_matrix = data['correlation'].set_index(data['correlation'].columns[0])
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='RdBu',
        zmid=0,
        text=np.round(corr_matrix.values, 2),
        texttemplate='%{text}',
        textfont={"size": 10}
    ))
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 20px;'>
    <p><b>NovaMart Marketing Analytics Dashboard</b> | Built with Streamlit & Plotly</p>
    <p>Masters of AI in Business - Data Visualization Assignment</p>
    <p style='font-size:15px; margin-top:10px;'>
        Crafted with ❤️ by 
        <a href="https://github.com/mercydeez" target="_blank" style="color:#1f77b4; text-decoration:none;">
            <b>Atharva Soundankar</b>
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
