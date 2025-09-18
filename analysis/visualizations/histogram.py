import seaborn as sns
import matplotlib.pyplot as plt
from .base import BaseVisualizer
from utils.config import VISUALIZATION_DEFAULTS

class HistogramVisualizer(BaseVisualizer):
    """Creates histograms with KDE for distribution analysis"""
    
    def create(
        self,
        column: str,
        title: str,
        bins: int = 20,
        kde: bool = True,
        color: str = 'skyblue'
    ):
        """Create a histogram with KDE"""
        # Create figure and axis
        self.fig, self.ax = plt.subplots(
            figsize=VISUALIZATION_DEFAULTS['figure_size']
        )
        
        # Create histogram with KDE
        sns.histplot(
            data=self.df,
            x=column,
            bins=bins,
            kde=kde,
            color=color,
            ax=self.ax
        )
        
        # Set title and labels
        self.ax.set_title(title, fontsize=14)
        self.ax.set_xlabel(column.replace('_', ' ').title(), fontsize=12)
        self.ax.set_ylabel('Frequency', fontsize=12)
        
        return self
    
    def get_figure(self):
        """Return the matplotlib figure object"""
        return self.fig