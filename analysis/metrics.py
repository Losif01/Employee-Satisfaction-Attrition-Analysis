import pandas as pd
from utils.config import THRESHOLDS
from utils.logger import logger

class MetricsCalculator:
    """Calculates key HR metrics from employee data"""
    
    @staticmethod
    def calculate_attrition_rate(df: pd.DataFrame) -> float:
        """Calculate overall attrition rate"""
        return df['left'].mean()
    
    @staticmethod
    def attrition_rate_by_group(
        df: pd.DataFrame, 
        group_by_col: str
    ) -> pd.DataFrame:
        """Calculate attrition rate by specified group"""
        logger.debug(f"Calculating attrition rate by {group_by_col}")
        return df.groupby(group_by_col)['left'].mean().reset_index()
    
    @staticmethod
    def mean_metrics_by_group(
        df: pd.DataFrame, 
        group_by_col: str,
        metrics_cols: list
    ) -> pd.DataFrame:
        """Calculate mean metrics by specified group"""
        logger.debug(f"Calculating mean metrics by {group_by_col}")
        return df.groupby(group_by_col)[metrics_cols].mean().reset_index()
    
    @staticmethod
    def identify_high_risk_employees(df: pd.DataFrame) -> pd.DataFrame:
        """Identify high-risk employees based on business thresholds"""
        logger.info("Identifying high-risk employees")
        return df[
            (df['satisfaction_level'] < THRESHOLDS['low_satisfaction']) & 
            (df['last_evaluation'] > THRESHOLDS['high_evaluation']) & 
            (df['average_montly_hours'] > THRESHOLDS['high_hours'])
        ]
    
    @staticmethod
    def get_satisfaction_distribution(df: pd.DataFrame) -> pd.Series:
        """Get satisfaction level distribution"""
        return df['satisfaction_level'].value_counts(bins=10, sort=False)