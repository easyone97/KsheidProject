import streamlit as st

class OWASPApp:
    def __init__(self):
        pass

    def assign_session(self, session_state, parent_app):
        self.session_state = session_state
        self.parent_app = parent_app

    def run(self):
        st.title("OWASP Top 10 for LLMs")
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.write("OWASP에서 발표한 LLM 애플리케이션에 영향을 미치는 가장 치명적인 취약점 상위 10가지")
        st.markdown("<br><br>", unsafe_allow_html=True)
        with open("Downloadfile/OWASP-Top-10-for-LLMs-2023-v1_1.pdf", "rb") as file:
            st.download_button(
                label="Download OWASP Top 10 for LLMs PDF",
                data=file,
                file_name="OWASP-Top-10-for-LLMs-2023-v1_1.pdf",
                mime="application/pdf",
            )
if __name__ == "__main__":
    app = OWASPApp()
    app.run()
