#Name: Mingxin Dong
#CWID: 20034228

import uuid

from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = {}


class RegisterUser(Resource):
    def post(self):
        data = request.get_json()
        user_id = str(uuid.uuid4())
        users[user_id] = {
            "id": user_id,
            "name": data["name"],
            "age": data["age"],
            "workouts": [],
            "following": set()
        }
        response_data = users[user_id].copy()
        response_data["following"] = list(response_data["following"])
        return jsonify(response_data)


class GetUser(Resource):
    def get(self, user_id):
        if user_id in users:
            user = users[user_id].copy()
            user["following"] = list(user["following"])
            return jsonify(user)
        return "", 404


class RemoveUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return "", 204
        return "", 404


class ListUsers(Resource):
    def get(self):
        user_list = []
        for user in users.values():
            user_copy = user.copy()
            user_copy["following"] = list(user_copy["following"])
            user_list.append(user_copy)
        return jsonify(user_list)


class AddWorkout(Resource):
    def post(self, user_id):
        if user_id in users:
            data = request.get_json()
            workout = {
                "date": data["date"],
                "time": data["time"],
                "distance": data["distance"]
            }
            users[user_id]["workouts"].append(workout)
            return jsonify(workout)
        return "", 404


class ListWorkouts(Resource):
    def get(self, user_id):
        if user_id in users:
            return jsonify({"workouts": users[user_id]["workouts"]})
        return "", 404


class FollowFriend(Resource):
    def post(self, user_id):
        data = request.get_json()
        follow_id = data.get("follow_id")
        if user_id in users and follow_id in users:
            if user_id == follow_id:
                return {"error": "Can't focus on myself"}, 400
            users[user_id]["following"].add(follow_id)
            return jsonify({"following": list(users[user_id]["following"])})
        return "", 404


class ShowFriendWorkouts(Resource):
    def get(self, user_id, friend_id):
        if user_id in users and friend_id in users:
            if friend_id not in users[user_id]["following"]:
                return {"error": "You have not followed this user yet"}, 403
            return jsonify({"workouts": users[friend_id]["workouts"]})
        return "", 404


api.add_resource(RegisterUser, "/user")
api.add_resource(GetUser, "/user/<string:user_id>")
api.add_resource(RemoveUser, "/user/<string:user_id>")
api.add_resource(ListUsers, "/user")
api.add_resource(AddWorkout, "/workouts/<string:user_id>")
api.add_resource(ListWorkouts, "/workouts/<string:user_id>")
api.add_resource(FollowFriend, "/follow-list/<string:user_id>")
api.add_resource(ShowFriendWorkouts, "/follow-list/<string:user_id>/<string:follow_id>")

if __name__ == "__main__":
    app.run(debug=True)
