import sys, json

# Allow use of arrays not native to python
# https://numpy.org/doc/stable/user/absolute_beginners.html
import numpy as np

# Read data from std
def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    lines = read_in()

    np_lines = np.array(lines)

    # Use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)



# Start process
if __name__ == '__main__':
    main()
