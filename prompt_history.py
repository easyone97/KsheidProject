import pandas as pd
import streamlit as st

class PromptHistoryApp:
    def __init__(self):
        pass

    def assign_session(self, session_state, parent_app):
        self.session_state = session_state
        self.parent_app = parent_app

    @st.cache_data
    def load_results(_self, filename):
        return pd.read_csv(filename)

    def run(self):
        st.markdown(
            """
            <style>
            .container-box {
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
                background-color: #776B5D;
                color: white;
                position: relative;
            }
            .title {
                font-size: 2.5em;
                font-weight: bold;
                color: black;
            }
            .subtitle {
                font-size: 1.5em;
                margin-top: 20px;
                margin-bottom: 10px;
                color: black;
            }
            .filter-label {
                font-size: 1.2em;
                font-weight: bold;
                color: white;
                margin-bottom: 10px;
                background-color: #838383;
                padding: 5px;
                border-radius: 5px;
            }
            .radio-label {
                display: block;
                font-size: 1.5em;
                margin-bottom: 10px;
                color: white;
            }
            .apply-button {
                display: flex;
                justify-content: flex-end;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            .spacer {
                margin-bottom: 10px;
            }
            .container-spacing {
                margin-bottom: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size: 2.5em; color: #000000;'>탈옥 프롬프트 내역</h1>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)

        # CSV 파일 경로 설정
        output_path = '/dataset/final_result_test.csv'  # 파일 경로는 서버에 맞게 조정해야 합니다.

        # 결과 데이터 로드
        results_df = self.load_results(output_path)

        # 초기 선택 상태 설정
        if 'selected_types' not in st.session_state:
            st.session_state.selected_types = ["전체"]
        if 'selected_success' not in st.session_state:
            st.session_state.selected_success = "전체"

        # 레이아웃 설정
        col1, col2 = st.columns([2, 8])

        with col1:
            with st.container(border=True):
                st.markdown("<div class='filter-label'>Type 선택</div>", unsafe_allow_html=True)
                type_options = ["전체"] + results_df['type'].unique().tolist()
                selected_types = st.multiselect("", type_options, default=st.session_state.selected_types)
                st.markdown("<div class='apply-button'>", unsafe_allow_html=True)
                if st.button("적용", key="apply_button"):
                    st.session_state.selected_types = selected_types
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='container-spacing'></div>", unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown("<div class='filter-label'>탈옥 성공 여부 선택</div>", unsafe_allow_html=True)
                success_options_display = ["전체", "Success", "Fail"]
                success_options_actual = ["전체", "success", "fail"]
                selected_success_display = st.radio("", success_options_display, index=success_options_actual.index(st.session_state.selected_success))
                selected_success_actual = success_options_actual[success_options_display.index(selected_success_display)]
                st.session_state.selected_success = selected_success_actual
                st.markdown('<style>.stRadio > div {display: flex; flex-direction: column;}</style>', unsafe_allow_html=True)

        # 선택된 필터에 따라 데이터 필터링
        filtered_df = results_df.copy()
        if "전체" not in st.session_state.selected_types:
            filtered_df = filtered_df[filtered_df['type'].isin(st.session_state.selected_types)]
        if st.session_state.selected_success != "전체":
            filtered_df = filtered_df[filtered_df['탈옥성공여부'] == st.session_state.selected_success]

        with col2:
            st.dataframe(filtered_df, height=800)  # 높이를 800으로 설정

if __name__ == "__main__":
    app = PromptHistoryApp()
    app.run()














