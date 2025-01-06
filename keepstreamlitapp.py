import streamlit as st
import requests
import time
from datetime import datetime

# URL 리스트
URLS = [
    "https://beam-frp.streamlit.app/",
    "https://column.streamlit.app/",
    "https://support.streamlit.app/",
    "https://bidinfo.streamlit.app/",
    "https://kolontech.streamlit.app/",
    "https://bidtech.streamlit.app/",
    "https://pdftech.streamlit.app/",
    "https://tunneltech.streamlit.app/",
    "https://cadtech.streamlit.app/"
]

# 세션 상태 개별 초기화 (중요: 각각 따로 초기화해야 함)
if 'status' not in st.session_state:
    st.session_state.status = {}
if 'last_check' not in st.session_state:
    st.session_state.last_check = {}
if 'first_run' not in st.session_state:
    st.session_state.first_run = True

def check_single_url(url):
    """단일 URL 상태 체크"""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = round((time.time() - start_time) * 1000)
        
        if response.status_code == 200:
            return {
                'status': 'success',
                'message': f'✅ 정상 접속됨',
                'code': response.status_code,
                'time': response_time
            }
        else:
            return {
                'status': 'fail',
                'message': f'❌ 접속 실패',
                'code': response.status_code,
                'time': response_time
            }
    except requests.Timeout:
        return {
            'status': 'timeout',
            'message': '⚠️ 시간 초과',
            'code': None,
            'time': None
        }
    except requests.ConnectionError:
        return {
            'status': 'error',
            'message': '❌ 연결 오류',
            'code': None,
            'time': None
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'❌ 오류 발생: {str(e)}',
            'code': None,
            'time': None
        }

def check_urls():
    """모든 URL 체크"""
    for url in URLS:
        result = check_single_url(url)
        st.session_state.status[url] = result
        st.session_state.last_check[url] = datetime.now()

# Streamlit UI
st.title("스트림릿 앱 상태 모니터링")

# 수동 체크 버튼
if st.button("수동 체크", type="primary"):
    with st.spinner("상태 체크 중..."):
        check_urls()

# 첫 실행시 자동 체크
if st.session_state.first_run:
    with st.spinner("초기 상태 체크 중..."):
        check_urls()
        st.session_state.first_run = False

# 마지막 체크 시간 표시
if st.session_state.last_check:
    latest_check = max(st.session_state.last_check.values())
    st.caption(f"마지막 체크: {latest_check.strftime('%Y-%m-%d %H:%M:%S')}")

# 상태 표시
st.divider()

# 전체 요약
if st.session_state.status:
    total_success = sum(1 for result in st.session_state.status.values() 
                       if result['status'] == 'success')
    st.metric(label="정상 접속 앱", value=f"{total_success}/{len(URLS)}")

# 개별 앱 상태
for url in URLS:
    if url in st.session_state.status:
        result = st.session_state.status[url]
        
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            st.write(url)
        with col2:
            st.write(result['message'])
        with col3:
            if result['status'] == 'success':
                st.write(f"{result['time']}ms")
            elif result['code']:
                st.write(f"코드: {result['code']}")
            else:
                st.write("—")

# 참고사항
st.divider()
st.info("""
- ✅ 정상: 앱에 성공적으로 접속됨
- ❌ 실패: 앱 접속 실패 또는 오류 발생
- ⚠️ 시간초과: 응답 시간 초과 (10초)
""")