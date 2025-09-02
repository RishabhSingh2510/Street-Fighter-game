# 🎮 Street Fighter Game (Python + Pygame)

A **2D fighting game** inspired by classic arcade titles, built using **Python** and **Pygame**.  
The project demonstrates **Object-Oriented Programming (OOP)** concepts while providing a fun, customizable gameplay experience.

---

## Features
- **Two-player fighting mechanics** with health bars and attack logic.
- **Sprite-based animations** for characters.
- **Background music & sound effects** (Dragon Ball Z theme included).
- **Custom backgrounds** for immersive gameplay.
- **Character customization**: swap out sprite images to create your own fighters.
- Modular code using OOP principles:
  - `Game.py` → core game loop
  - `Player1.py` / `Player2.py` → player classes
  - `PlayerHealth.py` → health management
  - `sprite.py` → sprite handling
  - `SplashScreen.py` → intro splash screen

---

## 📂 Project Structure
```
Street-Fighter-game/
├── Game.py             # Main game loop
├── Player1.py          # Player 1 logic
├── Player2.py          # Player 2 logic
├── PlayerHealth.py     # Health bar system
├── sprite.py           # Sprite animations
├── SplashScreen.py     # Splash/intro screen
├── assets/             # Backgrounds, sprites, sounds
│   ├── bg.jpg
│   ├── Splashbg.jpeg
│   └── Dragon Ball Z.mp3
```

---

## Getting Started

### 1. Install Dependencies
Make sure you have Python 3.8+ and Pygame installed:
```bash
pip install pygame
```

### 2. Run the Game
```bash
python Game.py
```

---

## Customization
- Replace `bg.jpg` or `Splashbg.jpeg` with your own background images.
- Swap character sprites in `Player1.py` and `Player2.py` to use your own fighters.
- Replace the audio file in `assets/` to change background music.

---

## Tech Stack
- **Python** for game logic.
- **Pygame** for rendering, input handling, and multimedia.

---

## License
This project is open-source and free to use for educational and personal projects.

