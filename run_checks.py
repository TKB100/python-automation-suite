import subprocess
import argparse

# Open and reads tools from tools.txt
with open("tools.txt", "r") as f:
    tools = [line.strip() for line in f.readlines()] # 1st it reads every line in the file and returns a list (f.readlines()), then it removes any leading/trailing whitespace from each line (line.strip()) and creates a new list of cleaned tool names.

# Loop through each tool and check if it's installed
for tool in tools:
    tool = tool.strip()
    try:
        result = subprocess.run([tool, "--version"], capture_output = True, text = True)

        if result.returncode == 0:
            output = result.stdout.strip() or result.stderr.strip()
            version = output.split()[1]
            print(f"✅ {tool} is available: {version}")
        else:
            print(f"❌ {tool} not found")
    
    except FileNotFoundError:
        print(f"{tool} not found")


def check_tool(tool):
    try:
        result = subprocess.run([tool, "--version"], capture_output = True, text = True)
        return result.returncode == 0
    except FileNotFoundError:
        return False