import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.markdown("""
    <style>
        /* Global Styles */
        .main {
            background-color: #2a3d66;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #1e2a3d;
            color: white;
        }
        h1, h2, h3, h4, h5 {
            color: #70b7f7;
        }
        p {
            font-size: 16px;
            color: #d1e0e0;
        }

        /* Button Styles */
        .stButton>button {
            background-color: #70b7f7;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            padding: 10px 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #5698cb;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        /* Text Input Fields */
        .stTextInput>div>input {
            background-color: #d1e0e0;
            border-radius: 8px;
            font-size: 16px;
            color: #333;
            padding: 8px 12px;
        }

        /* Section Divider */
        .st-divider {
            border-color: #70b7f7;
        }

        /* Titles and Subtitles */
        .stHeader {
            color: #70b7f7;
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Plotly Chart Background */
        .stPlotlyChart {
            background-color: #1e2a3d;
            border-radius: 10px;
        }

        /* File Uploader Styles */
        .stFileUploader>div>div>input {
            background-color: #d1e0e0;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 16px;
            color: #333;
        }

        /* Download Button Styling */
        .stDownloadButton>button {
            background-color: #70b7f7;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            padding: 10px 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stDownloadButton>button:hover {
            background-color: #5698cb;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Interactive Visualizations with Plotly and Streamlit")
st.markdown("<h2 class='stHeader'>Explore Interactive Visualizations</h2>", unsafe_allow_html=True)

# --- Input for Author Information ---
st.sidebar.header("Visualization Skill Workshop - Plotly")
name = st.sidebar.text_input("Enter your name")
usn = st.sidebar.text_input("Enter your roll no.")
instructor_name = st.sidebar.text_input("Course Instructor Name")

# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: #70b7f7;'>Created by:</h5>"
        f"<p>{name} (USN: {usn})</p>"
        f"<p>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )

# --- File Upload Section ---
st.sidebar.header("Upload Your Own Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # If the user uploaded a CSV file, load it into a DataFrame
    if uploaded_file.name.endswith(".csv"):
        uploaded_data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        uploaded_data = pd.read_excel(uploaded_file)
    
    st.write("## Dataset Overview")
    st.write(uploaded_data.head())

    # Optional: Provide a download link for the dataset
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(uploaded_data)
    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="uploaded_dataset.csv",
        mime="text/csv",
        key="download-csv",
        help="Click here to download your dataset as CSV",
        use_container_width=True
    )

# --- Load Default Dataset (for those who don't upload a file) ---
if uploaded_file is None:
    tips = sns.load_dataset('tips')  # Loading the tips dataset

    # Display the first few rows of the dataset
    st.write("## Dataset Overview")
    st.write(tips.head())

# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)  # Add divider

# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
fig2.update_layout(
    xaxis_title="Day of the Week",
    yaxis_title="Average Tip ($)",
    font=dict(size=14),
    plot_bgcolor='#1e2a3d',  # Dark background for plot
    paper_bgcolor='#1e2a3d',  # Dark background for paper
    title_font=dict(size=20, color='#70b7f7'),
    xaxis_tickangle=-45,  # Tilt x-axis labels for better readability
)
st.plotly_chart(fig2, use_container_width=True)  # Display the chart

# --- Task 3: Interactive Histogram ---
st.subheader("Task 3: Histogram - Tip Distribution by Day")
st.markdown("<hr class='st-divider'>", unsafe_allow_html=True)  # Add divider

# Histogram: Tip distribution by day with color for each day
fig4 = px.histogram(
    tips, x='tip', color='day',
    title='Tip Distribution by Day',
    labels={'tip': 'Tip Amount ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
fig4.update_layout(
    xaxis_title="Tip Amount ($)",
    yaxis_title="Frequency",
    font=dict(size=14),
    plot_bgcolor='#1e2a3d',  # Dark background for plot
    paper_bgcolor='#1e2a3d',  # Dark background for paper
    title_font=dict(size=20, color='#70b7f7'),
    xaxis_tickangle=-45,  # Tilt x-axis labels for better readability
)
st.plotly_chart(fig4, use_container_width=True)  # Display the chart

st.subheader("Task 3: Box Chart - Total Bill vs Day")
fig5 = px.box(
    tips,
    x='day',  # Day of the week
    y='total_bill',  # Total bill amount
    color='time',  # Color by time (Lunch or Dinner)
    title='Distribution of Total Bill by Day (Color by Time)',
    labels={'total_bill': 'Total Bill ($)', 'day': 'Day of the Week', 'time': 'Time of Day'},
    template='ggplot2'  # Use plotly template for a blue-themed design
)
st.plotly_chart(fig5)
