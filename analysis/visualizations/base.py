import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from utils.config import VISUALIZATION_DEFAULTS
from pandas import DataFrame
class BaseVisualizer(ABC):
    """Abstract base class for all visualizations"""
    
    def __init__(self, df: DataFrame):
        self.df = df
        self.fig = None
        self.ax = None
    
    @abstractmethod
    def create(self, **kwargs):
        """Create the visualization"""
        pass
    
    def _setup_plot(self, title: str, xlabel: str = None, ylabel: str = None):
        """Setup common plot elements and ensure proper figure handling"""
        self.fig, self.ax = plt.subplots(
            figsize=VISUALIZATION_DEFAULTS['figure_size']
        )
        self.ax.set_title(title, fontsize=14)
        if xlabel:
            self.ax.set_xlabel(xlabel, fontsize=12)
        if ylabel:
            self.ax.set_ylabel(ylabel, fontsize=12)
        return self.ax
    
    def save(self, filepath: str, dpi: int = None):
        """Save the visualization to file"""
        if self.fig is None:
            raise ValueError("No figure to save - call create() first")
        
        dpi = dpi or VISUALIZATION_DEFAULTS['dpi']
        self.fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
        plt.close(self.fig)
    
    def show(self):
        """Display the visualization"""
        if self.fig is None:
            raise ValueError("No figure to show - call create() first")
        
        plt.tight_layout()
        plt.show()
    
    def get_figure(self):
        """Return the matplotlib figure object"""
        if self.fig is None:
            raise ValueError("No figure available - call create() first")
        return self.fig