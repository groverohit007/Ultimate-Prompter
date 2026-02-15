"""
Template Library Manager
========================
Save, load, search, and share prompt templates
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional


class TemplateManager:
    """Manages prompt templates with search, tags, and import/export"""
    
    def __init__(self, storage_path: str = "templates.json"):
        self.storage_path = storage_path
        self.templates = self._load_templates()
    
    def _load_templates(self) -> List[Dict[str, Any]]:
        """Load templates from storage"""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def _save_templates(self):
        """Save templates to storage"""
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(self.templates, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving templates: {e}")
            return False
    
    def save_template(self, name: str, prompt: str, category: str, 
                     emotion: str = "", motion: str = "", model: str = "",
                     tags: List[str] = None, notes: str = "") -> bool:
        """Save a new template"""
        template = {
            "id": len(self.templates) + 1,
            "name": name,
            "prompt": prompt,
            "category": category,
            "emotion": emotion,
            "motion": motion,
            "model": model,
            "tags": tags or [],
            "notes": notes,
            "created_at": datetime.now().isoformat(),
            "usage_count": 0
        }
        
        self.templates.append(template)
        return self._save_templates()
    
    def get_template(self, template_id: int) -> Optional[Dict[str, Any]]:
        """Get template by ID"""
        for template in self.templates:
            if template["id"] == template_id:
                return template
        return None
    
    def search_templates(self, query: str = "", category: str = "", 
                        emotion: str = "", motion: str = "", 
                        tags: List[str] = None) -> List[Dict[str, Any]]:
        """Search templates with filters"""
        results = self.templates.copy()
        
        if query:
            query_lower = query.lower()
            results = [t for t in results if 
                      query_lower in t["name"].lower() or 
                      query_lower in t["prompt"].lower() or
                      query_lower in t["notes"].lower()]
        
        if category:
            results = [t for t in results if t["category"] == category]
        
        if emotion:
            results = [t for t in results if t["emotion"] == emotion]
        
        if motion:
            results = [t for t in results if t["motion"] == motion]
        
        if tags:
            results = [t for t in results if any(tag in t["tags"] for tag in tags)]
        
        # Sort by usage count descending
        results.sort(key=lambda x: x["usage_count"], reverse=True)
        
        return results
    
    def increment_usage(self, template_id: int):
        """Increment usage count when template is used"""
        for template in self.templates:
            if template["id"] == template_id:
                template["usage_count"] += 1
                self._save_templates()
                break
    
    def delete_template(self, template_id: int) -> bool:
        """Delete a template"""
        self.templates = [t for t in self.templates if t["id"] != template_id]
        return self._save_templates()
    
    def export_templates(self, filename: str = "templates_export.json") -> bool:
        """Export all templates to file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.templates, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False
    
    def import_templates(self, filename: str) -> bool:
        """Import templates from file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                imported = json.load(f)
            
            # Add imported templates with new IDs
            max_id = max([t["id"] for t in self.templates], default=0)
            for template in imported:
                template["id"] = max_id + 1
                max_id += 1
                self.templates.append(template)
            
            return self._save_templates()
        except:
            return False
    
    def get_all_categories(self) -> List[str]:
        """Get unique categories"""
        return list(set(t["category"] for t in self.templates))
    
    def get_all_tags(self) -> List[str]:
        """Get all unique tags"""
        all_tags = []
        for template in self.templates:
            all_tags.extend(template["tags"])
        return list(set(all_tags))
    
    def get_stats(self) -> Dict[str, Any]:
        """Get template library statistics"""
        if not self.templates:
            return {
                "total_templates": 0,
                "most_used": None,
                "categories": {},
                "total_usage": 0
            }
        
        category_counts = {}
        for template in self.templates:
            cat = template["category"]
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        most_used = max(self.templates, key=lambda x: x["usage_count"])
        
        return {
            "total_templates": len(self.templates),
            "most_used": most_used,
            "categories": category_counts,
            "total_usage": sum(t["usage_count"] for t in self.templates)
        }
