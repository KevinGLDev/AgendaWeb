from models.users import Users

class Logins():

    @classmethod
    def login(self,db,user):
        try:
            verified_user = Users.query.filter(Users.username == user.username)
            
            if verified_user.first() != None:                

                new_user = Users(verified_user[0].username,Users.check_password(verified_user[0].password,user.password),verified_user[0].fullname,verified_user[0].email)
                return new_user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)