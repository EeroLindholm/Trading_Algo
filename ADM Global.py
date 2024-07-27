# ADM Global 

# Trading algorithm

print("Hello World")

# Video #2

from PIL import Image, ImageDraw

# Create an image with a white background
width, height = 800, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw a violet bee
# Bee's body
body_coords = [(350, 250), (450, 350)]
draw.ellipse(body_coords, fill=(138, 43, 226))  # Violet color

# Bee's head
head_coords = [(320, 220), (370, 270)]
draw.ellipse(head_coords, fill=(138, 43, 226))  # Violet color

# Bee's wings
left_wing_coords = [(290, 210), (340, 270)]
right_wing_coords = [(460, 210), (510, 270)]
draw.ellipse(left_wing_coords, fill=(200, 200, 200, 128))  # Light grey
draw.ellipse(right_wing_coords, fill=(200, 200, 200, 128))  # Light grey

# Bee's stripes
stripe1_coords = [(370, 270), (400, 300)]
stripe2_coords = [(400, 300), (430, 330)]
draw.rectangle(stripe1_coords, fill=(0, 0, 0))  # Black color
draw.rectangle(stripe2_coords, fill=(0, 0, 0))  # Black color

# Bee's antennae
draw.line([(340, 220), (320, 200)], fill=(0, 0, 0), width=3)
draw.line([(350, 220), (330, 200)], fill=(0, 0, 0), width=3)

# Bee's legs
draw.line([(370, 350), (360, 380)], fill=(0, 0, 0), width=3)
draw.line([(390, 350), (380, 380)], fill=(0, 0, 0), width=3)
draw.line([(410, 350), (400, 380)], fill=(0, 0, 0), width=3)

# Add a jumping motion effect with a shadow
shadow_coords = [(355, 255), (455, 355)]
draw.ellipse(shadow_coords, outline=(0, 0, 0, 128), width=2)

# Save the image
image_path = "/Users/eerolindholm/Documents/Portfolio/Code/Python file/jumping_violet_bee.png"
image.save(image_path)
image.show()

image_path


