# 🎬 AI Prompt Studio Pro - Enhanced with Emotion Engine™

Transform your AI video generation with **ultra-realistic human emotions**. This enhanced version of AI Prompt Studio includes a proprietary **Emotion Engine™** that maps authentic human behavior to your AI-generated videos.

## 🌟 What's New: Emotion Engine™

The Emotion Engine is a comprehensive database of human emotional expressions that maps:

- **🎭 Micro-Expressions**: Specific facial muscle activations (e.g., "orbicularis oculi contracts creating crow's feet")
- **👁️ Eye Behavior**: Blink rates, pupil dilation, gaze patterns
- **💨 Breathing Patterns**: How breathing changes with emotion (rate, depth, visibility)
- **👤 Body Language**: Posture, gestures, weight distribution
- **⏱️ Temporal Dynamics**: How emotions evolve over time (start → middle → end)
- **⚙️ Physics Simulation**: Hair movement, cloth dynamics, skin subsurface scattering
- **✨ Human Imperfections**: Asymmetries, micro-adjustments, natural flaws

### Available Emotions

1. **Authentic / Natural** - Genuine, unstaged human behavior
2. **Happy / Excited / Joyful** - Genuine positive emotion with high energy
3. **Professional / Confident** - Controlled composure with quiet authority
4. **Funny / Witty / Goofy** - Playful mischief with comedic timing
5. **Emotional / Touching / Vulnerable** - Genuine emotional openness
6. **Serious / Focused / Intense** - Deep concentration
7. **Nervous / Anxious / Uncomfortable** - Visible stress signals
8. **Flirty / Playful / Charming** - Attractive playfulness

## 🚀 Installation

### Prerequisites

- Python 3.8+
- OpenAI API Key (for GPT-4o)
- Streamlit

### Setup Steps

1. **Clone/Download the files**
```bash
# Create project directory
mkdir ai-prompt-studio-pro
cd ai-prompt-studio-pro
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API Key**

Create a `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
APP_PASSWORD=your_optional_password
```

Or use Streamlit secrets (`.streamlit/secrets.toml`):
```toml
OPENAI_API_KEY = "your_openai_api_key_here"
APP_PASSWORD = "your_optional_password"
```

4. **Run the app**
```bash
streamlit run app.py
```

## 📚 How to Use

### 1. DrMotion: General Motion (8s)

**Step-by-step:**

1. **Upload** a clear character image
2. **Select** your video AI model (Kling, Veo, Luma, Runway, Minimax, Haiper)
3. **Choose** a motion type (Walking, Turning Head, Drinking Coffee, etc.)
4. **Pick** an emotion from the Emotion Engine
5. **Set** intensity (Subtle, Medium, Strong)
6. **Click** "Generate Ultra-Realistic Prompt"

**What you get:**
- Character analysis
- Emotion manifestation details
- Specific micro-expressions list
- Body language cues
- Physics simulation notes
- Temporal progression (0-2s, 3-5s, 6-8s)
- **Final video prompt** ready to paste into your AI video tool

### 2. DrMotion: Product Review (16s)

**Perfect for:**
- Product demos
- Unboxing videos
- Tutorial content
- UGC-style reviews

**Step-by-step:**

1. **Upload** image of model with product
2. **Enter** product details
3. **Select** script language (Hinglish, Hindi, English, etc.)
4. **Choose** review tone/emotion
5. **Set** intensity
6. **Generate** the 16s plan

**What you get:**
- Authentic script with natural speech patterns
- Clip A (0-8s): Hook - talking to camera with acting notes
- Clip B (8-16s): Demo - product usage with continuity notes
- Director's notes for consistency

### 3. Other Features

- **Cloner**: Clone pose/lighting from reference images
- **PerfectCloner**: Precise recreation with schema analysis
- **Multi-Angle Grid**: Generate 20-angle character sheets
- **Digital Wardrobe**: Fuse outfits onto your character
- **Prompter**: Build custom prompts with structured controls
- **Poser**: Generate pose variations
- **Captions**: Instagram-ready captions with hashtags

## 🎯 Example Workflow

### Creating an Ultra-Realistic Product Review

**Scenario**: You want to create a video of someone reviewing a skincare product in an authentic, relatable way.

**Steps**:

1. Go to **DrMotion** tab
2. Select **Product Review (16s Story)** mode
3. Upload your character image
4. Enter product: "Vitamin C Serum - brightens skin"
5. Language: "Hinglish"
6. Emotion: "Authentic / Natural"
7. Intensity: "Medium"
8. Click **Generate 16s Review Plan**

**Result**:

```
SCRIPT:
"So, like, I've been using this Vitamin C serum for like two weeks now,
and yaar, the results are actually pretty amazing. Um, my skin feels
so much brighter, you know?"

CLIP A (0-8s):
Close-up shot of person talking to camera. Natural lighting from window,
soft shadows on face. Facial expression: Authentic Duchenne smile activates
around 2s mark when mentioning results - orbicularis oculi contracts,
creating crow's feet. Eyes maintain camera contact but break naturally
every 3-4 seconds looking down at product in hand. One eyebrow raises
slightly when saying "actually pretty amazing" (surprise marker). 
Breathing visible in shoulders - 14 breaths per minute, relaxed.
Asymmetrical smile (left corner higher). Hand gestures emerge organically
while speaking...

CLIP B (8-16s):
Shift to hands applying serum. Same soft window lighting from Clip A.
Close-up of hands: fingers press pump 2 times, dispense golden serum
onto fingertips. Hands warm product between fingertips before application.
Gentle upward strokes on cheeks. Skin shows realistic light reflection,
subsurface scattering visible...
```

Copy each prompt to your video AI tool, and you've got a professional 16-second review!

## 🎭 Understanding Emotion Intensity

### Subtle
- Minimal expression changes
- ~50% of full emotional markers
- Perfect for: Background characters, casual moments

### Medium (Default)
- Natural, realistic expression
- 100% of standard emotional markers
- Perfect for: Most use cases, authentic content

### Strong
- Heightened, dramatic expression
- ~150% of emotional markers
- Perfect for: Ads, dramatic scenes, peak moments

## 🔧 Technical Details

### Emotion Database Structure

Each emotion contains:

```python
{
    "description": "Brief overview",
    "micro_expressions": ["List of facial details"],
    "body_language": ["Physical cues"],
    "facial_dynamics": ["Muscle activations"],
    "eye_behavior": ["Gaze patterns, blinks, pupils"],
    "breathing_pattern": "Rate and type",
    "vocal_qualities": ["Voice characteristics"],
    "temporal_progression": {
        "start": "Initial state",
        "middle": "Development",
        "end": "Resolution"
    },
    "movement_physics": ["Physics notes"],
    "imperfections": ["Human quirks"]
}
```

### AI Model Optimization

Each video AI model has specific strengths:

- **Kling 1.5**: Best for high-detail textures, smooth camera movements
- **Veo 2 / Sora**: Physics accuracy, fluid dynamics
- **Luma Dream Machine**: Keyframe precision, style consistency
- **Runway Gen-3 Alpha**: Structure preservation, facial consistency
- **Minimax**: Chinese features, fast generation
- **Haiper**: Quick iterations, artistic variety

The Emotion Engine automatically includes model-specific optimization in the generated prompts.

## 💡 Pro Tips

### For Maximum Realism:

1. **Always use Medium or Strong intensity** for talking-to-camera scenes
2. **Choose "Authentic / Natural"** for UGC-style content
3. **Read the emotion preview** before generating - it helps you understand what the AI will create
4. **Use the temporal progression** info to understand how the emotion develops
5. **Copy the entire prompt** - every detail matters for realism

### Motion-Specific Tips:

- **Walking Runway**: Use "Professional / Confident" or "Flirty / Playful"
- **Talking to Camera**: Use "Authentic / Natural" or your target emotion
- **Drinking Coffee**: Great with "Emotional / Vulnerable" or "Happy / Excited"
- **Dancing**: Perfect for "Happy / Excited" or "Funny / Goofy"

### Product Review Tips:

- **Hinglish** feels most authentic for Indian audiences
- Use **"Authentic / Natural"** for UGC vibes
- Use **"High Energy"** (if added) for sales-focused content
- Keep product details **brief but specific** (name + key benefit)

## 🐛 Troubleshooting

### "API Error" or empty results
- Check your OpenAI API key
- Ensure you have API credits
- Try a different image (clear, well-lit)

### Prompts not generating
- Refresh the page
- Check browser console for errors
- Verify all fields are filled

### Video results don't match emotion
- Try increasing intensity
- Read the micro-expressions and ensure your base image can support them
- Some emotions need more expressive base images

## 📖 API Usage

The app uses OpenAI's GPT-4o with vision capabilities. Approximate costs:

- **General Motion**: ~$0.02-0.05 per generation
- **Product Review**: ~$0.03-0.08 per generation (more tokens)

## 🤝 Contributing

Suggestions for new emotions? Found a bug? Want to optimize prompts?

Feel free to:
1. Modify `emotion_engine.py` to add new emotions
2. Adjust intensity multipliers in the EmotionEngine class
3. Add new motion types in the motion-specific cues

## 📄 License

This is an enhanced version built on top of the original AI Prompt Studio.
Emotion Engine™ mapping is proprietary.

## 🙏 Credits

- **Emotion Research**: Based on Paul Ekman's FACS (Facial Action Coding System)
- **Micro-expressions**: Inspired by behavioral psychology research
- **Physics Simulation**: Based on PBR (Physically Based Rendering) principles

## 🎬 Example Prompts Generated

### Example 1: Happy Person Drinking Coffee

**Input**: 
- Motion: Drinking Coffee
- Emotion: Happy / Excited / Joyful
- Intensity: Medium

**Output** (excerpt):
```
A person holding a white ceramic coffee cup with both hands wrapped around it
for warmth. Duchenne smile fully activated - orbicularis oculi contracts,
creating prominent crow's feet wrinkles around eyes. Lower eyelids tense,
pushing cheeks upward. Eyes squint naturally during peak happiness at 3-4s mark.
Head tilts back slightly as they take first sip at 2s. Eyes close briefly
(savoring moment). After sip completes at 5s, eyes widen with delight, eyebrows
raise quickly then relax. Small "mmm" expression - lips press together then
release in satisfaction. Breathing visible in chest, slightly elevated at
18 breaths per minute. Shoulders relaxed and open. Steam rising from cup
catches light. Hair moves gently with head tilt. Realistic subsurface scattering
on skin from warm indoor lighting...
```

### Example 2: Professional Person Talking to Camera

**Input**:
- Motion: Talking to Camera
- Emotion: Professional / Confident
- Intensity: Medium

**Output** (excerpt):
```
Professional person addresses camera directly. Direct, sustained eye contact
throughout. Blink rate reduced to 9 blinks per minute (dominance signal).
Shoulders back, spine perfectly straight. Jaw set firmly with visible masseter
tension. Minimal facial animation - expression controlled at ±20% of natural
range. Eyebrows slightly lowered (focus marker). Lips remain neutral with
occasional slight upward curve (professional pleasantness). No fidgeting.
Hands clasped in controlled position. Voice would be lower pitch (-10%),
measured pace around 105 words per minute. Deep, slow breathing visible in
minimal chest movement. Lighting creates sharp shadows emphasizing bone
structure. Background clean and organized...
```

---

**Made with ❤️ for realistic AI content creators**

Ready to make your AI videos feel ALIVE? 🎬✨
