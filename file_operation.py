def print_input_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))


# This function returns an array of [origin_label, destination_label, cost]
def parse_input_file(filename):
    result = []
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    for line in lines:
        if line == "END OF INPUT":
            break
        result.append(line.split())
    return result
