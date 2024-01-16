def calculate_total_open_seats(available):
    if 'combination' in available:
        combined_open_seats = available['combination']['maxEnrollCombinedSections'] - available['combination']['enrolledCountCombinedSections']
        per_class_open_seats = available['enrollmentStatus']['maxEnroll'] - available['enrollmentStatus']['enrolledCount']
        value = min(combined_open_seats, per_class_open_seats)
        return max(value, 0)
    else:
        return max(available['enrollmentStatus']['maxEnroll'] - available['enrollmentStatus']['enrolledCount'], 0)

# Example usage 1 - CS160, discussion section
# available = {
#     'combination': {
#         'maxEnrollCombinedSections': 90,
#         'enrolledCountCombinedSections': 118
#     },
#     'enrollmentStatus': {
#         'maxEnroll': 74,
#         'enrolledCount': 72
#     }
# }

# Example usage 2 - CS160, Lecture
available = {
    'combination': {
        'maxEnrollCombinedSections': 120,
        'enrolledCountCombinedSections': 118
    },
    'enrollmentStatus': {
        'maxEnroll': 74,
        'enrolledCount': 72
    }
}

total_open_seats = calculate_total_open_seats(available)
print("Total Open Seats:", total_open_seats)
