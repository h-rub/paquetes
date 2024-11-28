class Comment:
    def __init__(self, post_id, comment_id, name, email, body):
        self.post_id = post_id
        self.comment_id = comment_id
        self.name = name
        self.email = email
        self.body = body

    @classmethod
    def from_dict(cls, data):
        return cls(
            post_id = data.get("postId"),
            comment_id = data.get("id"),
            name = data.get("name"),
            email = data.get("email"),
            body = data.get("body")
        )
    
    def to_dict(self):
        return {
            "postId": self.post_id,
            "id": self.comment_id,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }
    
    def __str__(self):
        return f"Comment(post_id: {self.post_id}, ID: {self.comment_id}, Name: {self.name}, Email: {self.email}, Body: {self.body})"