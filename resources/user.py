from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=str,
        required=True,
        help="Please submit an email"
    )
    parser.add_argument('plaintext_password',
        type=str,
        required=True,
        help="Please submit a password"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists."}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully"}, 201