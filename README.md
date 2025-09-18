# Employee Satisfaction & Attrition Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.32.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive HR analytics dashboard that analyzes employee satisfaction, identifies attrition risks, and provides actionable insights for talent retention strategies.

## Features

- **22 In-Depth Analyses**: Explore every aspect of employee satisfaction and attrition
- **Interactive Dashboard**: Filter data by department and salary level in real-time
- **Advanced Visualizations**: Box plots, violin plots, heatmaps, clustering, and more
- **Risk Identification**: Automatically detect high-risk employees (top performers at risk of leaving)
- **Actionable Insights**: Business interpretations for each analysis
- **Export Functionality**: Generate and download comprehensive reports
- **Complete Warning Suppression**: Clean output without distracting warnings

## Key Business Insights

- Identifies employees with **low satisfaction + high performance** - your most valuable at-risk talent
- Reveals **department-specific attrition patterns** to target retention efforts
- Shows the impact of **salary, promotions, and workload** on employee retention
- Uncovers **optimal project loads** for maintaining employee satisfaction
- Highlights **career stagnation periods** (3-5 years tenure) where attrition peaks

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://employeesatisfaction.streamlit.app/)

**The above badge must open for you a GUI you could explore** 

##  Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Losif01/Employee-Satisfaction-Attrition-Analysis
cd Employee-Satisfaction-Attrition-Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

##  Project Structure

```
.
├── analysis
│   ├── clustering.py
│   ├── data_loader.py
│   ├── __init__.py
│   ├── metrics.py
│   ├── question_bank.py
│   └── visualizations
│       ├── barplot.py
│       ├── base.py
│       ├── boxplot.py
│       ├── cluster_plot.py
│       ├── heatmap.py
│       ├── histogram.py
│       ├── __init__.py
│       ├── kdeplot.py
│       ├── scatterplot.py
│       └── violinplot.py
├── app.py
├── data
│   ├── Employee Attrition.csv
│   ├── __init__.py
│   └── Questions.txt
├── README.md
├── requirements.txt
├── test.py
└── utils
    ├── config.py
    ├── __init__.py
    └── logger.py

5 directories, 25 files
```

##  How It Works

The dashboard performs a comprehensive analysis of employee data through 22 interconnected questions that fall into these categories:

### 🔹 Satisfaction Analysis
- Department-wise satisfaction levels
- Salary vs. satisfaction correlation  
- Impact of promotions on morale
- Optimal project load for satisfaction

### 🔹 Attrition Risk Assessment
- High-risk employee identification
- Departmental attrition rates
- Tenure-based turnover patterns
- Salary band impact on retention

### 🔹 Performance Patterns
- Evaluation score distributions
- Workload vs. performance relationships
- Career progression effects
- Clustering of employee segments

### 🔹 Advanced Analytics
- 2D heatmap of satisfaction vs. evaluation
- PCA-based employee clustering
- Violin plots for distribution analysis
- Multi-metric comparisons by salary

##  Business Value

This tool helps HR teams and business leaders:

- **Reduce turnover costs** by identifying at-risk employees early
- **Improve retention** with data-driven interventions
- **Optimize resource allocation** by focusing on high-impact departments
- **Enhance talent management** through personalized career development
- **Validate HR initiatives** with measurable outcomes


##  Technical Architecture

Built with software engineering best practices:
- **MVC-inspired design** for clean separation of concerns
- **Reusable visualization classes** for consistent styling
- **Centralized question bank** for easy maintenance
- **Configurable thresholds** for business rules
- **Comprehensive error handling** for production readiness

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Built using Streamlit for rapid dashboard development
- Leveraging pandas and scikit-learn for data science operations
- Inspired by real-world HR analytics challenges

---

*Empowering organizations to retain their most valuable asset: people.* 

##  Contact Me

Have questions about the project or interested in collaboration? Feel free to reach out!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/your-profile/)
[![GitLab](https://img.shields.io/badge/GitLab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)](https://gitlab.com/skillIssueCM)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:losif.ai.2050@gmail.com)

### Connect With Me

<p align="left">
  <a href="https://www.linkedin.com/in/yousef-fawzi/" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linkedin/linkedin-original.svg" alt="linkedin" width="40" height="40"/>
  </a>
    <a href="https://gitlab.com/skillIssueCM" target="_blank">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/gitlab/gitlab-original.svg" alt="gitlab" width="40" height="40"/>
  </a>
  <a href="mailto:losif.ai.2050@gmail.com" target="_blank">
    <img src="https://imgs.search.brave.com/YjZyc-VnhgEy7ANjFgVM-SlrvLHkQ7FeRZU7_OtLHo8/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/c3ZncmVwby5jb20v/c2hvdy80NTIyMTMv/Z21haWwuc3Zn" alt="gmail" width="40" height="40"/>
  </a>
</p>

**Email:** [losif.ai.2050@gmail.com](mailto:losif.ai.2050@gmail.com)  
**LinkedIn:** [Yousef F.](https://www.linkedin.com/in/yousef-fawzi/)

*Open to opportunities, collaborations, and discussions about data science, HR analytics, and machine learning applications in business.*