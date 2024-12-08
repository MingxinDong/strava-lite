# strava-lite

## Project Information
- **Name**: Mingxin Dong
- **Stevens Email**: mdong5@stevens.edu
- **GitHub Repository**: []

## Project Description
Strava Lite is a simplified version of the popular fitness tracking application Strava. It provides basic functionality for users to track their workouts and connect with other users.

### Features
- User Management
  - Register new users
  - View user profiles
  - Remove users
  - List all users
- Workout Tracking
  - Add new workouts with date, time, and distance
  - View workout history
- Social Features
  - Follow other users
  - View followed users' workouts

## API Endpoints
- `/user` (POST) - Register new user
- `/user/<user_id>` (GET) - Get user details
- `/user/<user_id>` (DELETE) - Remove user
- `/user` (GET) - List all users
- `/workouts/<user_id>` (POST) - Add new workout
- `/workouts/<user_id>` (GET) - List user's workouts
- `/follow-list/<user_id>` (POST) - Follow another user
- `/follow-list/<user_id>/<follow_id>` (GET) - View friend's workouts

## Technical Challenges and Solutions

### Challenge 1: JSON Serialization of Set Objects
**Problem**: Python's set objects are not JSON serializable, which caused errors when trying to return the user's following list.

**Solution**: Implemented a conversion step before JSON serialization, converting set objects to lists. This was done by creating a copy of the user data and converting the following set to a list before returning the response.

### Challenge 2: Route Management
**Problem**: Initially had issues with conflicting routes and unclear API endpoint naming.

**Solution**: Reorganized the API routes to be more RESTful and intuitive, separating concerns between user management, workout tracking, and social features.

### Challenge 3: Error Handling
**Problem**: Needed to handle various edge cases like self-following and accessing unauthorized workout data.

**Solution**: Implemented proper error checking and status codes:
- Added 400 status code for self-following attempts
- Added 403 status code for unauthorized workout access
- Added 404 status code for non-existent resources

## Running the Application
1. Install required dependencies:
