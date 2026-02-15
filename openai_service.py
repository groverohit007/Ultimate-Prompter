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
    def cloner_analyze_filelike(self, uploaded_file, master_dna: str) -> Dict[str, Any]:
        data_url = self._filelike_to_data_url(uploaded_file)
        instructions = (
            "Analyze the image's pose, lighting, camera angle, and background style.\n"
            "Do NOT analyze body measurements or specific biometrics.\n"
            "Return valid JSON with keys: full_prompt, negative_prompt.\n"
            "Construct the 'full_prompt' by combining the provided MASTER DNA with your analysis of the scene."
        )
        user_text = f"MASTER DNA:\n{master_dna}\n\nAnalyze the scene/lighting/pose of this image and merge it with the DNA."
        messages = [
            {"role": "system", "content": instructions},
            {"role": "user", "content": [{"type": "text", "text": user_text}, {"type": "image_url", "image_url": {"url": data_url}}]},
        ]
        return self._call_chat_json(messages, max_tokens=1000)

    # -------------------- PERFECT CLONER --------------------
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
