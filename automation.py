import subprocess

result = subprocess.run(["Python3", "--version"], capture_output=True, text=True)

if result.returncode != 0:
    print("Error: Could not determine Python version.")
else:
    output = result.stdout.strip() or result.stderr.strip()
    version = output.split()[1]
    print(f"Python version: {version}")