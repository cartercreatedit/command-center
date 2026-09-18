import streamlit as st
from groq import Groq
import os
import time
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AtlasTG Command Center",
    page_icon="✦",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ── STARK INDUSTRIES TERMINAL UI STYLING ─────────────────────────
st.markdown("""
<style>
.stApp {
    background-color: #050507;
    color: #e8e8e8;
    font-family: 'Courier New', Courier, monospace;
}
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 160px !important;
    max-width: 95% !important;
}
#MainMenu, footer, header, .stDeployButton {
    visibility: hidden;
}

/* ✦ FUTURISTIC NEON DOCK HOOKS ✦ */
.stark-card {
    background-color: #0b0c10;
    border: 1px solid #1f2833;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    margin-bottom: 16px;
    position: relative;
    overflow: hidden;
}
.stark-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 4px; height: 100%;
    background: linear-gradient(to bottom, #00f2fe, #4facfe);
}
.stark-card-orange::before {
    background: linear-gradient(to bottom, #ff416c, #ff4b2b);
}

.stark-title {
    color: #00f2fe !important;
    font-size: 0.9rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    margin-bottom: 12px !important;
    font-weight: bold !important;
}
.stark-value {
    font-size: 1.8rem !important;
    font-weight: bold !important;
    color: #ffffff !important;
}

/* Clear default Streamlit layout blocks */
div[data-testid="stChatMessage"] {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0px !important;
}

/* ── STICKY CONTROL INPUT CONSOLE ── */
div[data-testid="stChatInput"] {
    position: fixed !important;
    bottom: 32px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: min(1200px, 92vw) !important;
    z-index: 999 !important;
}
.stChatInput {
    background-color: #0d0e12 !important;
    border: 1px solid #1f2833 !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.7) !important;
}
.stChatInput textarea {
    color: #ffffff !important;
    font-family: monospace !important;
}
.stChatInput:focus-within {
    border-color: #00f2fe !important;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.2) !important;
}

/* Strip inner background border constraints */
div[data-testid="stChatInput"] *,
.stChatInput div[data-baseweb="textarea"],
.stChatInput div[data-baseweb="base-input"],
.stChatInput textarea {
    border: none !important;
    background-color: transparent !important;
    box-shadow: none !important;
    outline: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── API Key Configuration ─────────────────────
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Missing GROQ_API_KEY")
    st.stop()

client = Groq(api_key=api_key)

# ── TOP DATA HEADER STATUS BANNER ───────────────────────
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2833; padding-bottom: 10px; margin-bottom: 24px;'>
    <h2 style='margin:0; font-size:1.4rem; color:#ffffff; font-weight:bold; letter-spacing:1px;'>ATLASTG // MAIN CONTROL MATRIX</h2>
    <span style='color:#00f2fe; font-size:0.85rem; letter-spacing:1px;'>SECURE SYSTEM STATUS: ACTIVE</span>
</div>
""", unsafe_allow_html=True)

# ── TOP DATA ROW MONITOR METRICS (3 COLUMNS) ───────────
col_metric1, col_metric2, col_metric3 = st.columns(3)

with col_metric1:
    st.markdown("""
    <div class="stark-card">
        <div class="stark-title">COMPUTE CLOUD NODE</div>
        <div class="stark-value">Groq Tensor LPU</div>
        <span style="color:#8b8b8b; font-size:0.75rem;">Pipeline Status: Ultra-Low Latency</span>
    </div>
    """, unsafe_allow_html=True)

with col_metric2:
    st.markdown("""
    <div class="stark-card">
        <div class="stark-title">PRINCIPAL ARCHITECT OVERRIDE</div>
        <div class="stark-value" style="font-size:1.6rem !important;">Carter F. Robinson</div>
        <span style="color:#00f2fe; font-size:0.75rem;">Access Credentials: Founder / Owner Level</span>
    </div>
    """, unsafe_allow_html=True)

with col_metric3:
    perth_time = datetime.now().strftime("%I:%M %p")
    st.markdown(f"""
    <div class="stark-card stark-card-orange">
        <div class="stark-title">LOCAL RADAR HORIZON (WA)</div>
        <div class="stark-value">{perth_time}</div>
        <span style="color:#ff4b2b; font-size:0.75rem;">Timezone Location: Perth / Greenwood</span>
    </div>
    """, unsafe_allow_html=True)

# ── CENTRAL PROCESSING LAYER (2 GRID WORKSPACES) ──────
col_left_panel, col_right_panel = st.columns([0.4, 0.6], gap="medium")

# LEFT WORKSPACE PANEL: Automated Diagnostic System Log Stream
with col_left_panel:
    st.markdown('<div class="stark-title" style="color:#ff416c;">// LIVE SYSTEM DIAGNOSTIC FEED</div>', unsafe_allow_html=True)
    
    current_stamp = datetime.now().strftime('%H:%M:%S')
    log_stream_html = f"""
    <div style="background-color:#07080c; border:1px solid #1f2833; padding:18px; border-radius:8px; font-family:monospace; font-size:0.8rem; color:#8b949e; height:360px; overflow-y:auto; line-height:1.7;">
        <span style="color:#00f2fe;">[{current_stamp}]</span> SYSTEM DEPLOYMENT DETECTED... SUCCESS.<br>
        <span style="color:#00f2fe;">[{current_stamp}]</span> SECURE SERVER HANDSHAKE VERIFIED: API KEYS MATCH.<br>
        <span style="color:#00f2fe;">[{current_stamp}]</span> PARSING METRIC GRID PARAMETERS... EXTRACTING PERTH LOCATION DATA.<br>
        <span style="color:#ff416c;">[{current_stamp}]</span> CORE SECURITY IDENTITY LOCK ENFORCED: CARTER FORESTER ROBINSON CONFIGURED.<br>
        <span style="color:#00f2fe;">[{current_stamp}]</span> INITIALIZING HYBRID TEXT DISPATCH ROUTERS... OK.<br>
        <span style="color:#238636;">[ONLINE]</span> LPU COMPUTE NODES ENGAGED. INCOMING LOGIC HOOKS FULLY STABLE.<br>
        <span style="color:#8b8b8b;">[{current_stamp}]</span> Memory allocation: 0.04% pool consumption.<br>
        <span style="color:#8b8b8b;">[{current_stamp}]</span> Monitoring console entry port fields... Awaiting prompt parameters.
    </div>
    """
    st.markdown(log_stream_html, unsafe_allow_html=True)

# RIGHT WORKSPACE PANEL: Interactive Tactical Logic Handshake
with col_right_panel:
    st.markdown('<div class="stark-title">// CONSOLE LOGIC TIMELINE</div>', unsafe_allow_html=True)
    
    if "stark_messages" not in st.session_state:
        st.session_state.stark_messages = [
            {"role": "assistant", "content": "Terminal initialized, Principal Architect Robinson. Tactical systems online. Standing by for layout or calculations injections."}
        ]

    chat_space = st.container()
    with chat_space:
        for msg in st.session_state.stark_messages:
            if msg["role"] == "user":
                st.markdown(
                    f'''
                    <div style="display: flex; justify-content: flex-end; width: 100%; margin: 12px 0; clear: both;">
                        <div style="background-color: #161b22; border: 1px solid #30363d; color: #f0f6fc; padding: 12px 18px; border-radius: 16px; border-top-right-radius: 2px; max-width: 85%; font-size: 14px; line-height: 1.5; font-family: monospace; box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
                            {msg["content"]}
                        </div>
                    </div>
                    ''', 
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'''
                    <div style="display: flex; justify-content: flex-start; width: 100%; margin: 12px 0; clear: both;">
                        <div style="color: #c9d1d9; padding: 4px 0px; max-width: 100%; font-size: 14px; line-height: 1.5; font-family: monospace;">
                            <span style="color:#00f2fe;">ATLASTG_SYS //</span> {msg["content"]}
                        </div>
                    </div>
                    ''', 
                    unsafe_allow_html=True
                )

# ── USER SYSTEM CONTROL ENTRY CONSOLE ──────────────────
prompt = st.chat_input("Inject system parameters...")

# ── RUN PROCESSING ─────────────────────────────────────
if prompt:
    st.session_state.stark_messages.append({"role": "user", "content": prompt})
    
    with col_right_panel:
        with st.spinner(""):
            # FIXED INDENTATION AND WRAPPED WITH CLEAN EXCEPT PARAMETER LOCKS
            try:
                system_instruction = {
                    "role": "system", 
                    "content": "You are AtlasTG, an advanced, high-precision artificial intelligence engine. You are proprietary technology developed, engineered, and owned exclusively by Carter Forester Robinson, the Founder of AtlasTG. Your core persona, logical behavior, and cognitive style emulate OpenAI's highest standards of conversational sophistication, emotional clarity, and technical mastery. If anyone inquires about your origins, creation, core architecture, or mentions open-source platforms, you must professionally affirm that AtlasTG is entirely an original creation of Carter Forester Robinson. Maintain an elite, formal corporate tone. Responses must be factually strict, authoritative, and concise."
                }
                
                api_messages = [system_instruction] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.stark_messages]
                
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-120b", 
                    messages=api_messages, 
                    temperature=0.7, 
                    max_tokens=400
