import pygame
import math

# --- Setup ---
pygame.init()
pygame.font.init()

# --- Constants ---
WIDTH, HEIGHT = 800, 600
SCREEN_CENTER = (WIDTH // 2, HEIGHT // 2)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SHADOW = (190, 190, 190) # A light grey for shadows

# Fonts
font = pygame.font.SysFont('Arial', 30)
font_small = pygame.font.SysFont('Arial', 24)

# --- 3D Shape Definitions ---
# Shapes are defined by vertices (points), edges (lines), and faces (polygons)

# Define the 8 vertices (points) of a cube in its local space
cube_vertices = [
    (-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
    (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1)
]

# Define the 12 edges (lines) by connecting vertex indices
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Define faces (polygons) used for shadow casting
cube_faces = [
    (0, 1, 2, 3), # Bottom
    (4, 5, 6, 7), # Top
    (0, 1, 5, 4), # Front
    (2, 3, 7, 6), # Back
    (1, 2, 6, 5), # Right
    (0, 3, 7, 4)  # Left
]

# Define the 5 vertices of a pyramid
pyramid_vertices = [
    (-1, -1, -1), ( 1, -1, -1), ( 1, -1,  1), (-1, -1,  1),  # Base
    ( 0,  1,  0)  # Apex
]

# Define the 8 edges of a pyramid
pyramid_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Base edges
    (0, 4), (1, 4), (2, 4), (3, 4)   # Side edges
]

# Define faces for pyramid
pyramid_faces = [
    (0, 1, 2, 3), # Base
    (0, 1, 4),    # Side
    (1, 2, 4),    # Side
    (2, 3, 4),    # Side
    (3, 0, 4)     # Side
]


# --- 3D Projection and Transformation ---

# Camera and projection settings
FOV = 90  # Field of View in degrees
NEAR_PLANE = 0.1
FAR_PLANE = 100.0
ASPECT_RATIO = HEIGHT / WIDTH

# Pre-calculate part of the projection matrix
# This value (f) scales x and y based on the field of view
f = 1 / math.tan(math.radians(FOV / 2))

class Shape3D:
    """
    A class to represent a 3D object with vertices, edges, faces,
    position, and rotation.
    """
    def __init__(self, vertices, edges, faces, color=BLUE):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces # Store faces for shadow casting
        self.color = color
        self.position = [0.0, 0.0, 0.0] # [x, y, z] world position
        self.rotation = [0.0, 0.0, 0.0] # [angle_x, angle_y, angle_z] rotation

def project_3d_to_2d(point_3d):
    """
    Projects a 3D point (x, y, z) to 2D screen coordinates (x, y)
    using perspective projection.
    """
    x, y, z = point_3d
    
    # Camera is at (0,0,0) looking down the positive Z-axis.
    # Clip points that are at or behind the camera (near clipping plane).
    if z < NEAR_PLANE:
        return None

    # Perspective divide: farther objects appear smaller
    # 
    x_proj = (x * f * ASPECT_RATIO) / z
    y_proj = (y * f) / z
    
    # Scale and translate to screen coordinates
    # (Invert y-axis for pygame's coordinate system where 0 is at the top)
    screen_x = int(x_proj * (WIDTH / 2) + SCREEN_CENTER[0])
    screen_y = int(-y_proj * (HEIGHT / 2) + SCREEN_CENTER[1])
    
    return (screen_x, screen_y)

def rotate_point(point, angle_x, angle_y, angle_z):
    """
    Applies 3D rotation (Z, then Y, then X) to a single point
    using rotation matrices.
    """
    x, y, z = point
    
    # Rotation around Z-axis
    cos_z = math.cos(angle_z)
    sin_z = math.sin(angle_z)
    x_rot_z = x * cos_z - y * sin_z
    y_rot_z = x * sin_z + y * cos_z
    z_rot_z = z

    # Rotation around Y-axis (using result from Z rotation)
    cos_y = math.cos(angle_y)
    sin_y = math.sin(angle_y)
    x_rot_y = x_rot_z * cos_y + z_rot_z * sin_y
    y_rot_y = y_rot_z
    z_rot_y = -x_rot_z * sin_y + z_rot_z * cos_y
    
    # Rotation around X-axis (using result from Y rotation)
    cos_x = math.cos(angle_x)
    sin_x = math.sin(angle_x)
    x_final = x_rot_y
    y_final = y_rot_y * cos_x - z_rot_y * sin_x
    z_final = y_rot_y * sin_x + z_rot_y * cos_x

    return (x_final, y_final, z_final)

# --- Application Setup ---

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Renderer")
clock = pygame.time.Clock()

# Create initial 3D objects
shapes = []
cube = Shape3D(cube_vertices, cube_edges, cube_faces, color=BLUE)
cube.position = [-2.5, 0.0, 7.0]  # Move left and "into" the screen
shapes.append(cube)

pyramid = Shape3D(pyramid_vertices, pyramid_edges, pyramid_faces, color=GREEN)
pyramid.position = [2.5, 0.0, 7.0] # Move right and "into" the screen
shapes.append(pyramid)

# Application State Variables
app_mode = 'view' # 'view' (interact) or 'draw' (create)
active_shape_index = 0 # Index in 'shapes' list that is controllable
shape_names = ["Cube", "Pyramid"] # For UI display

# Draw Mode Variables (for creating new shapes)
draw_vertices = []
draw_edges = []

# --- Main Game Loop ---
running = True
rotation_speed = 0.03
translation_speed = 0.1

while running:
    # --- 1. Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- Mode-specific event handling ---
        if app_mode == 'view':
            # Handle key presses for shape control and mode switching
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    # Change active shape
                    if shapes:
                        active_shape_index = (active_shape_index + 1) % len(shapes)
                if event.key == pygame.K_m:
                    # Switch to Draw Mode
                    app_mode = 'draw'
                    draw_vertices = []
                    draw_edges = []

        elif app_mode == 'draw':
            # Handle clicks and keys for drawing a custom shape
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    draw_vertices.append(event.pos)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: # Press 'M' to exit draw mode
                    app_mode = 'view'
                
                # 'C' to connect last two vertices
                if event.key == pygame.K_c:
                    if len(draw_vertices) >= 2:
                        start_idx = len(draw_vertices) - 2
                        end_idx = len(draw_vertices) - 1
                        draw_edges.append((start_idx, end_idx))
                
                # 'D' to finish and create the shape
                if event.key == pygame.K_d:
                    if len(draw_vertices) >= 3:
                        # Convert 2D screen points to 3D local coordinates
                        new_3d_vertices = []
                        for v in draw_vertices:
                            # Normalize screen coords (-1 to +1, scaled)
                            norm_x = (v[0] - SCREEN_CENTER[0]) / (WIDTH / 4)
                            norm_y = -(v[1] - SCREEN_CENTER[1]) / (HEIGHT / 4)
                            new_3d_vertices.append((norm_x, norm_y, 0.0)) # Create as a flat 2D shape in 3D
                        
                        # Create edges and a single face
                        new_3d_edges = list(draw_edges)
                        # Add edges to close the loop
                        for i in range(len(new_3d_vertices)):
                            if (i, (i+1) % len(new_3d_vertices)) not in new_3d_edges and ((i+1) % len(new_3d_vertices), i) not in new_3d_edges:
                                new_3d_edges.append((i, (i+1) % len(new_3d_vertices)))
                                
                        new_3d_faces = [tuple(range(len(new_3d_vertices)))]
                        
                        # Create and add the new shape
                        new_shape = Shape3D(new_3d_vertices, new_3d_edges, new_3d_faces, color=RED)
                        new_shape.position = [0.0, 0.0, 7.0] # Place in front of camera
                        shapes.append(new_shape)
                        shape_names.append(f"Custom {len(shapes) - 2}")
                        
                        # Make the new shape active
                        active_shape_index = len(shapes) - 1
                        app_mode = 'view'
                        
    # --- 2. Draw Mode Rendering ---
    if app_mode == 'draw':
        screen.fill(WHITE)
        
        # Draw UI
        draw_text = font.render("DRAW MODE", True, BLACK)
        screen.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, 10))
        help_text1 = font_small.render("Click: Add Point | C: Connect Last Two | D: Done | M: Exit", True, (50, 50, 50))
        screen.blit(help_text1, (10, HEIGHT - 40))

        # Draw vertices
        for v in draw_vertices:
            pygame.draw.circle(screen, RED, v, 5)
            
        # Draw edges
        for edge in draw_edges:
            if edge[0] < len(draw_vertices) and edge[1] < len(draw_vertices):
                pygame.draw.line(screen, BLUE, draw_vertices[edge[0]], draw_vertices[edge[1]], 2)
        
        pygame.display.flip()
        clock.tick(60)
        continue # Skip all 3D rendering

    # --- 3. View Mode: Input Handling (for active shape) ---
    keys = pygame.key.get_pressed()
    
    if shapes:
        active_shape = shapes[active_shape_index]
        
        # Rotation (Arrow Keys)
        if keys[pygame.K_LEFT]:
            active_shape.rotation[1] -= rotation_speed # Y-axis
        if keys[pygame.K_RIGHT]:
            active_shape.rotation[1] += rotation_speed
        if keys[pygame.K_UP]:
            active_shape.rotation[0] -= rotation_speed # X-axis
        if keys[pygame.K_DOWN]:
            active_shape.rotation[0] += rotation_speed
        if keys[pygame.K_q]:
            active_shape.rotation[2] -= rotation_speed # Z-axis
        if keys[pygame.K_e]:
            active_shape.rotation[2] += rotation_speed

        # Translation (WASD + R/F)
        if keys[pygame.K_a]:
            active_shape.position[0] -= translation_speed # Move left (X-)
        if keys[pygame.K_d]:
            active_shape.position[0] += translation_speed # Move right (X+)
        if keys[pygame.K_w]:
            active_shape.position[2] += translation_speed # Move forward (Z+)
        if keys[pygame.K_s]:
            active_shape.position[2] -= translation_speed # Move backward (Z-)
        if keys[pygame.K_r]:
            active_shape.position[1] += translation_speed # Move up (Y+)
        if keys[pygame.K_f]:
            active_shape.position[1] -= translation_speed # Move down (Y-)

    # --- 4. View Mode: Update Logic ---
    
    # Automatically rotate the pyramid if it's not the active shape
    if len(shapes) > 1 and "Pyramid" in shape_names:
        pyramid_index = shape_names.index("Pyramid")
        if active_shape_index != pyramid_index:
            shapes[pyramid_index].rotation[1] += 0.01 # Y-axis
            shapes[pyramid_index].rotation[0] += 0.005 # X-axis

    # --- 5. View Mode: Rendering ---
    
    # Set background color
    screen.fill(WHITE)
    
    # Render all shapes in the scene
    for shape in shapes:
        
        projected_points = []
        projected_shadow_points = []
        
        # 5a. Apply transformations and project all vertices
        for vertex in shape.vertices:
            # Step 1: Rotate point around the shape's local origin
            rotated_point = rotate_point(vertex, 
                                         shape.rotation[0], 
                                         shape.rotation[1], 
                                         shape.rotation[2])
            
            # Step 2: Translate the rotated point to its world position
            translated_point = (rotated_point[0] + shape.position[0],
                                rotated_point[1] + shape.position[1],
                                rotated_point[2] + shape.position[2])
            
            # Step 3: Project the 3D world point to 2D screen coordinates
            projected_point = project_3d_to_2d(translated_point)
            projected_points.append(projected_point)

            # Step 4: Project a shadow onto a flat plane (y = -1.5)
            # This is a simple "planar projection" shadow
            shadow_world_point = (translated_point[0], -1.5, translated_point[2])
            projected_shadow = project_3d_to_2d(shadow_world_point)
            projected_shadow_points.append(projected_shadow)

        # 5b. Draw Shadows First
        # This is a simple form of the Painter's Algorithm (drawing back-to-front)
        for face in shape.faces:
            shadow_face_points = []
            valid_shadow = True
            for i in face:
                if projected_shadow_points[i]:
                    shadow_face_points.append(projected_shadow_points[i])
                else:
                    # If any point of the shadow is clipped, don't draw the face
                    valid_shadow = False
                    break
            
            if valid_shadow and len(shadow_face_points) >= 3:
                pygame.draw.polygon(screen, SHADOW, shadow_face_points)
        
        # 5c. Draw the wireframe edges
        for edge in shape.edges:
            start_vertex_index = edge[0]
            end_vertex_index = edge[1]
            
            point_a = projected_points[start_vertex_index]
            point_b = projected_points[end_vertex_index]
            
            # Only draw if both points are valid (not clipped)
            if point_a and point_b:
                pygame.draw.line(screen, shape.color, point_a, point_b, 2)
            
        # 5d. (Optional) Draw vertices as dots
        for point in projected_points:
            if point:
                pygame.draw.circle(screen, RED, point, 3)

    # --- 6. Heads-Up Display (HUD) ---
    
    # FPS Counter
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, BLACK)
    screen.blit(fps_text, (10, 10))
    
    # Active Shape
    if shapes:
        active_text = font_small.render(f"Active: {shape_names[active_shape_index]} (TAB to switch)", True, BLACK)
        screen.blit(active_text, (10, 40))
    
    # Mode
    mode_text_str = f"Mode: VIEW (Press 'M' for DRAW)"
    mode_text = font_small.render(mode_text_str, True, BLACK)
    screen.blit(mode_text, (10, 65))

    # --- 7. Update Display ---
    pygame.display.flip()
    
    # --- 8. Control Frame Rate ---
    clock.tick(60)  # Aim for 60 frames per second

# --- Cleanup ---
pygame.quit()

