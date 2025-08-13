import os

base = 'stimuli/ai_generated/woman_filtered'
ethnicities = ['asian', 'black', 'latino', 'white']

paths = []
for group in ethnicities:
    folder = os.path.join(base, group)
    for file in os.listdir(folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            paths.append(f'"{folder}/{file}"')

# Print list for JS
print("const imagePaths = [\n  " + ",\n  ".join(paths) + "\n];")