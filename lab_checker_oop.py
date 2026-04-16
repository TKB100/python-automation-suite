from oop import Tool

with open("tools.txt", "r") as f:
    tools = [line.strip() for line in f.readlines()]

reports = []

for tool in tools:
    t = Tool(tool)
    installed = t.check()
    reports.append(t)

print("===== Lab Environment Report =====")
for report in reports:
    installed = report.check()
    icon = "✅" if installed else "❌"
    print(f"{icon} {report.name} | version: {report.version}")

print("==================================")