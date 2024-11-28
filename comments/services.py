from .models import Comment
import requests

class CommentService:
    def __init__(self, json_placeholder_service):
        self.json_placeholder_service = json_placeholder_service

    def get_all_comments(self):
        try:
            response = self.json_placeholder_service.get_all_comments()
            return [Comment.from_dict(comment) for comment in response]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
    
    def get_all_comments_by_post(self):
        """ 
        Tarea a realizar. 
        """
        pass

    def create_comment(self):
        """ 
        Tarea a realizar. 
        """
        pass

    