def swap(int_array: list[int], a: int, b: int) -> None:
	tmp = int_array[a]
	int_array[a] = int_array[b]
	int_array[b] = tmp


def insertion_sort(int_array: list[int]) -> None:
	for i in range(1, len(int_array)):
		j = i
		while j > 0 and int_array[j] < int_array[j - 1]:
			swap(int_array, j, j - 1)
			j -= 1
