from models import Post
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_posts(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            response_json = response.json()
            return [Post.from_dict(post) for post in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
    
    def get_posts_by_user(self, user_id):
        pass

    def create_post(self, title, body, user_id):
        try:
            payload = {
                "title": title,
                "body": body,
                "userId": user_id
            }
            response = requests.post(f"{self.base_url}/posts", json=payload)
            post_data = response.json()
            return Post.from_dict(post_data)
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None