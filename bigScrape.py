import subprocess

# Define the paths to the different main.py files relative to this master script
subfolder_paths = [
    'EURUSD/main.py',
    'precious_metals/main.py',
    'MSE/evaporation_materials/main.py',
    'sputtering_targets/main.py',
    'evaporation_materials/main.py',
    'Crucibles_and_crucible_heaters/E-Beam_sources.py',
    'Crucibles_and_crucible_heaters/HTE_LTE_crucibles.py', 
    'Crucibles_and_crucible_heaters/thermal_crucibles.py',
    'other_products/boat_sources.py',
    'other_products/box_sources.py',
    'other_products/thermal_filament_sources.py',
    'other_products/thermal_rods.py'
]

# Iterate over each path and run the script using subprocess
for path in subfolder_paths:
    print(f"Running script at: {path}")
    subprocess.run(['python', path], check=True)

print("All scripts have been run.")


