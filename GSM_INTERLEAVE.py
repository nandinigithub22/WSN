def gsm_interleave(input1, input2):
    # Check if inputs have the same length
    if len(input1) != len(input2):
        raise ValueError('Both inputs must have the same length.')

    # Initialize the list to store interleaved elements
    interleaved = []

    # Interleave the elements
    for i in range(len(input1)):
        # Append the element from the first input list
        interleaved.append(input1[i])
        # Append the element from the second input list with an offset of 3
        interleaved.append(input2[(i + 3) % len(input2)])

    return interleaved

# Example usage
input1 = [1, 2, 3, 4, 5, 6, 7, 8]  # First input list
input2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # Second input list

# Call the gsm_interleave function and store the result
interleaved = gsm_interleave(input1, input2)

# Print the interleaved list
print('Interleaved:')
print(interleaved)
