🤖 AI Job Market Data Analysis Dashboard
An interactive web application built with Streamlit to visualize and analyze trends in the AI job market. This dashboard provides insights into job titles, salaries, company locations, and required skills to help professionals navigate the AI landscape.

🚀 Live Demo
[AI Job Market Dashboard Link](https://abhi6378-ai-job-market-dashboard-ai-job-bezjzh.streamlit.app/)

✨ Key Insights & Features
Top AI Job Titles: Visualizes which roles are most in-demand (e.g., Data Scientist, ML Engineer).

Salary Analysis: Breaks down average salaries by experience level and country.

Company Insights: Identifies top-hiring companies and analyzes how company size impacts pay.

Remote Work Trends: Shows the distribution of Remote vs. Onsite vs. Hybrid roles.

Dynamic Filtering: Users can filter the entire dataset by Year, Location, and Experience Level.

Data Export: Filtered results can be downloaded directly as a CSV file.

🛠️ Tech Stack
Language: Python

Web Framework: Streamlit

Data Manipulation: Pandas

Data Visualization: Plotly Express, Seaborn, Matplotlib

📂 Project Structure
Plaintext

├── ai_job.py              # Main Streamlit application code
├── requirements.txt       # List of required Python libraries
├── AI_job_data.csv        # The dataset used for analysis
└── README.md              # Project documentation
⚙️ Local Setup
To run this project locally, follow these steps:

Clone the repository:

Bash

git clone https://github.com/abhi6378/AI-Job-Market-Dashboard.git
cd AI-Job-Market-Dashboard
Create a virtual environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the app:

Bash

streamlit run ai_job.py
📊 Dataset
The dashboard uses an AI_job_data.csv file containing details such as job titles, company names, experience levels, salaries in USD, and remote work categories.

Developed by Abhishek - Feel free to connect!

📝 End of README content 📝