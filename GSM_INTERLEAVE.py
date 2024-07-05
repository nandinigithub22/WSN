def gsm_interleave(input1, input2):
    # Check if inputs have the same length
    if len(input1) != len(input2):
        raise ValueError('Both Inputs must have the same length.')

    # Initialize the list to store interleaved elements
    interleaved = []

    # Interleave the elements 
    for i in range(len(input1)):
        interleaved.append(input1[i])
        interleaved.append(input2[(i + 3) % len(input2)])

    return interleaved

# Example usage
input1 = [1, 2, 3, 4, 5, 6, 7, 8]
input2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
interleaved = gsm_interleave(input1, input2)
print('Interleaved:')
print(interleaved)
