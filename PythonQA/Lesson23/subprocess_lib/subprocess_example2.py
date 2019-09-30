import subprocess

program = "gedit"
process = subprocess.Popen(program)
code = process.wait()

print(code)
