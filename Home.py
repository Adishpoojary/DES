import streamlit as st
from PIL import Image

st.set_page_config(page_title="DES Brute-Force Simulator", page_icon="🔐", layout="centered")



st.title("DES Brute-Force Simulator")

st.markdown(
    """
    ### Welcome to the DES Brute-Force Simulator!

    This interactive tool is designed to help you understand the Data Encryption Standard (DES) and the principles behind brute-force attacks. Explore how DES encryption works, simulate a brute-force attack to see its limitations, and delve into the theoretical aspects of cryptographic security.

    Navigate through the pages using the sidebar to:
    - **Theory**: Learn about DES, its structure, and keyspace scaling.
    - **Simulation**: Run a toy brute-force attack to observe its mechanics.
    - **Encryption & Decryption**: Encrypt and decrypt messages using DES.
    - **Procedure**: Understand the implementation details of the simulation.
    - **Conclusion**: Discover key observations and takeaways from the simulations.
    """
)

st.info("This is an educational tool. Do not use it for malicious purposes.")

# Optional: Add a separator or a visual element here if desired
st.markdown("---")

# Display the logo in a more integrated way, perhaps at the bottom or in a smaller column if needed
# For now, I'll keep it simple and remove the column layout for the main intro
try:
    img = Image.open("assets/logo.png")
    st.image(img, width=160, caption="DES Simulator Logo", use_column_width=False)
except Exception:
    st.write("")

st.markdown("---")
st.subheader("Quick Links")
st.write("- [Theory](Theory)")
st.write("- [Simulation](Simulation)")
st.write("- [Encryption & Decryption](Encryption)")
st.write("- [Procedure](Procedure)")
st.write("- [Conclusion](Conclusion)")
