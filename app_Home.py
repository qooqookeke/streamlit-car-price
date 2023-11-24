import streamlit as st

def run_home_app():
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보를 넣으면, 차 구매 금액도 예측해 줍니다.')

    st.text('AWS에 배포까지 된 앱입니다.')
    
    img_url = 'https://image-cdn.hypb.st/https%3A%2F%2Fkr.hypebeast.com%2Ffiles%2F2023%2F01%2Fgenesis-convertible-to-be-mass-produced-ft.jpeg?w=960&cbr=1&q=90&fit=max'
    
    st.image(img_url)
