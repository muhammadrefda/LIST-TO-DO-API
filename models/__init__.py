class ListToDo:
    title = ""
    description = ""
    finished_at = ""
    created_at = ""
    updated_at = ""
    deleted_at = ""

    def __init__(self, title, description, finished_at, created_at, updated_at, deleted_at):
        self.title = title
        self.description = description
        self.finished_at = finished_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


todos = []

sample_todo = ListToDo("Sample todo", "This is a sample todo", "", "28-12-2022 18:34:59", "", "")

todos.append(sample_todo)
