# 📊 Employee Satisfaction & Attrition Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.32.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive HR analytics dashboard that analyzes employee satisfaction, identifies attrition risks, and provides actionable insights for talent retention strategies.

## 🌟 Features

- **22 In-Depth Analyses**: Explore every aspect of employee satisfaction and attrition
- **Interactive Dashboard**: Filter data by department and salary level in real-time
- **Advanced Visualizations**: Box plots, violin plots, heatmaps, clustering, and more
- **Risk Identification**: Automatically detect high-risk employees (top performers at risk of leaving)
- **Actionable Insights**: Business interpretations for each analysis
- **Export Functionality**: Generate and download comprehensive reports
- **Complete Warning Suppression**: Clean output without distracting warnings

## 📈 Key Business Insights

- Identifies employees with **low satisfaction + high performance** - your most valuable at-risk talent
- Reveals **department-specific attrition patterns** to target retention efforts
- Shows the impact of **salary, promotions, and workload** on employee retention
- Uncovers **optimal project loads** for maintaining employee satisfaction
- Highlights **career stagnation periods** (3-5 years tenure) where attrition peaks

## 🖥️ Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app)

*(Replace with your actual deployment URL)*

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/employee-satisfaction-analyzer.git
cd employee-satisfaction-analyzer
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

## 📂 Project Structure

```
employee_satisfaction_analyzer/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Dependencies
├── analysis/                 # Core analysis modules
│   ├── data_loader.py        # Data loading and preprocessing
│   ├── metrics.py            # Key HR metrics calculation
│   ├── clustering.py         # Employee segmentation
│   ├── question_bank.py      # All 22 analysis questions
│   └── visualizations/       # Custom visualization classes
├── utils/                    # Utility functions
│   ├── config.py             # Configuration settings
│   └── logger.py             # Logging setup
└── data/                     # Data files
    └── Employee Attrition.csv
```

## 🔍 How It Works

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

## 🎯 Business Value

This tool helps HR teams and business leaders:

- **Reduce turnover costs** by identifying at-risk employees early
- **Improve retention** with data-driven interventions
- **Optimize resource allocation** by focusing on high-impact departments
- **Enhance talent management** through personalized career development
- **Validate HR initiatives** with measurable outcomes

## 📤 Export & Reporting

Generate comprehensive reports with:
- Current filter settings
- Key metrics summary
- Selected analysis interpretation
- Data sample

Perfect for sharing with stakeholders and documenting findings.

## 🛠️ Technical Architecture

Built with software engineering best practices:
- **MVC-inspired design** for clean separation of concerns
- **Reusable visualization classes** for consistent styling
- **Centralized question bank** for easy maintenance
- **Configurable thresholds** for business rules
- **Comprehensive error handling** for production readiness

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built using Streamlit for rapid dashboard development
- Leveraging pandas and scikit-learn for data science operations
- Inspired by real-world HR analytics challenges

---

*Empowering organizations to retain their most valuable asset: people.* 💼✨