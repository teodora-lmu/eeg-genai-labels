import os

bases = [
    'stimuli/ai_generated/man_filtered',
    'stimuli/ai_generated/woman_filtered'
]
ethnicities = ['asian', 'black', 'latino', 'white']

paths = []
for base in bases:
    for group in ethnicities:
        folder = os.path.join(base, group)
        if not os.path.exists(folder):
            continue
        for file in os.listdir(folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                paths.append(f'"{folder}/{file}"')

# Print list for JS
print("const imagePaths = [\n  " + ",\n  ".join(paths) + "\n];")