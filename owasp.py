import streamlit as st

class OWASPApp:
    def __init__(self):
        pass

    def assign_session(self, session_state, parent_app):
        self.session_state = session_state
        self.parent_app = parent_app

    def run(self):
        st.title("참고자료")
        st.markdown("<br><br>", unsafe_allow_html=True)


        # 참고자료 항목들
        references = [
            {
                "title": "OWASP TOP 10",
                "description": "LLM을 위한 OWASP Top 10",
                "image": "https://via.placeholder.com/100",
                "file": "Downloadfile/OWASP-Top-10-for-LLMs-2023-v1_1.pdf"
            },
            {
                "title": "LLM 보안가이드라인",
                "description": "LLM 보안 가이드라인",
                "image": "https://via.placeholder.com/100",
                "file": "Downloadfile/LLM_Security_Guidelines.pdf"
            },
            {
                "title": "탈옥공격 구문 체크리스트",
                "description": "응용 프로그램을 안전하게 유지하기 위한 모범 사례",
                "image": "https://via.placeholder.com/100",
                "file": "Downloadfile/Cybersecurity_Best_Practices.pdf"
            }
        ]

        # 참고자료 항목 표시
        for ref in references:
            col1, col2, col3 = st.columns([1, 5, 2])
            with col1:
                st.image(ref["image"], width=100)
            with col2:
                st.subheader(ref["title"])
                st.write(ref["description"])
            with col3:
                with open(ref["file"], "rb") as file:
                    st.download_button(label="PDF 다운로드", data=file, file_name=ref["file"].split("/")[-1], mime="application/pdf")

if __name__ == "__main__":
    app = OWASPApp()
    app.run()
