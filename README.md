# pygame DVD simulation

A lightweight Pygame simulation of the bouncing DVD logo, featuring an auto-scaling telemetry interface and bounce physics.

## Features
- **Physics Robustness:** Coordinate clamping prevents the logo from passing through walls, even at extreme speeds.
- **Dynamic HUD:** The metrics panel (FPS, RGB color, bounce counter, current speed) scales fully via a single `info_text_size` variable.
- **Interactivity:** Adjust movement speed in real-time while the simulation is running.

## Controls
- Click `+` on the screen to increase speed.
- Click `-` on the screen to decrease speed.

## Running the Simulation
```bash
pip install pygame
python main.py
```
