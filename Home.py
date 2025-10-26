import streamlit as st
from PIL import Image

st.set_page_config(page_title="DES Brute-Force Simulator", page_icon="🔐", layout="centered")

# Load Custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Try to load CSS, continue if file doesn't exist
try:
    load_css()
except FileNotFoundError:
    pass

# Hero Section with Icon
st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔐</div>
    </div>
""", unsafe_allow_html=True)

st.title("DES Brute-Force Simulator")

# Animated subtitle
st.markdown("""
    <div style=" font-size: 1.2rem; color: #b8c5d6; margin-bottom: 2rem;">
        An Interactive Educational Tool for Understanding Cryptographic Security
    </div>
""", unsafe_allow_html=True)

st.markdown(
    """
    ### 🎯 Welcome to the DES Brute-Force Simulator!

    This project is an educational DES brute-force simulator. It lets users encrypt a message with a DES key, then demonstrates how an attacker could attempt to recover that key by testing many candidate keys. Because full DES keyspace (2⁵⁶) is too large for a single laptop, the simulator uses a toy mode that fixes most key bits and only varies the lowest N bits so we can demonstrate exponential growth and time/complexity practically.”

    Navigate through the pages using the sidebar to:
    - **📘 Theory**: Learn about DES, its structure, and keyspace scaling.
    - **🔑 Encryption & Decryption**: Encrypt and decrypt messages using DES, plus simulate brute-force attacks.
    - **🧭 Procedure**: Understand the implementation details of the simulation.
    - **✅ Conclusion**: Discover key observations and takeaways from the simulations.
    """
)

# Feature Cards
st.markdown("---")
st.markdown("### ✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(102, 126, 234, 0.1); border-radius: 12px; border: 1px solid rgba(102, 126, 234, 0.3); text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔒</div>
            <h4>Encryption</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Encrypt data with DES algorithm using custom or random keys</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(240, 147, 251, 0.1); border-radius: 12px; border: 1px solid rgba(240, 147, 251, 0.3); text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
            <h4>Brute-Force</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Simulate attacks and understand computational complexity</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.3); text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
            <h4>Analytics</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Visualize attack progress and timing analysis</p><br>
        </div>
    """, unsafe_allow_html=True)

# st.info("⚠️ This is an educational tool. Do not use it for malicious purposes.")

#st.markdown("---")

# Logo Display
try:
    img = Image.open("assets/logo.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_column_width=True)
except Exception:
    pass

st.markdown("---")

# Quick Navigation
st.subheader("🚀 Quick Navigation")

nav_col1, nav_col2 = st.columns(2)

with nav_col1:
    st.markdown("""
        - [📘 Theory](Theory) - Learn DES fundamentals
        - [🔑 Simulation](Encryption) - Encrypt, decrypt & attack
    """)

with nav_col2:
    st.markdown("""
        - [🧭 Procedure](Procedure) - Implementation details
        - [✅ Conclusion](Conclusion) - Key takeaways
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #b8c5d6;">
        <p>Built with ❤️ for Cryptography Education</p>
        <p style="font-size: 0.8rem; margin-top: 0.5rem;">
            DES Brute-Force Simulator © 2025 | For Educational Use Only
        </p>
    </div>
""", unsafe_allow_html=True)