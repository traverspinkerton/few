from models.user import UserModel

def authenticate(username, password):
    print("inside authenticate function")
    user = UserModel.find_by_email(username)
    print("user: ", user)
    if user and user.is_correct_password(password):
        print("user found and password correct")
        return user
    
def identity(payload):
    print("inside authenticate function")
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)