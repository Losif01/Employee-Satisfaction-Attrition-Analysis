import seaborn as sns
from .base import BaseVisualizer
from utils.config import VISUALIZATION_DEFAULTS

class BoxPlotVisualizer(BaseVisualizer):
    """Creates box plots for categorical comparisons"""
    
    def create(
        self,
        x: str,
        y: str,
        title: str,
        palette: str = None,
        rotation: int = None,
        order: list = None
    ):
        """Create a box plot"""
        ax = self._setup_plot(title, xlabel=x, ylabel=y)
        
        palette = palette or VISUALIZATION_DEFAULTS['palette']
        rotation = rotation if rotation is not None else VISUALIZATION_DEFAULTS['rotation']
        
        sns.boxplot(
            x=x,
            y=y,
            data=self.df,
            palette=palette,
            order=order,
            ax=ax
        )
        
        if rotation:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
        
        return self