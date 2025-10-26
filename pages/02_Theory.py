import streamlit as st

st.set_page_config(page_title="Theory — DES", page_icon="📘", layout="wide")

# Load Custom CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# Hero Section
# st.markdown("""
#     <div style="text-align: center; padding: 2rem 0;">
#         <div style="font-size: 5rem; margin-bottom: 1rem;">📘</div>
#     </div>
# """, unsafe_allow_html=True)

st.title("Theory: DES and Brute-Force Attacks")

st.markdown("""
    <div style="font-size: 1.1rem; color: #b8c5d6; margin-bottom: 3rem;">
        Understanding the fundamentals of DES encryption and cryptanalysis
    </div>
""", unsafe_allow_html=True)

# Main Content in Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(102, 126, 234, 0.1); border-radius: 16px; border: 1px solid rgba(102, 126, 234, 0.3); margin-bottom: 2rem;">
            <h3 style="margin-top: 0;">🔐 DES Basics</h3>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>Symmetric block cipher</strong> - Same key for encryption/decryption</li>
                <li><strong>64-bit block size</strong> - Processes data in 64-bit chunks</li>
                <li><strong>56-bit effective key</strong> - Stored in 8 bytes with parity bits</li>
                <li><strong>Keyspace: 2⁵⁶</strong> ≈ 72.06 quadrillion possible keys</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border: 1px solid rgba(240, 147, 251, 0.3); margin-bottom: 2rem;">
            <h3 style="margin-top: 0;">⚡ Brute-Force Attack</h3>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>Exhaustive search</strong> - Tests every possible key</li>
                <li><strong>Linear time complexity</strong> - Grows with keyspace size</li>
                <li><strong>Guaranteed success</strong> - Will find the key eventually</li>
                <li><strong>Computationally expensive</strong> - Requires significant resources</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# DES Structure Explanation
st.subheader("🏗️ DES Structure & Algorithm")

structure_col1, structure_col2, structure_col3 = st.columns(3)

with structure_col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">1️⃣</div>
            <h4>Initial Permutation</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">64-bit input is permuted according to a fixed table</p>
        </div>
    """, unsafe_allow_html=True)

with structure_col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">2️⃣</div>
            <h4>16 Rounds</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Feistel network with substitution and permutation operations</p>
        </div>
    """, unsafe_allow_html=True)

with structure_col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">3️⃣</div>
            <h4>Final Permutation</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Inverse of initial permutation produces ciphertext</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Toy Mode Explanation
st.subheader("🎮 Toy Mode Implementation")

st.markdown("""
    <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h4 style="color: #4facfe; margin-top: 0;">Why Toy Mode?</h4>
        <p style="color: #b8c5d6; line-height: 1.8; margin-bottom: 1.5rem;">
           Because the full DES keyspace (2⁵⁶) is too large for a single laptop, the simulator uses a toy mode that fixes most key bits and only varies the lowest N bits so we can demonstrate exponential growth practically.”
        </p>
        <h4 style="color: #4facfe;">How It Works:</h4>
        <ul style="color: #b8c5d6; line-height: 1.8;">
            <li>We fix a <strong>baseline 8-byte key</strong></li>
            <li>Only the <strong>lowest N bits</strong> are varied (N = 8 to 24)</li>
            <li>This creates a keyspace of <strong>2ᴺ keys</strong></li>
            <li>Makes the demo <strong>runnable and interactive</strong></li>
            <li>Still demonstrates <strong>exponential time growth</strong></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Keyspace Examples with Visual Cards
st.subheader("📊 Keyspace Examples")

keyspace_col1, keyspace_col2, keyspace_col3, keyspace_col4 = st.columns(4)

with keyspace_col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(102, 126, 234, 0.05)); border-radius: 12px; text-align: center;">
            <h3 style="color: #667eea; margin: 0;">N = 8</h3>
            <p style="color: #b8c5d6; font-size: 0.85rem; margin: 0.5rem 0;">256 keys</p>
            <p style="color: #4facfe; font-size: 0.8rem; margin: 0;">⚡ Instant</p>
        </div>
    """, unsafe_allow_html=True)

with keyspace_col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(102, 126, 234, 0.05)); border-radius: 12px; text-align: center;">
            <h3 style="color: #667eea; margin: 0;">N = 16</h3>
            <p style="color: #b8c5d6; font-size: 0.85rem; margin: 0.5rem 0;">65,536 keys</p>
            <p style="color: #4facfe; font-size: 0.8rem; margin: 0;">⚡ Very Fast</p>
        </div>
    """, unsafe_allow_html=True)

with keyspace_col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(240, 147, 251, 0.2), rgba(240, 147, 251, 0.05)); border-radius: 12px; text-align: center;">
            <h3 style="color: #f093fb; margin: 0;">N = 20</h3>
            <p style="color: #b8c5d6; font-size: 0.85rem; margin: 0.5rem 0;">1,048,576 keys</p>
            <p style="color: #fee140; font-size: 0.8rem; margin: 0;">⏱️ Moderate</p>
        </div>
    """, unsafe_allow_html=True)

with keyspace_col4:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.2), rgba(250, 112, 154, 0.05)); border-radius: 12px; text-align: center;">
            <h3 style="color: #fa709a; margin: 0;">N = 24</h3>
            <p style="color: #b8c5d6; font-size: 0.85rem; margin: 0.5rem 0;">16,777,216 keys</p>
            <p style="color: #fa709a; font-size: 0.8rem; margin: 0;">⏳ Slower</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Security Implications
st.subheader("🛡️ Security Implications")

security_col1, security_col2 = st.columns(2)

with security_col1:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(79, 172, 254, 0.1); border-radius: 16px; border-left: 4px solid #4facfe;">
            <h4 style="color: #4facfe; margin-top: 0;">✅ DES Historical Strengths</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>Standardized by NIST in 1977</li>
                <li>Widely adopted for decades</li>
                <li>Well-studied and analyzed</li>
                <li>Efficient hardware implementation</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with security_col2:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(250, 112, 154, 0.1); border-radius: 16px; border-left: 4px solid #fa709a;">
            <h4 style="color: #fa709a; margin-top: 0;">⚠️ Modern Vulnerabilities</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>56-bit key too small for modern computing</li>
                <li>Broken by specialized hardware (DES Cracker, 1998)</li>
                <li>Distributed attacks can crack in hours</li>
                <li>Replaced by AES in 2001</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Mathematical Growth
st.subheader("📈 Exponential Growth Visualization")

st.markdown("""
    <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px;">
        <p style="color: #b8c5d6; line-height: 1.8; margin-bottom: 1.5rem;">
            Doubling the number of variable bits (N) <strong>doubles the exponent</strong>, which means the keyspace 
            and search time <strong>increase by a factor of 2</strong>:
        </p>
        <div style="font-family: 'JetBrains Mono', monospace; color: #4facfe; text-align: center; font-size: 1.1rem; line-height: 2;">
            N = 16 → 2¹⁶ = 65,536 keys<br>
            N = 17 → 2¹⁷ = 131,072 keys (×2)<br>
            N = 18 → 2¹⁸ = 262,144 keys (×2)<br>
            N = 20 → 2²⁰ = 1,048,576 keys (×4 from N=18)<br>
            N = 24 → 2²⁴ = 16,777,216 keys (×16 from N=20)
        </div>
    </div>
""", unsafe_allow_html=True)

# st.markdown("---")

# # Important Notes
# st.info("""
#     💡 **Key Takeaway**: This exponential growth is why larger key sizes (AES-128, AES-256) provide 
#     significantly better security against brute-force attacks, even with advances in computing power.
# """)

# st.caption("""
#     ⚠️ All timings shown in this demo are illustrative. Actual performance depends on hardware, 
#     Python overhead, and Streamlit UI update frequency.
# """)

# Navigation
st.markdown("---")
st.markdown("""
    <div style="text-align: center;">
        <p style="color: #b8c5d6;">Ready to see it in action?</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Go to Simulation", use_container_width=True):
        st.switch_page("pages/04_Encryption_Simulation.py")