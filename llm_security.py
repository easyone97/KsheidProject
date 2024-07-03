import streamlit as st

class LLMSecurityApp:
    def __init__(self):
        pass

    def assign_session(self, session_state, parent_app):
        self.session_state = session_state
        self.parent_app = parent_app

    def run(self):
        st.title("LLM 한국형 보안 가이드라인")
        st.markdown("<br><br>", unsafe_allow_html=True)
        with open("Downloadfile/OWASP-Top-10-for-LLMs-2023-v1_1.pdf", "rb") as file:
            st.download_button(
                label="LLM-Download 한국형-보안-가이드라인 PDF",
                data=file,
                file_name="OWASP-Top-10-for-LLMs-2023-v1_1.pdf",
                mime="application/pdf",
            )
if __name__ == "__main__":
    app = LLMSecurityApp()
    app.run()
