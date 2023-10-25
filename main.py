import sys
import importlib

COURSE_TO_DETECT = [
    'CS168',
]

def check_course_availability(course_name):
    try:
        course_module = importlib.import_module(f"courses.{course_name.lower()}")
    except ModuleNotFoundError:
        print(f"Course plugin for {course_name} not found.")
        return None

    course_class = getattr(course_module, course_name, None)
    if course_class is None:
        print(f"Course class for {course_name} not found in the module.")
        return None

    course = course_class()
    return course.check_availability()

def main():
    course_names = COURSE_TO_DETECT
    if course_names is None or len(course_names) == 0:
        print("No courses are waiting to be detected. Consider either adding courses to the list or removing the action.")
        sys.exit(1)

    available_courses = []
    for course_name in course_names:
        result = check_course_availability(course_name)
        if result:
            available_courses.append((course_name, result))

    if available_courses:
        print("\nAvailable courses:")
        for course_name, message in available_courses:
            print(f"{course_name}: {message}")
    else:
        print("\nNo courses are currently available.")
        sys.exit(0)

    # if any of the courses are available, exit with 1, to make the action fail, to trigger the email notification
    sys.exit(1)

if __name__ == "__main__":
    main()
