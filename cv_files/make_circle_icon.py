from PIL import Image, ImageDraw

def create_circular_icon(input_path, output_path):
    try:
        # Open the image
        img = Image.open(input_path).convert("RGBA")
        
        # Create a circular mask
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        width, height = img.size
        # Draw a white circle on the black mask
        draw.ellipse((0, 0, width, height), fill=255)
        
        # Apply the mask
        output = Image.new('RGBA', img.size, (0, 0, 0, 0))
        output.paste(img, (0, 0), mask=mask)
        
        # Resize to standard favicon size (optional, but good for performance)
        # Keeping high res for now as it's just a shortcut icon, but usually 32x32 or 64x64 is standard. 
        # The user's original is likely larger (profile photo).
        # Let's resize it to a reasonable icon size, e.g., 64x64 or 192x192 for modern screens
        output = output.resize((192, 192), Image.Resampling.LANCZOS)
        
        # Save
        output.save(output_path)
        print(f"Successfully created circular icon at {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Adjust paths as per the user's workspace
    create_circular_icon('e:/Verosariferdinand/cv_files/1.jpg', 'e:/Verosariferdinand/cv_files/1_circle.png')
