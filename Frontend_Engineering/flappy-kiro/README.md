# Flappy Kiro

An arcade-style game where you control Ghosty, a ghost that navigates through walls with gaps. Features three difficulty levels and a global leaderboard.

## Local Development Setup

1. Start the containerized environment:
```bash
docker-compose up --build
```

2. Access the game:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Game Controls
- **Spacebar**: Make Ghosty ascend
- **Difficulty Levels**: Easy, Medium, Hard

## Architecture
- Frontend: HTML/JavaScript with OTEL logging
- Backend: Python Flask API with OTEL logging
- Storage: JSON file for leaderboard
- Containerized for local testing before cloud deployment