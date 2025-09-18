import seaborn as sns
from .base import BaseVisualizer

class ClusterPlotVisualizer(BaseVisualizer):
    """Creates visualizations for clustered data"""
    
    def create(
        self,
        x: str = 'pca1',
        y: str = 'pca2',
        hue: str = 'cluster',
        title: str = 'Employee Clusters',
        palette: str = 'Set1'
    ):
        """Create a cluster visualization using PCA components"""
        ax = self._setup_plot(title, xlabel=x, ylabel=y)
        
        sns.scatterplot(
            x=x,
            y=y,
            hue=hue,
            data=self.df,
            palette=palette,
            alpha=0.7,
            ax=ax
        )
        
        return self