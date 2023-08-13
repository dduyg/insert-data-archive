import os
import pandas as pd
from PIL import Image
from datetime import datetime
import colorsys

# Define time ranges and corresponding hex color ranges
time_ranges = [
    ("Morning", (6, 12), ['#E7D48F', '#EDDB6F', '#e2cc0d']),
    ("Noon", (12, 15), ['#CEDCB8', '#B4F735', '#4AD83D']),
    ("Afternoon", (15, 18), ['#87B7B6', '#15C3C3', '#377D9B']),
    ("Evening", (18, 0), ['#EDB7CF', '#FD94CF', '#CC5CCC', '#CB21B5']),
    ("Night", (0, 6), ['#CFBCD0', '#93849F', '#5449C7', '#131F8F'])
]

# Function to categorize the time range based on hour
def categorize_time_range(hour):
    for label, (start, end), _ in time_ranges:
        # Check if hour falls within the range, considering wraparound for Night category
        if (start <= end and start <= hour < end) or (start > end and (start <= hour or hour < end)):
            return label

# Function to generate a hex color based on the given range and ratio
def generate_hex_color(min_hex, max_hex, ratio):
    r1, g1, b1 = [int(min_hex[i:i + 2], 16) for i in (1, 3, 5)]
    r2, g2, b2 = [int(max_hex[i:i + 2], 16) for i in (1, 3, 5)]
    
    # Interpolate color components based on the ratio
    r = int(r1 + ratio * (r2 - r1))
    g = int(g1 + ratio * (g2 - g1))
    b = int(b1 + ratio * (b2 - b1))
    
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

# Function to analyze images in the given directory
def analyze_images(directory):
    image_data = []  # To store processed image data
    skipped_images = []  # To store images without DateTimeOriginal tag
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            
            try:
                img = Image.open(filepath)
                exif_data = img._getexif()
                
                if exif_data and 36867 in exif_data:  # Check for DateTimeOriginal tag
                    capture_time = exif_data[36867]  # Extract DateTimeOriginal tag value
                    datetime_obj = datetime.strptime(capture_time, "%Y:%m:%d %H:%M:%S")  # Convert to datetime
                    hour = datetime_obj.hour
                    time_category = categorize_time_range(hour)  # Categorize time range
                    
                    for label, (start, end), hex_range in time_ranges:
                        if label == time_category:
                            ratio = (hour - start) / (end - start)
                            hex_color = generate_hex_color(hex_range[0], hex_range[-1], ratio)  # Generate color
                            # Add processed image data to the list
                            image_data.append({
                                "image": filename,
                                "time": datetime_obj.strftime("%H:%M"),
                                "category": time_category,
                                "hex_color_code": hex_color
                            })
                            break
                else:
                    skipped_images.append(filename)  # No DateTimeOriginal tag
            except (AttributeError, KeyError, ValueError) as e:
                print(f"Error processing image {filename}: {e}")
                pass
    
    return image_data, skipped_images

if __name__ == "__main__":
    input_directory = "path/to/your/images/folder"
    output_data, skipped_images = analyze_images(input_directory)
    
    df = pd.DataFrame(output_data)  # Create DataFrame from processed image data
    df.to_csv("output_data.csv", index=False)  # Export DataFrame to CSV file
    
    print("Processed images:")
    for entry in output_data:
        print(entry)
    
    if skipped_images:
        print("\nSkipped images without DateTimeOriginal tag:")
        for image in skipped_images:
            print(image)
