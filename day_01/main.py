with open("input.txt") as file:
    data = file.read().splitlines()

# Part 1

left_list_sorted = sorted([int(pair.split()[0]) for pair in data])
right_list_sorted = sorted([int(pair.split()[1]) for pair in data])

distance_list = []

for left_distance, right_distance in zip(left_list_sorted, right_list_sorted):
    distance = abs(left_distance - right_distance)
    distance_list.append(distance)

print(sum(distance_list))

# Part 2

left_list = [int(pair.split()[0]) for pair in data]
right_list = [int(pair.split()[1]) for pair in data]

similarity_scores = []

for id_left in left_list:
    count = right_list.count(id_left)
    score = id_left * count
    similarity_scores.append(score)

print(sum(similarity_scores))
