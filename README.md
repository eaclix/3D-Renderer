# 🧩 **Python 3D Renderer**

A simple yet powerful **3D Renderer** built entirely in **Python** using only the **Pygame** library.
This project was developed to explore the **core principles of 3D graphics**, including **vector math**, **matrix transformations**, **perspective projection**, and **3D-to-2D rendering** — all from scratch.

🎥 <img width="500" height="500" alt="Image" src="https://github.com/user-attachments/assets/0b1268fc-69e0-470d-96bf-fb3ca4f7d113" />

---

## 🚀 **Features**

✅ **Real-time 3D Rendering** — All transformations and projections are handled on the CPU in real time.

✅ **Object-Oriented Architecture** — `Shape3D` class manages all 3D objects cleanly and efficiently.

✅ **Full 3D Control** — Move and rotate objects freely along **X**, **Y**, and **Z** axes.

✅ **Perspective Camera** — Realistic depth perception where distant objects appear smaller.

✅ **Built-in Shapes** — Includes **Cube** and **Pyramid** examples.

✅ **Interactive Shape Editor** — Create custom shapes in **Draw Mode**.

✅ **Simple Shadow Projection** — Flat shadows projected on the ground plane.

✅ **On-Screen HUD** — Displays FPS, current shape, and input mode dynamically.

---

## ⚙️ **Setup & Installation**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YourUsername/3D-Renderer.git
cd 3D-Renderer
```

### 2️⃣ Install Dependencies

Only **pygame** is required:

```bash
pip install pygame
```

### 3️⃣ Run the Renderer

```bash
python 3d_renderer.py
```

---

## 🎮 **Controls**

### 🧭 View Mode

**Move Active Shape**

* `W / S` → Move Forward / Backward *(Z-axis)*
* `A / D` → Move Left / Right *(X-axis)*
* `R / F` → Move Up / Down *(Y-axis)*

**Rotate Active Shape**

* `↑ / ↓` → Rotate on X-axis
* `← / →` → Rotate on Y-axis
* `Q / E` → Roll on Z-axis

**Scene Controls**

* `TAB` → Switch Active Shape
* `M` → Toggle Draw Mode

---

### ✏️ Draw Mode

* 🖱️ **Left Click** — Add a new vertex
* `C` — Connect last two points with an edge
* `D` — Finalize shape creation
* `M` — Cancel and return to View Mode

---

## 🌱 **Future Improvements**

✨ **Solid Rendering** — Implement **Painter’s Algorithm** for filled faces.
✨ **Z-Buffering** — Depth-based pixel rendering for realistic occlusion.
✨ **Mouse Camera Controls** — Add mouse-driven navigation (mouselook).
✨ **.OBJ Import** — Load 3D models from tools like **Blender**.

---

## 🧠 **Learning Outcomes**

This renderer is a hands-on deep dive into:

* 3D coordinate systems (local, world, view, projection)
* Matrix transformations and homogeneous coordinates
* Perspective projection math
* Real-time rendering logic and optimization

---

## 📸 **Preview**

<img width="500" height="500" alt="Image" src="https://github.com/user-attachments/assets/0b1268fc-69e0-470d-96bf-fb3ca4f7d113" />

<img width="500" height="500" alt="Image" src="https://github.com/user-attachments/assets/e7563074-f6fb-4e76-9029-4cbd22e33952" />

---

## 🤝 **Contributing**

Pull requests are welcome! Feel free to open issues for bugs, suggestions, or feature requests.
If you build something cool with this, share it — I’d love to see it!

---

