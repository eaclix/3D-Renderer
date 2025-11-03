# 🧱 3D Renderer
*A Simple Python 3D Wireframe Renderer built from scratch using Pygame.*

![3D Renderer Screenshot](assets/screenshot.png)
<!-- You can replace this with an actual image or GIF later -->

---

## 🧠 Overview

This project is a **basic 3D scene editor** and renderer built entirely in Python using only **Pygame** for 2D drawing and windowing.  
It’s designed to help understand the **fundamentals of 3D graphics**, including:

- Vector math  
- Perspective projection  
- 3D-to-2D transformation pipelines  

---

## ✨ Features

✅ **Real-time 3D Rendering**  
All transformations and projections are computed on the CPU in real-time.

✅ **Object-Oriented Design**  
A `Shape3D` class manages multiple objects in the scene.

✅ **Full 3D Control**  
Translate and rotate active objects along all three axes (X, Y, Z).

✅ **Perspective Projection Camera**  
Objects farther away appear smaller — creating a true 3D perspective.

✅ **Multiple Shape Support**  
Comes with a Cube 🧊 and Pyramid 🔺 by default.

✅ **Custom Shape Editor (Draw Mode)**  
Click to draw a 2D shape, which is then converted into a 3D object.

✅ **Simple Shadow Casting**  
Objects cast flat projected shadows onto the ground plane.

✅ **Heads-Up Display (HUD)**  
Shows FPS, active shape, and current input mode.

---

## 🕹️ Controls

### 🎥 View Mode
**Move Active Shape**
| Key | Action |
|-----|---------|
| `W` / `S` | Move Forward / Backward (Z-axis) |
| `A` / `D` | Move Left / Right (X-axis) |
| `R` / `F` | Move Up / Down (Y-axis) |

**Rotate Active Shape**
| Key | Action |
|-----|---------|
| `↑` / `↓` | Rotate around X-axis |
| `←` / `→` | Rotate around Y-axis |
| `Q` / `E` | Roll around Z-axis |

**Scene Controls**
| Key | Action |
|-----|---------|
| `TAB` | Switch active (controllable) shape |
| `M` | Toggle Draw Mode |

---

### ✏️ Draw Mode
| Key / Action | Description |
|---------------|-------------|
| **Left Mouse Click** | Add a new vertex |
| **C** | Connect last two points with an edge |
| **D** | Finish drawing and create 3D object |
| **M** | Cancel drawing and return to View Mode |

---

## 🚀 How to Run

1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName

2️⃣ Install Dependencies

You only need Pygame:
pip install pygame

3️⃣ Run the Renderer
python simple_3d_renderer.py

💡 Future Ideas
 Implement solid-face rendering using the Painter’s Algorithm (back-to-front sorting).
 Add Z-Buffering (depth buffering) for accurate solid rendering.
 Implement mouse-based camera controls (mouselook).
 Write a simple .obj file loader to import models from Blender.

📷 Screenshots / Demo
Example Scene	Draw Mode	Shadow Example

	
	
🧩 Tech Stack

Language: Python 🐍

Graphics Library: Pygame 🎮

Rendering Type: CPU-based 3D Wireframe

🧑‍💻 Author

Eakansh Bhardwaj
📫 [YourEmail@example.com
]
🌐 [Portfolio / LinkedIn / GitHub link here]
