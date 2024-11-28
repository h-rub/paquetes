from json_placeholder import JSONPlaceHolderService
from posts.serializers import PostSerializer
from posts.services import PostService
from comments.services import CommentService
from comments.serializers import CommentSerializer

json_placeholder_adapter = JSONPlaceHolderService()
post_service = PostService(json_placeholder_adapter)

response = post_service.get_all_posts()

serializer = PostSerializer()

serializer(response)

print(serializer.data)

# response_create_post = post_service.create_post(title="Mi primer post", body="Este es mi primer post en la API", user_id="1001")

# print(response_create_post)

# comments_service = CommentService(json_placeholder_adapter)

# comments = comments_service.get_all_comments()

# comment_serializer = CommentSerializer()

# comment_serializer(comments)

# print(comment_serializer.data)