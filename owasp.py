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

        # 왼쪽 공백을 맞추기 위한 스타일
        st.markdown(
            """
            <style>
            .reference-item {
                display: flex;
                margin-left: 120px; /* 제목 "참고자료"의 가로 길이만큼 설정 */
            }
            .reference-text {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

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
                "image": "Images/checklist.jpg",
                "file": "Downloadfile/jailbreakPrompt.csv"
            }
        ]

        # 참고자료 항목 표시
        for index, ref in enumerate(references):
            st.markdown(
                f"""
                <div class="reference-item">
                    <div>
                        <img src="{ref['image']}" width="150">
                    </div>
                    <div class="reference-text">
                        <h3>{ref['title']}</h3>
                        <p>{ref['description']}</p>
                        <a download="{ref['file'].split("/")[-1]}" href="data:{'application/pdf' if ref['file'].endswith('.pdf') else 'text/csv'};base64,{ref['file']}">
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





