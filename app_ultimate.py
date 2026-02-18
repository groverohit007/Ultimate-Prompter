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
from ultra_realism_engine import UltraRealismEngine

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
if "custom_emotions" not in st.session_state:
    st.session_state.custom_emotions = {}

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
        if stats['emotions_breakdown']:
            for emotion, count in sorted(stats['emotions_breakdown'].items(), key=lambda x: x[1], reverse=True):
                st.write(f"{emotion}: {count}")
        else:
            st.info("No data yet - generate your first prompt!")
    
    with col2:
        st.markdown("### Models Used")
        if stats['models_breakdown']:
            for model, count in sorted(stats['models_breakdown'].items(), key=lambda x: x[1], reverse=True):
                st.write(f"{model}: {count}")
        else:
            st.info("No data yet - generate your first prompt!")
    
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
# TAB 4: Other Tools (Fully Implemented)
######################
with tabs[4]:
    st.header("📸 Professional Tools Suite")
    
    tool = st.selectbox("Select Tool", [
        "🎯 Cloner + Ultra Realism",
        "✨ PerfectCloner", 
        "📐 Multi-Angle Grid", 
        "👗 Digital Wardrobe", 
        "✍️ Prompter Builder", 
        "🕺 Poser", 
        "📝 Caption Generator"
    ])
    
    # ========== CLONER + ULTRA REALISM ==========
    if tool == "🎯 Cloner + Ultra Realism":
        st.subheader("🎯 Cloner + Ultra Realism Engine")
        st.info("Clone a scene with photorealistic enhancements for images that look like real people")
        
        img = st.file_uploader("Upload Reference Image", type=["jpg","png","webp","jpeg"], key="clone_img")
        
        col1, col2 = st.columns(2)
        with col1:
            use_ultra_realism = st.checkbox("✨ Enable Ultra Realism Engine", value=True, help="Add photorealistic enhancements")
        with col2:
            if use_ultra_realism:
                realism_level = st.select_slider("Realism Level", ["Medium", "High", "Maximum"], value="High")
            else:
                realism_level = None
        
        if use_ultra_realism:
            st.caption("Ultra Realism adds: Natural skin texture, realistic lighting, authentic imperfections, professional camera simulation")
        
        if img and st.button("🔍 Analyze & Clone", type="primary"):
            with st.spinner("Analyzing scene and applying Master DNA..."):
                data = svc.cloner_analyze_filelike(img, st.session_state.master_prompt)
            
            base_prompt = data.get("full_prompt", "")
            
            # Apply Ultra Realism if enabled
            if use_ultra_realism:
                from ultra_realism_engine import UltraRealismEngine
                
                with st.spinner("Applying Ultra Realism enhancements..."):
                    enhanced_prompt = UltraRealismEngine.enhance_prompt(base_prompt, realism_level)
                    negative_prompt = UltraRealismEngine.get_negative_prompt()
                
                st.success("✅ Ultra-Realistic Prompt Generated!")
                
                # Show realism analysis
                analysis = UltraRealismEngine.analyze_for_realism(base_prompt)
                col_a, col_b = st.columns(2)
                col_a.metric("Realism Score", f"{analysis['realism_score']}/100")
                col_b.metric("Level", analysis['realism_level'])
                
                if analysis['suggestions']:
                    with st.expander("💡 Realism Suggestions"):
                        for sugg in analysis['suggestions']:
                            st.write(f"• {sugg}")
                
                st.divider()
                
                # Main prompt
                st.markdown("### 🎯 Enhanced Prompt (With Ultra Realism)")
                st.text_area("Copy this to your image generator", value=enhanced_prompt, height=400, key="clone_enhanced")
                copy_button("📋 Copy Enhanced Prompt", enhanced_prompt, "clone_enh")
                
                # Negative prompt
                st.markdown("### 🚫 Negative Prompt (For Ultra Realism)")
                st.text_area("Paste this in negative prompt field", value=negative_prompt, height=100, key="clone_neg")
                copy_button("📋 Copy Negative Prompt", negative_prompt, "clone_neg_btn")
                
                # Show base prompt for comparison
                with st.expander("📄 Base Prompt (Without Ultra Realism)"):
                    st.text_area("", value=base_prompt, height=200, key="clone_base")
            
            else:
                # Standard cloner without ultra realism
                st.success("✅ Standard Clone Generated!")
                st.text_area("Cloned Prompt", value=base_prompt, height=300, key="clone_std")
                copy_button("📋 Copy Prompt", base_prompt, "clone_std_btn")
    
    # ========== PERFECT CLONER ==========
    elif tool == "✨ PerfectCloner":
        st.subheader("✨ PerfectCloner")
        st.caption("Precisely recreate an image with detailed schema analysis")
        
        pimg = st.file_uploader("Upload Image to Recreate", type=["jpg","png","webp","jpeg"], key="pc_img")
        identity_lock = st.checkbox("🔒 Enable Identity Lock", value=True, help="Maintain character identity from Master DNA")
        
        if pimg and st.button("🔬 Analyze Schema", type="primary"):
            with st.spinner("Performing detailed analysis..."):
                data = svc.perfectcloner_analyze_filelike(pimg, st.session_state.master_prompt, identity_lock)
            
            st.success("✅ Schema Analysis Complete!")
            
            rec_prompt = data.get("recreation_prompt", "")
            neg_prompt = data.get("negative_prompt", "")
            notes = data.get("notes", "")
            
            st.text_area("Recreation Prompt", value=rec_prompt, height=300, key="pc_rec")
            
            col1, col2 = st.columns(2)
            with col1:
                copy_button("📋 Copy Recreation Prompt", rec_prompt, "pc_rec_btn")
            with col2:
                if st.button("💾 Save as Template"):
                    template_mgr.save_template(
                        name=f"PerfectClone - {datetime.now().strftime('%Y%m%d')}",
                        prompt=rec_prompt,
                        category="PerfectCloner",
                        tags=["perfect_clone", "recreation"],
                        notes=notes
                    )
                    st.success("Saved to Templates!")
            
            with st.expander("📊 Full Analysis Data"):
                st.json(data)
    
    # ========== MULTI-ANGLE GRID ==========
    elif tool == "📐 Multi-Angle Grid":
        st.subheader("📐 Multi-Angle Character Sheet")
        st.caption("Generate 20 unique camera angles for your character")
        
        ref_img = st.file_uploader("Upload Character Reference", type=["png","jpg","webp","jpeg"], key="mag_img")
        
        if st.button("🔄 Reset", key="mag_reset_btn"):
            st.session_state.multi_angle_data = None
            st.rerun()
        
        if ref_img and st.button("📊 Generate 20-Angle Plan", type="primary"):
            with st.spinner("Planning 20 unique angles..."):
                plan = svc.multi_angle_planner_filelike(ref_img, st.session_state.master_prompt)
            
            if plan:
                st.session_state.multi_angle_data = plan
                st.success("✅ 20-Angle Plan Generated!")
                st.rerun()
        
        # Show plan if exists
        if st.session_state.multi_angle_data:
            plan_data = st.session_state.multi_angle_data
            
            st.divider()
            st.markdown("### Step 1: Generate Grid")
            st.text_area("Grid Generation Prompt", value=plan_data.get("grid_prompt",""), height=150, key="mag_grid")
            copy_button("📋 Copy Grid Prompt", plan_data.get("grid_prompt",""), "mag_grid_btn")
            
            st.divider()
            st.markdown("### Step 2: Select Individual Angle")
            
            angles_list = plan_data.get("angles", [])
            angle_options = [f"{a.get('id',0)}. {a.get('name','Unknown')}" for a in angles_list]
            
            selected_option = st.selectbox("Choose Angle", angle_options, key="mag_select")
            
            if selected_option:
                idx = int(selected_option.split(".")[0]) - 1
                if 0 <= idx < len(angles_list):
                    selected_angle = angles_list[idx]
                    
                    st.success(f"Selected: **{selected_angle.get('name')}**")
                    
                    # Generate physics-enhanced prompt
                    final_prompt = svc.build_physics_prompt(st.session_state.master_prompt, selected_angle)
                    
                    st.text_area("Physics-Enhanced Prompt", value=final_prompt, height=250, key="mag_final")
                    copy_button("📋 Copy Angle Prompt", final_prompt, "mag_final_btn")
    
    # ========== DIGITAL WARDROBE ==========
    elif tool == "👗 Digital Wardrobe":
        st.subheader("👗 Digital Wardrobe")
        st.caption("Fuse outfit from reference onto your character")
        
        wardrobe_img = st.file_uploader("Upload Outfit Reference", type=["png","jpg","webp","jpeg"], key="wardrobe_img")
        
        st.info("💡 Tip: Upload an image showing the outfit you want. The tool will extract the clothing and fuse it with your character.")
        
        if wardrobe_img and st.button("🧵 Analyze & Wear Outfit", type="primary"):
            with st.spinner("Extracting outfit details and fusing with character..."):
                w_data = svc.wardrobe_fuse_filelike(wardrobe_img, st.session_state.master_prompt)
            
            st.success("✅ Outfit Fused!")
            
            outfit_desc = w_data.get("outfit_description", "")
            fused_prompt = w_data.get("fused_prompt", "")
            
            with st.expander("👔 Outfit Description"):
                st.write(outfit_desc)
            
            st.text_area("Final Prompt with Outfit", value=fused_prompt, height=300, key="wardrobe_final")
            
            col1, col2 = st.columns(2)
            with col1:
                copy_button("📋 Copy Wardrobe Prompt", fused_prompt, "wardrobe_btn")
            with col2:
                if st.button("💾 Save as Template"):
                    template_mgr.save_template(
                        name=f"Wardrobe - {datetime.now().strftime('%Y%m%d')}",
                        prompt=fused_prompt,
                        category="Wardrobe",
                        tags=["outfit", "wardrobe"],
                        notes=f"Outfit: {outfit_desc[:100]}"
                    )
                    st.success("Saved!")
    
    # ========== PROMPTER BUILDER ==========
    elif tool == "✍️ Prompter Builder":
        st.subheader("✍️ Prompter - Structured Prompt Builder")
        st.caption("Build professional prompts with dropdown selections")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Character & Pose**")
            pose = st.selectbox("Pose", ["Confident stance", "Sitting relaxed", "Walking toward camera", "Close-up portrait", "Action pose", "Casual lean"], key="p_pose")
            attire = st.selectbox("Attire", ["Professional suit", "Casual jeans and t-shirt", "Formal dress", "Business casual", "Athletic wear", "Traditional clothing"], key="p_attire")
            jewellery = st.selectbox("Accessories", ["Minimal jewelry", "Statement pieces", "Watch only", "None", "Traditional jewelry"], key="p_jewel")
        
        with col2:
            st.markdown("**Environment & Technical**")
            lighting = st.selectbox("Lighting", ["Soft natural light", "Golden hour", "Studio softbox", "Dramatic side lighting", "Neon/urban", "Overcast natural"], key="p_light")
            camera_angle = st.selectbox("Camera Angle", ["Eye level", "Slightly low angle", "High angle", "Profile view", "Over-the-shoulder"], key="p_cam")
            background = st.selectbox("Background", ["Blurred studio", "Urban street", "Nature/outdoor", "Modern interior", "Minimalist solid color"], key="p_bg")
        
        st.divider()
        
        camera_lens = st.selectbox("Lens Choice", ["50mm f/1.8 (natural)", "85mm f/1.4 (portrait)", "35mm f/2 (environmental)", "24mm f/2.8 (wide)"], key="p_lens")
        
        if st.button("🎨 Generate Structured Prompt", type="primary"):
            fields = {
                "pose": pose,
                "attire": attire,
                "lighting": lighting,
                "camera_angle": camera_angle,
                "camera_lens": camera_lens,
                "background": background,
                "jewellery": jewellery
            }
            
            prompt = svc.prompter_build(st.session_state.master_prompt, fields)
            
            st.success("✅ Structured Prompt Generated!")
            st.text_area("Generated Prompt", value=prompt, height=350, key="prompter_result")
            
            col_a, col_b = st.columns(2)
            with col_a:
                copy_button("📋 Copy Prompt", prompt, "prompter_btn")
            with col_b:
                if st.button("💾 Save as Template"):
                    template_mgr.save_template(
                        name=f"Prompter - {pose[:20]}",
                        prompt=prompt,
                        category="Prompter",
                        tags=["prompter", "structured", attire.split()[0].lower()],
                        notes=f"Pose: {pose}, Lighting: {lighting}"
                    )
                    st.success("Saved!")
    
    # ========== POSER ==========
    elif tool == "🕺 Poser":
        st.subheader("🕺 Poser - Pose Variation Generator")
        st.caption("Generate 5 pose variations from a reference")
        
        poser_img = st.file_uploader("Upload Reference Pose", type=["jpg","png","webp","jpeg"], key="poser_img")
        
        col1, col2 = st.columns(2)
        with col1:
            pose_style = st.selectbox("Style Direction", ["Casual & Natural", "Elegant & Graceful", "Edgy & Bold", "Professional & Composed", "Dynamic & Active"], key="poser_style")
        with col2:
            num_variations = st.slider("Number of Variations", 3, 7, 5, key="poser_num")
        
        if poser_img and st.button("🎭 Generate Pose Variations", type="primary"):
            with st.spinner("Creating pose variations..."):
                st.session_state.poser_data = svc.poser_variations_filelike(poser_img, st.session_state.master_prompt, pose_style)
            
            st.success(f"✅ Generated {num_variations} Pose Variations!")
            st.rerun()
        
        # Display variations
        if st.session_state.poser_data:
            data = st.session_state.poser_data
            prompts = data.get("prompts", [])[:num_variations]
            scene_lock = data.get("scene_lock", "")
            
            st.divider()
            st.markdown("### Choose Your Variation")
            
            # Create radio options
            variation_names = [p.get("pose_name", f"Pose {i+1}") for i, p in enumerate(prompts)]
            selected_variation = st.radio("Select Pose", variation_names, key="poser_select")
            
            # Find selected variation
            for p in prompts:
                if p.get("pose_name") == selected_variation:
                    st.success(f"**Selected:** {p.get('pose_name')}")
                    
                    # Build full prompt
                    full_prompt = f"{st.session_state.master_prompt}\n\n"
                    full_prompt += f"POSE: {p.get('pose_name')}\n"
                    full_prompt += f"DESCRIPTION: {p.get('pose_description')}\n"
                    full_prompt += f"FACIAL EXPRESSION: {p.get('facial_expression')}\n\n"
                    full_prompt += f"SCENE CONSISTENCY: {scene_lock}"
                    
                    st.text_area("Pose Prompt", value=full_prompt, height=250, key="poser_final")
                    
                    col_x, col_y = st.columns(2)
                    with col_x:
                        copy_button("📋 Copy Pose Prompt", full_prompt, "poser_copy")
                    with col_y:
                        if st.button("💾 Save as Template"):
                            template_mgr.save_template(
                                name=f"Poser - {p.get('pose_name')}",
                                prompt=full_prompt,
                                category="Poser",
                                tags=["poser", "pose", pose_style.split()[0].lower()],
                                notes=p.get('pose_description', '')
                            )
                            st.success("Saved!")
                    break
    
    # ========== CAPTION GENERATOR ==========
    elif tool == "📝 Caption Generator":
        st.subheader("📝 Instagram Caption Generator")
        st.caption("Generate engaging captions with hashtags")
        
        cap_img = st.file_uploader("Upload Image", type=["jpg","png","webp","jpeg"], key="cap_img")
        
        col1, col2 = st.columns(2)
        with col1:
            caption_style = st.selectbox("Caption Tone", ["Funny & Witty", "Serious & Professional", "Inspirational & Motivational", "Casual & Friendly", "Mysterious & Intriguing"], key="cap_style")
        with col2:
            caption_lang = st.selectbox("Language", ["English", "Hindi", "Hinglish", "Spanish"], key="cap_lang")
        
        include_emojis = st.checkbox("Include Emojis", value=True)
        num_hashtags = st.slider("Number of Hashtags", 3, 10, 4, key="cap_hashtags")
        
        if cap_img and st.button("✍️ Generate Caption", type="primary"):
            with st.spinner("Writing caption..."):
                # Extract base style
                style_map = {
                    "Funny & Witty": "Funny",
                    "Serious & Professional": "Serious",
                    "Inspirational & Motivational": "Inspirational",
                    "Casual & Friendly": "Engaging",
                    "Mysterious & Intriguing": "Mysterious"
                }
                base_style = style_map.get(caption_style, "Engaging")
                
                res = svc.captions_generate_filelike(cap_img, base_style, caption_lang)
            
            st.success("✅ Caption Generated!")
            
            caption_text = res.get("caption", "")
            hashtags_list = res.get("hashtags", [])[:num_hashtags]
            
            # Show caption
            st.markdown("### 📱 Your Caption")
            st.text_area("Caption Text", value=caption_text, height=120, key="cap_text")
            
            # Show hashtags
            st.markdown("### #️⃣ Hashtags")
            hashtags_str = " ".join(hashtags_list)
            st.text_input("Hashtags", value=hashtags_str, key="cap_hash_display")
            
            # Combined output
            st.divider()
            st.markdown("### 📋 Complete Post")
            complete_post = f"{caption_text}\n\n{hashtags_str}"
            st.text_area("Copy entire post", value=complete_post, height=150, key="cap_complete")
            
            copy_button("📋 Copy Complete Post", complete_post, "cap_copy")

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

