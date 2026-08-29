def can_ship(weights, days, capacity):

    days_used = 1
    current_load = 0

    for weight in weights:

        if current_load + weight > capacity:

            days_used += 1
            current_load = weight

        else:

            current_load += weight

    return days_used <= days


def ship_within_days(weights, days):

    left = max(weights)
    right = sum(weights)

    answer = right

    while left <= right:

        capacity = (left + right) // 2

        if can_ship(weights, days, capacity):

            answer = capacity
            right = capacity - 1

        else:

            left = capacity + 1

    return answer


weights = [1, 2, 3, 1, 1]
days = 4

print(ship_within_days(weights, days))