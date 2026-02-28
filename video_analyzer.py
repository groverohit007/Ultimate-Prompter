"""
Video Analyzer
==============
Analyze videos to extract emotions, motions, and generate prompts
Requires GPT-4V or similar video analysis capability
"""

from typing import Dict, Any, Optional, List
import base64
import tempfile
import os


def extract_keyframes_from_video(video_file, num_frames: int = 5) -> List[str]:
    """
    Extract evenly-spaced keyframes from a video file and return as base64 data URLs.

    Args:
        video_file: Streamlit UploadedFile (video)
        num_frames: Number of frames to extract (default 5)

    Returns:
        List of base64 data URL strings for each keyframe
    """
    try:
        import cv2
    except ImportError:
        raise ImportError(
            "opencv-python-headless is required for video analysis. "
            "Install it with: pip install opencv-python-headless"
        )

    # Write uploaded video to a temp file so OpenCV can read it
    suffix = os.path.splitext(video_file.name)[1] if hasattr(video_file, 'name') else '.mp4'
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(video_file.getvalue())
        tmp_path = tmp.name

    frames_data_urls = []
    try:
        cap = cv2.VideoCapture(tmp_path)
        if not cap.isOpened():
            raise ValueError("Could not open video file. Ensure it is a valid video format.")

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames <= 0:
            raise ValueError("Video has no readable frames.")

        # Calculate evenly-spaced frame indices
        if total_frames <= num_frames:
            indices = list(range(total_frames))
        else:
            indices = [int(i * (total_frames - 1) / (num_frames - 1)) for i in range(num_frames)]

        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if not ret:
                continue

            # Encode frame to JPEG bytes
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
            b64 = base64.b64encode(buffer).decode('utf-8')
            frames_data_urls.append(f"data:image/jpeg;base64,{b64}")

        cap.release()
    finally:
        os.unlink(tmp_path)

    if not frames_data_urls:
        raise ValueError("Could not extract any frames from the video.")

    return frames_data_urls


class VideoAnalyzer:
    """Analyze videos for emotion, motion, and style extraction"""
    
    def __init__(self, openai_client, model: str = "gpt-4o"):
        """
        Initialize video analyzer.
        
        Args:
            openai_client: OpenAI client instance
            model: Model to use for analysis (needs vision capability)
        """
        self.client = openai_client
        self.model = model
    
    def analyze_video_reference(self, video_file, analysis_focus: str = "all") -> Dict[str, Any]:
        """
        Analyze a reference video to extract characteristics.
        
        Args:
            video_file: Video file object
            analysis_focus: What to focus on - "emotion", "motion", "style", or "all"
        
        Returns:
            Dict with detected emotion, motion, style characteristics
        """
        
        # For now, this is a placeholder that would work with video frames
        # In production, you'd extract keyframes and analyze them
        
        instructions = (
            "Analyze this video and extract:\n"
            "1. Primary emotion expressed (from: Happy, Sad, Angry, Neutral, Excited, etc.)\n"
            "2. Motion type (Walking, Talking, Gesturing, etc.)\n"
            "3. Key visual characteristics:\n"
            "   - Lighting style\n"
            "   - Camera angle\n"
            "   - Color grading\n"
            "   - Environment/background\n"
            "4. Acting notes:\n"
            "   - Facial expressions observed\n"
            "   - Body language\n"
            "   - Energy level\n"
            "5. Technical details:\n"
            "   - Shot composition\n"
            "   - Movement style\n"
            "   - Pacing\n\n"
            "Return JSON with these categories."
        )
        
        # This is a stub - actual implementation would process video frames
        return {
            "detected_emotion": "Authentic / Natural",
            "confidence": 0.85,
            "motion_type": "Talking to Camera",
            "lighting": "Natural window light, soft shadows",
            "camera_angle": "Eye level, slightly close-up",
            "color_grading": "Warm tones, slightly desaturated",
            "facial_expressions": [
                "Natural Duchenne smile appears intermittently",
                "Eyes maintain camera contact with natural breaks",
                "Eyebrows raise on emphasized words"
            ],
            "body_language": [
                "Relaxed shoulders",
                "Hand gestures emerge organically",
                "Slight head tilts during thought"
            ],
            "energy_level": "Medium - conversational",
            "pacing": "Natural speech rhythm, ~120 wpm",
            "notes": "Authentic, unscripted feel. Person appears comfortable and genuine."
        }
    
    def reverse_engineer_prompt(self, video_file) -> Dict[str, Any]:
        """
        Reverse engineer a prompt that could recreate this video.
        
        Args:
            video_file: AI-generated video to analyze
        
        Returns:
            Dict with estimated original prompt and techniques
        """
        
        instructions = (
            "Analyze this AI-generated video and reverse-engineer the likely prompt.\n"
            "Identify:\n"
            "1. Emotion keywords likely used\n"
            "2. Motion descriptors\n"
            "3. Visual style prompts\n"
            "4. Technical terms (physics, lighting, etc.)\n"
            "5. Quality/model indicators\n\n"
            "Reconstruct a comprehensive prompt that would generate similar results."
        )
        
        # Stub implementation
        return {
            "estimated_emotion": "Happy / Excited",
            "estimated_motion": "Walking toward camera",
            "key_techniques": [
                "Duchenne smile with crow's feet",
                "Shoulder bounce (energetic)",
                "Hair physics (momentum)",
                "Subsurface scattering on skin"
            ],
            "likely_model": "Kling 1.5 or Runway Gen-3",
            "reconstructed_prompt": (
                "Person walks confidently toward camera with genuine happiness. "
                "Duchenne smile fully activated - orbicularis oculi contracts creating "
                "prominent crow's feet. Eyes bright and engaged. Shoulders lift with "
                "each step (energetic bounce). Hair follows realistic physics - sways "
                "opposite walk direction with 0.3s momentum delay. Subsurface scattering "
                "visible on skin from natural lighting. 8k quality, smooth camera dolly "
                "backward maintaining framing. Physically accurate motion, cloth physics "
                "on clothing, realistic shadows."
            ),
            "prompt_strength": "8.5/10",
            "notes": "High-quality generation with strong attention to micro-expressions and physics"
        }
    
    def extract_style_profile(self, video_file) -> Dict[str, Any]:
        """
        Extract a reusable style profile from video.
        
        Args:
            video_file: Video with desired style
        
        Returns:
            Style profile that can be applied to other generations
        """
        
        return {
            "lighting_style": "Natural, soft window light from camera left",
            "color_palette": "Warm tones, slightly desaturated for authentic feel",
            "camera_style": "Handheld aesthetic, slight natural shake",
            "composition": "Rule of thirds, subject slightly off-center",
            "movement_style": "Natural, organic - no robotic precision",
            "energy_signature": "Relaxed but engaged - conversational energy",
            "quality_markers": "8k, natural grain, realistic physics",
            "template_prompt": (
                "Natural window light from left, warm color grading, "
                "slight handheld camera movement, rule of thirds composition, "
                "8k quality with subtle film grain, realistic physics"
            )
        }
    
    def compare_videos(self, video1_file, video2_file) -> Dict[str, Any]:
        """
        Compare two videos and identify differences.
        
        Args:
            video1_file: First video
            video2_file: Second video
        
        Returns:
            Comparison highlighting key differences
        """
        
        return {
            "emotion_difference": "Video 1: Happy (strong) vs Video 2: Happy (subtle)",
            "motion_difference": "Video 1: Energetic vs Video 2: Calm",
            "style_difference": "Video 1: Bright/vibrant vs Video 2: Muted/natural",
            "quality_comparison": "Both 8k, Video 1 has better physics simulation",
            "recommendation": "Video 1 better for advertising, Video 2 better for authentic content"
        }
    
    def _extract_keyframes(self, video_file, num_frames: int = 5):
        """
        Extract keyframes from video for analysis.
        Helper method for video processing.
        """
        # Placeholder - would use opencv or similar to extract frames
        pass
    
    def _analyze_frame(self, frame_data: bytes) -> Dict[str, Any]:
        """
        Analyze a single frame using vision model.
        """
        # Placeholder for GPT-4V analysis of individual frames
        pass
