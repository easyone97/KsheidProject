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

        # 다운로드 버튼 스타일 설정
        st.markdown("""
            <style>
            .stDownloadButton > button {
                background-color: #87CEEB;
                color: white;
                border: none;
                padding: 8px 16px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }
            .stDownloadButton > button:hover {
                background-color: #00BFFF;
            }
            .reference-item {
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 20px;
            }
            .reference-text {
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            .reference-text h3 {
                font-size: 24px;
            }
            .reference-text p {
                font-size: 18px;
            }
            </style>
        """, unsafe_allow_html=True)

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
                "image": "Images/checklist.png",
                "file": "Downloadfile/jailbreakPrompt.csv"
            }
        ]

        # 참고자료 항목 표시
        for index, ref in enumerate(references):
            with st.container():
                col0, col1, col2, col3 = st.columns([1, 2, 6, 2])
                with col0:
                    st.empty()  # 빈 컬럼으로 공백 추가
                with col1:
                    st.image(ref["image"], width=150)
                with col2:
                    st.markdown(
                        f"""
                        <div class="reference-item">
                            <div class="reference-text">
                                <h3>{ref['title']}</h3>
                                <p>{ref['description']}</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                with col3:
                    with open(ref["file"], "rb") as file:
                        st.markdown(
                            f"""
                            <div class="reference-item">
                                <div>
                                    <a href="data:{"application/pdf" if ref["file"].endswith(".pdf") else "text/csv"};base64,{file.read().decode('utf-8')}" download="{ref["file"].split("/")[-1]}" class="stDownloadButton">
                                        <button>PDF 다운로드</button>
                                    </a>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

if __name__ == "__main__":
    app = OWASPApp()
    app.run()









