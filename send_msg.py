import requests

def send_sms():
    target_number = "+916005412606"
    message_body = "🛡️ IG-Alert: Unusual login attempt. Verify your account to avoid lockout: https://instagram.com-security-check@8db5df8cd1d5a402-157-48-6-202.serveousercontent.com"
    
    url = "https://textbelt.com/text"
    payload = {
        'number': target_number,
        'message': message_body,
        'key': 'textbelt',
    }
    
    try:
        response = requests.post(url, data=payload)
        print(response.json())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_sms(
    
