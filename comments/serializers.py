class CommentSerializer:
    def __init__(self):
        self.data = []

    def __call__(self, data):
        print("Serializando comment")
        self.data = [obj.to_dict() for obj in data]