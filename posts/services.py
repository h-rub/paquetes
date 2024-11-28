from posts.models import Post
import requests

class PostService:
    def __init__(self, json_placeholder_service):
        self.json_placeholder_service = json_placeholder_service

    def get_all_posts(self):
        try:
            response = self.json_placeholder_service.get_all_posts()
            return [Post.from_dict(post) for post in response]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
    
    def get_posts_by_user(self, user_id):
        """ 
        Tarea a realizar. 
        """
        pass

    def create_post(self, title, body, user_id):
        try:
            response = self.json_placeholder_service.create_post(title, body, user_id)
            return Post.from_dict(response)
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None