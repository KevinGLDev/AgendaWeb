from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flasksite.models import User



class RegistrationForm(FlaskForm):
    username = StringField('School Id',
                           validators=[DataRequired(), Length(min=2, max=20)])


    firstName=StringField('First Name',
                          validators=[DataRequired(), Length(min=2, max=20)])

    lastName=StringField('Last Name',
                         validators=[DataRequired(), Length(min=2, max=20)])

    day = StringField('Date of birth: Day',
                      validators=[DataRequired(), Length(min=1, max=20)])

    month = StringField('Date of birth: Month',
                        validators=[DataRequired(), Length(min=1, max=20)])

    year = StringField('Date of birth: Year',
                       validators=[DataRequired(), Length(min=1, max=20)])

    interest1=StringField('Area of Intererst 1',
                          validators=[DataRequired(), Length(min=2, max=20)])

    interest2=StringField('Area of Intererst 2',
                          validators=[DataRequired(), Length(min=2, max=20)])

    interest3=StringField('Area of Intererst 3',
                          validators=[DataRequired(), Length(min=2, max=20)])


    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    picture=FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('School ID',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')





class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')