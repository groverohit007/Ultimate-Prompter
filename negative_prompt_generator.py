"""
Negative Prompt Generator
==========================
Generates comprehensive negative prompts to avoid common AI mistakes
"""

from typing import List, Dict, Any


class NegativePromptGenerator:
    """Generate negative prompts based on context"""
    
    UNIVERSAL_NEGATIVES = [
        "static facial expression",
        "frozen expression",
        "robotic movements",
        "mechanical blinking (avoid 1-second intervals)",
        "perfectly symmetrical face",
        "dead eyes / soulless gaze",
        "no pupil dilation",
        "flat lighting",
        "baked lighting",
        "cartoon / anime style",
        "bad anatomy",
        "deformed face",
        "blurry / out of focus",
        "low quality",
        "pixelated",
        "jpeg artifacts",
        "watermark / signature",
        "text overlay",
        "logo",
        "timestamp"
    ]
    
    EMOTION_SPECIFIC_NEGATIVES = {
        "Happy / Excited / Joyful": [
            "sad expression",
            "frowning",
            "downturned mouth",
            "flat affect",
            "no eye crinkle (Duchenne marker missing)",
            "forced smile (no orbicularis oculi)",
            "tense jaw",
            "closed body language"
        ],
        "Professional / Confident": [
            "nervous fidgeting",
            "slouching",
            "avoiding eye contact",
            "uncertain expression",
            "excessive smiling",
            "overly casual posture",
            "rapid blinking (nervousness)"
        ],
        "Serious / Focused / Intense": [
            "smiling",
            "laughing",
            "playful expression",
            "distracted gaze",
            "excessive blinking",
            "casual posture",
            "relaxed jaw"
        ],
        "Authentic / Natural": [
            "overly posed",
            "studio perfect",
            "Instagram filter look",
            "airbrushed skin",
            "plastic appearance",
            "too perfect symmetry",
            "model pose",
            "advertising look"
        ],
        "Emotional / Touching / Vulnerable": [
            "smiling broadly",
            "upbeat expression",
            "confident posture",
            "strong eye contact",
            "energetic movement",
            "loud demeanor"
        ],
        "Funny / Witty / Goofy": [
            "serious expression",
            "formal posture",
            "restrained movement",
            "deadpan delivery (unless intentional)",
            "professional demeanor",
            "no exaggeration"
        ],
        "Nervous / Anxious / Uncomfortable": [
            "confident posture",
            "steady hands",
            "calm expression",
            "slow breathing",
            "relaxed jaw",
            "direct prolonged eye contact"
        ],
        "Flirty / Playful / Charming": [
            "aggressive stance",
            "serious expression",
            "closed body language",
            "no smile",
            "distant gaze",
            "formal demeanor"
        ]
    }
    
    MOTION_SPECIFIC_NEGATIVES = {
        "Walking Runway": [
            "stumbling",
            "awkward gait",
            "looking down",
            "hunched shoulders",
            "stiff movement",
            "arms not swinging naturally"
        ],
        "Turning Head & Smiling": [
            "neck snap / too fast turn",
            "eyes don't lead the turn",
            "smile before turn completes",
            "hair doesn't follow physics",
            "robotic rotation"
        ],
        "Drinking Coffee": [
            "cup empty (no liquid physics)",
            "hands not wrapping cup naturally",
            "no steam from hot beverage",
            "drinking without swallowing",
            "eyes don't close or look down"
        ],
        "Typing": [
            "hands not on keyboard",
            "fingers not moving",
            "looking at keyboard constantly (unless hunting-pecking)",
            "no screen reflection in eyes",
            "no body slight movement"
        ],
        "Dancing": [
            "off-beat movement",
            "stiff joints",
            "no weight transfer",
            "hair doesn't move with rhythm",
            "clothing static"
        ],
        "Running": [
            "arms not pumping",
            "no forward lean",
            "feet landing flat",
            "no breathing visible",
            "hair static (no wind effect)"
        ],
        "Talking to Camera": [
            "no lip sync",
            "static head position",
            "no blinking",
            "eyes not focused on camera",
            "no breathing between sentences",
            "hands completely still"
        ]
    }
    
    PHYSICS_NEGATIVES = [
        "hair defying gravity",
        "cloth clipping through body",
        "rigid fabric (no natural draping)",
        "no cloth physics",
        "no hair movement",
        "floating objects",
        "inconsistent lighting direction",
        "shadows disappearing",
        "no subsurface scattering on skin",
        "skin looks plastic",
        "no realistic reflections",
        "ambient occlusion missing"
    ]
    
    MODEL_SPECIFIC_NEGATIVES = {
        "Kling 1.5": [
            "low texture quality",
            "smooth skin (too perfect)",
            "no fabric detail",
            "camera shake",
            "inconsistent lighting"
        ],
        "Veo 2 / Sora": [
            "physics errors",
            "gravity mistakes",
            "floating objects",
            "unrealistic fluid dynamics",
            "light penetrating solid objects"
        ],
        "Luma Dream Machine": [
            "style inconsistency between frames",
            "abrupt transitions",
            "keyframe mismatch",
            "jerky camera movement"
        ],
        "Runway Gen-3 Alpha": [
            "facial feature drift",
            "identity morphing",
            "structure breakdown",
            "inconsistent face between frames"
        ],
        "Minimax": [
            "expression override (unnatural)",
            "too smooth motion",
            "cultural inaccuracy",
            "feature exaggeration"
        ],
        "Haiper": [
            "artistic interpretation when realism needed",
            "style shift mid-video",
            "oversimplification of details"
        ]
    }
    
    @classmethod
    def generate(cls, emotion: str = "", motion: str = "", model: str = "",
                include_physics: bool = True) -> str:
        """Generate comprehensive negative prompt"""
        
        negatives = cls.UNIVERSAL_NEGATIVES.copy()
        
        # Add emotion-specific negatives
        if emotion and emotion in cls.EMOTION_SPECIFIC_NEGATIVES:
            negatives.extend(cls.EMOTION_SPECIFIC_NEGATIVES[emotion])
        
        # Add motion-specific negatives
        if motion and motion in cls.MOTION_SPECIFIC_NEGATIVES:
            negatives.extend(cls.MOTION_SPECIFIC_NEGATIVES[motion])
        
        # Add physics negatives
        if include_physics:
            negatives.extend(cls.PHYSICS_NEGATIVES)
        
        # Add model-specific negatives
        if model and model in cls.MODEL_SPECIFIC_NEGATIVES:
            negatives.extend(cls.MODEL_SPECIFIC_NEGATIVES[model])
        
        # Remove duplicates and join
        unique_negatives = list(dict.fromkeys(negatives))
        
        return ", ".join(unique_negatives)
    
    @classmethod
    def generate_structured(cls, emotion: str = "", motion: str = "", 
                          model: str = "", include_physics: bool = True) -> Dict[str, List[str]]:
        """Generate negative prompt with categories"""
        
        structured = {
            "universal": cls.UNIVERSAL_NEGATIVES.copy(),
            "emotion_specific": cls.EMOTION_SPECIFIC_NEGATIVES.get(emotion, []),
            "motion_specific": cls.MOTION_SPECIFIC_NEGATIVES.get(motion, []),
            "physics": cls.PHYSICS_NEGATIVES if include_physics else [],
            "model_specific": cls.MODEL_SPECIFIC_NEGATIVES.get(model, [])
        }
        
        return structured
    
    @classmethod
    def get_critical_negatives(cls, emotion: str = "", motion: str = "") -> List[str]:
        """Get the most critical negatives for this context (top 10)"""
        
        critical = [
            "robotic movements",
            "static facial expression",
            "dead eyes / soulless gaze",
            "no pupil dilation",
            "bad anatomy"
        ]
        
        # Add top emotion-specific
        if emotion and emotion in cls.EMOTION_SPECIFIC_NEGATIVES:
            critical.extend(cls.EMOTION_SPECIFIC_NEGATIVES[emotion][:3])
        
        # Add top motion-specific
        if motion and motion in cls.MOTION_SPECIFIC_NEGATIVES:
            critical.extend(cls.MOTION_SPECIFIC_NEGATIVES[motion][:2])
        
        return critical[:10]
