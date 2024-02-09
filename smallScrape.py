import subprocess


# Define the paths to the different main.py files relative to this master script
subfolder_paths = [
    'EURUSD/main.py',
    'precious_metals/main.py'
    ]

# Iterate over each path and run the script using subprocess
for path in subfolder_paths:
    print(f"Running script at: {path}")
    subprocess.run(['python', path], check=True)

print("Both exchange rate and precious metal prices scrapes have been run!")
