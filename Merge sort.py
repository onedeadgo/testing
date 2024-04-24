def merge_sort(data, start, end):
  """Sorts a portion of the list using merge sort algorithm.

  Args:
      data: The list to be sorted.
      start: Starting index of the sublist to sort.
      end: Ending index of the sublist to sort (inclusive).

  Returns:
      None (sorts the data list in-place).
  """
  if start < end:
    # Find the middle point of the sublist
    mid = (start + end) // 2

    # Recursively sort the first and second halves
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)

    # Merge the sorted halves
    merge(data, start, mid, end)

def merge(data, start, mid, end):
  """Merges two sorted sublists into a single sorted sublist.

  Args:
      data: The list containing the sublists to merge.
      start: Starting index of the first sublist.
      mid: Ending index of the first sublist (inclusive, also the starting index of the second sublist).
      end: Ending index of the second sublist (inclusive).
  """
  # Create temporary arrays for the sublists
  left_size = mid - start + 1
  right_size = end - mid
  left = [None] * left_size
  right = [None] * right_size

  # Copy data to temporary arrays
  for i in range(left_size):
    left[i] = data[start + i]
  for i in range(right_size):
    right[i] = data[mid + 1 + i]

  # Merge the temporary arrays back into the original list
  i = 0
  j = 0
  k = start
  while i < left_size and j < right_size:
    if left[i] <= right[j]:
      data[k] = left[i]
      i += 1
    else:
      data[k] = right[j]
      j += 1
    k += 1

  # Copy the remaining elements (if any)
  while i < left_size:
    data[k] = left[i]
    i += 1
    k += 1
  while j < right_size:
    data[k] = right[j]
    j += 1
    k += 1

# Get user input for the list
data = []
num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
  element = int(input("Enter element {}: ".format(i+1)))
  data.append(element)

# Print the unsorted list
print("Unsorted list:", data)

# Sort the list using merge sort
merge_sort(data, 0, len(data) - 1)

# Print the sorted list
print("Sorted list:", data)
