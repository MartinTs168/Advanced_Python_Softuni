def gather_credits(credits_needed, *args):
    gathered_credits = 0
    courses_attended = set()

    for course, value in args:

        if gathered_credits >= credits_needed:
            break

        if course not in courses_attended:
            courses_attended.add(course)
            gathered_credits += value

    if gathered_credits >= credits_needed:
        sorted_courses = sorted(courses_attended)
        return (f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
                f"Courses: {', '.join(sorted_courses)}")

    return (f"You need to enroll in more courses! "
            f"You have to gather {credits_needed - gathered_credits} credits more.")


# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
