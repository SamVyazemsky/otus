import sys

print(sys.argv)
print(sys.executable)
print(sys.path)
sys.path.append("/path/to/my/module")
print(sys.path)
print(sys.platform)
os = sys.platform
if os == "win32":
    import _winreg
elif os.startswith('linux'):
    import subprocess
    subprocess.Popen(["ls, -l"])
sys.exit(0)
