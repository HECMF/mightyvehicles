from PIL import Image

img = Image.new('RGBA', (128, 128), (0, 0, 0, 0))

# Swiss International Air Lines livery colors
WHITE = (255, 255, 255, 255)
NEAR_WHITE = (248, 248, 250, 255)
SWISS_RED = (226, 0, 26, 255)
DARK_GREY = (70, 72, 78, 255)
MED_GREY = (145, 148, 155, 255)
LIGHT_GREY = (200, 202, 208, 255)
WINDOW_DARK = (25, 35, 55, 255)
COCKPIT_GLASS = (35, 60, 95, 255)
COCKPIT_FRAME = (55, 58, 65, 255)
ENGINE_DARK = (52, 55, 62, 255)
ENGINE_MED = (78, 80, 88, 255)
ENGINE_INTAKE = (95, 98, 105, 255)
GEAR_DARK = (42, 44, 50, 255)
WING_TOP = (208, 210, 215, 255)
WING_BTM = (168, 170, 175, 255)
NAV_RED = (255, 0, 0, 255)
NAV_GREEN = (0, 200, 0, 255)


def fill(x, y, w, h, color):
    for py in range(y, y + h):
        for px in range(x, x + w):
            if 0 <= px < 128 and 0 <= py < 128:
                img.putpixel((px, py), color)


def px(x, y, color):
    if 0 <= x < 128 and 0 <= y < 128:
        img.putpixel((x, y), color)


# ===========================================================
# FUSELAGE (W=6, H=6, D=24, UV=[0,0])
# UV area: 60 x 30 from (0,0)
# ===========================================================

# Top face: (24,0) 6x24 - white roof with subtle centerline
fill(24, 0, 6, 24, WHITE)
for z in range(0, 24):
    px(27, z, NEAR_WHITE)  # subtle center seam

# Bottom face: (30,0) 6x24 - dark grey belly
fill(30, 0, 6, 24, DARK_GREY)
# Panel lines on belly
for z in range(0, 24, 6):
    for x in range(30, 36):
        px(x, z, MED_GREY)

# Right side: (0,24) 24x6  (x=0 = nose, x=23 = tail)
fill(0, 24, 24, 6, WHITE)
fill(0, 28, 24, 1, LIGHT_GREY)
fill(0, 29, 24, 1, DARK_GREY)
# Passenger windows (row y=26) from x=3 to x=18
for wx in range(3, 19, 2):
    px(wx, 26, WINDOW_DARK)
# Door outlines
px(3, 25, LIGHT_GREY)
px(3, 26, LIGHT_GREY)
px(3, 27, LIGHT_GREY)
px(12, 25, LIGHT_GREY)  # mid-cabin door
px(12, 26, LIGHT_GREY)
px(12, 27, LIGHT_GREY)

# Front face (nose end): (24,24) 6x6
fill(24, 24, 6, 6, WHITE)
fill(24, 28, 6, 1, LIGHT_GREY)
fill(24, 29, 6, 1, DARK_GREY)

# Left side: (30,24) 24x6  (x=30 = tail, x=53 = nose)
fill(30, 24, 24, 6, WHITE)
fill(30, 28, 24, 1, LIGHT_GREY)
fill(30, 29, 24, 1, DARK_GREY)
# Passenger windows (mirrored)
for wx in range(35, 51, 2):
    px(wx, 26, WINDOW_DARK)
# Door outlines
px(50, 25, LIGHT_GREY)
px(50, 26, LIGHT_GREY)
px(50, 27, LIGHT_GREY)
px(41, 25, LIGHT_GREY)
px(41, 26, LIGHT_GREY)
px(41, 27, LIGHT_GREY)

# Back face (tail end): (54,24) 6x6
fill(54, 24, 6, 6, WHITE)
fill(54, 28, 6, 1, LIGHT_GREY)
fill(54, 29, 6, 1, DARK_GREY)

# ===========================================================
# NOSE (W=4, H=4, D=4, UV=[0,30])
# ===========================================================

# Top: (4,30) 4x4
fill(4, 30, 4, 4, WHITE)

# Bottom: (8,30) 4x4
fill(8, 30, 4, 4, DARK_GREY)

# Right: (0,34) 4x4
fill(0, 34, 4, 4, WHITE)
fill(0, 37, 4, 1, MED_GREY)

# Front (nose tip): (4,34) 4x4
fill(4, 34, 4, 4, LIGHT_GREY)
fill(5, 34, 2, 3, WHITE)  # lighter center
px(5, 37, MED_GREY)
px(6, 37, MED_GREY)
# Radome detail (dark nose cone tip)
px(5, 35, MED_GREY)
px(6, 35, MED_GREY)

# Left: (8,34) 4x4
fill(8, 34, 4, 4, WHITE)
fill(8, 37, 4, 1, MED_GREY)

# Back: (12,34) 4x4
fill(12, 34, 4, 4, WHITE)
fill(12, 37, 4, 1, MED_GREY)

# ===========================================================
# COCKPIT (W=5, H=3, D=6, UV=[0,40])
# ===========================================================

# Top: (6,40) 5x6 - cockpit roof
fill(6, 40, 5, 6, WHITE)

# Bottom: (11,40) 5x6
fill(11, 40, 5, 6, WHITE)

# Right side windows: (0,46) 6x3
fill(0, 46, 6, 3, COCKPIT_FRAME)
# Glass panels with dividers
fill(1, 46, 2, 2, COCKPIT_GLASS)
fill(4, 46, 1, 2, COCKPIT_GLASS)

# Front windshield: (6,46) 5x3
fill(6, 46, 5, 3, COCKPIT_FRAME)
fill(7, 46, 1, 2, COCKPIT_GLASS)
fill(9, 46, 1, 2, COCKPIT_GLASS)

# Left side windows: (11,46) 6x3
fill(11, 46, 6, 3, COCKPIT_FRAME)
fill(12, 46, 1, 2, COCKPIT_GLASS)
fill(14, 46, 2, 2, COCKPIT_GLASS)

# Back: (17,46) 5x3
fill(17, 46, 5, 3, WHITE)

# ===========================================================
# LEFT WING (W=14, H=1, D=6, UV=[0,50])
# ===========================================================

# Top: (6,50) 14x6 - silver wing with panel detail
fill(6, 50, 14, 6, WING_TOP)
# Flap line
for x in range(6, 20):
    px(x, 54, LIGHT_GREY)
# Engine pylon shadow
px(9, 52, MED_GREY)
px(9, 53, MED_GREY)
# Wing tip - navigation light (red on left wing = port)
px(19, 52, NAV_RED)
px(19, 53, NAV_RED)

# Bottom: (20,50) 14x6
fill(20, 50, 14, 6, WING_BTM)
for x in range(20, 34):
    px(x, 54, MED_GREY)

# Edge faces (1px tall)
fill(0, 56, 6, 1, WING_TOP)
fill(6, 56, 14, 1, WING_TOP)
fill(20, 56, 6, 1, WING_TOP)
fill(26, 56, 14, 1, WING_BTM)

# ===========================================================
# RIGHT WING (W=14, H=1, D=6, UV=[0,58])
# ===========================================================

# Top: (6,58) 14x6
fill(6, 58, 14, 6, WING_TOP)
for x in range(6, 20):
    px(x, 62, LIGHT_GREY)
px(9, 60, MED_GREY)
px(9, 61, MED_GREY)
# Navigation light (green on right wing = starboard)
px(19, 60, NAV_GREEN)
px(19, 61, NAV_GREEN)

# Bottom: (20,58) 14x6
fill(20, 58, 14, 6, WING_BTM)
for x in range(20, 34):
    px(x, 62, MED_GREY)

# Edge faces
fill(0, 64, 6, 1, WING_TOP)
fill(6, 64, 14, 1, WING_TOP)
fill(20, 64, 6, 1, WING_TOP)
fill(26, 64, 14, 1, WING_BTM)

# ===========================================================
# TAIL VERTICAL (W=1, H=6, D=4, UV=[60,0])
# This is the iconic SWISS red tail with white cross!
# ===========================================================

# Top: (64,0) 1x4
fill(64, 0, 1, 4, SWISS_RED)

# Bottom: (65,0) 1x4
fill(65, 0, 1, 4, SWISS_RED)

# Right side: (60,4) 4x6 - RED with Swiss cross
fill(60, 4, 4, 6, SWISS_RED)
# Swiss cross:
# Vertical bar (2px wide, 4px tall, centered)
px(61, 5, WHITE); px(62, 5, WHITE)
px(61, 6, WHITE); px(62, 6, WHITE)
px(61, 7, WHITE); px(62, 7, WHITE)
px(61, 8, WHITE); px(62, 8, WHITE)
# Horizontal bar (4px wide, 2px tall, centered)
px(60, 6, WHITE); px(63, 6, WHITE)
px(60, 7, WHITE); px(63, 7, WHITE)

# Front edge: (64,4) 1x6
fill(64, 4, 1, 6, SWISS_RED)

# Left side: (65,4) 4x6 - RED with Swiss cross
fill(65, 4, 4, 6, SWISS_RED)
px(66, 5, WHITE); px(67, 5, WHITE)
px(66, 6, WHITE); px(67, 6, WHITE)
px(66, 7, WHITE); px(67, 7, WHITE)
px(66, 8, WHITE); px(67, 8, WHITE)
px(65, 6, WHITE); px(68, 6, WHITE)
px(65, 7, WHITE); px(68, 7, WHITE)

# Back edge: (69,4) 1x6
fill(69, 4, 1, 6, SWISS_RED)

# ===========================================================
# TAIL HORIZONTAL (W=10, H=1, D=3, UV=[60,10])
# ===========================================================

# Top: (63,10) 10x3 - white
fill(63, 10, 10, 3, WHITE)

# Bottom: (73,10) 10x3
fill(73, 10, 10, 3, LIGHT_GREY)

# Edges (1px tall)
fill(60, 13, 3, 1, WHITE)
fill(63, 13, 10, 1, WHITE)
fill(73, 13, 3, 1, WHITE)
fill(76, 13, 10, 1, WHITE)

# ===========================================================
# LEFT ENGINE (W=3, H=3, D=4, UV=[60,16])
# ===========================================================

# Top: (64,16) 3x4
fill(64, 16, 3, 4, ENGINE_DARK)
fill(65, 16, 1, 4, ENGINE_MED)  # highlight

# Bottom: (67,16) 3x4
fill(67, 16, 3, 4, ENGINE_DARK)

# Right: (60,20) 4x3
fill(60, 20, 4, 3, ENGINE_DARK)
fill(60, 20, 4, 1, ENGINE_MED)  # top edge lighter

# Front (intake): (64,20) 3x3 - circular intake detail
fill(64, 20, 3, 3, ENGINE_MED)
px(65, 21, ENGINE_DARK)  # center hub
px(64, 20, ENGINE_INTAKE)
px(66, 20, ENGINE_INTAKE)
px(64, 22, ENGINE_INTAKE)
px(66, 22, ENGINE_INTAKE)

# Left: (67,20) 4x3
fill(67, 20, 4, 3, ENGINE_DARK)
fill(67, 20, 4, 1, ENGINE_MED)

# Back (exhaust): (71,20) 3x3
fill(71, 20, 3, 3, ENGINE_DARK)
px(72, 21, (100, 85, 70, 255))  # warm exhaust tint

# ===========================================================
# RIGHT ENGINE (W=3, H=3, D=4, UV=[60,24])
# ===========================================================

# Top: (64,24) 3x4
fill(64, 24, 3, 4, ENGINE_DARK)
fill(65, 24, 1, 4, ENGINE_MED)

# Bottom: (67,24) 3x4
fill(67, 24, 3, 4, ENGINE_DARK)

# Right: (60,28) 4x3
fill(60, 28, 4, 3, ENGINE_DARK)
fill(60, 28, 4, 1, ENGINE_MED)

# Front (intake): (64,28) 3x3
fill(64, 28, 3, 3, ENGINE_MED)
px(65, 29, ENGINE_DARK)
px(64, 28, ENGINE_INTAKE)
px(66, 28, ENGINE_INTAKE)
px(64, 30, ENGINE_INTAKE)
px(66, 30, ENGINE_INTAKE)

# Left: (67,28) 4x3
fill(67, 28, 4, 3, ENGINE_DARK)
fill(67, 28, 4, 1, ENGINE_MED)

# Back (exhaust): (71,28) 3x3
fill(71, 28, 3, 3, ENGINE_DARK)
px(72, 29, (100, 85, 70, 255))

# ===========================================================
# LANDING GEAR LEFT (W=1, H=3, D=2, UV=[76,0])
# ===========================================================
fill(78, 0, 1, 2, GEAR_DARK)   # Top
fill(79, 0, 1, 2, GEAR_DARK)   # Bottom
fill(76, 2, 2, 3, GEAR_DARK)   # Right
fill(78, 2, 1, 3, GEAR_DARK)   # Front
fill(79, 2, 2, 3, GEAR_DARK)   # Left
fill(81, 2, 1, 3, GEAR_DARK)   # Back
# Wheel detail
px(76, 4, (30, 30, 35, 255))
px(80, 4, (30, 30, 35, 255))

# ===========================================================
# LANDING GEAR RIGHT (W=1, H=3, D=2, UV=[76,6])
# ===========================================================
fill(78, 6, 1, 2, GEAR_DARK)
fill(79, 6, 1, 2, GEAR_DARK)
fill(76, 8, 2, 3, GEAR_DARK)
fill(78, 8, 1, 3, GEAR_DARK)
fill(79, 8, 2, 3, GEAR_DARK)
fill(81, 8, 1, 3, GEAR_DARK)
px(76, 10, (30, 30, 35, 255))
px(80, 10, (30, 30, 35, 255))

# Save
out = '/mnt/c/Privat/Minecraft/Mighty Mobs/mightyvehicles/MightyVehicles_RP/textures/entity/flugzeug.png'
img.save(out)
print(f"Swiss Air texture saved to {out}")
