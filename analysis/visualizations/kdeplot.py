import seaborn as sns
from .base import BaseVisualizer

class KDEPlotVisualizer(BaseVisualizer):
    """Creates KDE plots for distribution comparisons"""
    
    def create(
        self,
        x: str,
        hue: str,
        title: str,
        palette: str = 'coolwarm',
        shade: bool = True
    ):
        """Create a KDE plot with hue separation"""
        ax = self._setup_plot(title, xlabel=x)
        
        sns.kdeplot(
            data=self.df,
            x=x,
            hue=hue,
            palette=palette,
            shade=shade,
            ax=ax
        )
        
        return self