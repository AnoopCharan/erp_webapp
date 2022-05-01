from rest_framework.authtoken.models import Token

# Get user token

def get_token(user, asHeader:bool = False):
    """
    get authorization token for a user, user header True to get authorization header for requests methods
    use user = request.user
    """
    token = Token.objects.get(user=user).key
    
    if asHeader:
        requestHeader = {'Authorization':f"Token {token}"}
        return requestHeader
    return token