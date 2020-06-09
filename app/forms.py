# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Me lembre")
    submit = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(
        "Repita a senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Registrar-se")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Por favor use um usuário diferente")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Por favor use um email diferente.")


class EditProfileForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired()])
    about_me = TextAreaField("Sobre mim", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(
                    "Por favor, utilize um usuário diferente, esse já existe!"
                )


class EmptyForm(FlaskForm):
    submit = SubmitField("Submit")


class PostForm(FlaskForm):
    post = TextAreaField(
        "Diga algo", validators=[DataRequired(), Length(min=1, max=140)]
    )
    submit = SubmitField("Submit")


class ResetPasswordRequestForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Solicitar reset de senha")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(
        "Repita a senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Resete sua senha")
