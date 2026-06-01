import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 (연락처 및 링크)
with st.sidebar:
    st.header("Contact & Links")
    st.write("📧 이메일: your_email@example.com")
    st.write("🐙 GitHub: [github.com/yourid](https://github.com)")
    st.write("📝 블로그: [velog.io/@yourid](https://velog.io)")
    
    st.markdown("---")
    st.caption("© 2026. All rights reserved.")

# 3. 메인 화면 - 헤더 영역
st.title("👋 안녕하세요, [홍길동]입니다!")
st.subheader("데이터와 개발로 세상을 바꾸고 싶은 주니어 개발자입니다.")

# 4. 프로필 및 소개 (2개 컬럼 레이아웃)
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지 (URL이나 로컬 이미지 파일 경로 입력 가능)
    # 여기서는 샘플 이미지를 사용합니다. 본인 사진으로 바꾸려면 파일명을 적어주세요.
    st.image("https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png", width=180)

with col2:
    st.markdown("""
    ### 📌 About Me
    * **이름:** 홍길동 (Hong Gil Dong)
    * **생년월일:** 199X. XX. XX
    * **한 줄 소개:** 끊임없이 배우고 공유하는 것을 즐깁니다. 새로운 기술을 탐구하고 문제를 해결할 때 가장 큰 보람을 느낍니다.
    """)

st.markdown("---")

# 5. 기술 스택 (Tech Stacks)
st.header("🛠️ Tech Stacks")
col_tech1, col_tech2 = st.columns(2)

with col_tech1:
    st.markdown("**Languages**")
    st.code("Python, JavaScript, SQL", language="text")

with col_tech2:
    st.markdown("**Frameworks & Tools**")
    st.code("Streamlit, FastAPI, Git, Docker", language="text")

st.markdown("---")

# 6. 프로젝트 및 경험 (Projects)
st.header("🚀 Projects")

with st.expander("📂 1. 스트림릿을 활용한 포트폴리오 웹사이트 제작"):
    st.write("**기간:** 2026.05 ~ 2026.06 (1인 프로젝트)")
    st.write("**설명:** 파이썬만으로 빠르게 웹 애플리케이션을 구축할 수 있는 Streamlit을 활용하여 개인 포트폴리오를 제작했습니다.")
    st.write("**주요 기능:** 프로필 소개, 기술 스택 시각화, 실시간 방명록 기능")

with st.expander("📂 2. 데이터 분석 및 시각화 대시보드 구축"):
    st.write("**기간:** 2026.02 ~ 2026.04")
    st.write("**설명:** 공공 데이터를 활용하여 지역별 트렌드를 분석하고 시각화하는 대시보드를 개발했습니다.")
    st.write("**사용한 기술:** Python, Pandas, Plotly")

st.markdown("---")

# 7. 간단한 인터랙티브 기능 (방명록)
st.header("💌 방명록")
st.write("방문해주셔서 감사합니다! 응원의 한 마디를 남겨주세요.")

# 세션 상태를 이용한 간단한 메시지 저장 (앱이 새로고침되면 초기화되지만 데모용으로 좋습니다)
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form(key="guestbook_form", clear_on_submit=True):
    visitor_name = st.text_input("이름/닉네임", max_chars=20)
    visitor_msg = st.text_area("메시지", max_chars=100)
    submit_button = st.form_submit_button(label="남기기")

if submit_button:
    if visitor_name and visitor_msg:
        st.session_state.messages.append(f"**{visitor_name}**: {visitor_msg}")
        st.success("메시지가 등록되었습니다!")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요.")

# 남겨진 메시지 출력
if st.session_state.messages:
    for msg in reversed(st.session_state.messages):
        st.info(msg)