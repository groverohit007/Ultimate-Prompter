"""
Ultra Realism Engine
====================
Advanced techniques for generating photorealistic images that look like real people
"""

from typing import Dict, Any, List


class UltraRealismEngine:
    """Generate prompts with photorealistic enhancements"""
    
    REALISM_TECHNIQUES = {
        "skin": {
            "base": "Natural skin texture with visible pores, fine lines, and subtle imperfections",
            "advanced": [
                "Subsurface scattering (light penetrating skin layers)",
                "Microdetails: freckles, small moles, fine hair (peach fuzz)",
                "Natural color variation (not uniform - redness in cheeks, darker around eyes)",
                "Visible skin texture under makeup (if wearing any)",
                "Realistic blood vessel visibility (subtle blue/red undertones)",
                "Natural shine/oil on T-zone (forehead, nose)",
                "Pore size variation across face",
                "Tiny skin imperfections: old acne scars, fine wrinkles, texture"
            ]
        },
        
        "eyes": {
            "base": "Realistic eyes with natural reflections and imperfections",
            "advanced": [
                "Catchlights (reflections of light source in pupils)",
                "Visible iris texture (crypts, furrows, collarette)",
                "Slight redness in corners (natural blood vessels)",
                "Limbal ring (darker ring around iris)",
                "Pupils react to light (slightly different sizes if natural)",
                "Eyelashes: individual strands, varying lengths, not perfect",
                "Small veins visible in sclera (white of eye)",
                "Natural moisture/glassiness",
                "Subtle asymmetry between left and right eye"
            ]
        },
        
        "hair": {
            "base": "Natural hair with individual strands and realistic physics",
            "advanced": [
                "Individual hair strands visible (not a solid mass)",
                "Flyaway hairs and baby hairs",
                "Natural color variation (highlights, lowlights from sun exposure)",
                "Realistic hair density (scalp slightly visible in parts)",
                "Hair follows gravity and physics",
                "Natural shine patterns (not uniform glossiness)",
                "Split ends or texture variation (if applicable)",
                "Hair roots slightly darker than ends",
                "Natural hair direction flow"
            ]
        },
        
        "lighting": {
            "base": "Natural lighting with realistic shadows and highlights",
            "advanced": [
                "Three-point lighting: key light, fill light, rim light",
                "Realistic shadow softness (depends on light distance)",
                "Color temperature matching (warm indoor vs cool outdoor)",
                "Specular highlights on skin, eyes, lips",
                "Ambient occlusion (darkening in crevices and folds)",
                "Realistic falloff (inverse square law)",
                "Natural bounce light (light reflecting from surfaces)",
                "Atmospheric perspective if outdoors",
                "Realistic exposure (not overblown or underexposed)"
            ]
        },
        
        "camera": {
            "base": "Shot with professional camera characteristics",
            "advanced": [
                "Natural depth of field (realistic bokeh in background)",
                "Slight lens distortion (depends on focal length)",
                "Chromatic aberration (subtle color fringing - optional)",
                "Natural vignetting (slight darkening at edges)",
                "Film grain or sensor noise (very subtle)",
                "Realistic motion blur if movement",
                "Proper focus point (eyes sharp, background soft)",
                "Natural color science (not oversaturated)",
                "Shot on professional camera: Sony A7IV, Canon R5, Nikon Z9"
            ]
        },
        
        "proportions": {
            "base": "Anatomically correct human proportions",
            "advanced": [
                "Natural asymmetry (no perfect symmetry - humans aren't symmetric)",
                "Realistic head-to-body ratio",
                "Proper facial feature proportions (golden ratio loosely)",
                "Natural hand size and finger proportions",
                "Realistic body type (not idealized - natural variation)",
                "Age-appropriate features (wrinkles, skin elasticity for age)",
                "Natural posture (slight imperfections, not model-perfect)",
                "Realistic muscle definition (if applicable)",
                "Natural weight distribution"
            ]
        },
        
        "details": {
            "base": "Environmental and context realism",
            "advanced": [
                "Natural interaction with environment (shadows on face from objects)",
                "Realistic fabric textures on clothing",
                "Natural wrinkles and folds in clothing",
                "Proper perspective and scale",
                "Atmospheric effects (haze if distance, moisture if applicable)",
                "Natural color grading (not Instagram-filtered)",
                "Realistic material properties (metals reflect, fabrics absorb)",
                "Environmental reflections in eyes and shiny surfaces",
                "Natural caustics (light patterns through/around objects)"
            ]
        },
        
        "imperfections": {
            "base": "Natural human imperfections that prove authenticity",
            "advanced": [
                "Slightly uneven skin tone",
                "Small blemishes or spots",
                "Natural under-eye variation (not heavy bags, just natural shadow)",
                "Slightly asymmetric facial features",
                "Natural teeth (not Hollywood perfect white)",
                "Visible pores and skin texture",
                "Fine lines around eyes when smiling",
                "Natural eyebrow variation (not perfectly groomed)",
                "Realistic nail texture and cuticles if hands visible"
            ]
        }
    }
    
    NEGATIVE_PROMPTS_ULTRA = [
        "airbrushed skin",
        "plastic skin",
        "doll-like appearance",
        "perfect symmetry",
        "uncanny valley",
        "CGI look",
        "3D render appearance",
        "video game character",
        "mannequin",
        "wax figure",
        "oversaturated colors",
        "Instagram filter look",
        "beauty filter",
        "smooth skin (no texture)",
        "glowing skin (unnatural)",
        "perfect features",
        "no pores visible",
        "uniform skin tone",
        "fake-looking",
        "synthetic appearance",
        "too perfect",
        "idealized features",
        "flawless skin"
    ]
    
    @classmethod
    def enhance_prompt(cls, base_prompt: str, realism_level: str = "High") -> str:
        """
        Enhance a prompt with ultra-realism techniques.
        
        Args:
            base_prompt: Original character/scene description
            realism_level: "Medium", "High", or "Maximum"
        
        Returns:
            Enhanced prompt with realism techniques
        """
        
        # Determine how many techniques to include
        technique_counts = {
            "Medium": 2,
            "High": 3,
            "Maximum": 5
        }
        count = technique_counts.get(realism_level, 3)
        
        # Build enhancement sections
        enhancements = [
            base_prompt,
            "",
            "ULTRA-REALISM ENHANCEMENTS:",
            ""
        ]
        
        # Add skin realism
        enhancements.append("SKIN REALISM:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['skin']['base']}")
        for technique in cls.REALISM_TECHNIQUES['skin']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add eye realism
        enhancements.append("EYE REALISM:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['eyes']['base']}")
        for technique in cls.REALISM_TECHNIQUES['eyes']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add hair realism
        enhancements.append("HAIR REALISM:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['hair']['base']}")
        for technique in cls.REALISM_TECHNIQUES['hair']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add lighting
        enhancements.append("LIGHTING REALISM:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['lighting']['base']}")
        for technique in cls.REALISM_TECHNIQUES['lighting']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add camera
        enhancements.append("CAMERA REALISM:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['camera']['base']}")
        for technique in cls.REALISM_TECHNIQUES['camera']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add proportions
        enhancements.append("ANATOMICAL ACCURACY:")
        enhancements.append(f"  {cls.REALISM_TECHNIQUES['proportions']['base']}")
        for technique in cls.REALISM_TECHNIQUES['proportions']['advanced'][:count]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add imperfections (critical for realism)
        enhancements.append("AUTHENTIC IMPERFECTIONS (Critical for realism):")
        for technique in cls.REALISM_TECHNIQUES['imperfections']['advanced'][:count + 2]:
            enhancements.append(f"  • {technique}")
        enhancements.append("")
        
        # Add quality markers
        enhancements.extend([
            "QUALITY & TECHNICAL:",
            "  • 8K resolution, high detail",
            "  • Professional photography",
            "  • Shot on: Sony A7IV with 85mm f/1.4 lens",
            "  • Natural color grading",
            "  • Photorealistic, not illustration",
            "  • Real person, not AI-generated look",
            ""
        ])
        
        return "\n".join(enhancements)
    
    @classmethod
    def get_negative_prompt(cls) -> str:
        """Get comprehensive negative prompt for ultra-realism"""
        return ", ".join(cls.NEGATIVE_PROMPTS_ULTRA)
    
    @classmethod
    def analyze_for_realism(cls, prompt: str) -> Dict[str, Any]:
        """
        Analyze a prompt and score its realism potential.
        Enhanced to recognize both technical keywords AND visual detail descriptions.
        
        Returns dict with realism score and suggestions.
        """
        
        score = 0
        suggestions = []
        prompt_lower = prompt.lower()
        
        # CATEGORY 1: Technical Realism Keywords (10 points each, max 50)
        technical_keywords = [
            "natural", "realistic", "photorealistic", "8k", "detailed",
            "pores", "texture", "imperfections", "natural lighting",
            "subsurface scattering", "professional", "camera"
        ]
        
        for keyword in technical_keywords:
            if keyword in prompt_lower:
                score += 10
        
        # Cap technical keywords at 50 points
        score = min(score, 50)
        
        # CATEGORY 2: Visual Detail Descriptors (5 points each, max 40)
        # These are words that indicate detailed physical description
        detail_descriptors = [
            "skin tone", "eye color", "hair color", "face shape", "nose shape",
            "lip", "eyebrow", "eyelash", "facial structure", "cheekbone",
            "jawline", "chin", "forehead", "complexion", "freckles",
            "mole", "beauty mark", "iris", "pupil", "catchlight"
        ]
        
        detail_score = 0
        for descriptor in detail_descriptors:
            if descriptor in prompt_lower:
                detail_score += 5
        
        score += min(detail_score, 40)
        
        # CATEGORY 3: Photography Terms (5 points each, max 30)
        photo_terms = [
            "lighting", "shadow", "depth of field", "bokeh", "lens",
            "focal length", "exposure", "shot on", "sony", "canon",
            "nikon", "f/", "85mm", "50mm", "portrait lens"
        ]
        
        photo_score = 0
        for term in photo_terms:
            if term in prompt_lower:
                photo_score += 5
        
        score += min(photo_score, 30)
        
        # CATEGORY 4: Bonus for Length (detailed descriptions)
        word_count = len(prompt.split())
        if word_count > 200:
            score += 20  # Long detailed prompt bonus
        elif word_count > 100:
            score += 10
        
        # PENALTIES: Unrealistic keywords (-15 each)
        problematic = [
            "perfect", "flawless", "beautiful", "gorgeous", "stunning",
            "smooth skin", "glowing", "airbrushed", "magazine cover",
            "model perfect", "Instagram filter"
        ]
        
        for keyword in problematic:
            if keyword in prompt_lower:
                score -= 15
                suggestions.append(f"⚠️ Remove '{keyword}' - use natural descriptions instead")
        
        # Generate suggestions based on score
        if score < 40:
            suggestions.extend([
                "Add specific skin texture details (visible pores, fine lines, natural color variation)",
                "Include detailed eye description (color, shape, iris texture, catchlights)",
                "Describe hair in detail (color, texture, individual strands, natural shine)",
                "Mention professional camera equipment (Sony A7IV, 85mm f/1.4 lens)",
                "Add natural lighting description (soft window light, realistic shadows)"
            ])
        elif score < 70:
            suggestions.extend([
                "Good detail! Add more physical feature specifics (face shape, nose shape, lip fullness)",
                "Include natural imperfections (slight asymmetry, small blemishes)",
                "Mention photographic qualities (depth of field, bokeh, film grain)"
            ])
        else:
            suggestions.append("✅ Excellent realism! Prompt has strong photorealistic potential.")
        
        # Determine realism level
        if score < 40:
            realism_level = "Low"
        elif score < 70:
            realism_level = "Medium"
        elif score < 90:
            realism_level = "High"
        else:
            realism_level = "Ultra-High"
        
        return {
            "realism_score": max(0, min(100, score)),
            "realism_level": realism_level,
            "suggestions": suggestions
        }
    
    @classmethod
    def get_preset(cls, preset_name: str) -> str:
        """
        Get pre-configured ultra-realism preset.
        
        Presets: "Portrait", "Full Body", "Close-up", "Environmental"
        """
        
        presets = {
            "Portrait": (
                "Professional portrait photography. Natural skin with visible pores and texture. "
                "Realistic eye details with catchlights and iris texture. Individual hair strands. "
                "Natural facial asymmetry. Soft natural lighting with realistic shadows. "
                "Shot on Sony A7IV, 85mm f/1.4, natural depth of field. "
                "Photorealistic, looks like real person, authentic imperfections."
            ),
            
            "Full Body": (
                "Full body professional photograph. Natural human proportions with slight asymmetry. "
                "Realistic fabric textures and natural clothing wrinkles. Natural posture with weight distribution. "
                "Environmental interaction (shadows, reflections). Natural lighting with proper falloff. "
                "Shot on Canon R5, 35mm f/1.8. Photorealistic, authentic details, real person."
            ),
            
            "Close-up": (
                "Extreme close-up photography with macro detail. Every pore visible, individual eyelashes, "
                "skin texture with fine lines and natural imperfections. Realistic subsurface scattering. "
                "Intimate detail showing humanity - small blemishes, fine wrinkles, natural skin variation. "
                "Shot on Nikon Z9 with 105mm macro lens. Ultra-detailed, photorealistic, hyperreal."
            ),
            
            "Environmental": (
                "Person in natural environment with realistic interaction. Environmental lighting affecting face, "
                "natural shadows from surroundings, atmospheric perspective. Realistic scale and proportion in scene. "
                "Natural color temperature from environment. Person affected by weather/environment (wind in hair, etc). "
                "Shot on location with natural light. Documentary photography style, authentic moment."
            )
        }
        
        return presets.get(preset_name, presets["Portrait"])
