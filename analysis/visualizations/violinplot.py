from .base import BaseVisualizer
import seaborn as sns
import pandas as pd
from utils.config import VISUALIZATION_DEFAULTS

class ViolinPlotVisualizer(BaseVisualizer):
    """Creates violin plots for distribution comparisons"""
    
    def create(
        self,
        x: str,
        y: str,
        title: str,
        palette: str = None,
        rotation: int = None,
        order: list = None,
        inner: str = "box",
        bins: int = 5
    ):
        """
        Create a violin plot
        
        Args:
            x: Column for x-axis (categorical or binned numeric)
            y: Column for y-axis (numeric)
            title: Plot title
            palette: Color palette to use
            rotation: X-axis label rotation
            order: Order of categories
            inner: Representation of quartiles ("box", "quartile", "point", etc.)
            bins: Number of bins if x is numeric (will be binned automatically)
        """
        # If x is numeric, bin it first
        df_plot = self.df.copy()
        if pd.api.types.is_numeric_dtype(df_plot[x]):
            bin_labels = [f"{i+1}" for i in range(bins)]
            df_plot[f"{x}_bin"] = pd.cut(df_plot[x], bins=bins, labels=bin_labels)
            x_plot = f"{x}_bin"
            x_label = f"{x.replace('_', ' ').title()} Bins"
        else:
            x_plot = x
            x_label = x.replace('_', ' ').title()
        
        ax = self._setup_plot(title, xlabel=x_label, ylabel=y.replace('_', ' ').title())
        
        palette = palette or VISUALIZATION_DEFAULTS['palette']
        rotation = rotation if rotation is not None else VISUALIZATION_DEFAULTS['rotation']
        
        sns.violinplot(
            x=x_plot,
            y=y,
            data=df_plot,
            palette=palette,
            order=order,
            inner=inner,
            ax=ax
        )
        
        if rotation:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
        
        return self