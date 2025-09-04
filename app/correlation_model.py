import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler

class VolumePerformanceModel:
    def __init__(self):
        self.model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1)
        self.scaler = StandardScaler()
        
    def train(self, volume_data, performance_data):
        """Train model on historical volume-performance data"""
        X = self.scaler.fit_transform(volume_data)
        y = performance_data
        self.model.fit(X, y)
        
    def predict_performance(self, expected_volume, day_of_week, shift):
        """Predict performance metrics based on expected volume"""
        features = np.array([[expected_volume, day_of_week, shift]])
        features_scaled = self.scaler.transform(features)
        predicted_tat = self.model.predict(features_scaled)[0]
        
        return {
            "expected_volume": expected_volume,
            "predicted_tat": predicted_tat,
            "staffing_recommendation": self.calculate_staffing(expected_volume)
        }
    
    def calculate_staffing(self, volume):
        """Calculate required staffing based on volume"""
        base_staff = 5
        additional = volume // 100
        return base_staff + additional
