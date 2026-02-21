import base64
import json
from typing import Any, Dict, List

from openai import OpenAI
from emotion_engine import EmotionEngine


class OpenAIService:
    """
    Enhanced Streamlit-ready OpenAI service with Emotion Engine.
    Features: Cloner, PerfectCloner, Multi-Angle, Wardrobe, DrMotion (Enhanced), Poser, Captions, Prompter.
    NEW: Integrated EmotionEngine for ultra-realistic human behavior simulation.
    """

    def __init__(self, api_key: str, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    # -------------------- DR. MOTION (VIDEO) - ENHANCED --------------------

    def drmotion_generate(self, uploaded_file, model_choice: str, motion_type: str,
                         emotion: str, master_dna: str, intensity: str = "Medium") -> Dict[str, Any]:
        """
        Enhanced single-clip generation with deep Emotion Engine integration.

        Args:
            uploaded_file: Image file
            model_choice: Video AI model (Kling, Veo, Luma, Runway)
            motion_type: Type of motion (Walking, Turning, etc.)
            emotion: Emotion from EmotionEngine database
            master_dna: Character identity description
            intensity: Emotion intensity (Subtle, Medium, Strong)
        """
        data_url = self._filelike_to_data_url(uploaded_file)

        # Model-specific guidance
        model_guides = {
            "Kling 1.5": "Kling excels at: High detail textures, smooth camera movements, realistic cloth physics. Use descriptors: '8k quality', 'cinematic camera orbit', 'photorealistic skin texture', 'dynamic lighting shifts'.",
            "Veo 2 / Sora": "Veo/Sora masters: Physics accuracy, fluid dynamics, complex lighting. Use descriptors: 'physically accurate motion', 'realistic gravity', 'natural light interaction', 'consistent world physics'.",
            "Luma Dream Machine": "Luma strengths: Keyframe precision, style consistency, smooth transitions. Use descriptors: 'cinematic movement', 'start state to end state', 'dramatic camera work', 'keyframe animation'.",
            "Runway Gen-3 Alpha": "Runway Gen-3 best for: Structure preservation, facial consistency, controlled motion. Use descriptors: 'maintain facial features', 'smooth natural motion', 'structural coherence', 'speed control'.",
            "Minimax": "Minimax optimized for: Chinese features, fast generation, emotional expressions. Use descriptors: 'expressive faces', 'cultural authenticity', 'rapid motion', 'clear emotions'.",
            "Haiper": "Haiper strong at: Quick iterations, style variety, artistic motion. Use descriptors: 'creative movement', 'artistic interpretation', 'varied styles', 'expressive motion'."
        }
        guide = model_guides.get(model_choice, "Focus on realistic motion, natural physics, and authentic emotions.")

        # Get emotion breakdown from EmotionEngine
        emotion_prompt_section = EmotionEngine.build_emotion_prompt_section(emotion, intensity)
        motion_specific_cues = EmotionEngine.get_motion_specific_cues(motion_type, emotion)

        instructions = (
            f"You are Dr. Motion, an AI Video Prompt Specialist for {model_choice}.\n\n"
            f"MODEL OPTIMIZATION:\n{guide}\n\n"
            "YOUR MISSION:\n"
            "Create a video generation prompt that produces ULTRA-REALISTIC human motion and emotion.\n"
            "The AI model must see a REAL PERSON, not a robotic avatar.\n\n"
            "CRITICAL REQUIREMENTS:\n"
            "1. EMOTION AUTHENTICITY:\n"
            "   - Use the provided Emotion Database breakdown\n"
            "   - Describe SPECIFIC micro-expressions (not just 'looks happy')\n"
            "   - Include EXACT facial muscle activations (e.g., 'orbicularis oculi contracts creating crow's feet')\n"
            "   - Map emotion to BODY LANGUAGE (shoulders, hands, posture, weight distribution)\n"
            "   - Describe TEMPORAL PROGRESSION (how emotion evolves over 8 seconds)\n\n"
            "2. PHYSICS REALISM:\n"
            "   - Hair physics: How hair moves with motion (gravity, momentum, wind resistance)\n"
            "   - Cloth simulation: Fabric folding, stretching, natural draping\n"
            "   - Skin subsurface scattering: Light penetrating skin\n"
            "   - Weight transfer: How body weight shifts realistically\n"
            "   - Momentum and inertia: Natural movement follow-through\n\n"
            "3. HUMAN IMPERFECTIONS:\n"
            "   - Include asymmetries (one eye slightly different)\n"
            "   - Natural micro-movements (breathing, blinking, micro-adjustments)\n"
            "   - Timing variations (not perfectly mechanical)\n"
            "   - Environmental reactions (squinting in light, hair blown by wind)\n\n"
            "4. LIGHTING & CINEMATOGRAPHY:\n"
            "   - Describe light source changes during motion\n"
            "   - Shadow dynamics\n"
            "   - Camera movement that enhances emotion\n"
            "   - Depth of field adjustments\n\n"
            "OUTPUT JSON STRUCTURE:\n"
            "{\n"
            "  'character_analysis': 'Brief analysis of the input image',\n"
            "  'emotion_breakdown': 'How the specific emotion manifests in this motion',\n"
            "  'physics_notes': 'Key physics simulations needed',\n"
            "  'micro_expressions': 'List of 3-5 specific facial details',\n"
            "  'body_language_cues': 'List of 3-5 body movement details',\n"
            "  'temporal_flow': {\n"
            "    'seconds_0_2': 'What happens in first 2 seconds',\n"
            "    'seconds_3_5': 'Middle progression',\n"
            "    'seconds_6_8': 'How it concludes'\n"
            "  },\n"
            "  'final_video_prompt': 'The complete, detailed prompt for the AI video model'\n"
            "}\n"
        )

        user_text = (
            f"MASTER CHARACTER DNA:\n{master_dna}\n\n"
            f"VIDEO MODEL: {model_choice}\n"
            f"MOTION TYPE: {motion_type}\n"
            f"EMOTION INTENSITY: {intensity}\n\n"
            f"--- EMOTION DATABASE BREAKDOWN ---\n"
            f"{emotion_prompt_section}\n\n"
            f"--- MOTION-SPECIFIC ACTING CUES ---\n"
            f"{motion_specific_cues}\n\n"
            "TASK: Synthesize ALL the above information into a professional video prompt.\n"
            "The prompt should be SPECIFIC, DETAILED, and ACTIONABLE for the AI model.\n"
            "Make the human feel ALIVE and REAL.\n"
            "Return JSON as specified above."
        )

        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [
                {"type": "text", "text": user_text},
                {"type": "image_url", "image_url": {"url": data_url}}
            ]},
        ]
        return self._call_chat_json(messages, max_tokens=2500)

    def drmotion_product_review(self, uploaded_file, product_info: str, language: str,
                               emotion: str, master_dna: str, intensity: str = "Medium") -> Dict[str, Any]:
        """
        Enhanced 2-part product review sequence with emotion engine integration.
        Generates realistic script + visual prompts with authentic human behavior.
        """
        data_url = self._filelike_to_data_url(uploaded_file)

        # Get emotion details
        emotion_prompt_section = EmotionEngine.build_emotion_prompt_section(emotion, intensity)

        instructions = (
            "You are a Director of AI-Generated Product Reviews.\n"
            "Create a cohesive 16-second product review split into TWO 8-second clips.\n\n"
            "CRITICAL: This must feel like REAL user-generated content, not a corporate ad.\n\n"
            "REQUIREMENTS:\n"
            "1. SCRIPT AUTHENTICITY:\n"
            f"   - Language: {language}\n"
            f"   - Tone: {emotion}\n"
            "   - Must include natural speech patterns:\n"
            "     * Filler words: 'like', 'um', 'actually', 'you know' (for casual tones)\n"
            "     * Contractions: 'it's', 'I'm', 'you're' (not 'it is')\n"
            "     * Conversational flow: NOT scripted-sounding\n"
            "     * Emotional authenticity: Match the vocal qualities from emotion database\n\n"
            "2. VISUAL STORYTELLING:\n"
            "   CLIP A (0-8s): THE HOOK\n"
            "   - Focus on FACE and ACTING\n"
            "   - Establish emotion immediately\n"
            "   - Direct eye contact with camera (talking to viewer)\n"
            "   - Include specific micro-expressions from emotion database\n"
            "   - Show the product BRIEFLY in hand or frame\n\n"
            "   CLIP B (8-16s): THE DEMO\n"
            "   - Shift focus to PRODUCT usage\n"
            "   - Continue same emotion intensity\n"
            "   - Show hands interacting with product\n"
            "   - Maintain lighting/aesthetic consistency from Clip A\n"
            "   - Include result/benefit shots\n\n"
            "3. CONTINUITY:\n"
            "   - Lighting must match between clips\n"
            "   - Clothing/styling identical\n"
            "   - Background consistent\n"
            "   - Emotional arc flows naturally\n\n"
            "4. EMOTION MAPPING:\n"
            "   Use the provided emotion breakdown to inform:\n"
            "   - Facial expressions in Clip A\n"
            "   - Body language throughout\n"
            "   - Energy level\n"
            "   - Vocal delivery style\n\n"
            "OUTPUT JSON:\n"
            "{\n"
            "  'script_analysis': 'Brief note on script tone and language',\n"
            "  'script': 'The actual spoken dialogue (natural, authentic)',\n"
            "  'clip_1_visual_prompt': 'Detailed prompt for Clip A (face/acting)',\n"
            "  'clip_1_acting_notes': 'Specific micro-expressions and cues',\n"
            "  'clip_2_visual_prompt': 'Detailed prompt for Clip B (product demo)',\n"
            "  'clip_2_continuity': 'How this matches Clip A',\n"
            "  'director_notes': 'Overall guidance for consistency'\n"
            "}\n"
        )

        user_text = (
            f"MASTER CHARACTER DNA:\n{master_dna}\n\n"
            f"PRODUCT DETAILS: {product_info}\n"
            f"SCRIPT LANGUAGE: {language}\n"
            f"EMOTIONAL INTENSITY: {intensity}\n\n"
            f"--- EMOTION DATABASE BREAKDOWN ---\n"
            f"{emotion_prompt_section}\n\n"
            "TASK: Create an authentic, engaging product review video plan.\n"
            "The viewer should feel like they're watching a REAL PERSON, not an influencer reading a script.\n"
            "Return JSON as specified."
        )

        messages = [
            {"role": "system", "content": instructions},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            },
        ]
        return self._call_chat_json(messages, max_tokens=3000)

    # -------------------- DIGITAL WARDROBE --------------------
    def wardrobe_fuse_filelike(self, uploaded_file, master_dna: str) -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        instructions = (
            "Analyze outfit image (fabric, cut, texture, color). IGNORE the person/body.\n"
            "Fuse this outfit description with the user's locked 'Master Face DNA'.\n"
            "Generate a final image prompt.\n"
            "Return JSON: {outfit_description, fused_prompt}."
        )
        user_text = f"MASTER DNA:\n{master_dna}\n\nTask: Wear this outfit.\nOutput JSON."
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [{"type": "text", "text": user_text}, {"type": "image_url", "image_url": {"url": data_url}}]},
        ]
        return self._call_chat_json(messages, max_tokens=1500)

    # -------------------- MULTI-ANGLE GRID PLANNER --------------------
    def multi_angle_planner_filelike(self, uploaded_file, master_dna: str) -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        safe_dna_snippet = (master_dna or "")[:200]

        instructions = (
            "You are an expert Virtual Photography Director.\n"
            "Task: Design a 'Multi-Angle Character Sheet' (4x5 grid, 20 slots).\n"
            "1. Create a 'grid_prompt' for the image generator. CRITICAL: You MUST explicitly list the 20 angles in the prompt text (e.g., 'Slot 1: Front, Slot 2: Side...').\n"
            "   ALSO: Instruct the generator to 'Burn visible numbers 1-20 into the corner of each grid slot'.\n"
            "2. Return a structured list of these 20 angles.\n"
            "Return JSON keys: 'grid_prompt' (string), 'angles' (list of objects with id (1-20), name, description)."
        )

        user_text = (
            f"Character Context: {safe_dna_snippet}\n"
            "Task: Plan 20 distinct camera angles (Low, High, Dutch, Profile, Back, etc.).\n"
            "Output JSON."
        )

        messages = [
            {"role": "system", "content": instructions},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            },
        ]
        return self._call_chat_json(messages, max_tokens=2500)

    def build_physics_prompt(self, master_dna: str, angle_data: Dict[str, Any]) -> str:
        angle_name = angle_data.get("name", "Unknown Angle")
        angle_desc = angle_data.get("description", "")
        physics_block = (
            "LIGHTING & PHYSICS (PBR):\n"
            "- Physically Based Rendering (PBR), Raytraced GI.\n"
            "- Subsurface Scattering (SSS) on skin.\n"
            "- Fresnel reflections, Volumetric lighting.\n"
            "- Realistic cast shadows, Ambient Occlusion."
        )
        full_prompt = (
            f"{master_dna.strip()}\n\n"
            f"ANGLE: {angle_name}\nDESC: {angle_desc}\n\n"
            f"{physics_block}\n\n"
            "NEGATIVE: flat, baked lighting, cartoon, bad anatomy, blurry."
        )
        return full_prompt

    # -------------------- CAPTIONS --------------------
    def captions_generate_filelike(self, uploaded_file, style: str = "Engaging", language: str = "English") -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        instructions = "Analyze image. Write ONE Instagram caption with emojis + EXACTLY 4 hashtags. Return JSON: {caption, hashtags}."
        user_content = f"Style: {style}\nLanguage: {language}"
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [{"type": "text", "text": user_content}, {"type": "image_url", "image_url": {"url": data_url}}]},
        ]
        data = self._call_chat_json(messages, max_tokens=600)
        hashtags = data.get("hashtags") or []
        if isinstance(hashtags, list): hashtags = [str(h) for h in hashtags[:4]]
        return {"caption": data.get("caption", ""), "hashtags": hashtags}

    # -------------------- CLONER --------------------
    def cloner_analyze_filelike(self, uploaded_file, master_dna: str,
                                use_custom_hairstyle: bool = False,
                                custom_hairstyle: str = "",
                                use_custom_attire: bool = False,
                                custom_attire: str = "",
                                use_custom_makeup: bool = False,
                                custom_makeup: str = "") -> Dict[str, Any]:
        """
        SCENE TRANSFER CLONER - Extract scene from reference, apply to YOUR AI model.

        User's Workflow:
        1. Upload reference image (different person)
        2. AI extracts: pose, lighting, camera angle, background
        3. Creates prompt with YOUR AI model in that scene
        4. Optional: Override hairstyle, attire, makeup
        5. Includes body structure (36D, 34)
        6. Ready for Ultra Realism

        Args:
            uploaded_file: Reference image (scene to extract)
            master_dna: YOUR AI model's face/identity
            use_custom_hairstyle: If True, use custom_hairstyle
            custom_hairstyle: Hairstyle description to use
            use_custom_attire: If True, use custom_attire
            custom_attire: Attire description to use
            use_custom_makeup: If True, use custom_makeup
            custom_makeup: Makeup description to use
        """
        data_url = self._filelike_to_data_url(uploaded_file)

        # Build override instructions
        override_instructions = []
        if use_custom_hairstyle and custom_hairstyle:
            override_instructions.append(f"HAIRSTYLE: Use '{custom_hairstyle}' instead of reference hairstyle")
        else:
            override_instructions.append("HAIRSTYLE: Extract from reference image")

        if use_custom_attire and custom_attire:
            override_instructions.append(f"ATTIRE: Use '{custom_attire}' instead of reference attire")
        else:
            override_instructions.append("ATTIRE: Extract from reference image")

        if use_custom_makeup and custom_makeup:
            override_instructions.append(f"MAKEUP: Use '{custom_makeup}' instead of reference makeup")
        else:
            override_instructions.append("MAKEUP: Extract from reference image")

        override_text = "\n".join(override_instructions)

        instructions = f"""SCENE TRANSFER AI - Extract scene, NOT person!

    CRITICAL UNDERSTANDING:
    The person in the reference image is NOT who we're creating. We only want the SCENE (pose, lighting, camera, background). We'll place a DIFFERENT person (from Master DNA) into this scene.

    DO NOT EXTRACT OR DESCRIBE:
    ❌ Reference person's face shape
    ❌ Reference person's eye color
    ❌ Reference person's skin tone
    ❌ Reference person's nose/lips
    ❌ Reference person's body measurements
    ❌ ANY identity features of reference person

    ONLY EXTRACT THESE FROM REFERENCE:

    1. EXACT POSE & BODY POSITION:
       - Body orientation (facing camera, 3/4 turn, profile, back)
       - Standing/sitting/lying position
       - Head tilt (straight, tilted left/right, up/down)
       - Shoulder position
       - Arm positions (both arms separately: raised, lowered, bent, straight, crossed)
       - Hand positions and gestures
       - Leg positions if visible
       - Weight distribution
       - Overall posture (confident, relaxed, elegant, dynamic)

    2. FACIAL EXPRESSION & GAZE:
       - Expression (smiling, serious, neutral, playful, mysterious)
       - Smile type if smiling (closed, open, slight, broad)
       - Eye gaze direction (at camera, away, down, up, to side)
       - Face angle (straight, slight turn left/right)

    3. LIGHTING SETUP (DETAILED):
       - Main light position (front, left, right, top, back)
       - Light quality (soft/diffused, hard/direct)
       - Light type (natural window, studio softbox, outdoor sun, artificial)
       - Shadow direction and softness
       - Highlight areas on face/body
       - Fill light (yes/no, from where)
       - Rim/back light (yes/no)
       - Overall lighting mood (bright, moody, dramatic, natural)
       - Light color temperature (warm/golden, cool/blue, neutral)

    4. CAMERA DETAILS:
       - Camera angle (eye level, high angle looking down, low angle looking up)
       - Shot type (extreme close-up face, close-up, medium shot, full body, wide)
       - Camera distance from subject
       - Focal length (estimate: wide 24-35mm, standard 50mm, portrait 85mm, telephoto 100mm+)
       - Depth of field (very shallow/f1.4, shallow/f2.8, medium/f5.6, deep/f8+)
       - Background blur amount
       - Framing composition (centered, rule of thirds, off-center)

    5. BACKGROUND & ENVIRONMENT:
       - Background type (studio, outdoor, indoor, urban, nature)
       - Background color/tones
       - Background elements visible
       - Background blur/sharpness
       - Environmental mood

    6. PHOTO STYLE:
       - Overall style (portrait, fashion, editorial, casual, professional)
       - Color grading (natural, warm tones, cool tones, desaturated, vibrant)
       - Mood (cheerful, serious, dramatic, intimate, energetic)
       - Professional quality indicators

    7. HAIRSTYLE:
    {override_instructions[0]}

    8. ATTIRE/CLOTHING:
    {override_instructions[1]}

    9. MAKEUP:
    {override_instructions[2]}

    BODY STRUCTURE FOR PROMPT:
    Include tasteful feminine body: 36D bust, 34 inch bottoms, naturally proportioned, elegant figure. Describe how pose/attire shows this naturally.

    REALISM KEYWORDS (MUST INCLUDE ALL):
    - "natural skin texture with visible pores and fine lines"
    - "realistic lighting with natural shadows and highlights"
    - "photorealistic, looks like real person"
    - "8k quality, high detail, professional photography"
    - "shot on Sony A7IV with 85mm f/1.4 lens"
    - "natural depth of field with realistic bokeh"
    - "realistic subsurface scattering on skin"
    - "authentic human features with natural imperfections"
    - "individual hair strands visible with natural flow"
    - "professional color grading, natural tones"
    - "realistic anatomy and proportions"

    OUTPUT JSON:
    {{
      "full_prompt": "Complete prompt with: [1] Master DNA identity/face, [2] Body structure (36D, 34), [3] Exact pose from reference, [4] Exact lighting from reference, [5] Exact camera setup, [6] Hairstyle (custom or extracted), [7] Attire (custom or extracted), [8] Makeup (custom or extracted), [9] Background from reference, [10] ALL realism keywords. MINIMUM 500 WORDS. Ultra-detailed.",
      "negative_prompt": "different person, wrong identity, wrong face, smooth plastic skin, airbrushed, perfect skin, unrealistic, CGI, 3D render, cartoon, illustration, wrong pose, different lighting, different angle"
    }}

    PROMPT STRUCTURE:
    1. Start with Master DNA identity (YOUR AI model's face description)
    2. Add body structure (36D, 34, tasteful, natural)
    3. Describe exact pose from reference (ultra-detailed)
    4. Describe exact lighting setup
    5. Describe exact camera angle/framing
    6. Add hairstyle (custom or extracted)
    7. Add attire details (custom or extracted)
    8. Add makeup (custom or extracted)
    9. Add background/environment
    10. Add ALL realism keywords
    11. End with technical specs

    Make it 500+ words, ultra-detailed!"""

        user_text = f"""YOUR AI MODEL (Use this identity/face):
    {master_dna}

    BODY STRUCTURE TO USE:
    Tasteful feminine body with 36D bust, 34 inch bottom measurements, naturally proportioned, elegant figure, realistic anatomy.

    REFERENCE IMAGE (Extract SCENE only):
    Analyze this image and extract ONLY:
    - Exact pose and body position
    - Exact lighting setup
    - Exact camera angle and framing
    - Background/environment
    - Hairstyle (if not overridden)
    - Attire (if not overridden)
    - Makeup (if not overridden)

    OVERRIDES:
    {override_text}

    DO NOT extract or describe the reference person's facial features, skin tone, or identity. We're placing YOUR AI model (from Master DNA) into this scene.

    Create a 500+ word ultra-detailed prompt that puts YOUR AI model in this exact scene with all realism keywords."""

        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [
                {"type": "text", "text": user_text},
                {"type": "image_url", "image_url": {"url": data_url}}
            ]},
        ]

        return self._call_chat_json(messages, max_tokens=2500)


    def perfectcloner_analyze_filelike(self, uploaded_file, master_dna: str, identity_lock: bool = True) -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        instructions = "Analyze details (camera, lighting). Return JSON: recreation_prompt, negative_prompt, notes."
        user_text = f"Identity Lock: {identity_lock}\nDNA: {master_dna}\nAnalyze."
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [{"type": "text", "text": user_text}, {"type": "image_url", "image_url": {"url": data_url}}]},
        ]
        return self._call_chat_json(messages, max_tokens=1500)

    # -------------------- PROMPTER --------------------
    def prompter_build(self, master_dna: str, fields: Dict[str, str]) -> str:
        parts = [
            master_dna.strip(), "", "PROMPT:",
            f"Pose: {fields.get('pose', '')}",
            f"Attire: {fields.get('attire', '')}",
            f"Camera: {fields.get('camera_angle', '')} | {fields.get('camera_lens', '')}",
            f"Lighting: {fields.get('lighting', '')}",
            f"Background: {fields.get('background', '')}",
            f"Jewellery: {fields.get('jewellery', '')}", "",
            "PHYSICS & REALISM:",
            "- Physically Based Rendering (PBR), realistic shadows, natural skin texture",
            "- Shot on iPhone 17, f/16 look", "",
            "Negative prompt: blurry, bad anatomy, text, watermark"
        ]
        return "\n".join(parts)

    # -------------------- POSER --------------------
    def poser_variations_filelike(self, uploaded_file, master_dna: str, pose_style: str) -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        instructions = "Create 5 pose variations. Return JSON: {prompts: [{pose_name, pose_description, facial_expression}], scene_lock: string}."
        user_text = f"Style: {pose_style}\nReference DNA: {master_dna}\nAnalyze image."
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [{"type": "text", "text": user_text}, {"type": "image_url", "image_url": {"url": data_url}}]}
        ]
        return self._call_chat_json(messages)

    # -------------------- HELPERS --------------------
    def _filelike_to_data_url(self, uploaded_file) -> str:
        content = uploaded_file.getvalue()
        mime = getattr(uploaded_file, "type", "image/jpeg") or "image/jpeg"
        b64 = base64.b64encode(content).decode("utf-8")
        return f"data:{mime};base64,{b64}"

    def _sanitize_json_text(self, s: str) -> str:
        if not s: return s
        if s.startswith("```json"): s = s[7:]
        if s.startswith("```"): s = s[3:]
        if s.endswith("```"): s = s[:-3]
        return s.strip()

    def _call_chat_json(self, messages: list, max_tokens: int = 1000) -> Dict[str, Any]:
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                response_format={"type": "json_object"},
            )
            return json.loads(self._sanitize_json_text(resp.choices[0].message.content))
        except Exception as e:
            print(f"❌ OPENAI ERROR: {e}")
            if hasattr(e, 'response'):
                print(f"Response: {e.response}")
            return {}
