import requests

class JSONPlaceHolderService:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_all_posts(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            response_json = response.json()
            return response_json
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
            payload = {
                "title": title,
                "body": body,
                "userId": user_id
            }
            response = requests.post(f"{self.base_url}/posts", json=payload)
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None
    
    def get_all_comments(self):
        try:
            response = requests.get(f"{self.base_url}/comments")
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los comentarios: {e}")
            return []
        
    def create_comment(self):
        """ 
        Tarea a realizar. 
        """
        pass

    def get_all_comments_by_post(self):
        """ 
        Tarea a realizar. 
        """
        pass