def filter_tools(tools):
    return [tool for tool in tools if len(tool) > 3]

print(filter_tools(["git", "python3", "node", "go"]))
# should print: ['python3', 'node']

def describe_tool(tool, installed = False):
    if installed:
        return f"{tool}: ready"
    else:
         return f"{tool}: missing"

print(describe_tool("git", True))   # "git: ready"
print(describe_tool("git", False))  # "git: missing"
print(describe_tool("git"))         # "git: missing" (default)

def tool_report(tool, installed, version = "unknown"):
    tool_info = {
        "tool": tool,
        "installed": installed,
        "version": version
    }
    return tool_info

print(tool_report("git", True, "2.39"))
print(tool_report("node", False))