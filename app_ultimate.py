import os
import json
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from datetime import datetime

try:
    from streamlit_image_coordinates import streamlit_image_coordinates
    HAS_COORDS = True
except ImportError:
    HAS_COORDS = False

from dotenv import load_dotenv
from openai_service import OpenAIService
from master_dna import DEFAULT_MASTER_DNA
from emotion_engine import EmotionEngine
from audio_mapper import AudioEmotionMapper
from cultural_variations import CulturalVariations
from template_manager import TemplateManager
from analytics_tracker import AnalyticsTracker
from negative_prompt_generator import NegativePromptGenerator
from batch_processor import BatchProcessor

load_dotenv()
st.set_page_config(page_title="AI Prompt Studio Ultimate", layout="wide", page_icon="🎬")

# Copy Button Helper
def copy_button(label: str, text_to_copy: str, key_suffix: str = ""):
    import html, uuid
    safe = html.escape(text_to_copy or "")
    btn_id = f"copy_{uuid.uuid4().hex}_{key_suffix}"
    components.html(f"""
        <div style="margin:6px 0;">
          <button id="{btn_id}" style="padding:8px 12px;border-radius:8px;border:1px solid #ccc;cursor:pointer;background:#4CAF50;color:white;font-weight:bold;">{label}</button>
          <script>
            document.getElementById("{btn_id}").addEventListener("click", async () => {{
              await navigator.clipboard.writeText(`{safe}`);
              document.getElementById("{btn_id}").innerText = "✅ Copied!";
              setTimeout(() => document.getElementById("{btn_id}").innerText = "{label}", 1500);
            }});
          </script>
        </div>
    """, height=60)

# Emotion Preview
def show_emotion_preview(emotion_name: str, intensity: str = "Medium"):
    details = EmotionEngine.get_emotion_details(emotion_name)
    with st.expander(f"📖 {emotion_name} Preview", expanded=False):
        st.markdown(f"**{details['description']}**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🎭 Micro-Expressions:**")
            for expr in details['micro_expressions'][:3]:
                st.markdown(f"• {expr}")
        with col2:
            st.markdown("**👤 Body Language:**")
            for body in details['body_language'][:3]:
                st.markdown(f"• {body}")

# Auth
APP_PASSWORD = os.getenv("APP_PASSWORD", "").strip()
if APP_PASSWORD:
    if "auth_ok" not in st.session_state:
        st.session_state.auth_ok = False
    if not st.session_state.auth_ok:
        st.title("🎬 AI Prompt Studio Ultimate")
        pw = st.text_input("Password", type="password")
        if st.button("Login"):
            if pw == APP_PASSWORD:
                st.session_state.auth_ok = True
                st.rerun()
            else:
                st.error("Wrong password")
        st.stop()

# Setup
API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
if not API_KEY:
    st.error("Missing OPENAI_API_KEY")
    st.stop()

# Session State
if "master_prompt" not in st.session_state:
    st.session_state.master_prompt = DEFAULT_MASTER_DNA
if "model" not in st.session_state:
    st.session_state.model = "gpt-4o"
if "multi_angle_data" not in st.session_state:
    st.session_state.multi_angle_data = None
if "poser_data" not in st.session_state:
    st.session_state.poser_data = None
if "batch_results" not in st.session_state:
    st.session_state.batch_results = []

# Services
svc = OpenAIService(api_key=API_KEY, model=st.session_state.model)
template_mgr = TemplateManager()
analytics = AnalyticsTracker()

# Header
st.title("🎬 AI Prompt Studio Ultimate")
st.caption("✨ Emotion Engine™ | Audio Mapping | Batch Mode | Cultural Variations | Templates | Analytics")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.session_state.model = st.text_input("OpenAI Model", value=st.session_state.model)
    st.divider()
    stats = analytics.get_dashboard_stats()
    st.metric("Generations", stats['total_generations'])
    st.metric("Time Saved", f"{stats['time_saved_hours']}h")

# TABS
tabs = st.tabs(["🎬 DrMotion Enhanced", "📋 Templates", "📊 Analytics", "🎨 Custom", "📸 Other Tools", "⚙️ Config"])

######################
# TAB 0: DrMotion Enhanced
######################
with tabs[0]:
    st.header("🎬 DrMotion: Ultimate Video Prompt Engine")
    
    # Mode selector
    mode = st.radio("Mode", ["🎯 Single Generation", "🔥 Batch Mode", "🛍️ Product Review"], horizontal=True)
    st.divider()
    
    if mode == "🎯 Single Generation":
        img = st.file_uploader("Upload Character", type=["png","jpg","webp"], key="dm_img")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            model_choice = st.selectbox("Video Model", ["Kling 1.5","Veo 2 / Sora","Luma Dream Machine","Runway Gen-3 Alpha","Minimax","Haiper"])
        with col2:
            motion = st.selectbox("Motion", ["Walking Runway","Turning Head & Smiling","Drinking Coffee","Typing","Dancing","Running","Talking to Camera"])
        with col3:
            # Emotion Mixing
            use_mixing = st.checkbox("Mix Emotions", value=False)
            if use_mixing:
                primary_emotion = st.selectbox("Primary Emotion (70%)", EmotionEngine.get_all_emotions(), key="prim")
                secondary_emotion = st.selectbox("Secondary Emotion (30%)", EmotionEngine.get_all_emotions(), key="sec")
                emotion = f"{primary_emotion} + {secondary_emotion}"
            else:
                emotion = st.selectbox("Emotion", EmotionEngine.get_all_emotions())
        with col4:
            intensity = st.select_slider("Intensity", ["Subtle","Medium","Strong"], value="Medium")
        
        # Cultural Variation
        use_cultural = st.checkbox("Apply Cultural Variation", value=False)
        if use_cultural:
            culture = st.selectbox("Culture", CulturalVariations.get_available_cultures())
        else:
            culture = None
        
        # Show Preview
        if not use_mixing:
            show_emotion_preview(emotion, intensity)
        
        # Generate Button
        if img and st.button("🎬 Generate Ultra-Realistic Prompt", type="primary", use_container_width=True):
            with st.spinner("Generating..."):
                # Handle emotion mixing
                if use_mixing:
                    # This would require enhancing openai_service to accept mixed emotions
                    # For now, use primary
                    actual_emotion = primary_emotion
                else:
                    actual_emotion = emotion
                
                dm_data = svc.drmotion_generate(img, model_choice, motion, actual_emotion, st.session_state.master_prompt, intensity)
                
                # Track analytics
                analytics.track_generation("DrMotion", actual_emotion, motion, model_choice, intensity, 1, 0)
            
            if dm_data:
                st.success("✅ Generated!")
                
                # Show sections
                with st.expander("📊 Analysis", expanded=False):
                    st.write(dm_data.get("character_analysis", ""))
                    st.write(dm_data.get("emotion_breakdown", ""))
                
                with st.expander("🎭 Details", expanded=True):
                    if "micro_expressions" in dm_data:
                        st.markdown("**Micro-Expressions:**")
                        for expr in dm_data["micro_expressions"]:
                            st.markdown(f"• {expr}")
                    
                    if "body_language_cues" in dm_data:
                        st.markdown("**Body Language:**")
                        for cue in dm_data["body_language_cues"]:
                            st.markdown(f"• {cue}")
                
                st.divider()
                
                # Main Prompt
                final_prompt = dm_data.get("final_video_prompt", "")
                
                # Add cultural context if selected
                if use_cultural:
                    cultural_section = CulturalVariations.build_cultural_prompt_section(culture, actual_emotion)
                    final_prompt = f"{final_prompt}\n\n{cultural_section}"
                
                st.markdown("### 🎯 Final Video Prompt")
                st.text_area("", value=final_prompt, height=300, key="dm_final")
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    copy_button("📋 Copy Prompt", final_prompt, "dm")
                with col_b:
                    # Generate negative prompt
                    neg_prompt = NegativePromptGenerator.generate(actual_emotion, motion, model_choice)
                    copy_button("🚫 Copy Negative Prompt", neg_prompt, "dm_neg")
                with col_c:
                    # Generate audio prompt
                    audio_prompt = AudioEmotionMapper.build_audio_prompt(actual_emotion)
                    copy_button("🎙️ Copy Audio Prompt", audio_prompt, "dm_audio")
                
                # Show negative and audio in expanders
                with st.expander("🚫 Negative Prompt"):
                    st.text_area("", value=neg_prompt, height=150, key="neg_show")
                
                with st.expander("🎙️ Audio/Voice Prompt"):
                    st.text_area("", value=audio_prompt, height=200, key="audio_show")
                
                # Save Template Option
                if st.button("💾 Save as Template"):
                    template_mgr.save_template(
                        name=f"{motion} - {emotion}",
                        prompt=final_prompt,
                        category="DrMotion",
                        emotion=emotion,
                        motion=motion,
                        model=model_choice,
                        tags=[emotion, motion, model_choice],
                        notes=f"Generated on {datetime.now().strftime('%Y-%m-%d')}"
                    )
                    st.success("Template saved!")
    
    elif mode == "🔥 Batch Mode":
        st.info("Generate multiple variations at once!")
        
        img = st.file_uploader("Upload Character", type=["png","jpg","webp"], key="batch_img")
        
        batch_type = st.radio("Batch Type", ["Multiple Emotions", "Multiple Intensities", "Multiple Models"], horizontal=True)
        
        if batch_type == "Multiple Emotions":
            selected_emotions = st.multiselect("Select Emotions (max 5)", EmotionEngine.get_all_emotions(), max_selections=5)
            intensity = st.select_slider("Intensity", ["Subtle","Medium","Strong"], value="Medium")
            variations = [{"emotion": e, "intensity": intensity} for e in selected_emotions]
        
        elif batch_type == "Multiple Intensities":
            emotion = st.selectbox("Emotion", EmotionEngine.get_all_emotions(), key="batch_emo")
            variations = [{"emotion": emotion, "intensity": i} for i in ["Subtle","Medium","Strong"]]
        
        else:  # Multiple Models
            emotion = st.selectbox("Emotion", EmotionEngine.get_all_emotions(), key="batch_emo2")
            selected_models = st.multiselect("Select Models", ["Kling 1.5","Veo 2 / Sora","Luma Dream Machine","Runway Gen-3 Alpha"], max_selections=4)
            variations = [{"model": m} for m in selected_models]
        
        motion = st.selectbox("Motion", ["Walking Runway","Turning Head & Smiling","Drinking Coffee","Talking to Camera"], key="batch_motion")
        
        if img and variations and st.button("🚀 Generate Batch", type="primary"):
            with st.spinner(f"Generating {len(variations)} variations..."):
                results = []
                progress_bar = st.progress(0)
                
                for i, var in enumerate(variations):
                    try:
                        emo = var.get("emotion", emotion)
                        intens = var.get("intensity", "Medium")
                        mod = var.get("model", "Kling 1.5")
                        
                        result = svc.drmotion_generate(img, mod, motion, emo, st.session_state.master_prompt, intens)
                        result['variation'] = f"{emo} - {intens}" if batch_type != "Multiple Models" else mod
                        results.append(result)
                        
                        analytics.track_generation("DrMotion Batch", emo, motion, mod, intens, 1, 0)
                    except Exception as e:
                        results.append({"error": str(e), "variation": f"Variation {i+1}"})
                    
                    progress_bar.progress((i + 1) / len(variations))
                
                st.session_state.batch_results = results
            
            st.success(f"✅ Generated {len(results)} variations!")
            
            # Display results
            for i, result in enumerate(results):
                if "error" in result:
                    st.error(f"{result['variation']}: {result['error']}")
                else:
                    with st.expander(f"📄 {result['variation']}", expanded=i==0):
                        prompt = result.get("final_video_prompt", "")
                        st.text_area("", value=prompt, height=200, key=f"batch_{i}")
                        copy_button(f"📋 Copy {result['variation']}", prompt, f"batch_{i}")
    
    else:  # Product Review
        st.info("Generate 16s Product Review with Script + 2 Clips")
        
        img = st.file_uploader("Upload Product/Model", type=["png","jpg","webp"], key="pr_img")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            product = st.text_input("Product Details", "Vitamin C Serum - glowing skin")
        with col2:
            language = st.selectbox("Language", ["Hinglish","Hindi","English","Spanish"])
        with col3:
            emotion = st.selectbox("Tone", EmotionEngine.get_all_emotions(), key="pr_emo")
        
        intensity = st.select_slider("Intensity", ["Subtle","Medium","Strong"], value="Medium", key="pr_int")
        
        if img and st.button("🎬 Generate Review Plan", type="primary"):
            with st.spinner("Creating review..."):
                pr_data = svc.drmotion_product_review(img, product, language, emotion, st.session_state.master_prompt, intensity)
                analytics.track_generation("Product Review", emotion, "Review", "", intensity, 1, 0)
            
            if pr_data:
                st.success("✅ Review Plan Ready!")
                
                st.markdown("### 📝 Script")
                script = pr_data.get("script", "")
                st.text_area("", value=script, height=100, key="pr_script")
                copy_button("📋 Copy Script", script, "script")
                
                # Audio Prompt for Script
                audio_for_script = AudioEmotionMapper.build_audio_prompt(emotion, script)
                with st.expander("🎙️ Audio Prompt for Script"):
                    st.text_area("", value=audio_for_script, height=150, key="pr_audio")
                    copy_button("📋 Copy Audio", audio_for_script, "pr_audio")
                
                st.divider()
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown("#### 1️⃣ Clip A (0-8s)")
                    prompt_a = pr_data.get("clip_1_visual_prompt", "")
                    st.text_area("", value=prompt_a, height=250, key="pr_a")
                    copy_button("📋 Copy Clip A", prompt_a, "a")
                
                with col_b:
                    st.markdown("#### 2️⃣ Clip B (8-16s)")
                    prompt_b = pr_data.get("clip_2_visual_prompt", "")
                    st.text_area("", value=prompt_b, height=250, key="pr_b")
                    copy_button("📋 Copy Clip B", prompt_b, "b")

######################
# TAB 1: Templates
######################
with tabs[1]:
    st.header("📋 Template Library")
    
    tab_a, tab_b = st.tabs(["Browse Templates", "Save New"])
    
    with tab_a:
        # Search
        search_query = st.text_input("🔍 Search templates", "")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_cat = st.selectbox("Category", ["All"] + template_mgr.get_all_categories())
        with col2:
            filter_emotion = st.selectbox("Emotion", ["All"] + EmotionEngine.get_all_emotions())
        with col3:
            filter_tags = st.multiselect("Tags", template_mgr.get_all_tags())
        
        # Search
        results = template_mgr.search_templates(
            query=search_query,
            category=filter_cat if filter_cat != "All" else "",
            emotion=filter_emotion if filter_emotion != "All" else "",
            tags=filter_tags
        )
        
        st.write(f"Found {len(results)} templates")
        
        # Display
        for template in results:
            with st.expander(f"📄 {template['name']} ({template['usage_count']} uses)"):
                st.markdown(f"**Category:** {template['category']}")
                st.markdown(f"**Emotion:** {template['emotion']}")
                st.markdown(f"**Motion:** {template['motion']}")
                st.markdown(f"**Tags:** {', '.join(template['tags'])}")
                st.text_area("Prompt", value=template['prompt'], height=200, key=f"tpl_{template['id']}")
                
                col_x, col_y, col_z = st.columns(3)
                with col_x:
                    copy_button("📋 Copy", template['prompt'], f"tpl_{template['id']}")
                with col_y:
                    if st.button("✅ Use This", key=f"use_{template['id']}"):
                        template_mgr.increment_usage(template['id'])
                        st.success("Marked as used!")
                with col_z:
                    if st.button("🗑️ Delete", key=f"del_{template['id']}"):
                        template_mgr.delete_template(template['id'])
                        st.rerun()
        
        # Stats
        st.divider()
        stats = template_mgr.get_stats()
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Templates", stats['total_templates'])
        col2.metric("Total Uses", stats['total_usage'])
        if stats['most_used']:
            col3.metric("Most Used", stats['most_used']['name'])
    
    with tab_b:
        st.markdown("### Save Current Prompt as Template")
        
        tpl_name = st.text_input("Template Name", "My Awesome Prompt")
        tpl_prompt = st.text_area("Prompt", "", height=200)
        tpl_category = st.selectbox("Category", ["DrMotion", "Product Review", "Cloner", "Custom"])
        tpl_emotion = st.selectbox("Emotion", EmotionEngine.get_all_emotions(), key="tpl_emo")
        tpl_motion = st.text_input("Motion Type", "")
        tpl_tags = st.text_input("Tags (comma-separated)", "")
        tpl_notes = st.text_area("Notes", "")
        
        if st.button("💾 Save Template"):
            tags_list = [t.strip() for t in tpl_tags.split(",") if t.strip()]
            template_mgr.save_template(
                name=tpl_name,
                prompt=tpl_prompt,
                category=tpl_category,
                emotion=tpl_emotion,
                motion=tpl_motion,
                tags=tags_list,
                notes=tpl_notes
            )
            st.success("Template saved!")

######################
# TAB 2: Analytics
######################
with tabs[2]:
    st.header("📊 Analytics Dashboard")
    
    stats = analytics.get_dashboard_stats()
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Generations", stats['total_generations'])
    col2.metric("Avg Iterations", stats['avg_iterations'])
    col3.metric("Time Saved", f"{stats['time_saved_hours']} hours")
    col4.metric("Improvement", f"+{stats['improvement_rate']}%")
    
    st.divider()
    
    # Top stats
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("### 🎭 Top Emotion")
        st.info(stats['top_emotion'])
    with col_b:
        st.markdown("### 🎥 Top Model")
        st.info(stats['top_model'])
    with col_c:
        st.markdown("### ⚡ Top Feature")
        st.info(stats['top_feature'])
    
    st.divider()
    
    # Breakdowns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Emotions Used")
        for emotion, count in sorted(stats['emotions_breakdown'].items(), key=lambda x: x[1], reverse=True):
            st.write(f"{emotion}: {count}")
    
    with col2:
        st.markdown("### Models Used")
        for model, count in sorted(stats['models_breakdown'].items(), key=lambda x: x[1], reverse=True):
            st.write(f"{model}: {count}")
    
    st.divider()
    
    # Recent Activity
    st.markdown("### Recent Activity")
    recent = analytics.get_recent_activity(10)
    for activity in recent:
        st.text(f"{activity['timestamp'][:19]} | {activity['feature']} | {activity['emotion']} | {activity['model']}")
    
    # Reset
    if st.button("🔄 Reset Analytics"):
        analytics.reset_analytics()
        st.success("Analytics reset!")
        st.rerun()

######################
# TAB 3: Custom Emotions
######################
with tabs[3]:
    st.header("🎨 Custom Emotion Designer")
    st.info("Create your own custom emotions by mixing base emotions or defining from scratch")
    
    design_mode = st.radio("Mode", ["Mix Existing", "Define New"], horizontal=True)
    
    if design_mode == "Mix Existing":
        st.markdown("### Emotion Mixer")
        
        col1, col2 = st.columns(2)
        with col1:
            primary = st.selectbox("Primary Emotion", EmotionEngine.get_all_emotions(), key="mix_p")
            primary_weight = st.slider("Primary Weight", 0.0, 1.0, 0.7, 0.1)
        with col2:
            secondary = st.selectbox("Secondary Emotion", EmotionEngine.get_all_emotions(), key="mix_s")
            st.metric("Secondary Weight", f"{round((1-primary_weight)*100)}%")
        
        custom_name = st.text_input("Custom Emotion Name", f"Mixed: {primary} + {secondary}")
        
        if st.button("🎨 Create Mixed Emotion"):
            mixed = EmotionEngine.mix_emotions(primary, secondary, primary_weight)
            st.session_state.custom_emotions[custom_name] = mixed
            st.success(f"Created: {custom_name}")
            
            # Preview
            st.markdown("### Preview")
            st.markdown(f"**Description:** {mixed['description']}")
            st.markdown(f"**Mix Ratio:** {mixed['mix_ratio']}")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("**Micro-Expressions:**")
                for expr in mixed['micro_expressions']:
                    st.markdown(f"• {expr}")
            with col_b:
                st.markdown("**Body Language:**")
                for body in mixed['body_language']:
                    st.markdown(f"• {body}")
    
    else:
        st.markdown("### Define New Emotion")
        st.caption("Coming soon - full custom emotion builder")
        st.info("For now, use the Emotion Mixer to create custom combinations")
    
    # Show Custom Emotions
    if st.session_state.custom_emotions:
        st.divider()
        st.markdown("### Your Custom Emotions")
        for name, data in st.session_state.custom_emotions.items():
            with st.expander(name):
                st.write(data)

######################
# TAB 4: Other Tools (Cloner, etc.)
######################
with tabs[4]:
    st.header("📸 Other Tools")
    
    tool = st.selectbox("Select Tool", ["Cloner", "PerfectCloner", "Multi-Angle", "Wardrobe", "Prompter", "Poser", "Captions"])
    
    if tool == "Cloner":
        st.subheader("Cloner")
        img = st.file_uploader("Upload", type=["jpg","png","webp"], key="clone")
        if img and st.button("Analyze"):
            with st.spinner("Analyzing..."):
                data = svc.cloner_analyze_filelike(img, st.session_state.master_prompt)
            st.text_area("Prompt", value=data.get("full_prompt",""), height=250)
            copy_button("Copy", data.get("full_prompt",""), "clone")
    
    elif tool == "Captions":
        st.subheader("Captions")
        img = st.file_uploader("Upload", type=["jpg","png"], key="cap")
        style = st.selectbox("Style", ["Funny","Serious","Inspirational"])
        lang = st.radio("Language", ["English","Hindi"], horizontal=True)
        if img and st.button("Generate"):
            with st.spinner("Writing..."):
                res = svc.captions_generate_filelike(img, style, lang)
            st.text_area("Caption", value=res.get("caption",""), height=100)
            st.text_input("Hashtags", value=" ".join(res.get("hashtags",[])))
    
    # Add other tools similarly...

######################
# TAB 5: Settings
######################
with tabs[5]:
    st.header("⚙️ Configuration")
    
    st.markdown("### Master DNA")
    st.session_state.master_prompt = st.text_area("", value=st.session_state.master_prompt, height=300)
    
    st.divider()
    
    st.markdown("### API Keys")
    st.caption("Add additional API keys for advanced features")
    
    # Placeholder for additional APIs
    st.text_input("ElevenLabs API Key (for TTS)", type="password", help="Optional")
    st.text_input("Replicate API Key (for video analysis)", type="password", help="Optional")
    
    st.divider()
    
    st.markdown("### Export/Import")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📥 Export Templates"):
            if template_mgr.export_templates("my_templates.json"):
                st.success("Exported!")
    with col2:
        uploaded = st.file_uploader("Import Templates", type=["json"])
        if uploaded and st.button("📤 Import"):
            # Save uploaded file and import
            with open("temp_import.json", "wb") as f:
                f.write(uploaded.read())
            if template_mgr.import_templates("temp_import.json"):
                st.success("Imported!")

