from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from .forms import PostForm
from account.models import User, FriendshipRequest
from account.serializers import UserSerializer


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    user = User.objects.get(pk=request.user.id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({'posts': posts_serializer.data, 'user': user_serializer.data}, safe=False)


@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by=id)

    friends = user.friends.all()

    friend_requests = FriendshipRequest.objects.filter(created_by=request.user)
    print('FRIEND REQUESTS: ', friend_requests)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    friends_serializer = UserSerializer(friends, many=True).data,

    return JsonResponse({'posts': posts_serializer.data, 'user': user_serializer.data, 'friends': friends_serializer}, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)

    if (form.is_valid()):
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'Error': 'TODO'})
