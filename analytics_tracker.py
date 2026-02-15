"""
Analytics Tracker
=================
Track usage patterns, success rates, and optimize workflows
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, List
from collections import defaultdict


class AnalyticsTracker:
    """Track and analyze usage patterns"""
    
    def __init__(self, storage_path: str = "analytics.json"):
        self.storage_path = storage_path
        self.data = self._load_data()
    
    def _load_data(self) -> Dict[str, Any]:
        """Load analytics data"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    return json.load(f)
            except:
                return self._init_data()
        return self._init_data()
    
    def _init_data(self) -> Dict[str, Any]:
        """Initialize analytics structure"""
        return {
            "generations": [],
            "emotions_used": {},
            "motions_used": {},
            "models_used": {},
            "intensities_used": {},
            "features_used": {},
            "success_ratings": [],
            "average_iterations": [],
            "total_time_saved": 0,
            "created_at": datetime.now().isoformat()
        }
    
    def _save_data(self):
        """Save analytics data"""
        try:
            with open(self.storage_path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving analytics: {e}")
    
    def track_generation(self, feature: str, emotion: str = "", motion: str = "",
                        model: str = "", intensity: str = "", 
                        iterations: int = 1, success_rating: int = 0):
        """Track a generation event"""
        generation = {
            "timestamp": datetime.now().isoformat(),
            "feature": feature,
            "emotion": emotion,
            "motion": motion,
            "model": model,
            "intensity": intensity,
            "iterations": iterations,
            "success_rating": success_rating
        }
        
        self.data["generations"].append(generation)
        
        # Update counters
        if emotion:
            self.data["emotions_used"][emotion] = self.data["emotions_used"].get(emotion, 0) + 1
        
        if motion:
            self.data["motions_used"][motion] = self.data["motions_used"].get(motion, 0) + 1
        
        if model:
            self.data["models_used"][model] = self.data["models_used"].get(model, 0) + 1
        
        if intensity:
            self.data["intensities_used"][intensity] = self.data["intensities_used"].get(intensity, 0) + 1
        
        self.data["features_used"][feature] = self.data["features_used"].get(feature, 0) + 1
        
        if success_rating > 0:
            self.data["success_ratings"].append(success_rating)
        
        self.data["average_iterations"].append(iterations)
        
        # Estimate time saved (baseline: 30 min manual vs 0.5 min with tool)
        time_saved = 29.5 * iterations  # minutes
        self.data["total_time_saved"] += time_saved
        
        self._save_data()
    
    def get_dashboard_stats(self) -> Dict[str, Any]:
        """Get comprehensive dashboard statistics"""
        total_gens = len(self.data["generations"])
        
        if total_gens == 0:
            return {
                "total_generations": 0,
                "top_emotion": "N/A",
                "top_model": "N/A",
                "top_feature": "N/A",
                "avg_iterations": 0,
                "avg_success_rating": 0,
                "time_saved_hours": 0,
                "improvement_rate": 0
            }
        
        # Top emotion
        top_emotion = max(self.data["emotions_used"].items(), 
                         key=lambda x: x[1])[0] if self.data["emotions_used"] else "N/A"
        
        # Top model
        top_model = max(self.data["models_used"].items(),
                       key=lambda x: x[1])[0] if self.data["models_used"] else "N/A"
        
        # Top feature
        top_feature = max(self.data["features_used"].items(),
                         key=lambda x: x[1])[0] if self.data["features_used"] else "N/A"
        
        # Average iterations
        avg_iterations = sum(self.data["average_iterations"]) / len(self.data["average_iterations"]) if self.data["average_iterations"] else 0
        
        # Average success rating
        avg_success = sum(self.data["success_ratings"]) / len(self.data["success_ratings"]) if self.data["success_ratings"] else 0
        
        # Calculate improvement (baseline 5.2 iterations → current avg)
        baseline_iterations = 5.2
        improvement_rate = ((baseline_iterations - avg_iterations) / baseline_iterations * 100) if avg_iterations > 0 else 0
        
        return {
            "total_generations": total_gens,
            "top_emotion": f"{top_emotion} ({self.data['emotions_used'][top_emotion]} uses)" if top_emotion != "N/A" else "N/A",
            "top_model": f"{top_model} ({self.data['models_used'][top_model]} uses)" if top_model != "N/A" else "N/A",
            "top_feature": f"{top_feature} ({self.data['features_used'][top_feature]} uses)" if top_feature != "N/A" else "N/A",
            "avg_iterations": round(avg_iterations, 1),
            "avg_success_rating": round(avg_success, 1),
            "time_saved_hours": round(self.data["total_time_saved"] / 60, 1),
            "improvement_rate": round(improvement_rate, 1),
            "emotions_breakdown": self.data["emotions_used"],
            "models_breakdown": self.data["models_used"],
            "intensities_breakdown": self.data["intensities_used"]
        }
    
    def get_recent_activity(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent generation activity"""
        return sorted(self.data["generations"], 
                     key=lambda x: x["timestamp"], 
                     reverse=True)[:limit]
    
    def reset_analytics(self):
        """Reset all analytics data"""
        self.data = self._init_data()
        self._save_data()
