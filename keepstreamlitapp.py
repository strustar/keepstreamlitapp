import streamlit as st
import streamlit.components.v1 as components
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
    page_title="스트림릿 앱 오프너",
    page_icon="🌐",
    layout="wide"
)

# JavaScript 함수 정의
def get_js_code(urls, delay_ms):
    return f"""
        <script>
        const urls = {urls};
        const delay = {delay_ms};
        let openedWindows = [];
        
        function openUrlsSequentially(index) {{
            if (index >= urls.length) {{
                document.getElementById('closeButton').style.display = 'inline-block';
                return;
            }}
            
            const newWindow = window.open(urls[index], '_blank');
            openedWindows.push(newWindow);
            setTimeout(() => openUrlsSequentially(index + 1), delay);
        }}

        // 버튼 클릭 함수
        function openAllPages() {{
            openedWindows = [];  // 초기화
            document.getElementById('closeButton').style.display = 'none';
            openUrlsSequentially(0);
        }}

        // 열린 창 닫기 함수
        function closeAllPages() {{
            openedWindows.forEach(window => {{
                if (window && !window.closed) {{
                    window.close();
                }}
            }});
            openedWindows = [];
            document.getElementById('closeButton').style.display = 'none';
        }}
        </script>
    """

# 제목 및 설명
st.title("🌐 스트림릿 앱 오프너")
st.write("모든 스트림릿 앱을 한 번에 열고 닫을 수 있습니다.")

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

# JavaScript 컴포넌트 생성
js_code = get_js_code(URLS, delay * 1000)  # delay를 밀리초로 변환
components.html(f"""
    {js_code}
    <div style="display: flex; gap: 10px;">
        <button 
            onclick="openAllPages()"
            style="
                background-color: #FF4B4B;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
            "
        >
            🚀 모든 페이지 열기
        </button>
        
        <button 
            id="closeButton"
            onclick="closeAllPages()"
            style="
                background-color: #808080;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                font-weight: bold;
                display: none;
            "
        >
            🚫 열린 페이지 모두 닫기
        </button>
    </div>
""", height=60)

# 도움말
with st.expander("ℹ️ 도움말"):
    st.markdown("""
    ### 사용 방법
    1. 원하는 딜레이 시간을 설정합니다. (기본값: 3초)
    2. '모든 페이지 열기' 버튼을 클릭합니다.
    3. 모든 페이지가 열린 후, '열린 페이지 모두 닫기' 버튼이 나타납니다.
    4. 닫기 버튼을 클릭하면 새로 열린 페이지들만 닫힙니다.
    
    ### 주의사항
    - 브라우저 설정에 따라 팝업이 차단될 수 있습니다.
    - 너무 짧은 딜레이는 브라우저에 부담을 줄 수 있습니다.
    - 많은 탭이 한 번에 열리므로 시스템 자원을 고려하세요.
    """)

# 푸터
st.divider()
st.caption("© 2024 스트림릿 앱 오프너 | 문제 발생 시 관리자에게 문의하세요.")