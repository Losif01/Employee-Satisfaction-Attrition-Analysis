import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from utils.logger import logger

class EmployeeClusterer:
    """Performs clustering analysis on employee data"""
    
    def __init__(
        self,
        features: list = None,
        n_clusters: int = 3,
        random_state: int = 42
    ):
        self.features = features or [
            'satisfaction_level', 
            'last_evaluation', 
            'average_montly_hours'
        ]
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.kmeans = None
        self.pca = None
        self.cluster_centers = None
    
    def fit(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit clustering model and return DataFrame with cluster assignments"""
        logger.info(f"Fitting KMeans with {self.n_clusters} clusters")
        
        # Validate features
        missing = [f for f in self.features if f not in df.columns]
        if missing:
            raise ValueError(f"Missing features in DataFrame: {missing}")
        
        # Prepare data
        df_clean = df.dropna(subset=self.features).copy()
        X = df_clean[self.features]
        
        # Fit KMeans
        self.kmeans = KMeans(
            n_clusters=self.n_clusters,
            random_state=self.random_state,
            n_init=10
        )
        df_clean['cluster'] = self.kmeans.fit_predict(X)
        self.cluster_centers = self.kmeans.cluster_centers_
        
        # Apply PCA for visualization
        self.pca = PCA(n_components=2)
        X_pca = self.pca.fit_transform(X)
        df_clean['pca1'] = X_pca[:, 0]
        df_clean['pca2'] = X_pca[:, 1]
        
        logger.info(f"Clustering completed with inertia: {self.kmeans.inertia_:.2f}")
        return df_clean
    
    def get_cluster_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        """Get summary statistics for each cluster"""
        cluster_summary = df.groupby('cluster').agg({
            'satisfaction_level': 'mean',
            'last_evaluation': 'mean',
            'average_montly_hours': 'mean',
            'number_project': 'mean',
            'left': 'mean'
        }).reset_index()
        
        cluster_summary.columns = [
            'Cluster', 
            'Avg Satisfaction', 
            'Avg Evaluation', 
            'Avg Hours', 
            'Avg Projects',
            'Attrition Rate'
        ]
        
        return cluster_summary