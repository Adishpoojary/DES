import streamlit as st


st.set_page_config(page_title="Procedure", page_icon="🧭")


st.title("Procedure: How the simulation works")


st.markdown(
"""
1. A baseline 8-byte DES key is chosen (random or user-provided).
2. The plaintext is encrypted with that key (DES ECB with PKCS7 padding).
3. The simulator iterates candidate keys formed by keeping the high bits of the baseline key fixed and varying the lowest N bits.
4. For each candidate key, the ciphertext is decrypted; if the decrypted bytes equal the original plaintext, the key is declared recovered.


Implementation notes:
- DES ECB is used for simplicity. In real systems modes like CBC and additional protections (authentication) change attack viability.
- We test exact plaintext equality (post-unpadding) to confirm a correct key — decryption with the wrong key usually raises a padding error.
"""
)


st.markdown("---")
st.subheader("Performance and scaling")
st.write("The run time grows linearly with the number of keys tested. Doubling N doubles the exponent, i.e., increases keyspace by factor 2.")