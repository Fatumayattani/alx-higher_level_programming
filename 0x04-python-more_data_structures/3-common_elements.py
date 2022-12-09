#!/usr/bin/python3
def common_elements(set_1, set_2):

    # Create an empty set to store the common elements

    common_elements = set()



    # Iterate over the elements in set 1

    for element in set_1:

        # Check if the element is also in set 2

        if element in set_2:

            # If it is, add it to the common elements set

            common_elements.add(element)



    # Return the set of common elements

    return common_elements
