import seaborn as sns
import matplotlib.pyplot as plt
from .base import BaseVisualizer
from utils.config import VISUALIZATION_DEFAULTS

class ScatterPlotVisualizer(BaseVisualizer):
    """Creates scatter plots with optional regression lines"""
    
    def create(
        self,
        x: str,
        y: str,
        title: str,
        hue: str = None,
        size: str = None,
        alpha: float = None,
        palette: str = None,
        add_regression: bool = False,
        thresholds: dict = None,
        legend = None,
    ):
        """Create a scatter plot"""
        ax = self._setup_plot(title, xlabel=x, ylabel=y)
        alpha = alpha or VISUALIZATION_DEFAULTS['alpha']
        palette = palette or VISUALIZATION_DEFAULTS['palette']
        
        # Create base scatter plot
        sns.scatterplot(
            x=x,
            y=y,
            hue=hue,
            size=size,
            data=self.df,
            alpha=alpha,
            palette=palette,
            ax=ax,
            legend= legend
        )
        
        # Add regression line if requested
        if add_regression:
            sns.regplot(
                x=x,
                y=y,
                data=self.df,
                scatter=False,
                color='red',
                line_kws={'linewidth': 2},
                ax=ax
            )
        
        # Add threshold lines if provided
        if thresholds:
            for threshold_type, value in thresholds.items():
                if threshold_type == 'horizontal':
                    ax.axhline(y=value, color='red', linestyle='--', alpha=0.7)
                elif threshold_type == 'vertical':
                    ax.axvline(x=value, color='red', linestyle='--', alpha=0.7)
        
        # Remove legend if not needed
        if not hue and not size:
            ax.legend().remove()
        
        return self