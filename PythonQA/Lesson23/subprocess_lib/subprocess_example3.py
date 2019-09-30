# Import the module
import subprocess

# Ask the user for input
host = "ya.ru"

# Set up the echo command and direct the output to a pipe
"""
PIPE indicates that a new pipe to the child should be created.
The default setting is "None", which means that no redirection will occur.
The standard error (or stderr) can be STDOUT, which indicates that the stderr
data from the child process should be captured into the same file handle as
for stdout. 
"""
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print(output)
