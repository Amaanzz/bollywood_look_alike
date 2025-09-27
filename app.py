import os
import pickle

image_paths = []

base_folder = "faces/actor"

for actor in os.listdir(base_folder):
    actor_folder = os.path.join(base_folder, actor)
    if os.path.isdir(actor_folder):
        for file in os.listdir(actor_folder):
            full_path = os.path.join(actor_folder, file)
            if full_path.lower().endswith((".jpg", ".jpeg", ".png")):
                image_paths.append(full_path)


pickle.dump(image_paths,open('filenames.pkl','wb'))