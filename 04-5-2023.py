# Question 1: Which floor am I on?

def whichFloorAmIOn(instructions):

    # Start at floor 0
    floor = 0

    # Increment or decrement based on direction given
    for direction in instructions:
        if direction == '<':
            floor += 1
        elif direction == '>':
            floor -= 1
    return floor

instructions = """
<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
<>><<>><<>><
""" 

# 56
print(whichFloorAmIOn(instructions))

# ANALYSIS
# Time Complexity: O(n), where n is the length of the instructions string
# Space Complexity: O(1)