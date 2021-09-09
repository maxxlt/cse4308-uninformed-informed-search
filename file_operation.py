def print_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
