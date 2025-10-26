import streamlit as st

st.set_page_config(page_title="Procedure", page_icon="🧭", layout="wide")

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
#         <div style="font-size: 5rem; margin-bottom: 1rem;">🧭</div>
#     </div>
# """, unsafe_allow_html=True)

st.title("Procedure: How the Simulation Works")

st.markdown("""
    <div style="font-size: 1.1rem; color: #b8c5d6; margin-bottom: 3rem;">
        A deep dive into the implementation details and methodology
    </div>
""", unsafe_allow_html=True)

# Algorithm Overview
st.subheader("🔄 Algorithm Flow")

st.markdown("""
    <div style="padding: 2rem; background: rgba(102, 126, 234, 0.1); border-radius: 16px; border: 1px solid rgba(102, 126, 234, 0.3);">
        <p style="color: #b8c5d6; font-size: 1.1rem;">
            Our brute-force simulator follows a systematic approach to demonstrate cryptanalysis:
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Step-by-step process with beautiful cards
step_col1, step_col2 = st.columns(2)

with step_col1:
    st.markdown("""
        <div style="padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(102, 126, 234, 0.05)); border-radius: 16px; border-left: 4px solid #667eea; margin-bottom: 1.5rem; min-height: 200px;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin-right: 1rem;">1</div>
                <h3 style="margin: 0; color: #667eea;">Key Selection</h3>
            </div>
            <p style="color: #b8c5d6; line-height: 1.8;">
                A <strong>baseline 8-byte DES key</strong> is chosen. This can be either:
            </p>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>Randomly generated using cryptographically secure methods</li>
                <li>User-provided in hexadecimal format (16 hex characters)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="padding: 2rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.15), rgba(79, 172, 254, 0.05)); border-radius: 16px; border-left: 4px solid #4facfe; margin-bottom: 1.5rem; min-height: 200px;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #4facfe, #00f2fe); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin-right: 1rem;">3</div>
                <h3 style="margin: 0; color: #4facfe;">Candidate Key Generation</h3>
            </div>
            <p style="color: #b8c5d6; line-height: 1.8;">
                The simulator iterates through candidate keys by:
            </p>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>Keeping the <strong>high bits fixed</strong> (from baseline key)</li>
                <li>Varying only the <strong>lowest N bits</strong> from 0 to 2ᴺ-1</li>
                <li>Creating a manageable search space for demonstration</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with step_col2:
    st.markdown("""
        <div style="padding: 2rem; background: linear-gradient(135deg, rgba(240, 147, 251, 0.15), rgba(240, 147, 251, 0.05)); border-radius: 16px; border-left: 4px solid #f093fb; margin-bottom: 1.5rem; min-height: 200px;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #f093fb, #f5576c); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin-right: 1rem;">2</div>
                <h3 style="margin: 0; color: #f093fb;">Encryption</h3>
            </div>
            <p style="color: #b8c5d6; line-height: 1.8;">
                The plaintext is encrypted with the baseline key using:
            </p>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>DES algorithm</strong> in ECB mode</li>
                <li><strong>PKCS7 padding</strong> for proper block alignment</li>
                <li>This produces the <strong>target ciphertext</strong> to crack</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="padding: 2rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.15), rgba(250, 112, 154, 0.05)); border-radius: 16px; border-left: 4px solid #fa709a; margin-bottom: 1.5rem; min-height: 200px;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #fa709a, #fee140); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; margin-right: 1rem;">4</div>
                <h3 style="margin: 0; color: #fa709a;">Verification</h3>
            </div>
            <p style="color: #b8c5d6; line-height: 1.8;">
                For each candidate key:
            </p>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>Decrypt the target ciphertext</li>
                <li>Compare with original plaintext (post-unpadding)</li>
                <li>If match found → <strong>Key recovered!</strong></li>
                <li>If padding error → Wrong key, continue search</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Implementation Details
st.subheader("💻 Implementation Details")

impl_col1, impl_col2 = st.columns(2)

with impl_col1:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1); height: 100%;">
            <h4 style="color: #4facfe; margin-top: 0;">🔐 Cryptographic Library</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>PyCryptodome</strong> - Industry-standard crypto library</li>
                <li><strong>DES cipher</strong> - ECB mode for simplicity</li>
                <li><strong>PKCS7 padding</strong> - Ensures proper block size</li>
                <li><strong>Secure random</strong> - Cryptographically secure key generation</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with impl_col2:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1); height: 100%;">
            <h4 style="color: #f093fb; margin-top: 0;">⚡ Performance Optimizations</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>Exception handling</strong> - Catches invalid decryptions quickly</li>
                <li><strong>Progress updates</strong> - Batched UI updates (every 1/200th)</li>
                <li><strong>Early termination</strong> - Stops immediately when key found</li>
                <li><strong>Memory efficient</strong> - Processes keys one at a time</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Code Structure
st.markdown("""### 🔹 DES Utility Functions in Python""")
st.code("""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# 🔄 Convert integer to 8-byte key (for key generation)
def int_to_bytes64(value):
    # Converts integer to exactly 8 bytes (big-endian)
    return value.to_bytes(8, byteorder='big')

# 🔐 Encrypt plaintext using DES (ECB mode with PKCS7 padding)
def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded)
    # Return as hex string for readability
    return ciphertext.hex()

# 🔓 Decrypt ciphertext using DES (removes padding)
def des_decrypt(ciphertext_hex, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted.decode('utf-8')
""", language="python")


st.markdown("---")

# Key Functions
st.subheader("🔧 Core Functions")

func_col1, func_col2, func_col3 = st.columns(3)

with func_col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔒</div>
            <h4>des_encrypt()</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Encrypts plaintext using DES with PKCS7 padding in ECB mode</p>
        </div>
    """, unsafe_allow_html=True)

with func_col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔓</div>
            <h4>des_decrypt()</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Decrypts ciphertext and removes padding, validates key correctness</p>
        </div>
    """, unsafe_allow_html=True)

with func_col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center; height: 100%;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔄</div>
            <h4>int_to_bytes64()</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem;">Converts integer to 8-byte representation for key generation</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Performance Analysis
st.subheader("📊 Performance and Scaling")

st.markdown("""
    <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h4 style="color: #4facfe; margin-top: 0;">⏱️ Time Complexity Analysis</h4>
        <p style="color: #b8c5d6; line-height: 1.8; margin-bottom: 1.5rem;">
            The runtime of the brute-force attack is directly proportional to the keyspace size:
        </p>
        <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.3); border-radius: 8px; border-left: 4px solid #667eea;">
            <p style="color: #4facfe; font-family: 'JetBrains Mono', monospace; margin: 0; font-size: 1.1rem;">
                <strong>Time Complexity:</strong> O(2ᴺ)<br>
                <strong>Space Complexity:</strong> O(1)
            </p>
        </div>
        <br>
        <ul style="color: #b8c5d6; line-height: 1.8;">
            <li><strong>Linear growth</strong> with number of keys tested</li>
            <li><strong>Doubling N</strong> approximately doubles the search time</li>
            <li><strong>Average case:</strong> Key found at ~50% of keyspace</li>
            <li><strong>Worst case:</strong> Key is the last one tested</li>
            <li><strong>Best case:</strong> Key found immediately (very unlikely)</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Real-World Considerations
# st.subheader("🌐 Real-World Considerations")

# real_col1, real_col2 = st.columns(2)

# with real_col1:
#     st.markdown("""
#         <div style="padding: 2rem; background: rgba(102, 126, 234, 0.1); border-radius: 16px; border-left: 4px solid #667eea;">
#             <h4 style="color: #667eea; margin-top: 0;">⚠️ Simulation Limitations</h4>
#             <ul style="color: #b8c5d6; line-height: 1.8;">
#                 <li><strong>ECB mode</strong> - Simplified; real systems use CBC, CTR, GCM</li>
#                 <li><strong>No authentication</strong> - Real systems use HMAC or AEAD</li>
#                 <li><strong>Single-threaded</strong> - Production attacks use parallel processing</li>
#                 <li><strong>Known plaintext</strong> - We know what we're looking for</li>
#                 <li><strong>Python overhead</strong> - Much slower than optimized C/ASM</li>
#             </ul>
#         </div>
#     """, unsafe_allow_html=True)

# with real_col2:
#     st.markdown("""
#         <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border-left: 4px solid #f093fb;">
#             <h4 style="color: #f093fb; margin-top: 0;">🚀 Production Attack Techniques</h4>
#             <ul style="color: #b8c5d6; line-height: 1.8;">
#                 <li><strong>Distributed computing</strong> - Thousands of machines working in parallel</li>
#                 <li><strong>GPU acceleration</strong> - Massively parallel key testing</li>
#                 <li><strong>FPGA/ASIC</strong> - Custom hardware for speed</li>
#                 <li><strong>Rainbow tables</strong> - Precomputed hash lookups</li>
#                 <li><strong>Smart key ordering</strong> - Test likely keys first</li>
#             </ul>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# # Why DES was Broken
# st.subheader("💥 Historical Context: Breaking DES")

# st.markdown("""
#     <div style="padding: 2rem; background: rgba(250, 112, 154, 0.1); border-radius: 16px; border: 1px solid rgba(250, 112, 154, 0.3);">
#         <h4 style="color: #fa709a; margin-top: 0;">🏆 Notable DES Breaks</h4>
#         <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px; margin-bottom: 1rem;">
#             <p style="color: #b8c5d6; margin: 0;"><strong style="color: #4facfe;">1997 - DESCHALL Project:</strong> First public break using distributed computing (~96 days)</p>
#         </div>
#         <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px; margin-bottom: 1rem;">
#             <p style="color: #b8c5d6; margin: 0;"><strong style="color: #4facfe;">1998 - Deep Crack:</strong> EFF's custom hardware cracked DES in 56 hours</p>
#         </div>
#         <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px; margin-bottom: 1rem;">
#             <p style="color: #b8c5d6; margin: 0;"><strong style="color: #4facfe;">1999 - Combined Attack:</strong> Deep Crack + distributed.net broke DES in 22 hours</p>
#         </div>
#         <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px;">
#             <p style="color: #b8c5d6; margin: 0;"><strong style="color: #4facfe;">2006 - COPACOBANA:</strong> Custom FPGA machine cracked DES in ~7 days for $10,000</p>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("---")

# # Educational Value
# st.subheader("🎓 Educational Value")

# edu_col1, edu_col2, edu_col3 = st.columns(3)

# with edu_col1:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
#             <h4>Learn Concepts</h4>
#             <p style="color: #b8c5d6; font-size: 0.9rem;">Understand symmetric encryption and cryptanalysis fundamentals</p>
#         </div>
#     """, unsafe_allow_html=True)

# with edu_col2:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
#             <h4>Experiment</h4>
#             <p style="color: #b8c5d6; font-size: 0.9rem;">Test different keyspace sizes and observe exponential growth</p>
#         </div>
#     """, unsafe_allow_html=True)

# with edu_col3:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
#             <h4>Apply Knowledge</h4>
#             <p style="color: #b8c5d6; font-size: 0.9rem;">Understand why modern algorithms use larger key sizes</p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# # Important Notes
# st.info("""
#     💡 **Remember**: This is a simplified educational demonstration. Real-world cryptanalysis involves 
#     sophisticated techniques, massive computational resources, and often exploits implementation flaws 
#     rather than pure brute-force.
# """)

# st.warning("""
#     ⚠️ **Ethical Notice**: This tool is for educational purposes only. Unauthorized cryptanalysis of 
#     systems you don't own is illegal and unethical. Always obtain proper authorization before testing security.
# """)

st.markdown("---")

# Navigation
st.markdown("""
    <div style="text-align: center;">
        <p style="color: #b8c5d6;">Ready to try it yourself?</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔑 Start Encryption & Attack", use_container_width=True):
        st.switch_page("pages/04_Encryption_Simulation.py")