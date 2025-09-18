import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from analysis.data_loader import DataLoader
from analysis.metrics import MetricsCalculator
from analysis.question_bank import QuestionBank
from utils.config import THRESHOLDS
from utils.logger import logger

# Configure page
st.set_page_config(
    page_title="Employee Satisfaction Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'df' not in st.session_state:
    try:
        st.session_state.df = DataLoader().load_data()
        st.session_state.filtered_df = st.session_state.df.copy()
        logger.info("Data loaded successfully")
    except Exception as e:
        st.error(f"Failed to load data: {str(e)}")
        logger.error(f"Data loading error: {str(e)}")
        st.stop()

# Sidebar configuration
st.sidebar.title("📊 Employee Satisfaction Analyzer")
st.sidebar.markdown("### Filter Data")

# Department filter
dept_options = st.session_state.df['dept'].unique().tolist()
selected_depts = st.sidebar.multiselect(
    "Department",
    options=dept_options,
    default=dept_options
)

# Salary filter
salary_options = st.session_state.df['salary'].unique().tolist()
selected_salaries = st.sidebar.multiselect(
    "Salary Level",
    options=salary_options,
    default=salary_options
)

# Apply filters
if selected_depts and selected_salaries:
    mask = (
        st.session_state.df['dept'].isin(selected_depts) &
        st.session_state.df['salary'].isin(selected_salaries)
    )
    st.session_state.filtered_df = st.session_state.df[mask].copy()
else:
    st.session_state.filtered_df = st.session_state.df.copy()

# Display key metrics
st.sidebar.markdown("### Key Metrics")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric(
        "Total Employees", 
        f"{len(st.session_state.filtered_df):,}"
    )
with col2:
    attrition_rate = MetricsCalculator.calculate_attrition_rate(
        st.session_state.filtered_df
    )
    st.metric(
        "Attrition Rate", 
        f"{attrition_rate:.1%}"
    )

# High-risk employees
high_risk = MetricsCalculator.identify_high_risk_employees(
    st.session_state.filtered_df
)
st.sidebar.metric(
    "High-Risk Employees", 
    len(high_risk),
    delta=f"{len(high_risk)/len(st.session_state.filtered_df):.1%}"
)

# Question selection
st.sidebar.markdown("### Analysis Questions")
all_questions = QuestionBank.get_all_questions()
question_options = {
    q: f"{q.replace('q', 'Q').replace('_', ' ').title()} - {QuestionBank.get_question_metadata(q)['title']}" 
    for q in all_questions
}
selected_question = st.sidebar.selectbox(
    "Select Analysis",
    options=all_questions,
    format_func=lambda x: question_options[x],
    index=0
)

# Main content
st.title("Employee Satisfaction & Attrition Analysis")
st.markdown("""
This dashboard analyzes employee satisfaction and attrition drivers using HR data. 
Select an analysis question from the sidebar to explore insights.
""")

# Display selected analysis
if selected_question:
    try:
        # Get the analysis function dynamically
        analysis_func = getattr(QuestionBank, selected_question)
        
        # Run the analysis
        with st.spinner("Generating analysis..."):
            result = analysis_func(st.session_state.filtered_df)
        
        # Display analysis header
        st.subheader(result['metadata']['title'])
        st.write(result['metadata']['description'])
        
        # Show visualization - properly passing the figure
        try:
            fig = result['plot'].get_figure()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error displaying visualization: {str(e)}")
            logger.error(f"Figure display error: {str(e)}")
        
        # Show interpretation
        with st.expander("Business Interpretation", expanded=True):
            st.write(result['interpretation'])
            
        # Special handling for high-risk employee count
        if selected_question == 'q22_high_risk_employees' and 'high_risk_count' in result:
            st.info(f"Identified {result['high_risk_count']} high-risk employees matching the criteria")
        
        # Show data summary
        with st.expander("Data Summary"):
            st.dataframe(
                st.session_state.filtered_df.describe().T,
                use_container_width=True
            )
            
    except Exception as e:
        st.error(f"Error generating analysis: {str(e)}")
        logger.error(f"Analysis error for {selected_question}: {str(e)}")

# Clustering demo in sidebar
st.sidebar.markdown("### Clustering Demo")
if st.sidebar.checkbox("Show Employee Clusters"):
    try:
        from analysis.clustering import EmployeeClusterer
        
        clusterer = EmployeeClusterer()
        clustered_df = clusterer.fit(st.session_state.filtered_df)
        
        st.sidebar.subheader("Cluster Analysis")
        cluster_summary = clusterer.get_cluster_summary(clustered_df)
        st.sidebar.dataframe(cluster_summary.set_index('Cluster'), width=300)
        
        # Show cluster visualization
        from analysis.visualizations.cluster_plot import ClusterPlotVisualizer
        cluster_vis = ClusterPlotVisualizer(clustered_df)
        cluster_vis.create()
        st.sidebar.pyplot(cluster_vis.get_figure())
    except Exception as e:
        st.sidebar.error(f"Clustering error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Employee Satisfaction Analyzer** | 
Built with ❤️ using Streamlit | 
[Source Code](https://github.com/Losif01/Employee-Satisfaction-Attrition-Analysis)
""")

# # Add export functionality
# if st.sidebar.button("📥 Export Report"):
#     try:
#         # Get current analysis result
#         analysis_func = getattr(QuestionBank, selected_question)
#         result = analysis_func(st.session_state.filtered_df)
        
#         report = f"""
#         EMPLOYEE SATISFACTION ANALYSIS REPORT
#         Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
        
#         FILTERS APPLIED:
#         - Departments: {', '.join(selected_depts)}
#         - Salary Levels: {', '.join(selected_salaries)}
        
#         KEY METRICS:
#         - Total Employees: {len(st.session_state.filtered_df)}
#         - Attrition Rate: {attrition_rate:.1%}
#         - High-Risk Employees: {len(high_risk)} ({len(high_risk)/len(st.session_state.filtered_df):.1%})
        
#         SELECTED ANALYSIS: {result['metadata']['title']}
#         {result['interpretation']}
        
#         DATA SAMPLE:
#         {st.session_state.filtered_df.head().to_markdown(index=False)}
#         """
        
#         st.sidebar.download_button(
#             label="Download Report",
#             data=report,
#             file_name=f"employee_analysis_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.txt",
#             mime="text/plain"
#         )
#     except Exception as e:
#         st.sidebar.error(f"Report generation error: {str(e)}")
