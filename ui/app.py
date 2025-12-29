import streamlit as st
import requests

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="PRISM | Prompt Generator",
    layout="centered"
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style="text-align:center; margin-bottom:0.2em;">
        PRISM
    </h1>
    <p style="text-align:center; color: #6c757d; margin-top:0;">
        Search Prompt Generator
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- Input Section ----------------
st.markdown("### Research Topic")
topic = st.text_input(
    label="",
    placeholder="e.g. counter-UAV technologies, electronic warfare, radar systems"
)

# ---------------- Action Button ----------------
generate = st.button("Generate Search Prompts", use_container_width=True)

# ---------------- Output Section ----------------
if generate:
    if topic.strip():
        with st.spinner("Generating prompts..."):
            try:
                response = requests.get(
                    "http://127.0.0.1:8000/generate-prompts",
                    params={"topic": topic}
                )
                response.raise_for_status()
                data = response.json()

                st.markdown("### Generated Prompts")
                st.markdown("---")

                for i, prompt in enumerate(data.get("prompts", []), 1):
                    st.markdown(
                        f"""
                        <div style="
                            padding: 12px;
                            margin-bottom: 10px;
                            border-radius: 8px;
                            background-color: #f8f9fa;
                            border-left: 4px solid #4f46e5;
                        ">
                        <b>{i}.</b> {prompt}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            except Exception as e:
                st.error("Failed to fetch prompts from backend.")
    else:
        st.warning("Please enter a research topic.")

