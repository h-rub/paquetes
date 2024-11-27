from client import APIClient

from serializer import PostSerializer


client = APIClient("https://jsonplaceholder.typicode.com")

response = client.get_all_posts()

serializer = PostSerializer()

serializer(response)

print(serializer.data)

# response_create_post = client.create_post(title="Mi primer post", body="Este es mi primer post en la API", user_id="1001")

# print(response_create_post)