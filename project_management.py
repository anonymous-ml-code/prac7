'''
estimate time: 100 minutes
actual time time: 120 minutes
'''

import csv
from project import Project
import datetime


def main():
    """Main function for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")  # Load default projects
    print(f"Loaded {len(projects)} projects from projects.txt")

    while True:
        print_menu()
        choice = input(">>> ").lower()
        if choice == 'q':
            save_choice = input(
                "Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == "yes":
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
            break
        elif choice == 'l':
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")


def print_menu():
    """Print the menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from the given file."""
    projects = []
    try:
        with open(filename, 'r', newline='') as in_file:
            reader = csv.reader(in_file, delimiter='\t')
            next(reader)  # Skip header
            for row in reader:
                name, start_date, priority, cost_estimate, completion_percentage = row
                projects.append(
                    Project(
                        name,
                        start_date,
                        priority,
                        cost_estimate,
                        completion_percentage))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return projects


def save_projects(filename, projects):
    """Save projects to the given file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority",
                         "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost_estimate,
                project.completion_percentage
            ])


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()
    completed_projects.sort()

    print("\nIncomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(
            date_string, "%d/%m/%Y").date()
        filtered_projects = [p for p in projects if p.start_date > filter_date]
        filtered_projects.sort(key=lambda x: x.start_date)
        print("\nFiltered projects:")
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format.")


def add_new_project(projects):
    """Add a new project to the list."""
    print("\nLet's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(
        name,
        start_date,
        priority,
        cost_estimate,
        completion_percentage)
    projects.append(new_project)
    print(f"{name} added.")


def update_project(projects):
    """Update the percentage or priority of a selected project."""
    print("\nProjects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_choice = int(input("Project choice: "))
        selected_project = projects[project_choice]
        print(selected_project)

        new_percentage = input("New Percentage: ")
        if new_percentage:
            selected_project.completion_percentage = int(new_percentage)

        new_priority = input("New Priority: ")
        if new_priority:
            selected_project.priority = int(new_priority)

        print(f"{selected_project.name} updated.")
    except (ValueError, IndexError):
        print("Invalid choice.")


if __name__ == "__main__":
    main()
