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
                "title": "OWASP Top 10 for LLM",
                "description": "OWASP에서 발표한 LLM 애플리케이션에 영향을 미치는 가장 치명적인 취약점 상위 10가지",
                "image": "Images/owasp.jpeg",
                "file": "Downloadfile/OWASP-Top-10-for-LLMs-2023-v1_1.pdf"
            },
            {
                "title": "2024 LLM 한국형 보안 가이드라인",
                "description": "LLM 보안 가이드라인",
                "image": "Images/가이드라인.jpeg",
                "file": "Downloadfile/OWASP-Top-10-for-LLMs-2023-v1_1.pdf"
            },
            {
                "title": "탈옥공격 구문 체크리스트",
                "description": "탈옥공격의 위험성을 체크할 수 있는 구문 616개, 유해한 질문 6개",
                "image": "https://www.kindpng.com/picc/m/376-3767580_csv-file-icon-hd-png-download.png",
                "file": "Downloadfile/jailbreakPrompt.csv"
            }
        ]

        # 참고자료 항목 표시
        for index, ref in enumerate(references):
            col1, col2, col3 = st.columns([2, 6, 2], gap="medium")
            with col1:
                st.image(ref["image"], width=150)
            with col2:
                st.markdown(
                    f"""
                    <div style='display: flex; flex-direction: column; align-items: center;'>
                        <h3>{ref['title']}</h3>
                        <p>{ref['description']}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            with col3:
                with open(ref["file"], "rb") as file:
                    st.download_button(
                        label="PDF 다운로드" if ref["file"].endswith(".pdf") else "CSV 다운로드", 
                        data=file, 
                        file_name=ref["file"].split("/")[-1], 
                        mime="text/csv" if ref["file"].endswith(".csv") else "application/pdf",
                        key=f"download_button_{index}"
                    )

if __name__ == "__main__":
    app = OWASPApp()
    app.run()




