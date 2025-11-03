# 🧠 Python 3D Renderer

A **3D Wireframe Renderer** built **from scratch** in **Python**, using only **Pygame** for 2D drawing and windowing.

This project demonstrates the **core principles of real-time 3D rendering**, including transformations, projections, and shadows — all implemented manually without any external 3D engine.

https://github.com/user-attachments/assets/96a3dcf4-254e-400b-9083-870a5e62e942

---

## 🚀 Overview

This project recreates a simplified version of how real graphics engines like **Blender (Eevee)** or **Unity** handle 3D graphics — but entirely in Python code.  
It’s a hands-on implementation of the **3D Rendering Pipeline**.

---

## 🏗️ What I Built

### 🧩 Core Technology
- **Language:** Python  
- **Library:** Pygame (for windowing, input, and 2D drawing)
- **Rendering Type:** Wireframe Rendering (edges only)

### 🧠 Data Structures

| Type | Description | Example |
|------|--------------|---------|
| `vertices` | List of (x, y, z) coordinates representing points in local space | `[(-1, 1, -1), (1, 1, -1), ...]` |
| `edges` | List of (index1, index2) pairs connecting vertices with lines | `[(0,1), (1,2), ...]` |
| `faces` | List of (index1, index2, index3, …) tuples used for shadow drawing | `[(0,1,2,3), ...]` |

---

### 🌗 Shadows — *Planar Projection*

A simple **fake shadow** technique used in many old-school 3D games:
- Flatten the 3D object onto a virtual floor plane (e.g., `y = -1.5`).
- Draw the flattened 2D polygon using a darker color.

It’s fast and visually effective — though not physically accurate.

---

### 🌀 Transformation Pipeline

Every frame, each object passes through the following pipeline:

1. **Model Space:** Raw shape coordinates (e.g., cube from -1 to 1).  
2. **World Space:**  
   - Rotate vertices around the object’s center (`rotate_point`).  
   - Translate by the shape’s position to place it in the scene.  
3. **View Space:**  
   - The “camera” is fixed at `(0, 0, 0)` looking down the **Z-axis**.  
4. **Projection:**  
   - Use **Perspective Projection:**  
     \[
     \text{screen\_coord} = \frac{\text{world\_coord}}{\text{world\_z}}
     \]
     This division by `z` makes distant objects appear smaller — the essence of 3D perspective.  
5. **Screen Space:**  
   - Scale and center projected points to fit the 800×600 window.

---

## 🔀 Alternative Approaches

### 🧱 Rendering Alternatives

| Technique | Description | Complexity |
|------------|-------------|-------------|
| **Solid Face Rendering (Painter’s Algorithm)** | Sort faces by depth (Z-average) and draw polygons from back to front using `pygame.draw.polygon()` | Medium |
| **Z-Buffering (Depth Buffer)** | Maintain a depth grid for each pixel; only draw pixels closer to the camera | High (real GPU method) |

---

### ⚙️ Technology Alternatives

| Framework | Type | Description |
|------------|------|-------------|
| **PyOpenGL** | GPU-based | Real OpenGL in Python — offloads vertex math to the GPU |
| **ModernGL** | Modern GPU-based | A cleaner, Pythonic OpenGL interface — used in real-time applications |

This project, by contrast, is a **CPU Renderer** — all math runs on the CPU via Python loops.

---

## 🧮 Comparison to Blender

| Feature | 🧠 My Project | ⚡ Blender (Eevee) | ☀️ Blender (Cycles) |
|----------|---------------|-------------------|--------------------|
| **Who Does the Math?** | CPU (Python) | GPU (Graphics Card) | CPU or GPU |
| **Core Technique** | Rasterization (Manual) | Rasterization (Hardware-Accelerated) | Path Tracing (Simulated Light Physics) |
| **Goal** | Educational, Real-time Basics | Real-time Visualization | Photorealistic Rendering |
| **Speed** | 🐢 Slow (for Python) | ⚡ Very Fast (Real-time) | 🕐 Very Slow (Minutes/Frame) |
| **Lighting** | Flat / Fake Shadows | Dynamic Shaders, Materials | Physically Accurate Light Simulation |

> 🧩 In short:  
> I built the **Model-T version of Blender’s Eevee engine** — demonstrating the same *fundamental rasterization concepts* all real-time 3D graphics are built on.

---

## 💡 What I Learned

This project taught me far more than just rendering — it gave me a foundation in **graphics programming and software design**.

### 📘 Core Lessons

- **The 3D Pipeline:** Built a working version of  
  `Model → World → View → Projection → Screen`.  
- **Vector Math in Practice:** Applied `sin()`, `cos()`, and `(x, y, z)` math to control rotation and projection.  
- **State Management:** Handled rendering modes, frame timing, and scene updates.  
- **Data-Driven Design:** Added new shapes dynamically by defining vertices and edges — no need to rewrite the render loop.  
- **Abstraction:** Functions like `rotate_point()` and `project_3d_to_2d()` encapsulate complex math, making the code clean and reusable.

---

## 🧰 Tech Stack

| Category | Tool |
|-----------|------|
| **Language** | Python |
| **Graphics Library** | Pygame |
| **Math** | Numpy (optional for optimization) |
| **IDE** | VS Code / PyCharm |

---

