import requests

# Define the task data to create
new_task_data = {
    "title": "New Task",
    "description": "This is a new task."
}

# Send a POST request to create a new task
create_response = requests.post("http://localhost:8000/tasks/", json=new_task_data)

# Check the response status code and content for the POST request
print("POST Response:")
print(create_response.status_code)
print(create_response.json())

# Send a GET request to retrieve a list of tasks
get_response = requests.get("http://localhost:8000/tasks/")

# Check the response status code and content for the GET request
print("\nGET Response:")
print(get_response.status_code)
print(get_response.json())
