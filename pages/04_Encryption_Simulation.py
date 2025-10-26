# # pages/04_Encryption_Simulation.py
# import streamlit as st
# import time
# import base64
# from src.des_utils import des_encrypt, des_decrypt, int_to_bytes64, bytes_to_int64, generate_random_key

# st.set_page_config(page_title="Encryption, Decryption & Simulation — DES", page_icon="🔑")

# st.title("Encryption, Decryption & Simulation")

# # Create tabs for encryption/decryption and brute-force
# tab1, tab2 = st.tabs(["Encryption & Decryption", "Brute-Force Attack"])

# with tab1:
#     st.subheader("Encrypt/Decrypt Data with DES")
    
#     # Input for plaintext
#     plaintext_input = st.text_area("Enter plaintext to encrypt:", "Hello, this is a secret message!", key="combined_plaintext_input")
    
#     # Key options
#     key_mode_enc_dec = st.radio("Select key option:", ["Generate random key", "Enter hex key (16 hex chars)"], key="combined_key_mode_enc_dec")
    
#     if "combined_encryption_key" not in st.session_state:
#         st.session_state.combined_encryption_key = generate_random_key()
    
#     if key_mode_enc_dec.startswith("Generate"):
#         if st.button("🔄 Generate new key", key="combined_gen_enc_key"):
#             st.session_state.combined_encryption_key = generate_random_key()
#         combined_encryption_key = st.session_state.combined_encryption_key
#         st.code(f"Key (hex): {combined_encryption_key.hex()}")
#     else:
#         user_hex_enc_dec = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_enc_dec_hex_key")
#         if user_hex_enc_dec:
#             try:
#                 b = bytes.fromhex(user_hex_enc_dec)
#                 if len(b) == 8:
#                     combined_encryption_key = b
#                     st.session_state.combined_encryption_key = b
#                 else:
#                     st.error("Key must be exactly 8 bytes (16 hex chars).")
#                     combined_encryption_key = st.session_state.combined_encryption_key
#             except Exception:
#                 st.error("Invalid hex key.")
#                 combined_encryption_key = st.session_state.combined_encryption_key
#         else:
#             combined_encryption_key = st.session_state.combined_encryption_key
#             st.info("Using generated key until you provide a valid hex key.")
#             st.code(f"Key (hex): {combined_encryption_key.hex()}")
    
#     # Encrypt button
#     if st.button("🔒 Encrypt", key="combined_encrypt_btn"):
#         try:
#             plaintext_bytes = plaintext_input.encode("utf-8")
#             ciphertext_combined = des_encrypt(plaintext_bytes, combined_encryption_key)
            
#             st.success("Encryption successful!")
#             st.write("Ciphertext (hex):")
#             st.code(ciphertext_combined.hex())
            
#             base64_output_combined = base64.b64encode(ciphertext_combined).decode("utf-8")
#             st.write("Ciphertext (Base64):")
#             st.code(base64_output_combined)
            
#             st.session_state.combined_last_ciphertext = ciphertext_combined
#             st.session_state.combined_last_key = combined_encryption_key
            
#         except Exception as e:
#             st.error(f"Encryption failed: {str(e)}")

#     st.markdown("---")
#     st.subheader("Decrypt Data with DES")
    
#     input_format_dec = st.radio("Ciphertext format:", ["Hex", "Base64"], key="combined_input_format_dec")
    
#     ciphertext_input_dec = st.text_area("Enter ciphertext to decrypt:", 
#                                     value="" if "combined_last_ciphertext" not in st.session_state 
#                                     else (st.session_state.combined_last_ciphertext.hex() if input_format_dec == "Hex" 
#                                           else base64.b64encode(st.session_state.combined_last_ciphertext).decode("utf-8")), key="combined_ciphertext_input_dec")
    
#     key_mode_dec_combined = st.radio("Select key option:", ["Use last encryption key", "Enter hex key (16 hex chars)"], key="combined_dec_key_mode")
    
#     if key_mode_dec_combined.startswith("Use") and "combined_last_key" in st.session_state:
#         combined_decryption_key = st.session_state.combined_last_key
#         st.code(f"Key (hex): {combined_decryption_key.hex()}")
#     else:
#         user_hex_dec_combined = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_dec_hex_key")
#         if user_hex_dec_combined:
#             try:
#                 b = bytes.fromhex(user_hex_dec_combined)
#                 if len(b) == 8:
#                     combined_decryption_key = b
#                 else:
#                     st.error("Key must be exactly 8 bytes (16 hex chars).")
#                     combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
#             except Exception:
#                 st.error("Invalid hex key.")
#                 combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
#         elif "combined_last_key" in st.session_state:
#             combined_decryption_key = st.session_state.combined_last_key
#             st.code(f"Key (hex): {combined_decryption_key.hex()}")
#         else:
#             st.error("Please enter a valid key.")
#             combined_decryption_key = None
    
#     if st.button("🔓 Decrypt", key="combined_decrypt_btn"):
#         if not ciphertext_input_dec:
#             st.error("Please enter ciphertext to decrypt.")
#         elif combined_decryption_key is None:
#             st.error("Please provide a valid decryption key.")
#         else:
#             try:
#                 if input_format_dec == "Hex":
#                     try:
#                         ciphertext_bytes_dec = bytes.fromhex(ciphertext_input_dec)
#                     except ValueError:
#                         st.error("Invalid hex format. Please check your input.")
#                         st.stop()
#                 else:  # Base64
#                     try:
#                         ciphertext_bytes_dec = base64.b64decode(ciphertext_input_dec)
#                     except Exception:
#                         st.error("Invalid Base64 format. Please check your input.")
#                         st.stop()
                
#                 plaintext_dec = des_decrypt(ciphertext_bytes_dec, combined_decryption_key)
                
#                 st.success("Decryption successful!")
#                 st.write("Plaintext:")
                
#                 try:
#                     decoded_text_dec = plaintext_dec.decode("utf-8")
#                     st.code(decoded_text_dec)
#                 except UnicodeDecodeError:
#                     st.warning("The decrypted data is not valid UTF-8 text. Showing as hex:")
#                     st.code(plaintext_dec.hex())
                    
#             except Exception as e:
#                 st.error(f"Decryption failed: {str(e)}")
#                 st.info("This could be due to an incorrect key or corrupted ciphertext.")

# with tab2:
#     st.subheader("DES Brute-Force Attack Simulation")
#     st.markdown("""
#         This section allows you to simulate a brute-force attack on DES. 
#         You can define a plaintext, a baseline key, and the number of variable bits (N) 
#         to limit the search space for the brute-force attempt.
#     """)

#     plaintext_text = st.text_area("Plaintext to encrypt:", "Attack at dawn", key="combined_brute_force_plaintext")
#     plaintext = plaintext_text.encode("utf-8")

#     key_mode = st.radio("Baseline key selection:", ["Generate random baseline key", "Enter hex key (16 hex chars)"], key="combined_brute_force_key_mode")

#     if "combined_baseline_key" not in st.session_state:
#         st.session_state.combined_baseline_key = generate_random_key()

#     if key_mode.startswith("Generate"):
#         if st.button("🔄 Generate new baseline key", key="combined_brute_force_gen_key"):
#             st.session_state.combined_baseline_key = generate_random_key()
#         baseline_key = st.session_state.combined_baseline_key
#         st.code(f"Baseline key (hex): {baseline_key.hex()}")
#     else:
#         user_hex = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_brute_force_user_hex")
#         if user_hex:
#             try:
#                 b = bytes.fromhex(user_hex)
#                 if len(b) == 8:
#                     baseline_key = b
#                     st.session_state.combined_baseline_key = b
#                 else:
#                     st.error("Key must be exactly 8 bytes (16 hex chars).")
#                     baseline_key = st.session_state.combined_baseline_key
#             except Exception:
#                 st.error("Invalid hex key.")
#                 baseline_key = st.session_state.combined_baseline_key
#         else:
#             baseline_key = st.session_state.combined_baseline_key
#             st.info("Using generated baseline key until you provide a valid hex key.")
#             st.code(f"Baseline key (hex): {baseline_key.hex()}")

#     st.write("The plaintext will be encrypted with the baseline key to produce the target ciphertext for the brute-force attack.")
#     ciphertext = des_encrypt(plaintext, baseline_key)
#     st.code(f"Ciphertext (hex): {ciphertext.hex()}")

#     N = st.number_input("Number of variable bits to brute-force (N)", min_value=8, max_value=24, value=16, step=1, key="combined_brute_force_N")
#     show_progress = st.checkbox("Show live progress (slower)", value=True, key="combined_brute_force_show_progress")

#     st.markdown("---")

#     if st.button("🚀 Start brute-force attack", key="combined_brute_force_start_btn"):
#         st.info("Starting brute-force. Keep N small for interactive runs.")

#         target_ct = ciphertext
#         target_plain = plaintext
#         base_int = bytes_to_int64(baseline_key)
#         mask = (1 << N) - 1
#         base_prefix = base_int & (~mask)

#         start_time = time.time()
#         found = False
#         attempts = 0
#         total = 1 << N

#         progress_bar = st.progress(0) if show_progress else None
#         progress_text = st.empty() if show_progress else None

#         # iterate
#         update_every = max(1, total // 200)
#         for k in range(total):
#             attempts += 1
#             candidate_int = base_prefix | k
#             candidate_key = int_to_bytes64(candidate_int)
#             try:
#                 pt = des_decrypt(target_ct, candidate_key)
#                 if pt == target_plain:
#                     elapsed = time.time() - start_time
#                     st.success(f"Key found after {attempts:,} attempts in {elapsed:.3f} s")
#                     st.code(f"Recovered key (hex): {candidate_key.hex()}")
#                     found = True
#                     break
#             except Exception:
#                 # Bad padding or wrong key — ignore
#                 pass

#             if show_progress and (k % update_every == 0):
#                 progress = int((k / float(total)) * 100)
#                 progress_bar.progress(min(progress, 100))
#                 progress_text.text(f"Attempts: {attempts:,} / {total:,} ({progress}%)")

#         if not found:
#             elapsed = time.time() - start_time
#             st.warning(f"Key NOT found after exhausting the toy keyspace. Attempts: {attempts:,}. Time: {elapsed:.3f}s")

# st.markdown("---")
# st.caption("Note: DES uses a 56-bit key (8 bytes with parity bits) and operates on 64-bit blocks.")
# st.caption("For secure communications, consider using modern algorithms like AES instead of DES.")









# pages/04_Encryption_Simulation.py
import streamlit as st
import time
import base64
from src.des_utils import des_encrypt, des_decrypt, int_to_bytes64, bytes_to_int64, generate_random_key

st.set_page_config(page_title="Encryption & Simulation — DES", page_icon="🔑", layout="wide")

# Load Custom CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# Epic Hero Section with Animation
st.markdown("""
    <div style="text-align: center; padding: 3rem 0 2rem 0; position: relative;">
        <div style="font-size: 6rem; margin-bottom: 1rem; animation: float 3s ease-in-out infinite;">🔑</div>
        <h1 style="font-size: 3.5rem; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: titleShine 3s ease-in-out infinite;">
            Encryption & Attack Simulator
        </h1>
        <p style="font-size: 1.3rem; color: #b8c5d6; margin-top: 1rem; font-weight: 300;">
            Experience the power of DES encryption and witness real-time brute-force attacks
        </p>
    </div>
    
    <style>
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        @keyframes titleShine {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }
    </style>
""", unsafe_allow_html=True)

# Statistics Dashboard
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(102, 126, 234, 0.05)); border-radius: 16px; text-align: center; border: 1px solid rgba(102, 126, 234, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔐</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #667eea; font-family: 'JetBrains Mono', monospace;">56-bit</div>
            <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">DES Key Size</div>
        </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(79, 172, 254, 0.05)); border-radius: 16px; text-align: center; border: 1px solid rgba(79, 172, 254, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #4facfe; font-family: 'JetBrains Mono', monospace;">64-bit</div>
            <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Block Size</div>
        </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(240, 147, 251, 0.2), rgba(240, 147, 251, 0.05)); border-radius: 16px; text-align: center; border: 1px solid rgba(240, 147, 251, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎯</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #f093fb; font-family: 'JetBrains Mono', monospace;">DES</div>
            <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Encryption Std</div>
        </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
        <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.2), rgba(250, 112, 154, 0.05)); border-radius: 16px; text-align: center; border: 1px solid rgba(250, 112, 154, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔬</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #fa709a; font-family: 'JetBrains Mono', monospace;">PKCS7</div>
            <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Padding</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Enhanced Tabs with Icons
tab1, tab2 = st.tabs(["🔐 Encryption & Decryption Lab", "⚡ Brute-Force Attack Arena"])

with tab1:
    # Encryption Section with Grand Header
    st.markdown("""
        <div style="padding: 2.5rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.15)); border-radius: 20px; margin-bottom: 2rem; border: 2px solid rgba(102, 126, 234, 0.4); box-shadow: 0 10px 40px rgba(102, 126, 234, 0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 3rem; margin-right: 1rem;">🔒</div>
                <div>
                    <h2 style="margin: 0; color: #667eea; font-size: 2rem;">Encryption Laboratory</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #b8c5d6; font-size: 1.1rem;">Transform plaintext into secure ciphertext using DES encryption</p>
                </div>
            </div>
            <div style="padding: 1rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px; border-left: 4px solid #667eea;">
                <p style="color: #b8c5d6; margin: 0; line-height: 1.6;">
                    <strong>How it works:</strong> Your plaintext is encrypted using the Data Encryption Standard (DES) algorithm with your chosen key. 
                    The output can be viewed in both hexadecimal and Base64 formats for maximum compatibility.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Plaintext Input with Beautiful Styling
    st.markdown("""
        <div style="margin-bottom: 1rem;">
            <label style="font-size: 1.1rem; font-weight: 600; color: #667eea; display: block; margin-bottom: 0.5rem;">
                📝 Enter Your Secret Message
            </label>
        </div>
    """, unsafe_allow_html=True)
    
    plaintext_input = st.text_area(
        "",
        "Hello, this is a secret message!", 
        key="combined_plaintext_input",
        height=120,
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Configuration Section
    st.markdown("""
        <div style="padding: 2rem; background: rgba(79, 172, 254, 0.1); border-radius: 16px; border: 1px solid rgba(79, 172, 254, 0.3); margin-bottom: 2rem;">
            <h3 style="color: #4facfe; margin-top: 0; display: flex; align-items: center;">
                <span style="font-size: 2rem; margin-right: 0.5rem;">🔑</span>
                Encryption Key Configuration
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    key_col1, key_col2 = st.columns([1, 2])
    
    with key_col1:
        key_mode_enc_dec = st.radio(
            "Key Source:", 
            ["🎲 Generate random key", "✏️ Enter custom hex key"], 
            key="combined_key_mode_enc_dec"
        )
    
    with key_col2:
        if "combined_encryption_key" not in st.session_state:
            st.session_state.combined_encryption_key = generate_random_key()
        
        if key_mode_enc_dec.startswith("🎲"):
            st.markdown("""
                <div style="padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 8px; margin-bottom: 1rem;">
                    <p style="color: #b8c5d6; margin: 0; font-size: 0.9rem;">
                        🔒 Using cryptographically secure random key generation
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Generate New Random Key", key="combined_gen_enc_key", use_container_width=True):
                st.session_state.combined_encryption_key = generate_random_key()
                st.success("✨ New key generated successfully!")
            
            combined_encryption_key = st.session_state.combined_encryption_key
            
            st.markdown("**Current Key (Hexadecimal):**")
            st.code(f"{combined_encryption_key.hex()}", language="bash")
        else:
            st.markdown("""
                <div style="padding: 1rem; background: rgba(240, 147, 251, 0.1); border-radius: 8px; margin-bottom: 1rem;">
                    <p style="color: #b8c5d6; margin: 0; font-size: 0.9rem;">
                        ✏️ Enter your custom 8-byte key in hexadecimal format (16 characters)
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            user_hex_enc_dec = st.text_input(
                "Hex Key (16 characters)", 
                placeholder="Example: 0123456789abcdef",
                key="combined_enc_dec_hex_key"
            )
            if user_hex_enc_dec:
                try:
                    b = bytes.fromhex(user_hex_enc_dec)
                    if len(b) == 8:
                        combined_encryption_key = b
                        st.session_state.combined_encryption_key = b
                        st.success("✅ Valid key accepted!")
                    else:
                        st.error("❌ Key must be exactly 8 bytes (16 hex characters)")
                        combined_encryption_key = st.session_state.combined_encryption_key
                except Exception:
                    st.error("❌ Invalid hexadecimal format")
                    combined_encryption_key = st.session_state.combined_encryption_key
            else:
                combined_encryption_key = st.session_state.combined_encryption_key
                st.info("💡 Using generated key until you provide a valid hex key")
                st.code(f"{combined_encryption_key.hex()}", language="bash")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Encrypt Button - Grand Style
    encrypt_col1, encrypt_col2, encrypt_col3 = st.columns([1, 2, 1])
    with encrypt_col2:
        encrypt_clicked = st.button(
            "🔒 ENCRYPT MESSAGE", 
            key="combined_encrypt_btn", 
            use_container_width=True,
            type="primary"
        )
    
    if encrypt_clicked:
        try:
            with st.spinner("🔄 Encrypting your message..."):
                time.sleep(0.5)
                plaintext_bytes = plaintext_input.encode("utf-8")
                ciphertext_combined = des_encrypt(plaintext_bytes, combined_encryption_key)
                
                st.markdown("""
                    <div style="padding: 2rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.1)); border-radius: 16px; margin: 2rem 0; border: 2px solid #4facfe; text-align: center; animation: successPulse 1s ease-in-out;">
                        <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                        <h3 style="color: #00f2fe; margin: 0;">Encryption Successful!</h3>
                        <p style="color: #b8c5d6; margin-top: 0.5rem;">Your message has been securely encrypted</p>
                    </div>
                    <style>
                        @keyframes successPulse {
                            0% { transform: scale(0.95); opacity: 0; }
                            50% { transform: scale(1.02); }
                            100% { transform: scale(1); opacity: 1; }
                        }
                    </style>
                """, unsafe_allow_html=True)
                
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    st.markdown("""
                        <div style="padding: 1.5rem; background: rgba(102, 126, 234, 0.1); border-radius: 12px; border: 1px solid rgba(102, 126, 234, 0.3);">
                            <h4 style="color: #667eea; margin-top: 0;">🔢 Hexadecimal Output</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    st.code(ciphertext_combined.hex(), language="bash")
                    
                with result_col2:
                    base64_output_combined = base64.b64encode(ciphertext_combined).decode("utf-8")
                    st.markdown("""
                        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.3);">
                            <h4 style="color: #4facfe; margin-top: 0;">📦 Base64 Output</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    st.code(base64_output_combined, language="bash")
                
                st.session_state.combined_last_ciphertext = ciphertext_combined
                st.session_state.combined_last_key = combined_encryption_key
                
        except Exception as e:
            st.error(f"❌ Encryption failed: {str(e)}")

    st.markdown("---")
    
    # Decryption Section with Grand Header
    st.markdown("""
        <div style="padding: 2.5rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.15), rgba(0, 242, 254, 0.15)); border-radius: 20px; margin-bottom: 2rem; border: 2px solid rgba(79, 172, 254, 0.4); box-shadow: 0 10px 40px rgba(79, 172, 254, 0.2);">
            <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
                <div style="font-size: 3rem; margin-right: 1rem;">🔓</div>
                <div>
                    <h2 style="margin: 0; color: #4facfe; font-size: 2rem;">Decryption Laboratory</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #b8c5d6; font-size: 1.1rem;">Recover the original plaintext from encrypted ciphertext</p>
                </div>
            </div>
            <div style="padding: 1rem; background: rgba(0, 0, 0, 0.2); border-radius: 8px; border-left: 4px solid #4facfe;">
                <p style="color: #b8c5d6; margin: 0; line-height: 1.6;">
                    <strong>How it works:</strong> Provide the ciphertext and the correct decryption key to recover your original message. 
                    Supports both hexadecimal and Base64 input formats.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    input_format_dec = st.radio(
        "📋 Ciphertext Input Format:", 
        ["🔢 Hexadecimal", "📦 Base64"], 
        key="combined_input_format_dec",
        horizontal=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    ciphertext_input_dec = st.text_area(
        "🔐 Enter Ciphertext to Decrypt:", 
        value="" if "combined_last_ciphertext" not in st.session_state 
        else (st.session_state.combined_last_ciphertext.hex() if input_format_dec.startswith("🔢") 
              else base64.b64encode(st.session_state.combined_last_ciphertext).decode("utf-8")), 
        key="combined_ciphertext_input_dec",
        height=120
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Decryption Key Section
    st.markdown("""
        <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border: 1px solid rgba(240, 147, 251, 0.3); margin-bottom: 2rem;">
            <h3 style="color: #f093fb; margin-top: 0; display: flex; align-items: center;">
                <span style="font-size: 2rem; margin-right: 0.5rem;">🔑</span>
                Decryption Key Configuration
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    dec_key_col1, dec_key_col2 = st.columns([1, 2])
    
    with dec_key_col1:
        key_mode_dec_combined = st.radio(
            "Key Source:", 
            ["🔄 Use last encryption key", "✏️ Enter custom hex key"], 
            key="combined_dec_key_mode"
        )
    
    with dec_key_col2:
        if key_mode_dec_combined.startswith("🔄") and "combined_last_key" in st.session_state:
            combined_decryption_key = st.session_state.combined_last_key
            st.markdown("**Using Previous Encryption Key:**")
            st.code(f"{combined_decryption_key.hex()}", language="bash")
        else:
            user_hex_dec_combined = st.text_input(
                "Hex Key (16 characters)", 
                placeholder="Example: 0123456789abcdef",
                key="combined_dec_hex_key"
            )
            if user_hex_dec_combined:
                try:
                    b = bytes.fromhex(user_hex_dec_combined)
                    if len(b) == 8:
                        combined_decryption_key = b
                        st.success("✅ Valid key accepted!")
                    else:
                        st.error("❌ Key must be exactly 8 bytes (16 hex characters)")
                        combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
                except Exception:
                    st.error("❌ Invalid hexadecimal format")
                    combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
            elif "combined_last_key" in st.session_state:
                combined_decryption_key = st.session_state.combined_last_key
                st.info("💡 Using last encryption key")
                st.code(f"{combined_decryption_key.hex()}", language="bash")
            else:
                st.error("⚠️ Please enter a valid key")
                combined_decryption_key = None
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Decrypt Button
    decrypt_col1, decrypt_col2, decrypt_col3 = st.columns([1, 2, 1])
    with decrypt_col2:
        decrypt_clicked = st.button(
            "🔓 DECRYPT MESSAGE", 
            key="combined_decrypt_btn", 
            use_container_width=True,
            type="primary"
        )
    
    if decrypt_clicked:
        if not ciphertext_input_dec:
            st.error("❌ Please enter ciphertext to decrypt")
        elif combined_decryption_key is None:
            st.error("❌ Please provide a valid decryption key")
        else:
            try:
                with st.spinner("🔄 Decrypting your message..."):
                    time.sleep(0.5)
                    if input_format_dec.startswith("🔢"):
                        try:
                            ciphertext_bytes_dec = bytes.fromhex(ciphertext_input_dec)
                        except ValueError:
                            st.error("Invalid hex format. Please check your input.")
                            st.stop()
                    else:
                        try:
                            ciphertext_bytes_dec = base64.b64decode(ciphertext_input_dec)
                        except Exception:
                            st.error("Invalid Base64 format. Please check your input.")
                            st.stop()
                    
                    plaintext_dec = des_decrypt(ciphertext_bytes_dec, combined_decryption_key)
                    
                    st.markdown("""
                        <div style="padding: 2rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.1)); border-radius: 16px; margin: 2rem 0; border: 2px solid #4facfe; text-align: center; animation: successPulse 1s ease-in-out;">
                            <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                            <h3 style="color: #00f2fe; margin: 0;">Decryption Successful!</h3>
                            <p style="color: #b8c5d6; margin-top: 0.5rem;">Your original message has been recovered</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("""
                        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border: 1px solid rgba(79, 172, 254, 0.3); margin-bottom: 1rem;">
                            <h4 style="color: #4facfe; margin-top: 0;">📝 Recovered Plaintext:</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    try:
                        decoded_text_dec = plaintext_dec.decode("utf-8")
                        st.code(decoded_text_dec, language="text")
                    except UnicodeDecodeError:
                        st.warning("⚠️ Decrypted data is not valid UTF-8 text. Showing as hexadecimal:")
                        st.code(plaintext_dec.hex(), language="bash")
                        
            except Exception as e:
                st.error(f"❌ Decryption failed: {str(e)}")
                st.info("💡 This could be due to an incorrect key or corrupted ciphertext")

with tab2:
    # Brute-Force Grand Header
    st.markdown("""
        <div style="padding: 3rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.2), rgba(254, 225, 64, 0.15)); border-radius: 24px; margin-bottom: 3rem; border: 2px solid rgba(250, 112, 154, 0.5); box-shadow: 0 15px 50px rgba(250, 112, 154, 0.3); position: relative; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #fa709a, #fee140, #fa709a); animation: shimmer 2s linear infinite;"></div>
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
                <div style="font-size: 4rem; margin-right: 1.5rem; animation: pulse 2s ease-in-out infinite;">⚡</div>
                <div style="text-align: center;">
                    <h2 style="margin: 0; color: #fa709a; font-size: 2.5rem; text-shadow: 0 0 20px rgba(250, 112, 154, 0.5);">Brute-Force Attack Arena</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #b8c5d6; font-size: 1.2rem;">Witness the power of computational cryptanalysis</p>
                </div>
            </div>
            <div style="padding: 1.5rem; background: rgba(0, 0, 0, 0.3); border-radius: 12px; border-left: 4px solid #fa709a;">
                <p style="color: #b8c5d6; margin: 0; line-height: 1.8; font-size: 1.05rem;">
                    <strong>⚠️ Warning:</strong> This simulation demonstrates a brute-force attack by systematically testing candidate keys 
                    until the correct one is found. Configure your baseline key and variable bits (N) to control the search space complexity.
                </p>
            </div>
        </div>
        <style>
            @keyframes shimmer {
                0% { background-position: -100% 0; }
                100% { background-position: 100% 0; }
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.1); }
            }
        </style>
    """, unsafe_allow_html=True)

    # Configuration Grid
    config_col1, config_col2 = st.columns([2, 1])
    
    with config_col1:
        st.markdown("""
            <div style="padding: 1.5rem; background: rgba(102, 126, 234, 0.1); border-radius: 12px; border: 1px solid rgba(102, 126, 234, 0.3); margin-bottom: 1rem;">
                <h4 style="color: #667eea; margin-top: 0;">📝 Target Plaintext</h4>
                <p style="color: #b8c5d6; font-size: 0.9rem; margin: 0;">This message will be encrypted with the baseline key</p>
            </div>
        """, unsafe_allow_html=True)
        
        plaintext_text = st.text_area(
            "",
            "Attack at dawn", 
            key="combined_brute_force_plaintext",
            height=100,
            label_visibility="collapsed"
        )

    # Encode plaintext outside the column context
    plaintext_brute = plaintext_text.encode("utf-8")

    with config_col2:
        st.markdown("""
            <div style="padding: 1.5rem; background: rgba(240, 147, 251, 0.1); border-radius: 12px; border: 1px solid rgba(240, 147, 251, 0.3); margin-bottom: 1rem;">
                <h4 style="color: #f093fb; margin-top: 0;">🎯 Attack Parameters</h4>
                <p style="color: #b8c5d6; font-size: 0.9rem; margin: 0;">Variable bits to brute-force</p>
            </div>
        """, unsafe_allow_html=True)
        
        N = st.number_input(
            "",
            min_value=8, 
            max_value=24, 
            value=16, 
            step=1, 
            key="combined_brute_force_N",
            label_visibility="collapsed"
        )
        
        keyspace_size = 1 << N
        st.markdown(f"""
            <div style="padding: 1.5rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.1)); border-radius: 12px; text-align: center; border: 2px solid rgba(102, 126, 234, 0.4); margin-top: 1rem;">
                <p style="color: #667eea; font-weight: bold; margin: 0; font-size: 0.9rem;">KEYSPACE SIZE</p>
                <p style="color: #4facfe; font-size: 2rem; margin: 0.5rem 0; font-family: 'JetBrains Mono', monospace; font-weight: bold;">{keyspace_size:,}</p>
                <p style="color: #b8c5d6; font-size: 0.85rem; margin: 0;">possible keys to test</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Configuration
    st.markdown("""
        <div style="padding: 2rem; background: rgba(79, 172, 254, 0.1); border-radius: 16px; border: 1px solid rgba(79, 172, 254, 0.3); margin-bottom: 2rem;">
            <h3 style="color: #4facfe; margin-top: 0; display: flex; align-items: center;">
                <span style="font-size: 2rem; margin-right: 0.5rem;">🔑</span>
                Baseline Key Configuration
            </h3>
            <p style="color: #b8c5d6; margin: 0; line-height: 1.6;">The attack will vary only the lowest N bits of this baseline key</p>
        </div>
    """, unsafe_allow_html=True)

    key_mode = st.radio(
        "🎲 Key Generation Method:", 
        ["Generate random baseline key", "Enter hex key (16 hex chars)"], 
        key="combined_brute_force_key_mode"
    )

    if "combined_baseline_key" not in st.session_state:
        st.session_state.combined_baseline_key = generate_random_key()

    key_config_col1, key_config_col2 = st.columns([1, 2])
    
    with key_config_col1:
        if key_mode.startswith("Generate"):
            if st.button("🔄 Generate New Baseline Key", key="combined_brute_force_gen_key", use_container_width=True):
                st.session_state.combined_baseline_key = generate_random_key()
                st.success("✨ New baseline key generated!")
    
    with key_config_col2:
        if key_mode.startswith("Generate"):
            baseline_key = st.session_state.combined_baseline_key
            st.markdown("**Current Baseline Key (Hexadecimal):**")
            st.code(f"{baseline_key.hex()}", language="bash")
        else:
            user_hex = st.text_input(
                "Enter 16-character hex key", 
                placeholder="Example: 0123456789abcdef",
                key="combined_brute_force_user_hex"
            )
            if user_hex:
                try:
                    b = bytes.fromhex(user_hex)
                    if len(b) == 8:
                        baseline_key = b
                        st.session_state.combined_baseline_key = b
                        st.success("✅ Valid baseline key accepted!")
                    else:
                        st.error("❌ Key must be exactly 8 bytes (16 hex characters)")
                        baseline_key = st.session_state.combined_baseline_key
                except Exception:
                    st.error("❌ Invalid hexadecimal format")
                    baseline_key = st.session_state.combined_baseline_key
            else:
                baseline_key = st.session_state.combined_baseline_key
                st.info("💡 Using generated baseline key until you provide a valid hex key")
                st.code(f"{baseline_key.hex()}", language="bash")

    st.markdown("<br>", unsafe_allow_html=True)

    # Target Ciphertext Display
    st.markdown("""
        <div style="padding: 2rem; background: rgba(240, 147, 251, 0.1); border-radius: 16px; border: 1px solid rgba(240, 147, 251, 0.3); margin-bottom: 2rem;">
            <h3 style="color: #f093fb; margin-top: 0; display: flex; align-items: center;">
                <span style="font-size: 2rem; margin-right: 0.5rem;">🎯</span>
                Target Ciphertext
            </h3>
            <p style="color: #b8c5d6; margin-bottom: 1rem;">This is the encrypted version that the attack will attempt to crack</p>
        </div>
    """, unsafe_allow_html=True)
    
    ciphertext = des_encrypt(plaintext_brute, baseline_key)
    st.code(ciphertext.hex(), language="bash")

    st.markdown("<br>", unsafe_allow_html=True)

    # Attack Options
    show_progress = st.checkbox(
        "📊 Enable Live Progress Visualization (may slow down attack)", 
        value=True, 
        key="combined_brute_force_show_progress"
    )

    st.markdown("---")

    # Launch Attack Button
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <p style="color: #b8c5d6; font-size: 1.2rem; margin-bottom: 1.5rem;">
                ⚠️ Ready to launch the brute-force attack?
            </p>
        </div>
    """, unsafe_allow_html=True)

    attack_btn_col1, attack_btn_col2, attack_btn_col3 = st.columns([1, 2, 1])
    with attack_btn_col2:
        start_attack = st.button(
            "🚀 LAUNCH BRUTE-FORCE ATTACK", 
            key="combined_brute_force_start_btn", 
            use_container_width=True,
            type="primary"
        )

    if start_attack:
        st.info("Starting brute-force. Keep N small for interactive runs.")
        
        # Attack Initiated Banner
        st.markdown("""
            <div style="padding: 2.5rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.3), rgba(254, 225, 64, 0.2)); border-radius: 16px; margin: 2rem 0; border: 2px solid #fa709a; text-align: center; animation: attackStart 1s ease-in-out;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">⚔️</div>
                <h2 style="color: #fa709a; margin: 0; font-size: 2rem;">Attack Initiated</h2>
                <p style="color: #b8c5d6; margin-top: 0.5rem; font-size: 1.1rem;">Testing candidate keys sequentially...</p>
            </div>
            <style>
                @keyframes attackStart {
                    0% { transform: scale(0.9); opacity: 0; }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); opacity: 1; }
                }
            </style>
        """, unsafe_allow_html=True)

        target_ct = ciphertext
        target_plain = plaintext_brute
        base_int = bytes_to_int64(baseline_key)
        mask = (1 << N) - 1
        base_prefix = base_int & (~mask)

        start_time = time.time()
        found = False
        attempts = 0
        total = 1 << N

        # Progress Display Setup
        progress_bar = st.progress(0) if show_progress else None
        progress_text = st.empty() if show_progress else None

        # Attack Loop
        update_every = max(1, total // 200)
        for k in range(total):
            attempts += 1
            candidate_int = base_prefix | k
            candidate_key = int_to_bytes64(candidate_int)
            
            try:
                pt = des_decrypt(target_ct, candidate_key)
                if pt == target_plain:
                    elapsed = time.time() - start_time
                    
                    # SUCCESS ANIMATION
                    st.markdown("""
                        <div style="padding: 3rem; background: linear-gradient(135deg, rgba(79, 172, 254, 0.3), rgba(0, 242, 254, 0.2)); border-radius: 20px; margin: 2rem 0; border: 3px solid #00f2fe; text-align: center; animation: victoryPulse 1.5s ease-in-out; box-shadow: 0 0 50px rgba(0, 242, 254, 0.5);">
                            <div style="font-size: 5rem; margin-bottom: 1rem; animation: bounce 1s ease-in-out;">🎉</div>
                            <h1 style="color: #00f2fe; margin: 0; font-size: 3rem; text-shadow: 0 0 30px rgba(0, 242, 254, 0.8);">KEY RECOVERED!</h1>
                            <p style="color: #b8c5d6; margin-top: 1rem; font-size: 1.3rem;">The brute-force attack was successful!</p>
                        </div>
                        <style>
                            @keyframes victoryPulse {
                                0%, 100% { transform: scale(1); }
                                25% { transform: scale(1.05); }
                                50% { transform: scale(0.98); }
                                75% { transform: scale(1.02); }
                            }
                            @keyframes bounce {
                                0%, 100% { transform: translateY(0); }
                                50% { transform: translateY(-20px); }
                            }
                        </style>
                    """, unsafe_allow_html=True)
                    
                    # Statistics Display
                    stat_col1, stat_col2, stat_col3 = st.columns(3)
                    
                    with stat_col1:
                        st.markdown(f"""
                            <div style="padding: 2rem; background: rgba(102, 126, 234, 0.2); border-radius: 12px; text-align: center; border: 2px solid #667eea;">
                                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🔢</div>
                                <div style="font-size: 2rem; font-weight: bold; color: #667eea; font-family: 'JetBrains Mono', monospace;">{attempts:,}</div>
                                <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Total Attempts</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with stat_col2:
                        st.markdown(f"""
                            <div style="padding: 2rem; background: rgba(79, 172, 254, 0.2); border-radius: 12px; text-align: center; border: 2px solid #4facfe;">
                                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⏱️</div>
                                <div style="font-size: 2rem; font-weight: bold; color: #4facfe; font-family: 'JetBrains Mono', monospace;">{elapsed:.3f}s</div>
                                <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Time Elapsed</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with stat_col3:
                        keys_per_sec = int(attempts / elapsed) if elapsed > 0 else 0
                        st.markdown(f"""
                            <div style="padding: 2rem; background: rgba(240, 147, 251, 0.2); border-radius: 12px; text-align: center; border: 2px solid #f093fb;">
                                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">⚡</div>
                                <div style="font-size: 2rem; font-weight: bold; color: #f093fb; font-family: 'JetBrains Mono', monospace;">{keys_per_sec:,}</div>
                                <div style="font-size: 0.9rem; color: #b8c5d6; margin-top: 0.5rem;">Keys per Second</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Recovered Key Display
                    st.markdown("""
                        <div style="padding: 2rem; background: rgba(0, 242, 254, 0.1); border-radius: 16px; border: 2px solid #00f2fe; margin-top: 2rem;">
                            <h3 style="color: #00f2fe; margin-top: 0; text-align: center;">🔑 RECOVERED ENCRYPTION KEY</h3>
                        </div>
                    """, unsafe_allow_html=True)
                    st.code(f"Recovered key (hex): {candidate_key.hex()}", language="bash")
                    
                    # Success percentage
                    success_percentage = (attempts / total) * 100
                    st.markdown(f"""
                        <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; margin-top: 1rem; text-align: center;">
                            <p style="color: #b8c5d6; margin: 0; font-size: 1.1rem;">
                                Key found after searching <strong style="color: #00f2fe;">{success_percentage:.2f}%</strong> of the keyspace
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    found = True
                    break
            except Exception:
                pass  # Bad padding or wrong key — ignore

            # Update Progress
            if show_progress and (k % update_every == 0):
                progress = int((k / float(total)) * 100)
                progress_bar.progress(min(progress, 100))
                progress_text.text(f"Attempts: {attempts:,} / {total:,} ({progress}%)")

        # Attack Failed
        if not found:
            elapsed = time.time() - start_time
            
            st.markdown("""
                <div style="padding: 3rem; background: linear-gradient(135deg, rgba(250, 112, 154, 0.3), rgba(254, 225, 64, 0.2)); border-radius: 20px; margin: 2rem 0; border: 3px solid #fa709a; text-align: center;">
                    <div style="font-size: 5rem; margin-bottom: 1rem;">❌</div>
                    <h1 style="color: #fa709a; margin: 0; font-size: 2.5rem;">Key Not Found</h1>
                    <p style="color: #b8c5d6; margin-top: 1rem; font-size: 1.2rem;">Exhausted the entire keyspace without finding a match</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.warning(f"Key NOT found after exhausting the toy keyspace. Attempts: {attempts:,}. Time: {elapsed:.3f}s")

st.markdown("<br><br>", unsafe_allow_html=True)

# Grand Footer
st.markdown("""
    <div style="padding: 3rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(240, 147, 251, 0.15)); border-radius: 20px; margin-top: 3rem;">
        <div style="text-align: center;">
            <h3 style="color: #667eea; margin-top: 0;">💡 Important Notes</h3>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
            <div style="padding: 1.5rem; background: rgba(79, 172, 254, 0.1); border-radius: 12px; border-left: 4px solid #4facfe;">
                <h4 style="color: #4facfe; margin-top: 0;">🎯 Getting Started</h4>
                <p style="color: #b8c5d6; line-height: 1.6; margin: 0; font-size: 0.95rem;">
                    Start with N=16 for quick demonstrations. Gradually increase to observe exponential time growth.
                </p>
            </div>
            <div style="padding: 1.5rem; background: rgba(240, 147, 251, 0.1); border-radius: 12px; border-left: 4px solid #f093fb;">
                <h4 style="color: #f093fb; margin-top: 0;">⚠️ Security Notice</h4>
                <p style="color: #b8c5d6; line-height: 1.6; margin: 0; font-size: 0.95rem;">
                    DES is obsolete. Use modern algorithms like AES-256 for actual security needs.
                </p>
            </div>
            <div style="padding: 1.5rem; background: rgba(250, 112, 154, 0.1); border-radius: 12px; border-left: 4px solid #fa709a;">
                <h4 style="color: #fa709a; margin-top: 0;">🎓 Educational Purpose</h4>
                <p style="color: #b8c5d6; line-height: 1.6; margin: 0; font-size: 0.95rem;">
                    This tool is for learning only. Never use for unauthorized cryptanalysis.
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("Note: DES uses a 56-bit key (8 bytes with parity bits) and operates on 64-bit blocks.")
st.caption("For secure communications, consider using modern algorithms like AES instead of DES.")