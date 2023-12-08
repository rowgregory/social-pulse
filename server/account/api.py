from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer


@api_view(['GET'])
def foryou(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    print('SIGN UP: ', request.data)
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()

        # TODO: Send verification email later!
    else:
        print('FORM ERRORS: ', form.errors)
        message = 'Error'

    return JsonResponse({'message': message})


@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)


@api_view(['POST'])
def send_friend_request(request, pk):
    user = User.objects.get(pk=pk)

    friend_request = FriendshipRequest.objects.create(
        created_for=user, created_by=request.user)

    friend_request.save()

    return JsonResponse({'message': 'FRIEND REQUEST CREATED'})


@api_view(['POST'])
def handle_friend_request(request, pk, status):
    user = User.objects.get(pk=pk)
    friend_request = FriendshipRequest.objects.filter(
        created_for=request.user).get(created_by=user)
    friend_request.status = status
    friend_request.save()

    user.friends.add(request.user)
    user.friends_count = user.friends_count + 1
    user.save()

    request_user = request.user
    request_user.friends_count = request_user.friends_count + 1
    request_user.save()

    return JsonResponse({'message': 'Friend request handled'})
