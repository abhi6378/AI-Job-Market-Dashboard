import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# set the page title and layout 
st.set_page_config(page_title='AI Job Data insights', layout='wide')

# add title to web app
st.title("🤖 AI Job Data Analysis Dashboard")

# --- DATA LOADING LOGIC ---
# This part checks if the file exists in your GitHub repo first
default_file = "AI_job_data.csv"
df = None

# 1. Try to load from the repository automatically
if os.path.exists(default_file):
    df = pd.read_csv(default_file)
    st.success(f"✅ Automatically loaded data from {default_file}")
else:
    # 2. If file is not in repo, show an uploader
    uploaded_file = st.file_uploader("Or upload your AI_job_data.csv", type='csv')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

# --- DASHBOARD LOGIC ---
if df is not None:
    st.subheader('📊 Sample Data')
    st.dataframe(df.head())
    
    # Show basic info
    st.subheader('🔍 Dataset Overview')
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Shape of data:**", df.shape)
        st.write("**Columns:**", df.columns.tolist())
    with col2:
        st.write('**Missing values per column:**')
        st.write(df.isnull().sum())

    # --- Insight 1: Most Common Job Titles ---
    st.subheader("📌 Top AI Job Titles")
    top_titles = df['job_title'].value_counts().head(10)
    fig1 = px.bar(
        top_titles,
        x=top_titles.values,
        y=top_titles.index,
        orientation='h',
        color=top_titles.values,
        color_continuous_scale='viridis',
        labels={'x':'Number of Jobs', 'index':'Job titles'}
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ... (Keep the rest of your chart code here) ...
    # --------------------- Insight 2: Top Companies ---------------------
    st.subheader("🏢 Companies Hiring the Most")
    top_companies=df['company_name'].value_counts().head(10)
    fig2=px.bar(
        top_companies,
        x=top_companies.values,
        y=top_companies.index,
        orientation='h',
        color=top_companies.values,
        color_continuous_scale='blues',
        labels={'x':'Number of Jobs','index':'Job title'}

    )
    st.plotly_chart(fig2,use_container_width=True)

    # --------------------- Insight 3: Experience vs Salary ---------------------
    st.subheader("📈 Experience Level vs Average Salary")
    exp_salary=df.groupby('experience_level')['salary_usd'].mean().reset_index().sort_values(by='salary_usd')
    fig3 = px.bar(
        exp_salary,
        x='salary_usd',
        y='experience_level',
        orientation='h',
        labels={'experience_level': 'Experience Level', 'salary_usd': 'Average Salary (USD)'},
        color='salary_usd',
        color_continuous_scale='reds'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # --------------------- Insight 4: Remote Category Distribution ---------------------
    st.subheader("🏠 Remote Category Distribution")
    location_counts=df['remote_category'].value_counts()
    fig4=px.pie(
        location_counts,
        values=location_counts.values,
        names=location_counts.index,
        title='Remote vs Onsite vs Hybrid Jobs',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig4,use_container_width=True)

    # (Add the rest of your visualization logic as you had it)
    
else:
    st.warning('⚠️ No dataset found. Please ensure AI_job_data.csv is in your GitHub repository or upload it here.')