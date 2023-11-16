import requests

base_url = "https://jsonplaceholder.typicode.com"

# GET request to /posts
response = requests.get(f"{base_url}/posts")

if response.status_code == 200:
    # Filter titles with more than 6 words
    posts = response.json()
    filtered_posts = [post for post in posts if len(post['title'].split()) <= 6]

    # Filter out results with more than 3 lines of description
    filtered_posts = [post for post in filtered_posts if len(post['body'].split('\n')) <= 3]

    print("Filtered Posts:")
    for post in filtered_posts:
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("------")

# POST request to /posts
new_post_data = {
    'title': 'New Post',
    'body': 'This is a new post body.',
    'userId': 1
}
response = requests.post(f"{base_url}/posts", json=new_post_data)

if response.status_code == 201:
    print("New Post Created:")
    print(response.json())
else:
    print(f"Failed to create a new post. Status code: {response.status_code}")

# PUT request to /posts/{post_id}
post_id_to_update = 1
update_data = {
    'title': 'Updated Title',
    'body': 'This is the updated body.',
    'userId': 1
}
response = requests.put(f"{base_url}/posts/{post_id_to_update}", json=update_data)

if response.status_code == 200:
    print("Post Updated:")
    print(response.json())
else:
    print(f"Failed to update the post. Status code: {response.status_code}")

# DELETE request to /posts/{post_id}
post_id_to_delete = 1
response = requests.delete(f"{base_url}/posts/{post_id_to_delete}")

if response.status_code == 200:
    print(f"Post {post_id_to_delete} deleted successfully.")
else:
    print(f"Failed to delete the post. Status code: {response.status_code}")
