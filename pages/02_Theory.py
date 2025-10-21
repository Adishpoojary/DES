import streamlit as st


st.set_page_config(page_title="Theory — DES", page_icon="📘")


st.title("Theory: DES and Brute-Force Attacks")


st.markdown(
"""
**DES basics**


- DES is a symmetric block cipher with 64-bit block size and a 56-bit effective key (stored across 8 bytes with parity bits).
- Keyspace size: 2^56 ≈ 7.2058e16 keys.


**Brute-force**


- Brute-force means testing keys until the plaintext is recovered. Time grows linearly with keyspace size.
- This project uses a *toy* mode: it fixes a baseline 8-byte key and varies only the lowest *N* bits (so the keyspace is 2^N). This keeps the demo runnable.


**Why toy mode?**


- Full DES (2^56) cannot be exhaustively searched in reasonable time on a single laptop. Varying N between 8 and 24 shows exponential time growth clearly.
"""
)


st.markdown("---")
st.subheader("Keyspace examples")
st.write("- N = 16 -> 65,536 keys — trivial to explore")
st.write("- N = 24 -> 16,777,216 keys — possible but may take time depending on UI updates")


st.markdown("---")
st.caption("All timings shown in this demo are illustrative — hardware, Python overhead, and Streamlit UI updates affect wallclock time.")