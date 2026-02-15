"""
DrMotion Emotion Engine
=======================
Comprehensive emotion mapping for realistic AI video generation.
Maps emotions to micro-expressions, body language, vocal patterns, and temporal dynamics.
"""

from typing import Dict, Any, List


class EmotionEngine:
    """Database of realistic human emotions with detailed behavioral mappings."""
    
    EMOTION_DATABASE = {
        "Authentic / Natural": {
            "description": "Genuine, unstaged human behavior",
            "micro_expressions": [
                "Asymmetrical smile (authentic happiness marker)",
                "Crow's feet wrinkles around eyes when smiling",
                "Natural blink rate (12-20 per minute)",
                "Slight head tilts during thought",
                "Micro-grimaces before speaking (pre-speech tension)"
            ],
            "body_language": [
                "Weight shifting between feet (not statue-still)",
                "Breathing visible in shoulders/chest",
                "Hands making small adjustments (touching hair, face)",
                "Posture micro-corrections every 3-5 seconds",
                "Natural asymmetry (one shoulder slightly higher)"
            ],
            "facial_dynamics": [
                "Eyebrows raise slightly when emphasizing points",
                "Lips press together during pauses",
                "Nose wrinkles subtly during concentration",
                "Jaw tension releases between phrases",
                "Eyes dart to thinking position (up-left for memory recall)"
            ],
            "eye_behavior": [
                "Blinks complete before head turns",
                "Pupils adjust to light changes",
                "Brief moments of unfocus/daydreaming",
                "Eye contact breaks every 3-5 seconds (looks away naturally)",
                "Slower blink when processing information"
            ],
            "breathing_pattern": "Relaxed diaphragmatic breathing (12-16 breaths/min)",
            "vocal_qualities": [
                "Natural voice cracks on emotional words",
                "Slight hesitations: 'um', 'like', 'you know'",
                "Volume varies ±15% organically",
                "Breathing audible between long sentences",
                "Pace slows when explaining, speeds when excited"
            ],
            "temporal_progression": {
                "start": "Slight nervous energy (settling in)",
                "middle": "Comfortable flow, natural gestures",
                "end": "Relaxed conclusion, gentle smile"
            },
            "imperfections": [
                "Hair falls in face occasionally (brushed away)",
                "One eye opens slightly wider than the other",
                "Slight head bob when agreeing internally",
                "Tongue briefly touches lips (moistening)"
            ]
        },
        
        "Happy / Excited / Joyful": {
            "description": "Genuine positive emotion with high energy",
            "micro_expressions": [
                "Duchenne smile (eyes crinkle, cheeks lift)",
                "Eyebrows raise and relax quickly",
                "Lower eyelids tense (pushes cheeks up)",
                "Nasal wings flare slightly",
                "Upper teeth visible when smiling"
            ],
            "body_language": [
                "Shoulders rise and open (expansive posture)",
                "Hands move faster, larger gestures",
                "Weight on balls of feet (bouncing energy)",
                "Head tilts back during peak laughter",
                "Arms open/lift upward naturally"
            ],
            "facial_dynamics": [
                "Smile lines deepen (orbicularis oculi activation)",
                "Forehead smooths out (relaxed frontalis muscle)",
                "Cheeks stay elevated even when not speaking",
                "Mouth corners pull up asymmetrically (left often higher)",
                "Eyes squint more during genuine laughter"
            ],
            "eye_behavior": [
                "Pupils dilate (excitement response)",
                "Blink rate increases (16-26 per minute)",
                "Eyes widen during peak excitement",
                "Gaze direct and engaged",
                "Rapid eye contact (seeking to share joy)"
            ],
            "breathing_pattern": "Quick shallow breaths (18-24 breaths/min), visible chest movement",
            "vocal_qualities": [
                "Pitch rises 10-20% above baseline",
                "Faster speech (140-180 words/min)",
                "Laughter interrupts words",
                "Volume increases naturally (+20-30%)",
                "Breathiness from excitement"
            ],
            "temporal_progression": {
                "start": "Growing smile, eyes widening",
                "middle": "Peak expression - full Duchenne smile, animated",
                "end": "Afterglow - residual smile, relaxed contentment"
            },
            "movement_physics": [
                "Hair bounces with energetic movements",
                "Clothing shifts with larger gestures",
                "Slight bounce in stance (high energy)",
                "Faster micro-adjustments"
            ]
        },
        
        "Professional / Confident": {
            "description": "Controlled composure with quiet authority",
            "micro_expressions": [
                "Slight chin lift (confidence)",
                "Minimal eyebrow movement (controlled)",
                "Lips remain neutral or slight upward curve",
                "Steady, unwavering gaze",
                "Reduced facial animation (±20% of natural)"
            ],
            "body_language": [
                "Shoulders back, spine straight",
                "Symmetrical posture (balanced)",
                "Hands steepled or clasped (control)",
                "Minimal weight shifting",
                "Deliberate, slower movements"
            ],
            "facial_dynamics": [
                "Jaw set firmly (masseter tension)",
                "Minimal smile (professional pleasantness)",
                "Forehead smooth but eyebrows slightly lowered (focus)",
                "Lips press together between statements (decisiveness)",
                "Nose breathing visible (controlled, calm)"
            ],
            "eye_behavior": [
                "Reduced blink rate (8-12 per minute - dominance signal)",
                "Direct, sustained eye contact",
                "Pupils normal size (controlled arousal)",
                "Slow, deliberate eye movements",
                "Gaze holds steady during pauses"
            ],
            "breathing_pattern": "Deep, slow, controlled breaths (8-12 breaths/min), minimal chest movement",
            "vocal_qualities": [
                "Lower pitch (-10% from baseline)",
                "Measured pace (100-120 words/min)",
                "Crisp articulation",
                "Strategic pauses for emphasis",
                "Steady volume (no fluctuation)"
            ],
            "temporal_progression": {
                "start": "Establishing authority - direct gaze, firm posture",
                "middle": "Sustained confidence - minimal variation",
                "end": "Controlled conclusion - subtle nod of finality"
            },
            "movement_physics": [
                "Minimal clothing movement (stable posture)",
                "Hair stays in place (controlled motion)",
                "Smooth, calculated gestures"
            ]
        },
        
        "Funny / Witty / Goofy": {
            "description": "Playful mischief with comedic timing",
            "micro_expressions": [
                "One eyebrow raise (skeptical humor)",
                "Smirk (asymmetrical mouth)",
                "Eye roll or sideways glance",
                "Nose scrunch (playful disgust)",
                "Exaggerated expressions (20% over-animated)"
            ],
            "body_language": [
                "Shoulders shrug dramatically",
                "Hands gesture wildly/exaggerated",
                "Head tilts exaggerated (comedic effect)",
                "Body leans in for punchlines",
                "Playful stance (hip pop, loose posture)"
            ],
            "facial_dynamics": [
                "Eyebrows dance (rapid up/down)",
                "Cheeks puff out or suck in (silly faces)",
                "Tongue sticks out briefly",
                "Eyes widen then narrow (comedic beat)",
                "Lips purse then release (exaggerated)"
            ],
            "eye_behavior": [
                "Eyes dart around (building joke)",
                "Wink or double-take",
                "Pupils normal but eyes very expressive",
                "Blink rate varies wildly (timing comedy)",
                "Sideways glances to 'audience'"
            ],
            "breathing_pattern": "Irregular from laughter (16-22 breaths/min), snorts or giggles",
            "vocal_qualities": [
                "Pitch varies wildly (±30%)",
                "Pace changes for comic effect",
                "Strategic pauses before punchlines",
                "Exaggerated emphasis on key words",
                "Sound effects or vocal tricks"
            ],
            "temporal_progression": {
                "start": "Setup - normal with hints of mischief",
                "middle": "Build - exaggerated expressions increase",
                "end": "Punchline - peak expression, then quick return to straight face"
            },
            "movement_physics": [
                "Exaggerated hair movement",
                "Clothing bounces with jerky movements",
                "Quick, sharp gestures create momentum"
            ]
        },
        
        "Emotional / Touching / Vulnerable": {
            "description": "Genuine emotional openness, tender moments",
            "micro_expressions": [
                "Eyebrows knit together (sadness/concern)",
                "Lower lip slight quiver",
                "Eyes glisten (moisture without tears)",
                "Jaw trembles slightly",
                "Chin dimples (mentalis muscle tension)"
            ],
            "body_language": [
                "Shoulders curl inward (protective)",
                "Arms cross or hands clasp (self-soothing)",
                "Head lowers or tilts down",
                "Weight shifts to one leg (uncertainty)",
                "Hand touches face/neck (comfort-seeking)"
            ],
            "facial_dynamics": [
                "Forehead wrinkles (corrugator supercilii)",
                "Eyes narrow slightly (holding back tears)",
                "Nose tip reddens (blood flow from emotion)",
                "Lips press thin or quiver",
                "Cheeks may flush (parasympathetic response)"
            ],
            "eye_behavior": [
                "Blink rate decreases initially (8-10/min), then rapid blinking",
                "Eyes look down or away (vulnerability)",
                "Pupils slightly dilated (emotional arousal)",
                "Gaze unfocused (internal processing)",
                "Eyelids heavy (emotional fatigue)"
            ],
            "breathing_pattern": "Irregular, shallow (16-24 breaths/min), visible catching of breath",
            "vocal_qualities": [
                "Voice cracks or wavers",
                "Pitch rises slightly from tension",
                "Pace slows (processing emotion)",
                "Long pauses between thoughts",
                "Quieter volume (-20%)"
            ],
            "temporal_progression": {
                "start": "Fighting emotion - controlled but strained",
                "middle": "Vulnerability shows - micro-trembles, glistening eyes",
                "end": "Release or resolution - deep breath, soft smile"
            },
            "movement_physics": [
                "Minimal movement (stillness from emotion)",
                "Hair may fall forward (head lowered)",
                "Clothing barely moves (contained posture)"
            ]
        },
        
        "Serious / Focused / Intense": {
            "description": "Deep concentration with unwavering attention",
            "micro_expressions": [
                "Eyebrows slightly furrowed (focus)",
                "Lips pressed thin (determination)",
                "Jaw clenched subtly (tension)",
                "No smile (neutral/slightly stern)",
                "Nostrils may flare (increased oxygen)"
            ],
            "body_language": [
                "Perfectly still posture (locked in)",
                "Leaning slightly forward (engagement)",
                "Hands still or making precise gestures",
                "Shoulders squared (readiness)",
                "No fidgeting (complete focus)"
            ],
            "facial_dynamics": [
                "Forehead tension (glabella furrow)",
                "Eyes narrowed (concentration)",
                "Minimal facial movement (all energy on task)",
                "Breathing through nose (controlled)",
                "Jaw tension visible in cheeks"
            ],
            "eye_behavior": [
                "Very low blink rate (4-8/min - extreme focus)",
                "Pupils normal to slightly constricted",
                "Gaze locked (tunnel vision)",
                "No eye wandering",
                "Intense, penetrating stare"
            ],
            "breathing_pattern": "Slow, deep, controlled (6-10 breaths/min), invisible chest movement",
            "vocal_qualities": [
                "Low, steady pitch",
                "Deliberate, measured pace (90-110 words/min)",
                "Clear articulation",
                "No hesitation",
                "Firm, authoritative tone"
            ],
            "temporal_progression": {
                "start": "Gathering focus - eyes narrow, posture sets",
                "middle": "Peak concentration - minimal movement, laser focus",
                "end": "Task completion - slight exhale, micro-relaxation"
            },
            "movement_physics": [
                "Statue-like stillness",
                "Hair doesn't move (no excess motion)",
                "Clothing static (controlled posture)"
            ]
        },
        
        "Nervous / Anxious / Uncomfortable": {
            "description": "Visible stress and discomfort signals",
            "micro_expressions": [
                "Rapid blinking (stress response)",
                "Lips pursed or bitten",
                "Eyebrows raised and tense",
                "Forced smile (not reaching eyes)",
                "Swallowing frequently (dry mouth)"
            ],
            "body_language": [
                "Constant weight shifting",
                "Arms crossed (defensive)",
                "Hand fidgeting (fingers tapping, rubbing)",
                "Shoulders raised/tense",
                "Body angled away slightly"
            ],
            "facial_dynamics": [
                "Forehead sweating (stress response)",
                "Jaw tension (grinding/clenching)",
                "Lip licking (dry mouth)",
                "Eyes darting (scanning for escape)",
                "Facial muscles twitching"
            ],
            "eye_behavior": [
                "Rapid blink rate (20-30/min)",
                "Avoiding direct eye contact",
                "Pupils dilated (fight/flight)",
                "Eyes wide (hypervigilance)",
                "Gaze shifts rapidly"
            ],
            "breathing_pattern": "Rapid, shallow chest breathing (20-28 breaths/min), visible",
            "vocal_qualities": [
                "Higher pitch (+15-20%)",
                "Faster pace (rushed)",
                "Voice trembling/shaky",
                "Lots of filler words",
                "Volume fluctuates"
            ],
            "temporal_progression": {
                "start": "Initial discomfort - subtle tension",
                "middle": "Anxiety builds - visible fidgeting, rapid breathing",
                "end": "Relief if resolved OR peak anxiety"
            },
            "movement_physics": [
                "Constant small movements",
                "Hair brushed away repeatedly",
                "Clothing adjusted frequently"
            ]
        },
        
        "Flirty / Playful / Charming": {
            "description": "Attractive playfulness with subtle seduction",
            "micro_expressions": [
                "Raised eyebrow with slight smile",
                "Lips slightly parted (invitation)",
                "Coy smile (one corner up)",
                "Eyes half-lidded (bedroom eyes)",
                "Head tilt with eye contact"
            ],
            "body_language": [
                "Shoulders back (displaying)",
                "Touching own hair",
                "Leaning in slightly",
                "Playing with jewelry/clothing",
                "Hip pop (asymmetrical stance)"
            ],
            "facial_dynamics": [
                "Smile that builds slowly",
                "Lip bite or lick",
                "Dimples appear with smile",
                "Eyebrows raise and lower (playful)",
                "Blushing in cheeks"
            ],
            "eye_behavior": [
                "Extended eye contact then look away",
                "Pupils dilated (attraction)",
                "Looking up through lashes",
                "Slow blinks (seductive)",
                "Glances then looks away (coy)"
            ],
            "breathing_pattern": "Slightly elevated (14-18 breaths/min), chest rises visibly",
            "vocal_qualities": [
                "Softer, breathier voice",
                "Pitch varies (musical quality)",
                "Slower pace (seductive)",
                "Giggles or soft laughs",
                "Playful teasing tone"
            ],
            "temporal_progression": {
                "start": "Subtle interest - eye contact, slight smile",
                "middle": "Building attraction - playful gestures, hair touch",
                "end": "Peak charm - full smile, confident eye contact"
            },
            "movement_physics": [
                "Hair flips or tosses",
                "Clothing shifts with deliberate movements",
                "Smooth, flowing gestures"
            ]
        }
    }
    
    @classmethod
    def get_emotion_details(cls, emotion_name: str) -> dict:
        """Get detailed breakdown for an emotion."""
        return cls.EMOTION_DATABASE.get(emotion_name, cls.EMOTION_DATABASE["Authentic / Natural"])
    
    @classmethod
    def get_all_emotions(cls) -> list:
        """Get list of all available emotions."""
        return list(cls.EMOTION_DATABASE.keys())
    
    @classmethod
    def build_emotion_prompt_section(cls, emotion_name: str, intensity: str = "Medium") -> str:
        """
        Build a detailed prompt section for the given emotion.
        
        Args:
            emotion_name: The emotion to generate
            intensity: "Subtle", "Medium", or "Strong"
        """
        details = cls.get_emotion_details(emotion_name)
        
        # Intensity modifiers
        intensity_multipliers = {
            "Subtle": 0.5,
            "Medium": 1.0,
            "Strong": 1.5
        }
        mult = intensity_multipliers.get(intensity, 1.0)
        
        prompt_parts = [
            f"EMOTION: {emotion_name.upper()} (Intensity: {intensity})",
            f"Description: {details['description']}",
            "",
            "🎭 MICRO-EXPRESSIONS (Facial Details):"
        ]
        
        # Add micro-expressions with intensity adjustment
        for expr in details['micro_expressions'][:int(5 * mult)]:
            prompt_parts.append(f"   • {expr}")
        
        prompt_parts.extend([
            "",
            "👤 BODY LANGUAGE:"
        ])
        
        for body in details['body_language'][:int(5 * mult)]:
            prompt_parts.append(f"   • {body}")
        
        prompt_parts.extend([
            "",
            "👁️ EYE BEHAVIOR & GAZE:"
        ])
        
        for eye in details['eye_behavior'][:int(5 * mult)]:
            prompt_parts.append(f"   • {eye}")
        
        prompt_parts.extend([
            "",
            f"💨 BREATHING: {details['breathing_pattern']}",
            "",
            "🗣️ VOCAL QUALITIES (for reference):"
        ])
        
        for vocal in details.get('vocal_qualities', [])[:int(3 * mult)]:
            prompt_parts.append(f"   • {vocal}")
        
        # Temporal progression
        prog = details.get('temporal_progression', {})
        if prog:
            prompt_parts.extend([
                "",
                "⏱️ TEMPORAL DYNAMICS (How emotion evolves):",
                f"   Start (0-2s): {prog.get('start', 'N/A')}",
                f"   Middle (3-6s): {prog.get('middle', 'N/A')}",
                f"   End (7-8s): {prog.get('end', 'N/A')}"
            ])
        
        # Physics
        if 'movement_physics' in details:
            prompt_parts.extend([
                "",
                "⚙️ PHYSICS SIMULATION:"
            ])
            for phys in details['movement_physics']:
                prompt_parts.append(f"   • {phys}")
        
        # Imperfections for authenticity
        if 'imperfections' in details:
            prompt_parts.extend([
                "",
                "✨ AUTHENTIC IMPERFECTIONS (Make it human):"
            ])
            for imp in details['imperfections'][:3]:
                prompt_parts.append(f"   • {imp}")
        
        return "\n".join(prompt_parts)
    
    @classmethod
    def mix_emotions(cls, primary_emotion: str, secondary_emotion: str, 
                     primary_weight: float = 0.7) -> Dict[str, Any]:
        """
        Mix two emotions with specified weights to create nuanced expressions.
        
        Args:
            primary_emotion: Main emotion (70% by default)
            secondary_emotion: Secondary emotion (30% by default)
            primary_weight: Weight of primary emotion (0.0-1.0)
        
        Returns:
            Mixed emotion dictionary with combined characteristics
        """
        primary = cls.get_emotion_details(primary_emotion)
        secondary = cls.get_emotion_details(secondary_emotion)
        secondary_weight = 1.0 - primary_weight
        
        # Calculate how many markers to take from each
        primary_count = int(5 * primary_weight)
        secondary_count = int(5 * secondary_weight)
        
        mixed = {
            "description": f"{primary['description']} with undertones of {secondary['description']}",
            "micro_expressions": (
                primary['micro_expressions'][:primary_count] +
                secondary['micro_expressions'][:secondary_count]
            ),
            "body_language": (
                primary['body_language'][:primary_count] +
                secondary['body_language'][:secondary_count]
            ),
            "facial_dynamics": (
                primary['facial_dynamics'][:primary_count] +
                secondary['facial_dynamics'][:secondary_count]
            ),
            "eye_behavior": (
                primary['eye_behavior'][:primary_count] +
                secondary['eye_behavior'][:secondary_count]
            ),
            "breathing_pattern": f"{primary['breathing_pattern']} transitioning to {secondary['breathing_pattern']}",
            "vocal_qualities": (
                primary.get('vocal_qualities', [])[:primary_count] +
                secondary.get('vocal_qualities', [])[:secondary_count]
            ),
            "temporal_progression": {
                "start": primary['temporal_progression'].get('start', 'N/A'),
                "middle": f"Blending {primary_emotion} and {secondary_emotion}",
                "end": secondary['temporal_progression'].get('end', 'N/A')
            },
            "is_mixed": True,
            "mix_ratio": f"{int(primary_weight*100)}% {primary_emotion} / {int(secondary_weight*100)}% {secondary_emotion}"
        }
        
        return mixed
    
    @classmethod
    def get_motion_specific_cues(cls, motion_type: str, emotion_name: str) -> str:
        """
        Get specific acting cues for common motion types with emotional context.
        """
        motion_cues = {
            "Walking Runway": {
                "base": "Confident stride, hips sway naturally, arms move opposite legs",
                "Happy / Excited / Joyful": "Add slight bounce, brighter eyes, subtle smile grows with each step",
                "Professional / Confident": "Steady, measured pace, minimal upper body movement, direct gaze forward",
                "Flirty / Playful / Charming": "One foot crossing slightly in front, shoulder rotation, playful glance over shoulder"
            },
            "Turning Head & Smiling": {
                "base": "Head turns smoothly, eyes lead the turn, smile builds after turn completes",
                "Happy / Excited / Joyful": "Eyes crinkle before smile appears, Duchenne markers activate, head turn slightly faster",
                "Professional / Confident": "Controlled turn speed, minimal smile (pleasant not joyful), eyes hold contact",
                "Authentic / Natural": "Slight anticipation micro-expression before turn, asymmetrical smile activation"
            },
            "Drinking Coffee": {
                "base": "Hands wrap around cup, slight steam rising, eyes look down at cup then up",
                "Emotional / Touching / Vulnerable": "Slow sip, eyes close briefly (savoring/comfort), hands hold cup tighter (self-soothing)",
                "Professional / Confident": "Efficient sip, eyes remain engaged with 'camera', cup held casually",
                "Happy / Excited / Joyful": "Eyes widen after first sip (delight), small 'mmm' expression, quick second sip"
            },
            "Typing": {
                "base": "Fingers move across keyboard, eyes track screen, occasional glances at keys",
                "Serious / Focused / Intense": "Faster typing cadence, no looking at keys, jaw set, lean forward",
                "Nervous / Anxious / Uncomfortable": "Hesitant typing, backspace visible, shoulders tense, frequent errors",
                "Professional / Confident": "Smooth rhythm, proper posture, efficient movements"
            },
            "Dancing": {
                "base": "Body moves to implied rhythm, weight shifts, arms coordinate with steps",
                "Happy / Excited / Joyful": "Larger movements, spinning, hair flies, genuine laughter mid-dance",
                "Funny / Witty / Goofy": "Exaggerated moves, silly faces, intentionally awkward moments, comedic timing",
                "Flirty / Playful / Charming": "Hip movements emphasized, seductive shoulder rolls, eye contact with 'audience'"
            },
            "Running": {
                "base": "Natural running gait, arms pump opposite legs, breathing deepens",
                "Happy / Excited / Joyful": "Light on feet, slight smile, energetic arm swing, hair bounces wildly",
                "Serious / Focused / Intense": "Determined expression, rhythmic breathing, efficient stride, eyes locked on destination",
                "Nervous / Anxious / Uncomfortable": "Glances behind, uneven stride, tense shoulders, rapid breathing visible"
            },
            "Talking to Camera": {
                "base": "Eyes make camera contact, mouth articulates clearly, natural blinks",
                "Authentic / Natural": "Filler words present, slight hesitations, hand gestures emerge organically, eyes break contact naturally",
                "Professional / Confident": "Direct gaze, clear articulation, controlled hand gestures, minimal ums/ahs",
                "Emotional / Touching / Vulnerable": "Voice wavers slightly, eyes glisten, hand touches heart or face, vulnerable pauses"
            }
        }
        
        motion_data = motion_cues.get(motion_type, {})
        base_cue = motion_data.get("base", "")
        emotion_cue = motion_data.get(emotion_name, "")
        
        if emotion_cue:
            return f"{base_cue}\n\nEMOTIONAL LAYERING: {emotion_cue}"
        return base_cue
