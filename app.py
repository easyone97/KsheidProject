from pyngrok import ngrok

# ngrok 인증 토큰 설정
NGROK_AUTH_TOKEN = "2iHixcS66qd7anlPia70MqNakGt_2V7RBj4zqHHtKAhTouR5r"
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# ngrok 터널 열기 (HTTP 터널로 설정)
public_url = ngrok.connect(8501)
print(f"Streamlit 앱을 여기에서 확인할 수 있습니다: {public_url}")

# Streamlit 실행
!streamlit run main.py &

# Streamlit 실행 후, 애플리케이션이 제대로 실행되었는지 확인
import time
time.sleep(2)
