# ⚡ QUICK START GUIDE
## Get Your First Ultra-Realistic Video in 5 Minutes

---

## 📋 Prerequisites Checklist

Before you start, make sure you have:

- [ ] Python 3.8 or higher installed
- [ ] OpenAI API key (get it from platform.openai.com)
- [ ] The project files downloaded
- [ ] A clear character image (PNG/JPG)

---

## 🚀 Setup (One Time Only)

### Step 1: Install Dependencies

Open terminal/command prompt in the project folder:

```bash
pip install -r requirements.txt
```

⏱️ **Time**: ~2 minutes

### Step 2: Configure API Key

**Option A: Using .env file (Recommended)**

Create a file named `.env` in the project folder:

```env
OPENAI_API_KEY=sk-your-api-key-here
APP_PASSWORD=optional_password
```

**Option B: Using Streamlit Secrets**

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-your-api-key-here"
APP_PASSWORD = "optional_password"
```

⏱️ **Time**: ~1 minute

### Step 3: Launch the App

```bash
streamlit run app.py
```

Your browser will open automatically to `http://localhost:8501`

⏱️ **Time**: ~10 seconds

---

## 🎬 Your First Generation: Product Review

Let's create a realistic product review video!

### Step 1: Navigate to DrMotion Tab

1. Click on the **"🎬 DrMotion (Video)"** tab
2. You'll see two modes - select **"🛍️ Product Review (16s Story)"**

### Step 2: Upload Your Image

1. Click **"📤 Upload Product / Model with Product"**
2. Select a clear image (best: person holding product, looking at camera)
3. ✅ Image should be well-lit, clear face, resolution 512px+

**Pro Tip**: Use a photo of yourself or a model with the product in hand

### Step 3: Configure Settings

Fill in these fields:

```
🏷️ Product Details: "Vitamin C Serum - brightens skin"
🗣️ Script Language: "Hinglish" (or your preference)
🎭 Review Tone: "Authentic / Natural"
💪 Emotion Intensity: "Medium"
```

### Step 4: Preview the Emotion (Optional)

Click on **"📖 Authentic / Natural - Emotion Preview"** to see:
- What micro-expressions will be used
- Body language cues
- Breathing patterns
- Temporal flow

This helps you understand what the AI will generate!

### Step 5: Generate!

Click the big **"🎬 Generate 16s Review Plan"** button

⏱️ **Wait time**: 10-20 seconds

### Step 6: Review Results

You'll get 3 outputs:

**1. THE SCRIPT** (What to say)
```
Example:
"So like, I've been using this Vitamin C serum for two weeks,
and yaar, honestly? The results are pretty amazing actually..."
```

**2. CLIP A PROMPT** (0-8s: Talking to camera)
```
Example:
Close-up shot, person addresses camera. Authentic Duchenne smile 
activates at 2s - orbicularis oculi contracts, crow's feet visible.
Eyes maintain contact but break naturally every 3s. Hand holds 
product, gestures organically. Filler word 'like' adds authenticity...
[~300 more words of detailed acting/physics instructions]
```

**3. CLIP B PROMPT** (8-16s: Product demo)
```
Example:
Hands apply serum. Close-up: fingers press pump (2 pumps), serum 
glistens. Hands warm product between fingertips. Upward strokes on 
cheeks. Lighting matches Clip A. Skin shows subsurface scattering...
[~300 more words of detailed product demo instructions]
```

### Step 7: Copy & Use

1. Click **"📋 Copy Clip A"** - paste into your video AI tool
2. Generate video (wait for AI tool to process)
3. Click **"📋 Copy Clip B"** - paste into your video AI tool
4. Generate video
5. Combine both clips in order!

---

## 🎯 Your First Generation: Simple Motion

For a simpler test, try a general motion:

### Quick Setup:

1. Go to **"🎬 DrMotion (Video)"** tab
2. Select **"🎯 General Motion (8s)"** mode
3. Upload character image
4. Configure:
   - **🎥 Video AI Model**: "Kling 1.5" (or your preference)
   - **🏃 Motion Type**: "Turning Head & Smiling"
   - **🎭 Emotion**: "Happy / Excited / Joyful"
   - **💪 Intensity**: "Medium"

5. Click **"🎬 Generate Ultra-Realistic Prompt"**

### What You'll Get:

```
📊 Analysis Breakdown:
- Character analysis
- Emotion manifestation
- Micro-expressions (e.g., "Duchenne smile with crow's feet")
- Body language (e.g., "Shoulders lift and open")
- Physics notes (e.g., "Hair follows motion with 0.3s delay")
- Temporal progression:
  • 0-2s: Head turn initiates, smile begins
  • 3-5s: Peak smile, full Duchenne activation
  • 6-8s: Smile afterglow, settling

🎯 Final Video Prompt:
[300-500 words of ultra-detailed instructions]
```

Copy the final prompt to your video AI tool and generate!

---

## 🎨 Testing All Features

### Quick Tour:

**1. Cloner** (Tab 2)
- Upload reference image
- Get pose/lighting analysis
- Generate matching prompts

**2. PerfectCloner** (Tab 3)
- Upload image to recreate
- Get precise schema
- Perfect recreation prompts

**3. Multi-Angle Grid** (Tab 4)
- Upload character
- Plan 20 different angles
- Get physics-enhanced prompts

**4. Digital Wardrobe** (Tab 5)
- Upload outfit reference
- Fuse onto your character
- Get wearing prompts

**5. Prompter** (Tab 6)
- Select: Pose, Attire, Lighting, etc.
- Auto-generate structured prompt
- Quick iterations

**6. Poser** (Tab 7)
- Upload reference pose
- Generate 5 variations
- Choose your favorite

**7. Captions** (Tab 8)
- Upload image
- Get Instagram caption
- Includes hashtags

---

## 💡 Pro Tips for Best Results

### For Video Generation:

1. **Upload Quality Matters**
   - ✅ Clear, well-lit images
   - ✅ Face clearly visible
   - ✅ 512px minimum resolution
   - ❌ Avoid: Blurry, dark, occluded faces

2. **Choose Right Emotion**
   - Product reviews → "Authentic / Natural"
   - Runway → "Professional / Confident"
   - Comedy → "Funny / Witty / Goofy"
   - Serious content → "Serious / Focused / Intense"

3. **Intensity Settings**
   - Subtle = Background/ambient
   - Medium = Most realistic (default)
   - Strong = Dramatic/peak moments

4. **Read the Emotion Preview**
   - Helps you understand what will generate
   - Shows micro-expressions used
   - Explains body language

### For Master DNA (Settings Tab):

1. **Be Specific**
   - Don't: "Brown hair, pretty face"
   - Do: "Long flowing black hair with natural wave, oval face with defined cheekbones, warm brown eyes, honey-brown skin"

2. **Include Photography Style**
   - Lighting preferences
   - Camera style
   - Quality markers (8K, etc.)

3. **Consistency Anchors**
   - Mention distinctive features
   - Age range
   - Signature traits

---

## 🐛 Troubleshooting

### Problem: "API Error"
**Solution**: 
- Check API key in `.env` file
- Verify you have OpenAI credits
- Try refreshing the page

### Problem: Empty results / No prompt generated
**Solution**:
- Check image file is valid (PNG/JPG)
- Try a different, clearer image
- Refresh browser

### Problem: Results don't look realistic
**Solution**:
- Increase intensity to "Medium" or "Strong"
- Try "Authentic / Natural" emotion
- Use a clearer base image
- Read emotion preview before generating

### Problem: Can't copy prompts
**Solution**:
- Click the "📋 Copy" button (don't manually select text)
- Try a different browser
- Check clipboard permissions

---

## 📚 Next Steps

Once you've mastered the basics:

1. **Experiment with Emotions**
   - Try all 8 emotions
   - Compare results
   - Mix intensities

2. **Test Different Models**
   - Kling vs Veo vs Luma
   - Each has strengths
   - See which works best for you

3. **Optimize Master DNA**
   - Refine character description
   - Add unique traits
   - Lock in your signature style

4. **Chain Features**
   - Use Wardrobe → DrMotion
   - Use Multi-Angle → Poser
   - Use Cloner → PerfectCloner

---

## 🎯 Success Checklist

After your first generation, you should have:

- [ ] App running smoothly
- [ ] API key working
- [ ] Generated at least one video prompt
- [ ] Copied prompt to clipboard
- [ ] Understood emotion preview system
- [ ] Tested copy buttons
- [ ] Explored at least 2 tabs

**If you checked all boxes: Congratulations! You're ready to create ultra-realistic AI videos! 🎉**

---

## 🆘 Need Help?

Common questions:

**Q: Which video AI model should I use?**
A: Start with Kling 1.5 or Runway Gen-3 Alpha - they're most consistent.

**Q: How long are the generated prompts?**
A: 300-500 words on average - this detail is what makes them realistic!

**Q: Can I edit the generated prompts?**
A: Absolutely! They're starting points. Feel free to modify.

**Q: Do I need to use every detail?**
A: The AI models use what they can. More detail = better results.

**Q: Can I add my own emotions?**
A: Yes! Edit `emotion_engine.py` to add custom emotions.

---

**Happy generating! 🎬✨**

*Remember: The secret to ultra-realistic AI videos is in the details. The Emotion Engine provides those details automatically!*
