from run_checks import check_tool 
from fundamentals import tool_report

with open("tools.txt", "r") as f:
    tools = [line.strip() for line in f.readlines()]

reports = []

for tool in tools:
    installed = check_tool(tool)
    reports.append(tool_report(tool, installed))


print("===== Lab Environment Report =====")
for report in reports:
    icon = "✅" if report["installed"] else "❌"
    print(f"{icon} {report['tool']} | version: {report['version']}")

print("==================================")

