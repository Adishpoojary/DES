# pages/04_Encryption_Simulation.py
import streamlit as st
import time
import base64
from src.des_utils import des_encrypt, des_decrypt, int_to_bytes64, bytes_to_int64, generate_random_key

st.set_page_config(page_title="Encryption, Decryption & Simulation — DES", page_icon="🔑")

st.title("Encryption, Decryption & Simulation")

# Create tabs for encryption/decryption and brute-force
tab1, tab2 = st.tabs(["Encryption & Decryption", "Brute-Force Attack"])

with tab1:
    st.subheader("Encrypt/Decrypt Data with DES")
    
    # Input for plaintext
    plaintext_input = st.text_area("Enter plaintext to encrypt:", "Hello, this is a secret message!", key="combined_plaintext_input")
    
    # Key options
    key_mode_enc_dec = st.radio("Select key option:", ["Generate random key", "Enter hex key (16 hex chars)"], key="combined_key_mode_enc_dec")
    
    if "combined_encryption_key" not in st.session_state:
        st.session_state.combined_encryption_key = generate_random_key()
    
    if key_mode_enc_dec.startswith("Generate"):
        if st.button("🔄 Generate new key", key="combined_gen_enc_key"):
            st.session_state.combined_encryption_key = generate_random_key()
        combined_encryption_key = st.session_state.combined_encryption_key
        st.code(f"Key (hex): {combined_encryption_key.hex()}")
    else:
        user_hex_enc_dec = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_enc_dec_hex_key")
        if user_hex_enc_dec:
            try:
                b = bytes.fromhex(user_hex_enc_dec)
                if len(b) == 8:
                    combined_encryption_key = b
                    st.session_state.combined_encryption_key = b
                else:
                    st.error("Key must be exactly 8 bytes (16 hex chars).")
                    combined_encryption_key = st.session_state.combined_encryption_key
            except Exception:
                st.error("Invalid hex key.")
                combined_encryption_key = st.session_state.combined_encryption_key
        else:
            combined_encryption_key = st.session_state.combined_encryption_key
            st.info("Using generated key until you provide a valid hex key.")
            st.code(f"Key (hex): {combined_encryption_key.hex()}")
    
    # Encrypt button
    if st.button("🔒 Encrypt", key="combined_encrypt_btn"):
        try:
            plaintext_bytes = plaintext_input.encode("utf-8")
            ciphertext_combined = des_encrypt(plaintext_bytes, combined_encryption_key)
            
            st.success("Encryption successful!")
            st.write("Ciphertext (hex):")
            st.code(ciphertext_combined.hex())
            
            base64_output_combined = base64.b64encode(ciphertext_combined).decode("utf-8")
            st.write("Ciphertext (Base64):")
            st.code(base64_output_combined)
            
            st.session_state.combined_last_ciphertext = ciphertext_combined
            st.session_state.combined_last_key = combined_encryption_key
            
        except Exception as e:
            st.error(f"Encryption failed: {str(e)}")

    st.markdown("---")
    st.subheader("Decrypt Data with DES")
    
    input_format_dec = st.radio("Ciphertext format:", ["Hex", "Base64"], key="combined_input_format_dec")
    
    ciphertext_input_dec = st.text_area("Enter ciphertext to decrypt:", 
                                    value="" if "combined_last_ciphertext" not in st.session_state 
                                    else (st.session_state.combined_last_ciphertext.hex() if input_format_dec == "Hex" 
                                          else base64.b64encode(st.session_state.combined_last_ciphertext).decode("utf-8")), key="combined_ciphertext_input_dec")
    
    key_mode_dec_combined = st.radio("Select key option:", ["Use last encryption key", "Enter hex key (16 hex chars)"], key="combined_dec_key_mode")
    
    if key_mode_dec_combined.startswith("Use") and "combined_last_key" in st.session_state:
        combined_decryption_key = st.session_state.combined_last_key
        st.code(f"Key (hex): {combined_decryption_key.hex()}")
    else:
        user_hex_dec_combined = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_dec_hex_key")
        if user_hex_dec_combined:
            try:
                b = bytes.fromhex(user_hex_dec_combined)
                if len(b) == 8:
                    combined_decryption_key = b
                else:
                    st.error("Key must be exactly 8 bytes (16 hex chars).")
                    combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
            except Exception:
                st.error("Invalid hex key.")
                combined_decryption_key = st.session_state.get("combined_last_key", generate_random_key())
        elif "combined_last_key" in st.session_state:
            combined_decryption_key = st.session_state.combined_last_key
            st.code(f"Key (hex): {combined_decryption_key.hex()}")
        else:
            st.error("Please enter a valid key.")
            combined_decryption_key = None
    
    if st.button("🔓 Decrypt", key="combined_decrypt_btn"):
        if not ciphertext_input_dec:
            st.error("Please enter ciphertext to decrypt.")
        elif combined_decryption_key is None:
            st.error("Please provide a valid decryption key.")
        else:
            try:
                if input_format_dec == "Hex":
                    try:
                        ciphertext_bytes_dec = bytes.fromhex(ciphertext_input_dec)
                    except ValueError:
                        st.error("Invalid hex format. Please check your input.")
                        st.stop()
                else:  # Base64
                    try:
                        ciphertext_bytes_dec = base64.b64decode(ciphertext_input_dec)
                    except Exception:
                        st.error("Invalid Base64 format. Please check your input.")
                        st.stop()
                
                plaintext_dec = des_decrypt(ciphertext_bytes_dec, combined_decryption_key)
                
                st.success("Decryption successful!")
                st.write("Plaintext:")
                
                try:
                    decoded_text_dec = plaintext_dec.decode("utf-8")
                    st.code(decoded_text_dec)
                except UnicodeDecodeError:
                    st.warning("The decrypted data is not valid UTF-8 text. Showing as hex:")
                    st.code(plaintext_dec.hex())
                    
            except Exception as e:
                st.error(f"Decryption failed: {str(e)}")
                st.info("This could be due to an incorrect key or corrupted ciphertext.")

with tab2:
    st.subheader("DES Brute-Force Attack Simulation")
    st.markdown("""
        This section allows you to simulate a brute-force attack on DES. 
        You can define a plaintext, a baseline key, and the number of variable bits (N) 
        to limit the search space for the brute-force attempt.
    """)

    plaintext_text = st.text_area("Plaintext to encrypt:", "Attack at dawn", key="combined_brute_force_plaintext")
    plaintext = plaintext_text.encode("utf-8")

    key_mode = st.radio("Baseline key selection:", ["Generate random baseline key", "Enter hex key (16 hex chars)"], key="combined_brute_force_key_mode")

    if "combined_baseline_key" not in st.session_state:
        st.session_state.combined_baseline_key = generate_random_key()

    if key_mode.startswith("Generate"):
        if st.button("🔄 Generate new baseline key", key="combined_brute_force_gen_key"):
            st.session_state.combined_baseline_key = generate_random_key()
        baseline_key = st.session_state.combined_baseline_key
        st.code(f"Baseline key (hex): {baseline_key.hex()}")
    else:
        user_hex = st.text_input("Enter 16-hex-digit key (8 bytes). Example: 0123456789abcdef", key="combined_brute_force_user_hex")
        if user_hex:
            try:
                b = bytes.fromhex(user_hex)
                if len(b) == 8:
                    baseline_key = b
                    st.session_state.combined_baseline_key = b
                else:
                    st.error("Key must be exactly 8 bytes (16 hex chars).")
                    baseline_key = st.session_state.combined_baseline_key
            except Exception:
                st.error("Invalid hex key.")
                baseline_key = st.session_state.combined_baseline_key
        else:
            baseline_key = st.session_state.combined_baseline_key
            st.info("Using generated baseline key until you provide a valid hex key.")
            st.code(f"Baseline key (hex): {baseline_key.hex()}")

    st.write("The plaintext will be encrypted with the baseline key to produce the target ciphertext for the brute-force attack.")
    ciphertext = des_encrypt(plaintext, baseline_key)
    st.code(f"Ciphertext (hex): {ciphertext.hex()}")

    N = st.number_input("Number of variable bits to brute-force (N)", min_value=8, max_value=24, value=16, step=1, key="combined_brute_force_N")
    show_progress = st.checkbox("Show live progress (slower)", value=True, key="combined_brute_force_show_progress")

    st.markdown("---")

    if st.button("🚀 Start brute-force attack", key="combined_brute_force_start_btn"):
        st.info("Starting brute-force. Keep N small for interactive runs.")

        target_ct = ciphertext
        target_plain = plaintext
        base_int = bytes_to_int64(baseline_key)
        mask = (1 << N) - 1
        base_prefix = base_int & (~mask)

        start_time = time.time()
        found = False
        attempts = 0
        total = 1 << N

        progress_bar = st.progress(0) if show_progress else None
        progress_text = st.empty() if show_progress else None

        # iterate
        update_every = max(1, total // 200)
        for k in range(total):
            attempts += 1
            candidate_int = base_prefix | k
            candidate_key = int_to_bytes64(candidate_int)
            try:
                pt = des_decrypt(target_ct, candidate_key)
                if pt == target_plain:
                    elapsed = time.time() - start_time
                    st.success(f"Key found after {attempts:,} attempts in {elapsed:.3f} s")
                    st.code(f"Recovered key (hex): {candidate_key.hex()}")
                    found = True
                    break
            except Exception:
                # Bad padding or wrong key — ignore
                pass

            if show_progress and (k % update_every == 0):
                progress = int((k / float(total)) * 100)
                progress_bar.progress(min(progress, 100))
                progress_text.text(f"Attempts: {attempts:,} / {total:,} ({progress}%)")

        if not found:
            elapsed = time.time() - start_time
            st.warning(f"Key NOT found after exhausting the toy keyspace. Attempts: {attempts:,}. Time: {elapsed:.3f}s")

st.markdown("---")
st.caption("Note: DES uses a 56-bit key (8 bytes with parity bits) and operates on 64-bit blocks.")
st.caption("For secure communications, consider using modern algorithms like AES instead of DES.")