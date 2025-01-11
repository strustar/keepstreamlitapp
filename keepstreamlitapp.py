import streamlit as st
import webbrowser
import time

# URL 리스트 정의
URLS = [
    "https://beam-frp.streamlit.app/",
    "https://column.streamlit.app/",
    "https://support.streamlit.app/",
    "https://bidinfo.streamlit.app/",
    "https://kolontech.streamlit.app/",
    "https://bidtech.streamlit.app/",
    "https://pdftech.streamlit.app/",
    "https://tunneltech.streamlit.app/",
    "https://cadtech.streamlit.app/",
    "https://pptpdf.streamlit.app/",
    "https://cfdtech.streamlit.app/",
    "https://sjtech.streamlit.app/",
    "https://pptpdf.streamlit.app/"

]

# 페이지 설정
st.set_page_config(
    page_title="스트림릿 앱 오프너", page_icon="🌐", layout="wide"
)

# 제목 및 설명
st.title("🌐 스트림릿 앱 오프너")
st.write("모든 스트림릿 앱을 한 번에 열 수 있습니다.")

# URL 목록 표시
with st.sidebar:
    st.subheader("📋 앱 목록")
    for i, url in enumerate(URLS, 1):
        st.write(f"{i}. {url}")

# 실행 옵션
col1, col2 = st.columns(2)

with col1:
    delay = st.slider(
        "페이지 간 딜레이 (초)",
        min_value=1,
        max_value=5,
        value=3,
        help="각 페이지를 여는 사이의 대기 시간"
    )

with col2:
    auto_close = st.checkbox(
        "30초 후 자동으로 이 페이지 닫기",
        value=False,
        help="모든 페이지를 연 후 이 컨트롤 페이지를 자동으로 닫습니다."
    )

# 실행 버튼
if st.button("🚀 모든 페이지 열기", type="primary"):
    with st.spinner("페이지 여는 중..."):
        # 진행 상황을 보여주기 위한 프로그레스 바
        progress_bar = st.progress(0)
        
        # 각 URL을 새 탭에서 열기
        for i, url in enumerate(URLS):
            webbrowser.open_new_tab(url)
            progress = (i + 1) / len(URLS)
            progress_bar.progress(progress)
            time.sleep(delay)  # 설정된 딜레이만큼 대기
        
        st.success(f"✅ 총 {len(URLS)}개의 페이지를 모두 열었습니다!")
        
        # 자동 닫기 옵션이 선택된 경우
        if auto_close:
            st.warning("이 페이지는 30초 후 자동으로 닫힙니다...")
            st.markdown("""
                <script>
                    setTimeout(function() {
                        window.close();
                    }, 30000);
                </script>
                """, unsafe_allow_html=True)

# 도움말
with st.expander("ℹ️ 도움말"):
    st.markdown("""
    ### 사용 방법
    1. 원하는 딜레이 시간을 설정합니다. (기본값: 3초)
    2. 필요한 경우 자동 닫기 옵션을 선택합니다.
    3. '모든 페이지 열기' 버튼을 클릭합니다.
    4. 브라우저의 팝업 차단이 활성화되어 있다면 허용해주세요.
    
    ### 주의사항
    - 브라우저 설정에 따라 팝업이 차단될 수 있습니다.
    - 너무 짧은 딜레이는 브라우저에 부담을 줄 수 있습니다.
    - 많은 탭이 한 번에 열리므로 시스템 자원을 고려하세요.
    """)

# 푸터
st.divider()
st.caption("© 2024 스트림릿 앱 오프너 | 문제 발생 시 관리자에게 문의하세요.")