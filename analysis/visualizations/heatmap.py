import seaborn as sns
import pandas as pd
from .base import BaseVisualizer
from utils.logger import logger

class HeatmapVisualizer(BaseVisualizer):
    """Creates heatmaps for 2D relationships with proper interval handling"""
    
    def create(
        self,
        x_col: str,
        y_col: str,
        value_col: str,
        title: str,
        cmap: str = 'YlOrRd'
    ):
        """Create a heatmap from pre-binned data with proper interval handling"""
        try:
            # Create pivot table for heatmap
            heatmap_data = self.df.pivot_table(
                index=y_col,
                columns=x_col,
                values=value_col,
                aggfunc='mean'
            )
            
            # Handle Interval objects by converting to string representations
            if hasattr(heatmap_data.index, 'categories') and hasattr(heatmap_data.index.categories, 'left'):
                # If index contains Interval objects
                index_labels = [
                    f"{x.left:.1f}-{x.right:.1f}" if hasattr(x, 'left') else x 
                    for x in heatmap_data.index
                ]
                heatmap_data.index = index_labels
            
            if hasattr(heatmap_data.columns, 'categories') and hasattr(heatmap_data.columns.categories, 'left'):
                # If columns contain Interval objects
                column_labels = [
                    f"{x.left:.1f}-{x.right:.1f}" if hasattr(x, 'left') else x 
                    for x in heatmap_data.columns
                ]
                heatmap_data.columns = column_labels
            
            ax = self._setup_plot(title, xlabel=x_col, ylabel=y_col)
            
            # Create heatmap
            sns.heatmap(
                heatmap_data,
                cmap=cmap,
                annot=True,
                fmt='.2f',
                ax=ax
            )
            
            return self
            
        except Exception as e:
            logger.error(f"Heatmap creation failed: {str(e)}")
            raise