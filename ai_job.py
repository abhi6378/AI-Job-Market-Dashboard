import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#set the page title and layout 
st.set_page_config(page_title='AI Job Data insights',layout='wide')

#add title to add web app
st.title("🤖 AI Job Data Analysis Dashboard")
# Upload CSV file
uploaded_file=st.file_uploader("AI_job_data.csv",type='csv')

#if file uploaded load the dta
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)

    st.subheader('📊 Sample Data')
    st.dataframe(df.head())
     # Show basic info
    st.subheader('🔍 Dataset Overview')
    st.write("shape of data:",df.shape)
    st.write("Columns:",df.columns.tolist())
    st.write('missing values per columns:')
    st.write(df.isnull().sum())
    # --- Insight 1: Most Common Job Titles ---
    st.subheader("📌 Top AI Job Titles")
    top_titles = df['job_title'].value_counts().head(10)
    fig1=px.bar(
        top_titles,
        x=top_titles.values,
        y=top_titles.index,
        orientation='h',
        color=top_titles.values,
        color_continuous_scale='viridis',
        labels={'x':'Number of Jobs','index':'Job titles'}
    )
    st.plotly_chart(fig1,use_container_width=True)

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
        x='salary_usd',                 # x = salary because it's horizontal
        y='experience_level',
        orientation='h',                # horizontal bar chart
        labels={'experience_level': 'Experience Level', 'salary_usd': 'Average Salary (USD)'},
        color='salary_usd',
        color_continuous_scale='reds'
    )
    st.plotly_chart(fig3, use_container_width=True)

    # --------------------- Insight 4: Remote Category ---------------------
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

    # --------------------- Insight 5: Top Countries ---------------------
    st.subheader("🌍 Top Hiring Countries")
    top_locations=df['company_location'].value_counts().head(10)
    fig5=px.bar(
        x=top_locations.index,
        y=top_locations.values,
        labels={'x': 'Country', 'y': 'Number of Jobs'},
        color=top_locations.values,
        color_continuous_scale='greens'
    )
    st.plotly_chart(fig5,use_container_width=True)

    # --------------------- Part 3: Interactive Filters ---------------------
    st.header("🧩 Filter Jobs Dynamically")

    #get unique filter options
    years=sorted(df['year'].dropna().unique())
    locations=sorted(df['company_location'].dropna().unique())
    levels=sorted(df['experience_level'].dropna().unique())

    # Create Streamlit filter widgets
    selected_year=st.selectbox("Select Year",options=years)
    selected_location=st.selectbox("Select Location",options=locations)
    selected_level=st.selectbox("Select exprienceLevel",options=levels)

    #apply filter
    filtered_df=df[
        (df['year']==selected_year)&
        (df['company_location']==selected_location)&
        (df['experience_level']==selected_level)
    ]
    st.subheader("🔍 Filtered Jobs")
    st.dataframe(filtered_df)
    # --------------------- Download Filtered Data ---------------------
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=filtered_df.to_csv(index=False),
        file_name='filtered_ai_jobs.csv',
        mime='text/csv'
    )
    # --------------------- Skills Frequency Analysis ---------------------
    st.subheader("🛠️ Most Common Required Skills")
    if 'required_skills' in df.columns:
        #combine all skills into one
        all_skill=df['required_skills'].dropna().str.cat(sep=',')
        skill_list=[skill.strip() for skill in all_skill.split(',')]
        skill_series=pd.Series(skill_list).value_counts().head(15)

        fig6=px.bar(
            x=skill_series.values,
            y=skill_series.index,
            orientation='h',
            labels={'x': 'Count', 'y': 'Skill'},
            title='Top 15 Most Common Skills',
            color=skill_series.values,
            color_continuous_scale='tealgrn'

        )
        st.plotly_chart(fig6,use_container_width=True)
    else:
        st.warning("No 'required_skills' column found in the dataset.")
    # --------------------- Salary Trend by Country ---------------------
    st.subheader("🌍 Average Salary by Country")

    country_salary=df.groupby('company_location')['salary_usd'].mean().reset_index().sort_values(by='salary_usd',ascending=False).head(15)

    fig7=px.bar(
        country_salary,
        x='salary_usd',
        y='company_location',
        orientation='h',
        color='salary_usd',
        color_continuous_scale='cividis',
        labels={'company_location': 'Country', 'salary_usd': 'Average Salary (USD)'},
        title="Top 15 Countries by Average Salary"
    )
    st.plotly_chart(fig7, use_container_width=True)   

    # --------------------- Salary Trend by Company Size ---------------------
    st.subheader("🏢 Average Salary by Company Size")

    size_salary = df.groupby('company_size')['salary_usd'].mean().reset_index().sort_values(by='salary_usd')

    fig8 = px.bar(
        size_salary,
        x='company_size',
        y='salary_usd',
        color='salary_usd',
        color_continuous_scale='sunsetdark',
        labels={'company_size': 'Company Size', 'salary_usd': 'Average Salary (USD)'},
        title="Average Salary by Company Size"
    )
    st.plotly_chart(fig8, use_container_width=True)



else:
    st.warning('please upload a csv file to continue.')
