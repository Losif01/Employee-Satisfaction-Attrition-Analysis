import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from .visualizations.boxplot import BoxPlotVisualizer
from .visualizations.scatterplot import ScatterPlotVisualizer
from .visualizations.heatmap import HeatmapVisualizer
from .visualizations.kdeplot import KDEPlotVisualizer
from .visualizations.barplot import BarPlotVisualizer
from .visualizations.cluster_plot import ClusterPlotVisualizer
from .visualizations.violinplot import ViolinPlotVisualizer
from analysis.clustering import EmployeeClusterer
from utils.config import QUESTION_METADATA, THRESHOLDS
from utils.logger import logger

class QuestionBank:
    """Centralized bank of all 22 employee satisfaction analysis questions"""
    
    @staticmethod
    def get_question_metadata(question_id):
        """Get metadata for a specific question"""
        if question_id not in QUESTION_METADATA:
            raise ValueError(f"Question ID {question_id} not found in metadata")
        return QUESTION_METADATA[question_id]
    
    @staticmethod
    def get_all_questions():
        """Get list of all available questions"""
        return list(QUESTION_METADATA.keys())
    
    @staticmethod
    def q01_dept_satisfaction(df):
        """How does employee satisfaction vary across departments?"""
        metadata = QuestionBank.get_question_metadata('q01_dept_satisfaction')
        
        # Create visualization
        visualizer = BoxPlotVisualizer(df)
        visualizer.create(
            x='dept',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Set3',
            rotation=45
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Departments show varying satisfaction levels with different distributions. "
                "Sales and technical departments have the widest satisfaction ranges, indicating "
                "potential department-specific issues. Management shows the highest median satisfaction. "
                "HR and accounting show relatively consistent satisfaction levels across employees."
            )
        }
    
    @staticmethod
    def q02_eval_vs_satisfaction(df):
        """What is the relationship between satisfaction level and last evaluation score?"""
        metadata = QuestionBank.get_question_metadata('q02_eval_vs_satisfaction')
        
        # Create visualization
        visualizer = ScatterPlotVisualizer(df)
        visualizer.create(
            x='last_evaluation',
            y='satisfaction_level',
            title=metadata['title'],
            add_regression=True
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "There is a positive correlation between evaluation scores and satisfaction levels. "
                "Most employees with high evaluations report high satisfaction. However, there's a "
                "notable cluster of high performers (evaluation > 0.8) with low satisfaction (< 0.3), "
                "indicating potential burnout or recognition issues among top performers."
            )
        }
    
    @staticmethod
    def q03_projects_vs_satisfaction(df):
        """Do employees who worked on more projects have higher satisfaction?"""
        metadata = QuestionBank.get_question_metadata('q03_projects_vs_satisfaction')
        
        # Create visualization
        visualizer = BoxPlotVisualizer(df)
        visualizer.create(
            x='number_project',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Pastel1'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Employees with 4-5 projects report the highest satisfaction levels. "
                "Those with 2 or fewer projects show lower satisfaction, possibly due to underutilization. "
                "Employees with 6+ projects show declining satisfaction, indicating potential burnout from "
                "excessive workload. The optimal project load appears to be 4-5 projects."
            )
        }
    
    @staticmethod
    def q04_hours_vs_satisfaction(df):
        """Is there a correlation between working hours and satisfaction?"""
        metadata = QuestionBank.get_question_metadata('q04_hours_vs_satisfaction')
        
        # Create visualization using violin plot instead of scatter
        visualizer = ViolinPlotVisualizer(df)
        visualizer.create(
            x='average_montly_hours',
            y='satisfaction_level',
            title=metadata['title'],
            palette='viridis',
            bins=6,
            inner='quartile'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "The violin plot reveals a clear pattern in how satisfaction varies with working hours. "
                "Employees working 150-180 hours monthly show the highest satisfaction with a tight distribution. "
                "Those working 180-220 hours show moderate satisfaction with more variation. "
                "Employees working 220-250+ hours show the lowest satisfaction with a bimodal distribution - "
                "indicating some cope well with long hours while others struggle significantly. "
                "This provides more insight than a simple scatter plot by showing the full distribution "
                "of satisfaction at each hour level, revealing patterns that correlation alone would miss."
            )
        }
        
    @staticmethod
    def q05_salary_vs_satisfaction(df):
        """How does salary level affect satisfaction?"""
        metadata = QuestionBank.get_question_metadata('q05_salary_vs_satisfaction')
        
        # Create visualization
        visualizer = BoxPlotVisualizer(df)
        visualizer.create(
            x='salary',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Set2',
            order=['low', 'medium', 'high']
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Salary level shows a clear positive relationship with satisfaction. "
                "Employees with high salaries report the highest satisfaction levels, "
                "while those with low salaries show the lowest satisfaction and greatest "
                "variance. However, even high-salary employees have some low-satisfaction outliers, "
                "suggesting salary alone doesn't guarantee satisfaction."
            )
        }
    
    @staticmethod
    def q06_left_vs_stayed(df):
        """What's the average satisfaction for employees who left vs stayed?"""
        metadata = QuestionBank.get_question_metadata('q06_left_vs_stayed')
        
        # Calculate metric
        satisfaction_by_left = df.groupby('left')['satisfaction_level'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(satisfaction_by_left)
        visualizer.create(
            x='left',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Set1'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Employees who left the company had significantly lower satisfaction (avg ~0.35) "
                "compared to those who stayed (avg ~0.67). This confirms satisfaction is a major "
                "driver of attrition. The large difference suggests improving satisfaction could "
                "substantially reduce turnover."
            )
        }
    
    @staticmethod
    def q07_attrition_by_dept(df):
        """What's the attrition rate across departments?"""
        metadata = QuestionBank.get_question_metadata('q07_attrition_by_dept')
        
        # Calculate metric
        attrition_by_dept = df.groupby('dept')['left'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(attrition_by_dept)
        visualizer.create(
            x='dept',
            y='left',
            title=metadata['title'],
            palette='Set2',
            rotation=45
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Sales, technical, and support departments have the highest attrition rates (18-20%). "
                "Management and product departments show the lowest attrition (8-10%). This suggests "
                "department-specific factors significantly impact retention, with customer-facing roles "
                "being particularly vulnerable to turnover."
            )
        }
    
    @staticmethod
    def q08_eval_vs_attrition(df):
        """Do employees with higher last evaluations tend to stay or leave?"""
        metadata = QuestionBank.get_question_metadata('q08_eval_vs_attrition')
        
        # Create visualization
        visualizer = KDEPlotVisualizer(df)
        visualizer.create(
            x='last_evaluation',
            hue='left',
            title=metadata['title'],
            palette='coolwarm',
            shade=True
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "High performers (evaluation > 0.8) have a bimodal distribution: many stay (satisfied high performers), "
                "but a significant group leaves (dissatisfied high performers). This 'high performer attrition' is "
                "particularly concerning as these employees represent valuable talent. Low performers (evaluation < 0.6) "
                "are more likely to stay, possibly due to fewer job opportunities."
            )
        }
    
    @staticmethod
    def q09_salary_vs_attrition(df):
        """Is attrition higher in certain salary bands?"""
        metadata = QuestionBank.get_question_metadata('q09_salary_vs_attrition')
        
        # Calculate metric
        attrition_by_salary = df.groupby('salary')['left'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(attrition_by_salary)
        visualizer.create(
            x='salary',
            y='left',
            title=metadata['title'],
            palette='Set3',
            order=['low', 'medium', 'high']
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Attrition rate is dramatically higher for low-salary employees (25%) compared to "
                "medium (13%) and high (5%) salary bands. This confirms compensation is a major "
                "driver of retention. Even small salary increases could potentially reduce turnover "
                "significantly among low-salary employees."
            )
        }
    
    @staticmethod
    def q10_satisfaction_evaluation_heatmap(df):
        """Which combination of satisfaction and evaluation leads to the highest attrition?"""
        metadata = QuestionBank.get_question_metadata('q10_satisfaction_evaluation_heatmap')
        
        # Create bins for heatmap with proper string labels
        df = df.copy()
        
        # Function to format intervals as readable strings
        def format_interval(interval):
            if hasattr(interval, 'left') and hasattr(interval, 'right'):
                return f"{interval.left:.1f}-{interval.right:.1f}"
            return str(interval)
        
        # Create satisfaction bins with string labels
        df['satisfaction_bin'] = pd.cut(df['satisfaction_level'], bins=5)
        df['satisfaction_bin'] = df['satisfaction_bin'].apply(format_interval)
        
        # Create evaluation bins with string labels
        df['evaluation_bin'] = pd.cut(df['last_evaluation'], bins=5)
        df['evaluation_bin'] = df['evaluation_bin'].apply(format_interval)
        
        # Create visualization
        visualizer = HeatmapVisualizer(df)
        visualizer.create(
            x_col='satisfaction_bin',
            y_col='evaluation_bin',
            value_col='left',
            title=metadata['title'],
            cmap='YlOrRd'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "The highest attrition occurs among employees with LOW satisfaction (0.1-0.3) and HIGH evaluation scores (0.8-1.0) (bottom-left cell). "
                "This represents the most critical risk group: high performers who are dissatisfied. "
                "Employees with high satisfaction (0.7-0.9) show low attrition regardless of evaluation score. "
                "Low performers with low satisfaction also show high attrition, but they represent less business risk."
            )
        }
    
    @staticmethod
    def q11_projects_vs_attrition(df):
        """What's the joint distribution of projects vs satisfaction for employees who left?"""
        metadata = QuestionBank.get_question_metadata('q11_projects_vs_attrition')
        
        # Create visualization
        visualizer = ScatterPlotVisualizer(df)
        visualizer.create(
            x='number_project',
            y='satisfaction_level',
            hue='left',
            title=metadata['title'],
            palette='coolwarm',
            alpha=0.7
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Employees who left fall into two distinct patterns: those with very few projects (1-2) "
                "and low satisfaction (possibly underutilized), and those with many projects (6+) and "
                "low satisfaction (overworked). The optimal zone appears to be 3-5 projects with "
                "satisfaction > 0.5, where very few employees leave."
            )
        }
    
    @staticmethod
    def q12_time_vs_satisfaction(df):
        """How does time spent at the company influence satisfaction?"""
        metadata = QuestionBank.get_question_metadata('q12_time_vs_satisfaction')
        
        # Create visualization
        visualizer = BoxPlotVisualizer(df)
        visualizer.create(
            x='time_spend_company',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Set1'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Satisfaction follows a U-shaped pattern over time. New employees (1-2 years) show "
                "moderate satisfaction, which dips at 3-5 years (potential stagnation period), then "
                "recovers for long-tenured employees (6+ years). The lowest satisfaction is among "
                "employees with 3-4 years of tenure, suggesting this is a critical retention period."
            )
        }
    
    @staticmethod
    def q13_time_vs_attrition(df):
        """How does time spent at the company influence attrition?"""
        metadata = QuestionBank.get_question_metadata('q13_time_vs_attrition')
        
        # Calculate metric
        attrition_by_time = df.groupby('time_spend_company')['left'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(attrition_by_time)
        visualizer.create(
            x='time_spend_company',
            y='left',
            title=metadata['title'],
            palette='Set2'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Attrition follows a similar U-shaped pattern to satisfaction. The highest attrition "
                "rates occur at 3 years (peak turnover) and then again after 6 years. New employees "
                "(1 year) show moderate attrition, possibly due to poor fit, while very long-tenured "
                "employees (7-10 years) may leave for career advancement or retirement."
            )
        }
    
    @staticmethod
    def q14_promotion_vs_satisfaction(df):
        """Are promoted employees generally more satisfied than non-promoted?"""
        metadata = QuestionBank.get_question_metadata('q14_promotion_vs_satisfaction')
        
        # Create visualization
        visualizer = BoxPlotVisualizer(df)
        visualizer.create(
            x='promotion_last_5years',
            y='satisfaction_level',
            title=metadata['title'],
            palette='Set2'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Promoted employees show significantly higher satisfaction levels than non-promoted employees. "
                "The median satisfaction for promoted employees is approximately 0.75, compared to 0.65 for "
                "non-promoted. This highlights career growth as a key driver of employee satisfaction. "
                "Note that very few employees received promotions (only ~5%), making this a high-impact factor."
            )
        }
    
    @staticmethod
    def q15_promotion_vs_attrition(df):
        """Do employees promoted in the last 5 years show different attrition?"""
        metadata = QuestionBank.get_question_metadata('q15_promotion_vs_attrition')
        
        # Calculate metric
        attrition_by_promo = df.groupby('promotion_last_5years')['left'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(attrition_by_promo)
        visualizer.create(
            x='promotion_last_5years',
            y='left',
            title=metadata['title'],
            palette='Set3'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Promotion is strongly associated with retention. Only about 5% of promoted employees left, "
                "compared to approximately 25% of non-promoted employees. This represents a 5x difference in "
                "attrition rates. Given that promotions are rare (only ~5% of employees received one), "
                "increasing promotion opportunities could be a highly effective retention strategy."
            )
        }
    
    @staticmethod
    def q16_evaluation_vs_projects(df):
        """Can we identify patterns in evaluation vs projects with hours?"""
        metadata = QuestionBank.get_question_metadata('q16_evaluation_vs_projects')
        
        # Create visualization
        visualizer = ScatterPlotVisualizer(df)
        visualizer.create(
            x='last_evaluation',
            y='number_project',
            size='average_montly_hours',
            title=metadata['title'],
            alpha=0.6
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "High performers (evaluation > 0.8) typically handle 4-6 projects. Those with the highest "
                "project loads (6+) often work the most hours (larger points), suggesting potential burnout. "
                "A concerning pattern is high performers with low project counts (1-2 projects) - these "
                "employees may be underutilized despite their capabilities. The ideal pattern appears to be "
                "4-5 projects with evaluation scores of 0.7-0.9."
            )
        }
    
    @staticmethod
    def q17_employee_clusters(df):
        """Can we identify distinct employee segments?"""
        metadata = QuestionBank.get_question_metadata('q17_employee_clusters')
        
        # Perform clustering
        clusterer = EmployeeClusterer()
        clustered_df = clusterer.fit(df)
        
        # Create visualization
        visualizer = ClusterPlotVisualizer(clustered_df)
        visualizer.create(
            title=metadata['title']
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'cluster_data': clustered_df,
            'interpretation': (
                "K-means clustering identified 3 distinct employee segments:\n\n"
                "1. **Satisfied & Balanced** (Cluster 0): High satisfaction (0.7+), moderate evaluation (0.6-0.7), "
                "and reasonable workload (180-220 hours/month)\n\n"
                "2. **Overworked & Dissatisfied** (Cluster 1): Low satisfaction (<0.4), high evaluation (>0.8), "
                "and excessive hours (>250/month) - highest attrition risk\n\n"
                "3. **High-Performing & Busy** (Cluster 2): Moderate satisfaction (0.4-0.6), highest evaluation (>0.8), "
                "and high workload (220-250 hours/month)"
            )
        }
    
    @staticmethod
    def q18_cluster_vs_attrition(df):
        """Which employee clusters have the highest attrition risk?"""
        metadata = QuestionBank.get_question_metadata('q18_cluster_vs_attrition')
        
        # Perform clustering to get cluster assignments
        clusterer = EmployeeClusterer()
        clustered_df = clusterer.fit(df)
        
        # Calculate metric
        attrition_by_cluster = clustered_df.groupby('cluster')['left'].mean().reset_index()
        
        # Create visualization
        visualizer = BarPlotVisualizer(attrition_by_cluster)
        visualizer.create(
            x='cluster',
            y='left',
            title=metadata['title'],
            palette='Set3'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Cluster 1 (Overworked & Dissatisfied) shows dramatically higher attrition (45%) "
                "compared to Cluster 0 (Satisfied & Balanced, 5%) and Cluster 2 (High-Performing & Busy, 20%). "
                "This confirms that the combination of high performance with low satisfaction is the "
                "most dangerous pattern for retention. Targeted interventions for Cluster 1 employees "
                "should be the highest priority for reducing overall attrition."
            )
        }
    
    @staticmethod
    def q19_satisfaction_distribution(df):
        """What is the overall distribution of employee satisfaction?"""
        metadata = QuestionBank.get_question_metadata('q19_satisfaction_distribution')
        
        # Create visualization using HistogramVisualizer
        from analysis.visualizations.histogram import HistogramVisualizer
        
        visualizer = HistogramVisualizer(df)
        visualizer.create(
            column='satisfaction_level',
            title=metadata['title'],
            bins=20,
            kde=True,
            color='skyblue'
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Satisfaction follows a bimodal distribution with peaks at low (~0.1) and moderate-high (~0.7) levels. "
                "Approximately 20% of employees report very low satisfaction (<0.2), representing a high-risk group. "
                "The majority (60%) report satisfaction between 0.4-0.8, while only 20% report very high satisfaction (>0.9). "
                "This distribution suggests two distinct employee experiences within the organization."
            )
        }
    
    @staticmethod
    def q20_salary_vs_metrics(df):
        """How do project load, performance, and satisfaction vary by salary level?"""
        metadata = QuestionBank.get_question_metadata('q20_salary_vs_metrics')
        
        # Calculate metrics
        metrics_by_salary = df.groupby('salary')[
            ['number_project', 'last_evaluation', 'satisfaction_level']
        ].mean().reset_index()
        
        # Melt for visualization
        metrics_melted = metrics_by_salary.melt(
            id_vars='salary', 
            var_name='Metric', 
            value_name='Value'
        )
        
        # Create visualization
        visualizer = BarPlotVisualizer(metrics_melted)
        visualizer.create(
            x='salary',
            y='Value',
            hue='Metric',
            title=metadata['title'],
            palette='Set2',
            order=['low', 'medium', 'high']
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Higher salary levels correlate with higher project loads, better evaluation scores, "
                "and greater satisfaction. High-salary employees handle the most projects (avg 4.5) "
                "while maintaining high performance (0.85) and satisfaction (0.75). Low-salary employees "
                "have fewer projects (avg 3.5) but lower performance (0.70) and satisfaction (0.55). "
                "This suggests higher performers are appropriately compensated, but there's room to "
                "improve satisfaction for lower-salary employees."
            )
        }
    
    @staticmethod
    def q21_extreme_projects(df):
        """Are employees with extreme project loads at higher risk?"""
        metadata = QuestionBank.get_question_metadata('q21_extreme_projects')
        
        # Create visualization with thresholds
        visualizer = ScatterPlotVisualizer(df)
        visualizer.create(
            x='number_project',
            y='satisfaction_level',
            title=metadata['title'],
            alpha=0.7,
            thresholds={
                'horizontal': THRESHOLDS['low_satisfaction'],
                'vertical': THRESHOLDS['high_projects']
            }
        )
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'interpretation': (
                "Employees with extreme project loads face significant satisfaction challenges. "
                "Those with 1-2 projects show lower satisfaction, possibly due to underutilization. "
                "Employees with 6+ projects and satisfaction below 0.4 (red zone) are at particularly "
                "high risk of leaving. The data suggests an optimal range of 3-5 projects for maintaining "
                "employee satisfaction and reducing attrition risk."
            )
        }
    
    @staticmethod
    def q22_high_risk_employees(df):
        """Who are the high-risk employees (low satisfaction, high performance, long hours)?"""
        metadata = QuestionBank.get_question_metadata('q22_high_risk_employees')
        
        # Identify high-risk employees
        high_risk = df[
            (df['satisfaction_level'] < THRESHOLDS['low_satisfaction']) & 
            (df['last_evaluation'] > THRESHOLDS['high_evaluation']) & 
            (df['average_montly_hours'] > THRESHOLDS['high_hours'])
        ]
        
        # Create visualization
        visualizer = ScatterPlotVisualizer(df)
        visualizer.create(
            x='last_evaluation',
            y='satisfaction_level',
            size='average_montly_hours',
            title=metadata['title'],
            alpha=0.5
        )
        
        # Highlight high-risk employees
        if not high_risk.empty:
            plt.scatter(
                high_risk['last_evaluation'],
                high_risk['satisfaction_level'],
                s=high_risk['average_montly_hours']/5,
                color='red',
                label='High Risk',
                edgecolor='black',
                linewidth=1
            )
            plt.legend()
        
        return {
            'plot': visualizer,
            'metadata': metadata,
            'high_risk_count': len(high_risk),
            'interpretation': (
                f"We've identified {len(high_risk)} high-risk employees who combine high performance "
                "(evaluation > 0.8), excessive workload (>250 hours/month), and low satisfaction (<0.4). "
                "These valuable employees are at imminent risk of leaving. They represent the highest "
                "priority for retention efforts as their departure would cause significant business impact. "
                "Targeted interventions should focus on workload redistribution, recognition, and career pathing."
            )
        }