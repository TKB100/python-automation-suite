import subprocess
import argparse

parser = argparse.ArgumentParser(description="Check if a tool is installed and get its version.")
parser.add_argument("--tool", type = str, help = "The name of the tool to check (e.g., 'python3', 'node', 'git')." )
args = parser.parse_args()  

result = subprocess.run([args.tool, "--version"], capture_output=True, text=True)

if result.returncode == 0:
    output = result.stderr.strip() or result.stdout.strip()
    version = output.split()[1]
    print(f"✅ {args.tool} is available: {version}")
else:
    print(f"❌ {args.tool} not found")