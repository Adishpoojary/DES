import streamlit as st


st.set_page_config(page_title="Conclusion", page_icon="✅")


st.title("Conclusion & Takeaways")


st.markdown(
"""
- This simulation shows how brute-force time explodes with key length.
- Even though DES has a 56-bit effective key, hardware and distributed attack techniques were historically used to break it; this is why modern cryptography uses larger keys (AES-128/256).
- Use this tool to experiment with N values and observe timing differences.
"""
)


st.markdown("---")
st.caption("This project is for education and research only. Never use cryptanalysis tools for unauthorized activity.")