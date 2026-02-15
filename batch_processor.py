"""
Batch Processor
===============
Generate multiple prompt variations simultaneously
"""

from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


class BatchProcessor:
    """Process multiple generation requests in batch"""
    
    def __init__(self, max_workers: int = 3):
        """
        Initialize batch processor.
        
        Args:
            max_workers: Maximum concurrent API calls (default 3 to avoid rate limits)
        """
        self.max_workers = max_workers
        self.results = []
    
    def create_batch_job(self, base_params: Dict[str, Any], 
                        variations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Create a batch job combining base params with variations.
        
        Args:
            base_params: Common parameters (image, motion, master_dna, etc.)
            variations: List of dicts with varying parameters (emotion, intensity, etc.)
        
        Returns:
            List of complete parameter sets for each variation
        """
        jobs = []
        for i, variation in enumerate(variations):
            job = base_params.copy()
            job.update(variation)
            job['batch_id'] = i + 1
            jobs.append(job)
        
        return jobs
    
    def process_batch(self, jobs: List[Dict[str, Any]], 
                     processor_func, 
                     on_progress=None) -> List[Dict[str, Any]]:
        """
        Process batch of jobs concurrently.
        
        Args:
            jobs: List of parameter dicts
            processor_func: Function to call for each job (should accept job dict)
            on_progress: Optional callback function(completed, total)
        
        Returns:
            List of results
        """
        results = []
        total = len(jobs)
        completed = 0
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all jobs
            future_to_job = {
                executor.submit(processor_func, job): job 
                for job in jobs
            }
            
            # Process as they complete
            for future in as_completed(future_to_job):
                job = future_to_job[future]
                try:
                    result = future.result()
                    result['batch_id'] = job['batch_id']
                    result['success'] = True
                    results.append(result)
                except Exception as e:
                    results.append({
                        'batch_id': job['batch_id'],
                        'success': False,
                        'error': str(e),
                        'job': job
                    })
                
                completed += 1
                if on_progress:
                    on_progress(completed, total)
        
        # Sort by batch_id to maintain order
        results.sort(key=lambda x: x['batch_id'])
        
        return results
    
    @staticmethod
    def create_emotion_variations(emotions: List[str], intensity: str = "Medium") -> List[Dict[str, Any]]:
        """Helper: Create variation set for multiple emotions"""
        return [
            {"emotion": emotion, "intensity": intensity, "variation_name": f"{emotion} ({intensity})"}
            for emotion in emotions
        ]
    
    @staticmethod
    def create_intensity_variations(emotion: str, intensities: List[str]) -> List[Dict[str, Any]]:
        """Helper: Create variation set for multiple intensities"""
        return [
            {"emotion": emotion, "intensity": intensity, "variation_name": f"{emotion} - {intensity}"}
            for intensity in intensities
        ]
    
    @staticmethod
    def create_model_variations(models: List[str]) -> List[Dict[str, Any]]:
        """Helper: Create variation set for multiple models"""
        return [
            {"model": model, "variation_name": f"{model} optimized"}
            for model in models
        ]
    
    @staticmethod
    def create_mixed_variations(primary_emotion: str, secondary_emotions: List[str],
                              primary_weight: float = 0.7) -> List[Dict[str, Any]]:
        """Helper: Create variations mixing one primary with multiple secondaries"""
        return [
            {
                "primary_emotion": primary_emotion,
                "secondary_emotion": sec_emotion,
                "primary_weight": primary_weight,
                "variation_name": f"{int(primary_weight*100)}% {primary_emotion} + {int((1-primary_weight)*100)}% {sec_emotion}"
            }
            for sec_emotion in secondary_emotions
        ]
    
    def get_summary_stats(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Get summary statistics from batch results"""
        successful = [r for r in results if r.get('success', False)]
        failed = [r for r in results if not r.get('success', False)]
        
        return {
            "total_jobs": len(results),
            "successful": len(successful),
            "failed": len(failed),
            "success_rate": len(successful) / len(results) * 100 if results else 0,
            "failed_jobs": [r['batch_id'] for r in failed]
        }
