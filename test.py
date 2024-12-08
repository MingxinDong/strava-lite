#Name: Mingxin Dong
#CWID: 20034228
import requests

BASE_URL = "http://127.0.0.1:5000"  # 请根据你的Flask服务器地址进行调整


def test_register_user():
    response = requests.post(f"{BASE_URL}/user", json={"name": "Alice", "age": 25})
    data = response.json()
    print(data)
    return data["id"]


def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("User not found")


def test_remove_user(user_id):
    response = requests.delete(f"{BASE_URL}/user/{user_id}")
    print(f"Remove User Response: {response.status_code}")
    if response.status_code == 204:
        print("User removed successfully")
    else:
        print("User not found")


def test_list_users():
    response = requests.get(f"{BASE_URL}/user")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("No users found")


def test_add_workout(user_id):
    response = requests.post(f"{BASE_URL}/workouts/{user_id}",
                             json={"date": "2023-10-01", "time": "10:00", "distance": "5km"})
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("User not found")


def test_list_workouts(user_id):
    response = requests.get(f"{BASE_URL}/workouts/{user_id}")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("User not found")


def test_follow_friend(user_id, follow_id):
    response = requests.post(f"{BASE_URL}/follow-list/{user_id}", json={"follow_id": follow_id})
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("User or follow user not found")


def test_show_friend_workouts(user_id, friend_id):
    response = requests.get(f"{BASE_URL}/follow-list/{user_id}/{friend_id}")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("User or friend not found or not following")


if __name__ == "__main__":
    user_id_1 = test_register_user()
    user_id_2 = test_register_user()
    test_get_user(user_id_1)
    test_list_users()
    test_add_workout(user_id_1)
    test_list_workouts(user_id_1)
    test_follow_friend(user_id_1, user_id_2)
    test_show_friend_workouts(user_id_1, user_id_2)
    test_remove_user(user_id_1)
