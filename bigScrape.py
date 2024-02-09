import subprocess

# Define the paths to the different main.py files relative to this master script
subfolder_paths = [
    'EURUSD/main.py',
    'precious_metals/main.py',
    'MSE/evaporation_materials/main.py',
    'sputtering_targets/main.py',
    'evaporation_materials/main.py' 
]

# Iterate over each path and run the script using subprocess
for path in subfolder_paths:
    print(f"Running script at: {path}")
    subprocess.run(['python', path], check=True)

print("All scripts have been run.")


