import streamlit as st

st.set_page_config(page_title="Conclusion", page_icon="✅", layout="wide")

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
#         <div style="font-size: 5rem; margin-bottom: 1rem;">✅</div>
#     </div>
# """, unsafe_allow_html=True)

st.title("Conclusion & Key Takeaways")

st.markdown("""
    <div style="font-size: 1.1rem; color: #b8c5d6; margin-bottom: 3rem;">
        Understanding the implications of cryptographic security through hands-on exploration
    </div>
""", unsafe_allow_html=True)

# Main Summary
st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(240, 147, 251, 0.1)); border-radius: 16px; border: 1px solid rgba(102, 126, 234, 0.3); margin-bottom: 3rem;">
        <h3 style="color: #667eea; margin-top: 0; text-align: center;">🎯 Project Summary</h3>
        <p style="color: #b8c5d6; line-height: 1.8; font-size: 1.1rem; text-align: center;">
            This interactive simulator demonstrates how brute-force attacks work against DES encryption, 
            revealing why key length is critical for cryptographic security and why DES has been replaced 
            by modern algorithms like AES.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Key Observations
st.subheader("🔍 Key Observations")

obs_col1, obs_col2 = st.columns(2)

with obs_col1:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(79, 172, 254, 0.1); border-radius: 16px; border-left: 4px solid #4facfe; height: 100%;">
            <h4 style="color: #4facfe; margin-top: 0;">📈 Exponential Time Growth</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li>Doubling N (variable bits) <strong>doubles the keyspace</strong></li>
                <li>Attack time grows <strong>exponentially</strong> with key length</li>
                <li>Even small increases in N create <strong>massive time differences</strong></li>
                <li>N=16 vs N=24 shows <strong>256× increase</strong> in search space</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with obs_col2:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border-left: 4px solid #f093fb; height: 100%;">
            <h4 style="color: #f093fb; margin-top: 0;">🔐 DES Limitations</h4>
            <ul style="color: #b8c5d6; line-height: 1.8;">
                <li><strong>56-bit key</strong> is insufficient for modern security needs</li>
                <li>Specialized hardware can crack DES in <strong>hours to days</strong></li>
                <li>Distributed computing makes attacks <strong>highly feasible</strong></li>
                <li>Officially deprecated and replaced by <strong>AES in 2001</strong></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Why Modern Algorithms Are Better
# st.subheader("🚀 Modern Cryptography Advantages")

# st.markdown("""
#     <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
#         <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
#             <div style="padding: 1.5rem; background: rgba(102, 126, 234, 0.1); border-radius: 12px; text-align: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">🔑</div>
#                 <h4 style="color: #667eea;">Larger Key Sizes</h4>
#                 <p style="color: #b8c5d6; font-size: 0.9rem;">AES-128: 2¹²⁸ keys<br>AES-256: 2²⁵⁶ keys</p>
#                 <p style="color: #4facfe; font-size: 0.8rem; margin-top: 1rem;">Computationally infeasible to brute-force</p>
#             </div>
            
#             <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
#                 <h4 style="color: #4facfe;">Better Performance</h4>
#                 <p style="color: #b8c5d6; font-size: 0.9rem;">Hardware acceleration<br>Efficient implementations</p>
#                 <p style="color: #4facfe; font-size: 0.8rem; margin-top: 1rem;">Faster encryption without sacrificing security</p>
#             </div>
            
#             <div style="padding: 1.5rem; background: rgba(240, 147, 251, 0.1); border-radius: 12px; text-align: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
#                 <h4 style="color: #f093fb;">Advanced Modes</h4>
#                 <p style="color: #b8c5d6; font-size: 0.9rem;">GCM, CBC, CTR modes<br>Authenticated encryption</p>
#                 <p style="color: #4facfe; font-size: 0.8rem; margin-top: 1rem;">Protection against various attack vectors</p>
#             </div>
            
#             <div style="padding: 1.5rem; background: rgba(250, 112, 154, 0.1); border-radius: 12px; text-align: center;">
#                 <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
#                 <h4 style="color: #fa709a;">Cryptanalysis Resistant</h4>
#                 <p style="color: #b8c5d6; font-size: 0.9rem;">No known practical attacks<br>Extensively analyzed</p>
#                 <p style="color: #4facfe; font-size: 0.8rem; margin-top: 1rem;">Decades of security research validation</p>
#             </div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("---")

# Educational Insights
st.subheader("🎓 Educational Insights")

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.2);">
            <h4 style="color: #4facfe; text-align: center;">💡 Understanding</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem; line-height: 1.6;">
                Hands-on experience with encryption demonstrates abstract concepts like 
                keyspace, computational complexity, and security margins in practical terms.
            </p>
        </div>
    """, unsafe_allow_html=True)

with insight_col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.2);">
            <h4 style="color: #4facfe; text-align: center;">🔬 Experimentation</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem; line-height: 1.6;">
                Testing different N values allows direct observation of exponential growth, 
                making mathematical concepts tangible and memorable.
            </p>
        </div>
    """, unsafe_allow_html=True)

with insight_col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.2);">
            <h4 style="color: #4facfe; text-align: center;">🎯 Application</h4>
            <p style="color: #b8c5d6; font-size: 0.9rem; line-height: 1.6;">
                Understanding why DES failed helps appreciate modern cryptographic choices 
                and the importance of future-proof security design.
            </p>
        </div>
    """, unsafe_allow_html=True)

# st.markdown("---")

# # Practical Takeaways
# st.subheader("✨ Practical Takeaways")

# st.markdown("""
#     <div style="padding: 2rem; background: rgba(102, 126, 234, 0.1); border-radius: 16px; border: 1px solid rgba(102, 126, 234, 0.3);">
#         <ol style="color: #b8c5d6; line-height: 2; font-size: 1.05rem;">
#             <li><strong style="color: #667eea;">Key Length Matters:</strong> Always use cryptographic algorithms with sufficiently large keys (AES-128 minimum, AES-256 preferred)</li>
#             <li><strong style="color: #667eea;">Algorithm Selection:</strong> Use modern, well-vetted algorithms like AES, ChaCha20, or approved alternatives</li>
#             <li><strong style="color: #667eea;">Regular Updates:</strong> Keep cryptographic libraries updated to patch vulnerabilities and implementation flaws</li>
#             <li><strong style="color: #667eea;">Defense in Depth:</strong> Combine encryption with authentication (AEAD modes like AES-GCM) for comprehensive protection</li>
#             <li><strong style="color: #667eea;">Future-Proofing:</strong> Consider post-quantum cryptography for long-term data protection needs</li>
#             <li><strong style="color: #667eea;">Ethical Practice:</strong> Use cryptographic knowledge responsibly and only on systems you're authorized to test</li>
#         </ol>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("---")

# Performance Comparison Table
st.subheader("⚖️ DES vs. Modern Algorithms")

comparison_col1, comparison_col2 = st.columns([1, 1])

with comparison_col1:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(250, 112, 154, 0.1); border-radius: 16px; border: 2px solid rgba(250, 112, 154, 0.3);">
            <h4 style="color: #fa709a; text-align: center; margin-top: 0;">❌ DES (Deprecated)</h4>
            <table style="width: 100%; color: #b8c5d6; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Key Size:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">56 bits</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Block Size:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">64 bits</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Keyspace:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">2⁵⁶</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Status:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">Broken</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;"><strong>Security:</strong></td>
                    <td style="padding: 0.75rem; text-align: right; color: #fa709a;">Obsolete</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

with comparison_col2:
    st.markdown("""
        <div style="padding: 2rem; background: rgba(79, 172, 254, 0.1); border-radius: 16px; border: 2px solid rgba(79, 172, 254, 0.3);">
            <h4 style="color: #4facfe; text-align: center; margin-top: 0;">✅ AES (Current Standard)</h4>
            <table style="width: 100%; color: #b8c5d6; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Key Size:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">128/192/256 bits</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Block Size:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">128 bits</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Keyspace:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">2¹²⁸ to 2²⁵⁶</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.75rem;"><strong>Status:</strong></td>
                    <td style="padding: 0.75rem; text-align: right;">Secure</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem;"><strong>Security:</strong></td>
                    <td style="padding: 0.75rem; text-align: right; color: #00f2fe;">Industry Standard</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Real-World Impact
st.subheader("🌍 Real-World Impact")

st.markdown("""
    <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border: 1px solid rgba(240, 147, 251, 0.3);">
        <p style="color: #b8c5d6; line-height: 1.8; font-size: 1.05rem;">
            The lessons learned from DES's vulnerabilities have shaped modern cryptographic practices:
        </p>
        <ul style="color: #b8c5d6; line-height: 1.8; font-size: 1.05rem;">
            <li>💳 <strong>Financial Systems:</strong> Banking and payment processors use AES-256 for transaction security</li>
            <li>🔒 <strong>HTTPS/TLS:</strong> Web security relies on modern ciphers with large key sizes</li>
            <li>📱 <strong>Mobile Devices:</strong> Smartphone encryption uses AES hardware acceleration</li>
            <li>☁️ <strong>Cloud Storage:</strong> Services like AWS and Azure encrypt data at rest with AES</li>
            <li>🛡️ <strong>Government:</strong> Classified information requires AES-256 (NSA Suite B)</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Future Directions
# st.subheader("🔮 Looking Ahead: Post-Quantum Cryptography")

# future_col1, future_col2 = st.columns(2)

# with future_col1:
#     st.markdown("""
#         <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1); height: 100%;">
#             <h4 style="color: #667eea; margin-top: 0;">🖥️ Quantum Threat</h4>
#             <p style="color: #b8c5d6; line-height: 1.8;">
#                 Quantum computers threaten current public-key cryptography (RSA, ECC) through algorithms like 
#                 Shor's algorithm. Symmetric algorithms like AES remain relatively secure with doubled key sizes.
#             </p>
#             <ul style="color: #b8c5d6; line-height: 1.6; font-size: 0.9rem;">
#                 <li>AES-128 → AES-256 for quantum resistance</li>
#                 <li>Post-quantum algorithms in development</li>
#                 <li>NIST standardization process ongoing</li>
#             </ul>
#         </div>
#     """, unsafe_allow_html=True)

# with future_col2:
#     st.markdown("""
#         <div style="padding: 2rem; background: rgba(255, 255, 255, 0.03); border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1); height: 100%;">
#             <h4 style="color: #4facfe; margin-top: 0;">🚀 Next Generation</h4>
#             <p style="color: #b8c5d6; line-height: 1.8;">
#                 The cryptographic community is preparing for the quantum era with lattice-based, code-based, 
#                 and hash-based cryptographic schemes designed to resist quantum attacks.
#             </p>
#             <ul style="color: #b8c5d6; line-height: 1.6; font-size: 0.9rem;">
#                 <li>CRYSTALS-Kyber (key encapsulation)</li>
#                 <li>CRYSTALS-Dilithium (signatures)</li>
#                 <li>Hybrid approaches (classical + PQC)</li>
#             </ul>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# Final Message
st.markdown("""
    <div style="padding: 3rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(240, 147, 251, 0.15)); border-radius: 16px; text-align: center; border: 2px solid rgba(102, 126, 234, 0.3);">
        <h2 style="color: #667eea; margin-top: 0;">🎯 Final Thoughts</h2>
        <p style="color: #b8c5d6; line-height: 1.8; font-size: 1.15rem; max-width: 800px; margin: 0 auto;">
            Cryptography is a constantly evolving field. What's secure today may not be secure tomorrow. 
            The transition from DES to AES demonstrates the importance of staying vigilant, updating systems, 
            and preparing for future threats. Use this knowledge responsibly to build more secure systems.
        </p>
        <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">
            <p style="color: #4facfe; font-size: 1.1rem; font-weight: 600; margin: 0;">
                Thank you for exploring the DES Brute-Force Simulator!
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Important Disclaimers
# disclaimer_col1, disclaimer_col2 = st.columns(2)

# with disclaimer_col1:
#     st.error("""
#         ⚠️ **Legal Notice**: This tool is strictly for educational purposes. Unauthorized access to 
#         computer systems or data is illegal. Always obtain proper authorization before security testing.
#     """)

# with disclaimer_col2:
#     st.info("""
#         📚 **For Learning Only**: This project demonstrates cryptographic concepts in a simplified environment. 
#         Production systems require professional security audits and proper implementation.
#     """)

# st.markdown("---")

# Additional Resources
# st.subheader("📖 Additional Resources")

# resource_col1, resource_col2, resource_col3 = st.columns(3)

# with resource_col1:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 2.5rem; margin-bottom: 1rem;">📘</div>
#             <h4>Learn More</h4>
#             <p style="color: #b8c5d6; font-size: 0.85rem;">
#                 • Applied Cryptography<br>
#                 • Cryptography Engineering<br>
#                 • Introduction to Modern Cryptography
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

# with resource_col2:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 2.5rem; margin-bottom: 1rem;">🌐</div>
#             <h4>Online Courses</h4>
#             <p style="color: #b8c5d6; font-size: 0.85rem;">
#                 • Coursera: Cryptography I<br>
#                 • MIT OpenCourseWare<br>
#                 • Crypto 101 by Laurens Van Houtven
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

# with resource_col3:
#     st.markdown("""
#         <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; text-align: center;">
#             <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔧</div>
#             <h4>Standards</h4>
#             <p style="color: #b8c5d6; font-size: 0.85rem;">
#                 • NIST Cryptographic Standards<br>
#                 • IETF RFC Documents<br>
#                 • OWASP Cryptographic Guidelines
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("---")

# Back to Home
st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <p style="color: #b8c5d6; font-size: 1.1rem;">Ready to explore again?</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("Home.py")