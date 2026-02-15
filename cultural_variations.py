"""
Cultural Emotion Variations
============================
Same emotion, different cultural expressions
"""

from typing import Dict, Any, List


class CulturalVariations:
    """Maps emotions to cultural-specific expressions"""
    
    CULTURAL_DATABASE = {
        "American": {
            "Happy / Excited / Joyful": {
                "expression_style": "Outward, demonstrative, uninhibited",
                "smile_intensity": "Large, showing teeth, wide",
                "body_language": "Expansive gestures, open posture, animated",
                "eye_contact": "Direct and sustained",
                "personal_space": "Arms-length, comfortable with proximity",
                "vocal_style": "Loud, enthusiastic, expressive"
            },
            "Professional / Confident": {
                "expression_style": "Casual confidence, approachable authority",
                "smile_intensity": "Friendly smile, moderately wide",
                "body_language": "Relaxed but upright, hands visible",
                "eye_contact": "Strong, direct - shows confidence",
                "personal_space": "Standard, handshake distance",
                "vocal_style": "Clear, moderately loud, friendly"
            }
        },
        
        "Japanese": {
            "Happy / Excited / Joyful": {
                "expression_style": "Modest, contained, subtle joy",
                "smile_intensity": "Small, closed-mouth, eyes smile more",
                "body_language": "Minimal gestures, slight bow, hands together",
                "eye_contact": "Brief, respectful glances rather than staring",
                "personal_space": "Greater distance, formal boundary",
                "vocal_style": "Softer, higher pitch (especially women), gentle"
            },
            "Professional / Confident": {
                "expression_style": "Humble confidence, group-focused",
                "smile_intensity": "Very subtle, barely visible",
                "body_language": "Formal posture, minimal movement, slight bows",
                "eye_contact": "Limited - shows respect",
                "personal_space": "Formal distance maintained",
                "vocal_style": "Quiet, measured, respectful tone"
            }
        },
        
        "Italian": {
            "Happy / Excited / Joyful": {
                "expression_style": "Passionate, dramatic, whole-body expression",
                "smile_intensity": "Very wide, teeth showing, facial animation",
                "body_language": "Elaborate hand gestures, touching, animated",
                "eye_contact": "Intense, expressive, prolonged",
                "personal_space": "Very close, comfortable with touch",
                "vocal_style": "Loud, melodic, expressive inflection"
            },
            "Professional / Confident": {
                "expression_style": "Elegant confidence, stylish authority",
                "smile_intensity": "Warm smile, genuine",
                "body_language": "Expressive hands even in formal settings",
                "eye_contact": "Direct, warm, engaging",
                "personal_space": "Closer than Anglo cultures",
                "vocal_style": "Melodic, emphatic, clear"
            }
        },
        
        "British": {
            "Happy / Excited / Joyful": {
                "expression_style": "Understated, dry humor, ironic happiness",
                "smile_intensity": "Moderate, controlled, slight smirk",
                "body_language": "Reserved, minimal gestures, stiff upper lip",
                "eye_contact": "Polite but not intense",
                "personal_space": "Greater distance, formal",
                "vocal_style": "Controlled volume, witty, understatement"
            },
            "Professional / Confident": {
                "expression_style": "Formal confidence, traditional authority",
                "smile_intensity": "Minimal, professional",
                "body_language": "Very controlled, proper posture, formal",
                "eye_contact": "Professional, measured",
                "personal_space": "Formal distance strictly observed",
                "vocal_style": "Clear enunciation, controlled, proper"
            }
        },
        
        "Indian": {
            "Happy / Excited / Joyful": {
                "expression_style": "Warm, expressive, family-oriented joy",
                "smile_intensity": "Wide, genuine, eyes crinkle",
                "body_language": "Head wobble (positive), animated hands, expressive",
                "eye_contact": "Warm, respectful (varies by region/age)",
                "personal_space": "Comfortable with closeness, community-focused",
                "vocal_style": "Expressive, melodic, rising intonation"
            },
            "Professional / Confident": {
                "expression_style": "Respectful confidence, hierarchical awareness",
                "smile_intensity": "Warm but respectful",
                "body_language": "Slight head wobble, hands gesture, respectful posture",
                "eye_contact": "Respectful, mindful of hierarchy",
                "personal_space": "Varies by familiarity and gender",
                "vocal_style": "Clear, respectful tone, code-switching common"
            }
        },
        
        "Brazilian": {
            "Happy / Excited / Joyful": {
                "expression_style": "Exuberant, warm, physically affectionate",
                "smile_intensity": "Very wide, joyful, infectious",
                "body_language": "Touching, hugging, animated gestures",
                "eye_contact": "Direct, warm, prolonged",
                "personal_space": "Very close, touch is common",
                "vocal_style": "Loud, musical, enthusiastic"
            },
            "Professional / Confident": {
                "expression_style": "Warm authority, personable confidence",
                "smile_intensity": "Friendly, approachable smile",
                "body_language": "More relaxed than Anglo cultures, touch okay",
                "eye_contact": "Direct, friendly",
                "personal_space": "Closer, warmer",
                "vocal_style": "Warm, friendly, expressive"
            }
        },
        
        "Chinese": {
            "Happy / Excited / Joyful": {
                "expression_style": "Moderate expression, smile with restraint",
                "smile_intensity": "Medium, controlled, appropriate to context",
                "body_language": "Controlled gestures, group harmony focus",
                "eye_contact": "Moderate, respectful of hierarchy",
                "personal_space": "Context-dependent, formal in business",
                "vocal_style": "Moderate volume, respectful tone"
            },
            "Professional / Confident": {
                "expression_style": "Humble confidence, collective success",
                "smile_intensity": "Subtle, appropriate",
                "body_language": "Formal, minimal gestures, respectful posture",
                "eye_contact": "Limited with superiors, shows respect",
                "personal_space": "Formal distance in business",
                "vocal_style": "Measured, respectful, hierarchical awareness"
            }
        },
        
        "Middle Eastern": {
            "Happy / Excited / Joyful": {
                "expression_style": "Warm, generous, expressive hospitality",
                "smile_intensity": "Wide, genuine, welcoming",
                "body_language": "Expressive hands, touch among same gender, animated",
                "eye_contact": "Direct among same gender, modest cross-gender",
                "personal_space": "Close among friends, formal with opposite gender",
                "vocal_style": "Expressive, emphatic, warm"
            },
            "Professional / Confident": {
                "expression_style": "Dignified confidence, traditional respect",
                "smile_intensity": "Warm but dignified",
                "body_language": "Formal posture, respectful gestures",
                "eye_contact": "Strong among same gender, respectful cross-gender",
                "personal_space": "Gender-appropriate distance",
                "vocal_style": "Formal, respectful, emphatic when needed"
            }
        }
    }
    
    @classmethod
    def get_cultural_variation(cls, culture: str, emotion: str) -> Dict[str, Any]:
        """Get cultural-specific expression for emotion"""
        culture_data = cls.CULTURAL_DATABASE.get(culture, cls.CULTURAL_DATABASE["American"])
        return culture_data.get(emotion, {
            "expression_style": "Universal human expression",
            "smile_intensity": "Moderate",
            "body_language": "Natural",
            "eye_contact": "Appropriate",
            "personal_space": "Comfortable",
            "vocal_style": "Natural"
        })
    
    @classmethod
    def build_cultural_prompt_section(cls, culture: str, emotion: str) -> str:
        """Build prompt section for cultural variation"""
        variation = cls.get_cultural_variation(culture, emotion)
        
        prompt_parts = [
            f"CULTURAL CONTEXT: {culture.upper()}",
            f"EMOTION: {emotion}",
            "",
            f"Expression Style: {variation['expression_style']}",
            f"Smile Intensity: {variation['smile_intensity']}",
            f"Body Language: {variation['body_language']}",
            f"Eye Contact Pattern: {variation['eye_contact']}",
            f"Personal Space: {variation['personal_space']}",
            f"Vocal Style: {variation['vocal_style']}",
        ]
        
        return "\n".join(prompt_parts)
    
    @classmethod
    def get_available_cultures(cls) -> List[str]:
        """Get list of available cultural variations"""
        return list(cls.CULTURAL_DATABASE.keys())
    
    @classmethod
    def compare_cultures(cls, emotion: str, cultures: List[str]) -> Dict[str, Any]:
        """Compare how different cultures express same emotion"""
        comparison = {}
        for culture in cultures:
            comparison[culture] = cls.get_cultural_variation(culture, emotion)
        return comparison
