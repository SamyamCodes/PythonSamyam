def print_framed_word():
    # Get the word input from the user
    word = input("Word: ")
    
    # Determine the total width of the frame
    frame_width = 30
    
    # Calculate the padding needed on each side
    padding = (frame_width - len(word) - 2) // 2
    
    # Construct the frame
    top_bottom = '*' * frame_width
    # Adjust middle to ensure it fits exactly within 30 characters
    middle = '*' + ' ' * padding + word + ' ' * (frame_width - len(word) - padding - 2) + '*'
    
    # Print the framed word
    print(top_bottom)
    print(middle)
    print(top_bottom)

# Call the function
print_framed_word()
