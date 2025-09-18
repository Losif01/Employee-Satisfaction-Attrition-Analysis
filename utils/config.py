from pathlib import Path
#import pdb
# this works for anyone copying this from gitlab with no issues
UTILS_DIR = Path(__file__).parent
ROOT_DIR = Path(UTILS_DIR).parent

DATA_PATH = f"{ROOT_DIR}/data/Employee Attrition.csv"

#pdb.set_trace()
# Visualization defaults
VISUALIZATION_DEFAULTS = {
    "figure_size": (10, 6),
    "palette": "Set2",
    "rotation": 45,
    "alpha": 0.7,
    "dpi": 100
}

# Business thresholds
THRESHOLDS = {
    "low_satisfaction": 0.4,
    "high_evaluation": 0.8,
    "high_hours": 250,
    "high_projects": 6
}

# Question metadata
QUESTION_METADATA = {
    "q01_dept_satisfaction": {
        "title": "Employee Satisfaction Level by Department",
        "description": "Box plot showing satisfaction distribution across departments"
    },
    "q02_eval_vs_satisfaction": {
        "title": "Satisfaction Level vs Last Evaluation Score",
        "description": "Scatter plot with trendline showing correlation between satisfaction and evaluation"
    },
    "q03_projects_vs_satisfaction": {
        "title": "Satisfaction Level by Number of Projects",
        "description": "Violin plot showing satisfaction distribution across project counts"
    },
    "q04_hours_vs_satisfaction": {
        "title": "Satisfaction Level vs Average Monthly Hours",
        "description": "Scatter plot with density highlighting concentration areas"
    },
    "q05_salary_vs_satisfaction": {
        "title": "Satisfaction Level by Salary Level",
        "description": "Box plot comparing satisfaction across salary categories"
    },
    "q06_left_vs_stayed": {
        "title": "Average Satisfaction: Employees Who Left vs Stayed",
        "description": "Bar chart comparing mean satisfaction for attrition status"
    },
    "q07_attrition_by_dept": {
        "title": "Attrition Rate by Department",
        "description": "Bar chart showing proportion of employees who left per department"
    },
    "q08_eval_vs_attrition": {
        "title": "Last Evaluation Distribution: Left vs Stayed",
        "description": "Histogram overlay showing evaluation scores for attrition status"
    },
    "q09_salary_vs_attrition": {
        "title": "Attrition Rate by Salary Level",
        "description": "Bar chart showing attrition rates across salary bands"
    },
    "q10_satisfaction_evaluation_heatmap": {
        "title": "Attrition Rate by Satisfaction and Evaluation",
        "description": "2D heatmap revealing high-risk employee segments"
    },
    "q11_projects_vs_attrition": {
        "title": "Projects vs Satisfaction by Attrition Status",
        "description": "Scatter plot colored by attrition status"
    },
    "q12_time_vs_satisfaction": {
        "title": "Satisfaction Level by Time Spent at Company",
        "description": "Box plot showing satisfaction by tenure"
    },
    "q13_time_vs_attrition": {
        "title": "Attrition Rate by Time Spent at Company",
        "description": "Bar chart showing attrition by tenure"
    },
    "q14_promotion_vs_satisfaction": {
        "title": "Satisfaction Level by Promotion Status",
        "description": "Box plot comparing satisfaction for promoted vs non-promoted"
    },
    "q15_promotion_vs_attrition": {
        "title": "Attrition Rate by Promotion Status",
        "description": "Bar chart showing attrition rates by promotion status"
    },
    "q16_evaluation_vs_projects": {
        "title": "Evaluation vs Projects, Sized by Hours",
        "description": "Scatter plot showing relationship between evaluation, projects, and hours"
    },
    "q17_employee_clusters": {
        "title": "Employee Clusters (Satisfaction, Evaluation, Hours)",
        "description": "PCA scatter plot showing distinct employee segments"
    },
    "q18_cluster_vs_attrition": {
        "title": "Attrition Rate by Employee Cluster",
        "description": "Bar chart showing attrition risk by cluster"
    },
    "q19_satisfaction_distribution": {
        "title": "Distribution of Satisfaction Levels",
        "description": "Histogram with KDE showing overall satisfaction distribution"
    },
    "q20_salary_vs_metrics": {
        "title": "Average Metrics by Salary Level",
        "description": "Grouped bar chart showing project load, performance, and satisfaction by salary"
    },
    "q21_extreme_projects": {
        "title": "Projects vs Satisfaction with Outliers",
        "description": "Scatter plot highlighting employees with extreme project loads"
    },
    "q22_high_risk_employees": {
        "title": "High-Risk Employees",
        "description": "Scatter plot highlighting valuable but at-risk employees"
    }
}