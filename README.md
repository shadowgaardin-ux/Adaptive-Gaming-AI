# Adaptive Gaming AI — Prototype 0.1

A Python/Pygame starter game for a final-year AI project. This first milestone is a playable top-down arena; the opponent currently uses a simple pursuit rule.

## Requirements
- Python 3.10+
- Pygame 2.5+

## Run on Windows
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Controls
- WASD or arrow keys: move
- Space: shoot toward the opponent
- Esc: pause/unpause
- R: restart after defeat

## Roadmap
1. Playable baseline arena (current)
2. Gameplay event logging
3. Player behavior model
4. Adaptive opponent tactics
5. Procedural level generation with path validation
6. Evaluation against fixed-baseline behavior

The current AI is deliberately simple; adaptive learning is the next milestone.
