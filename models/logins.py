from models.users import Users


class Logins():

    @classmethod
    def login(self,user):
        try:
            verified_user = Users.query.filter(Users.username == user.username)
            
            if verified_user.first() != None:                

                new_user = Users(verified_user[0].id,verified_user[0].username,Users.check_password(verified_user[0].password,user.password),verified_user[0].fullname,verified_user[0].email,verified_user[0].area,verified_user[0].nivel)
                
                return new_user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_id(self,id):
        try:
            
            verified_user = Users.query.filter(Users.id == id)
            
            if verified_user.first() != None:   
                            
                
                return Users(verified_user[0].id,verified_user[0].username,None,verified_user[0].fullname,verified_user[0].email,verified_user[0].area,verified_user[0].nivel)
               
            else:
                
                return None

        except Exception as ex:
            raise Exception(ex)