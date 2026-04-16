import subprocess

class Tool:
    def __init__(self, name, version = "unknown"):
        self.name = name
        self.version = version

    def describe(self):
        print(f"{self.name} - version: {self.version}")

    def is_outdated(self):
        if self.version == "unknown":
            return True
        else:
            return False
        
    def check(self):
        try:
            result = subprocess.run([self.name, "--version"], capture_output=True, text=True)
            if result.returncode == 0:
                output = result.stdout.strip() or result.stderr.strip()
                parts = output.split()
                self.version = parts[2] if len(parts) > 2 else parts[1]
                return True
            return False
        except FileNotFoundError:
            return False

if __name__ == "__main__":
    t = Tool("git")
    print(t.check())
    print(t.version)

    t2 = Tool("faketool")
    print(t2.check())
    print(t2.version)