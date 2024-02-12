import requests

base_url = 'http://localhost:8000/api/tasks/'  # Replace with your API base URL

# GET - Retrieve a list of tasks
response = requests.get(base_url)
print(response.json())

# # GET - Retrieve a specific task by ID (Replace '1' with the desired task ID)
# task_id = 1
# response = requests.get(f'{base_url}{task_id}/')
# print(response.json())

# # POST - Create a new task
# new_task = {"title": "New Task", "description": "Task description"}
# response = requests.post(base_url, json=new_task)
# print(response.json())

# # PUT - Update an existing task by ID (Replace '1' with the desired task ID)
# updated_task = {"title": "Updated Task", "description": "Updated description"}
# response = requests.put(f'{base_url}{task_id}/', json=updated_task)
# print(response.json())

# # DELETE - Delete a specific task by ID (Replace '1' with the desired task ID)
# response = requests.delete(f'{base_url}{task_id}/')
