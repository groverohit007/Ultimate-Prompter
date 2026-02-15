"""
Audio Emotion Mapper
====================
Maps emotions to vocal characteristics for TTS/voiceover generation
"""

from typing import Dict, Any, List


class AudioEmotionMapper:
    """Maps emotions to detailed vocal/audio characteristics"""
    
    AUDIO_DATABASE = {
        "Authentic / Natural": {
            "pace_wpm": "120-140 words per minute",
            "pitch_variation": "±10% from baseline (natural fluctuation)",
            "emphasis_pattern": "Organic emphasis on key words, not scripted",
            "pause_strategy": {
                "short_pauses": "0.3-0.5s between phrases (natural breath)",
                "medium_pauses": "0.8-1.2s for thought transitions",
                "filler_sounds": "Um (0.2s), uh (0.15s), like (natural placement)"
            },
            "breath_sounds": [
                "Audible inhale before long sentences",
                "Soft exhale at phrase ends",
                "Breath catch when emotional"
            ],
            "vocal_quality": "Conversational, slightly informal, warm tone",
            "articulation": "Clear but not overly crisp - natural slurring of common words",
            "inflection_notes": [
                "Upward inflection on questions",
                "Downward at statement ends",
                "Slight upward on lists (non-final items)"
            ],
            "energy_level": "Medium, steady - like talking to a friend",
            "emotional_markers": [
                "Voice softens on intimate/personal topics",
                "Slight laugh in voice when amused",
                "Micro-hesitations before vulnerable statements"
            ],
            "tts_instructions": "Use 'conversational' preset. Add natural hesitations. Vary pacing organically.",
            "elevenlabs_settings": "Stability: 0.6, Clarity: 0.7, Style: 0.3"
        },
        
        "Happy / Excited / Joyful": {
            "pace_wpm": "140-180 words per minute (energized)",
            "pitch_variation": "+15-25% above baseline (excited elevation)",
            "emphasis_pattern": "Strong emphasis on positive words, animated delivery",
            "pause_strategy": {
                "short_pauses": "0.2-0.3s (quick, energetic)",
                "medium_pauses": "0.5-0.7s (minimal - excitement reduces pauses)",
                "filler_sounds": "Ooh! Wow! Yes! (exclamations)"
            },
            "breath_sounds": [
                "Quick, shallow breaths (excitement)",
                "Gasps of delight",
                "Breathless laughter"
            ],
            "vocal_quality": "Bright, resonant, higher register",
            "articulation": "Very clear, crisp - energy sharpens consonants",
            "inflection_notes": [
                "Upward sweeps on exciting words",
                "Lots of melodic variation",
                "Smile audible in voice"
            ],
            "energy_level": "High - 80-90% intensity throughout",
            "emotional_markers": [
                "Voice cracks from joy",
                "Laughter interrupts sentences",
                "Volume increases +20-30%",
                "Words tumble out faster"
            ],
            "tts_instructions": "Maximum energy. Add laughs. Speed up 1.2x. Brighten tone.",
            "elevenlabs_settings": "Stability: 0.4, Clarity: 0.8, Style: 0.6"
        },
        
        "Professional / Confident": {
            "pace_wpm": "100-120 words per minute (measured, deliberate)",
            "pitch_variation": "-5 to +5% (minimal, controlled)",
            "emphasis_pattern": "Strategic emphasis on key points only",
            "pause_strategy": {
                "short_pauses": "0.4-0.6s (deliberate)",
                "medium_pauses": "1.0-1.5s (for gravitas)",
                "filler_sounds": "None - eliminate ums/ahs"
            },
            "breath_sounds": [
                "Quiet, controlled breathing",
                "Deep breath before important statements",
                "No audible breath catch"
            ],
            "vocal_quality": "Low, resonant, authoritative",
            "articulation": "Crisp, precise, every syllable clear",
            "inflection_notes": [
                "Downward inflection (statements of fact)",
                "Minimal melodic variation",
                "Flat, steady on neutral info"
            ],
            "energy_level": "Medium-high - contained power",
            "emotional_markers": [
                "Voice deepens on key points",
                "Slight smile on positive outcomes (subtle)",
                "No emotional wavers"
            ],
            "tts_instructions": "Deep voice preset. Slow pace. Remove all hesitations. Authoritative.",
            "elevenlabs_settings": "Stability: 0.9, Clarity: 0.9, Style: 0.1"
        },
        
        "Funny / Witty / Goofy": {
            "pace_wpm": "Variable - 80-160 (comedic timing)",
            "pitch_variation": "±30-40% (wild swings for effect)",
            "emphasis_pattern": "Exaggerated emphasis, unexpected stress patterns",
            "pause_strategy": {
                "short_pauses": "Varies wildly",
                "medium_pauses": "Strategic pause before punchline (1-2s)",
                "filler_sounds": "Pfft, heh, mmm (comedic sounds)"
            },
            "breath_sounds": [
                "Snorts of laughter",
                "Exaggerated sighs",
                "Comedic gasps"
            ],
            "vocal_quality": "Playful, character voices, varying register",
            "articulation": "Varies - from crisp to deliberately sloppy",
            "inflection_notes": [
                "Exaggerated question inflections",
                "Sarcastic flat delivery",
                "Melodramatic rises and falls"
            ],
            "energy_level": "Variable - from deadpan to manic",
            "emotional_markers": [
                "Voice breaks into giggles",
                "Impressions/character voices",
                "Deliberate mispronunciations",
                "Comic timing pauses"
            ],
            "tts_instructions": "Vary wildly. Add sound effects. Exaggerate. Comic timing critical.",
            "elevenlabs_settings": "Stability: 0.3, Clarity: 0.6, Style: 0.8"
        },
        
        "Emotional / Touching / Vulnerable": {
            "pace_wpm": "90-110 words per minute (slow, processing)",
            "pitch_variation": "+10-15% (tension raises pitch slightly)",
            "emphasis_pattern": "Gentle emphasis, words weighted with meaning",
            "pause_strategy": {
                "short_pauses": "0.5-0.8s (processing emotion)",
                "medium_pauses": "1.5-3.0s (gathering composure)",
                "filler_sounds": "Soft sighs, breath catches"
            },
            "breath_sounds": [
                "Shakier breathing",
                "Catch in throat",
                "Deep steadying breath"
            ],
            "vocal_quality": "Softer, more fragile, slight tremor",
            "articulation": "Less crisp - emotion softens edges",
            "inflection_notes": [
                "Wavering on emotional words",
                "Voice drops on sad moments",
                "Slight upturn seeking comfort"
            ],
            "energy_level": "Low-medium - subdued by emotion",
            "emotional_markers": [
                "Voice cracks/breaks",
                "Tearfulness audible (thick voice)",
                "Volume drops -20-30%",
                "Words slow near breaking point"
            ],
            "tts_instructions": "Soft, vulnerable. Add wavers. Slow on emotional words. Breath catches.",
            "elevenlabs_settings": "Stability: 0.5, Clarity: 0.5, Style: 0.4"
        },
        
        "Serious / Focused / Intense": {
            "pace_wpm": "90-110 words per minute (deliberate)",
            "pitch_variation": "-10% (lower, more gravitas)",
            "emphasis_pattern": "Laser-focused emphasis on critical words",
            "pause_strategy": {
                "short_pauses": "0.3-0.5s (controlled)",
                "medium_pauses": "0.8-1.0s (no wasted time)",
                "filler_sounds": "None - absolute focus"
            },
            "breath_sounds": [
                "Controlled, deep breathing",
                "Nose breathing (quiet focus)",
                "No emotional breath"
            ],
            "vocal_quality": "Low, intense, unwavering",
            "articulation": "Extremely clear and precise",
            "inflection_notes": [
                "Flat, factual delivery",
                "Minimal melodic variation",
                "Firmness on key points"
            ],
            "energy_level": "High intensity, low volume - coiled power",
            "emotional_markers": [
                "Voice hardens on important points",
                "No lightness or playfulness",
                "Unbreakable focus audible"
            ],
            "tts_instructions": "Deep, serious tone. Minimal variation. Controlled power.",
            "elevenlabs_settings": "Stability: 0.9, Clarity: 0.95, Style: 0.2"
        },
        
        "Nervous / Anxious / Uncomfortable": {
            "pace_wpm": "130-160 words per minute (rushed, anxious)",
            "pitch_variation": "+20-30% (tension raises pitch)",
            "emphasis_pattern": "Uneven, words tumble out",
            "pause_strategy": {
                "short_pauses": "0.1-0.2s (minimal - rushing)",
                "medium_pauses": "Awkward 2-3s pauses (frozen)",
                "filler_sounds": "Um, uh, like, you know (frequent)"
            },
            "breath_sounds": [
                "Rapid, shallow breathing (audible)",
                "Nervous swallow (click in throat)",
                "Shaky exhales"
            ],
            "vocal_quality": "Higher, thinner, tremulous",
            "articulation": "Stumbles, repeated words, corrections",
            "inflection_notes": [
                "Upward inflection (uncertainty)",
                "Voice cracks from tension",
                "Squeaky on stressed words"
            ],
            "energy_level": "High but scattered - nervous energy",
            "emotional_markers": [
                "Voice shakes/quivers",
                "False starts: 'I- I mean...'",
                "Apologetic tone",
                "Words rush together"
            ],
            "tts_instructions": "Higher pitch. Add stutters. Rushed pacing. Lots of filler words.",
            "elevenlabs_settings": "Stability: 0.3, Clarity: 0.5, Style: 0.5"
        },
        
        "Flirty / Playful / Charming": {
            "pace_wpm": "110-130 words per minute (seductive pacing)",
            "pitch_variation": "±15% (musical, melodic)",
            "emphasis_pattern": "Playful stress, teasing inflection",
            "pause_strategy": {
                "short_pauses": "0.4-0.6s (seductive timing)",
                "medium_pauses": "1.0-1.5s (building tension)",
                "filler_sounds": "Soft giggles, hmm, mmm"
            },
            "breath_sounds": [
                "Soft, breathy quality",
                "Gentle laughs",
                "Knowing sighs"
            ],
            "vocal_quality": "Softer, breathier, warmer tone",
            "articulation": "Slightly softened - seductive",
            "inflection_notes": [
                "Upward lilt (playful)",
                "Melodic, sing-song quality",
                "Teasing rises"
            ],
            "energy_level": "Medium - relaxed confidence",
            "emotional_markers": [
                "Smile in voice",
                "Playful laugh mid-sentence",
                "Voice drops lower (intimate)",
                "Breathy on key words"
            ],
            "tts_instructions": "Soft, warm tone. Breathy quality. Playful inflections. Smile audible.",
            "elevenlabs_settings": "Stability: 0.6, Clarity: 0.6, Style: 0.5"
        }
    }
    
    @classmethod
    def get_audio_mapping(cls, emotion_name: str) -> Dict[str, Any]:
        """Get audio characteristics for emotion"""
        return cls.AUDIO_DATABASE.get(emotion_name, cls.AUDIO_DATABASE["Authentic / Natural"])
    
    @classmethod
    def build_audio_prompt(cls, emotion_name: str, script_text: str = "") -> str:
        """Build complete audio generation prompt"""
        audio_data = cls.get_audio_mapping(emotion_name)
        
        prompt_parts = [
            f"AUDIO/VOICE CHARACTERISTICS FOR: {emotion_name.upper()}",
            "",
            f"PACING: {audio_data['pace_wpm']}",
            f"PITCH VARIATION: {audio_data['pitch_variation']}",
            f"VOCAL QUALITY: {audio_data['vocal_quality']}",
            f"ENERGY LEVEL: {audio_data['energy_level']}",
            "",
            "PAUSE STRATEGY:",
        ]
        
        for pause_type, timing in audio_data['pause_strategy'].items():
            prompt_parts.append(f"  • {pause_type}: {timing}")
        
        prompt_parts.extend([
            "",
            "BREATH SOUNDS:"
        ])
        
        for breath in audio_data['breath_sounds']:
            prompt_parts.append(f"  • {breath}")
        
        prompt_parts.extend([
            "",
            "EMOTIONAL MARKERS:"
        ])
        
        for marker in audio_data['emotional_markers']:
            prompt_parts.append(f"  • {marker}")
        
        prompt_parts.extend([
            "",
            "ARTICULATION:",
            f"  {audio_data['articulation']}",
            "",
            "INFLECTION NOTES:"
        ])
        
        for note in audio_data['inflection_notes']:
            prompt_parts.append(f"  • {note}")
        
        prompt_parts.extend([
            "",
            "TTS INSTRUCTIONS:",
            f"  {audio_data['tts_instructions']}",
            "",
            "ELEVENLABS OPTIMAL SETTINGS:",
            f"  {audio_data['elevenlabs_settings']}",
        ])
        
        if script_text:
            prompt_parts.extend([
                "",
                "SCRIPT TO VOCALIZE:",
                f"  {script_text}"
            ])
        
        return "\n".join(prompt_parts)
    
    @classmethod
    def get_timing_markers(cls, emotion_name: str, script_text: str) -> List[Dict[str, Any]]:
        """
        Generate timing markers for script based on emotion.
        Returns list of {word_index, timing_note}
        """
        audio_data = cls.get_audio_mapping(emotion_name)
        
        # This is a simplified version - could be enhanced with NLP
        words = script_text.split()
        markers = []
        
        # Add pauses at punctuation
        for i, word in enumerate(words):
            if word.endswith(','):
                markers.append({
                    "position": i,
                    "type": "short_pause",
                    "duration": "0.3-0.5s"
                })
            elif word.endswith('.') or word.endswith('!') or word.endswith('?'):
                markers.append({
                    "position": i,
                    "type": "medium_pause",
                    "duration": "0.8-1.2s"
                })
        
        return markers
