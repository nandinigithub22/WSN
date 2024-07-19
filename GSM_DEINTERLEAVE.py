def gsm_deinterleave(interleaved):
    # Check if the length of interleaved list is even
    if len(interleaved) % 2 != 0:
        raise ValueError('Interleaved list length must be even.')

    # Calculate the length of de-interleaved lists
    length = len(interleaved) // 2

    # Initialize lists for de-interleaved elements
    deinterleaved1 = []
    deinterleaved2 = []

    # De-interleave the elements
    for i in range(length):
        deinterleaved1.append(interleaved[i * 2])  # Append to deinterleaved1 first
        deinterleaved2.append(interleaved[i * 2 + 1])  # Then append to deinterleaved2

    # Convert de-interleaved lists to arrays if they contain characters
    if isinstance(deinterleaved1[0], str):
        deinterleaved1 = ''.join(deinterleaved1)
        deinterleaved2 = ''.join(deinterleaved2)

    # Sort the de-interleaved lists if they contain characters
    if isinstance(deinterleaved1, str):
        deinterleaved1 = ''.join(sorted(deinterleaved1))
        deinterleaved2 = ''.join(sorted(deinterleaved2))

    return deinterleaved1, deinterleaved2

# Example 
interleaved = [1, 'e', 2, 'f', 3, 'g', 4, 'h', 5, 'a', 6, 'b', 7, 'c', 8, 'd']
deinterleaved1, deinterleaved2 = gsm_deinterleave(interleaved)
print('Deinterleaved input_one:')
print(deinterleaved1 data)
print('Deinterleaved input_two:')
print(deinterleaved2 data)
