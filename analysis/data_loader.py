import pandas as pd
from pathlib import Path
from utils.config import DATA_PATH
from utils.logger import logger

class DataLoader:
    """Singleton class for loading and preprocessing employee data"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataLoader, cls).__new__(cls)
            cls._instance._df = None
            logger.info("DataLoader singleton created")
        return cls._instance
    
    def load_data(self) -> pd.DataFrame:
        """Load and preprocess employee data"""
        if self._df is not None:
            logger.debug("Returning cached DataFrame")
            return self._df.copy()
        
        try:
            logger.info(f"Loading data from {DATA_PATH}")
            df = pd.read_csv(DATA_PATH)
            logger.info(f"Loaded {len(df)} records with {len(df.columns)} columns")
            
            # Preprocessing steps
            df = self._preprocess_data(df)
            self._df = df
            return df.copy()
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _preprocess_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply preprocessing steps to raw data"""
        logger.debug("Starting data preprocessing")
        
        # Create 'left' column if not present (simulation as in notebook)
        if 'left' not in df.columns:
            logger.warning("'left' column not found - simulating based on business rules")
            df['left'] = (
                (df['satisfaction_level'] < 0.4) & 
                (df['average_montly_hours'] > 250)
            ).astype(int)
        
        # Ensure categorical columns are properly typed
        categorical_cols = ['dept', 'salary', 'promotion_last_5years']
        for col in categorical_cols:
            if col in df.columns:
                df[col] = df[col].astype('category')
        
        logger.info("Data preprocessing completed successfully")
        return df