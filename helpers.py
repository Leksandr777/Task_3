import requests
import random

BASE_REGISTER_URL = "https://qa-stellarburgers.education-services.ru/api/auth/register"

BASE_DELETE_URL = "https://qa-stellarburgers.education-services.ru/api/auth/user"

def create_user():
    suffix = random.randint(1, 10000)
    user_password = "TestPassword" 
    user_data = {
        "email": f"test_user_{suffix}@test.ru",
        "password": user_password,
        "name": f"TestName_{suffix}"
    }
     
    response = requests.post(BASE_REGISTER_URL, json=user_data)
    response_data = response.json()
    
    if not response_data.get('success'):
        raise Exception(f"Ошибка регистрации: {response_data.get('message')}")
    
    user_info = response_data['user']
    user_info['password'] = user_password
    user_info['accessToken'] = response_data['accessToken']  # Добавляем это
    user_info['refreshToken'] = response_data['refreshToken']
    
    return user_info


def delete_user(user_info):
    headers = {"Authorization": f"{user_info['accessToken']}"}
    response = requests.delete(BASE_DELETE_URL, headers=headers)
    if response.status_code not in (202, 204):
        raise Exception(f"Ошибка при удалении пользователя: {response.status_code}")