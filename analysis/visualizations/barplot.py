import seaborn as sns
from .base import BaseVisualizer
from utils.config import VISUALIZATION_DEFAULTS

class BarPlotVisualizer(BaseVisualizer):
    """Creates bar plots for categorical metrics"""
    
    def create(
        self,
        x: str,
        y: str,
        title: str,
        palette: str = None,
        order: list = None,
        rotation: int = None,
        hue = None
    ):
        """Create a bar plot"""
        ax = self._setup_plot(title, xlabel=x, ylabel=y)
        
        palette = palette or VISUALIZATION_DEFAULTS['palette']
        rotation = rotation if rotation is not None else VISUALIZATION_DEFAULTS['rotation']
        
        sns.barplot(
            x=x,
            y=y,
            data=self.df,
            palette=palette,
            order=order,
            ax=ax,
            hue= hue
        )
        
        if rotation:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
        
        return self