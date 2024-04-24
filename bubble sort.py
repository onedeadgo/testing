def bubble_sort(data):
  """Sorts a list of data in ascending order using bubble sort algorithm.

  Args:
      data: A list of sortable elements.

  Returns:
      The sorted list.
  """
  # Get the length of the list
  n = len(data)
  
  # Outer loop to handle number of passes
  for i in range(n-1):
    swapped = False
    
    # Inner loop to compare adjacent elements
    for j in range(0, n-i-1):
      if data[j] > data[j + 1]:
        # Swap elements if they are in the wrong order
        data[j], data[j + 1] = data[j + 1], data[j]
        swapped = True
    
    # If we haven't made any swaps in this pass, the list is already sorted
    if not swapped:
      break
  
  return data

# Get user input for the list
data = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
  element = int(input("Enter element {}: ".format(i+1)))
  data.append(element)

# Print the unsorted list
print("Unsorted list:", data)

# Sort the list using bubble sort
sorted_data = bubble_sort(data)

# Print the sorted list
print("Sorted list:", sorted_data)
