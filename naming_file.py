import os

# Path to the main flower dataset directory
dataset_dir = "data"

# Loop over each class folder
for class_name in os.listdir(dataset_dir):
    class_path = os.path.join(dataset_dir, class_name)
    
    if os.path.isdir(class_path):
        print(f"Renaming images in: {class_name}")
        
        for i, filename in enumerate(os.listdir(class_path)):
            old_path = os.path.join(class_path, filename)

            # Ensure it's an image file
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                new_filename = f"image_{i+1}.jpg"
                new_path = os.path.join(class_path, new_filename)

                os.rename(old_path, new_path)
