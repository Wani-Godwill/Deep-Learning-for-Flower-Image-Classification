import os
import shutil
import random

# Paths
original_data_dir = "data"
base_output_dir = "dataset"

# Splits
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create subdirectories
for split in ['train', 'val', 'test']:
    for class_name in os.listdir(original_data_dir):
        class_dir = os.path.join(original_data_dir, class_name)
        if os.path.isdir(class_dir):
            split_dir = os.path.join(base_output_dir, split, class_name)
            os.makedirs(split_dir, exist_ok=True)

# Split images
for class_name in os.listdir(original_data_dir):
    class_dir = os.path.join(original_data_dir, class_name)
    if not os.path.isdir(class_dir):
        continue

    images = [f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = train_end + int(val_ratio * total)

    split_indices = {
        'train': images[:train_end],
        'val': images[train_end:val_end],
        'test': images[val_end:]
    }

    for split, split_files in split_indices.items():
        for file in split_files:
            src = os.path.join(class_dir, file)
            dst = os.path.join(base_output_dir, split, class_name, file)
            shutil.copyfile(src, dst)
