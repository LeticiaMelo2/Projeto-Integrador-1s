#define o formulário de cadastro usando a biblioteca WTForms, que ajuda a criar e validar formulários flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

class RegisterForm(FlaskForm): #cria o formulário, pegando do FlaskForm e traz funcionalidades de proteção
    first_name = StringField('Primeiro nome', render_kw={"placeholder": "Nome"}, validators=[DataRequired()]) #define campo de texto obrigatório
    last_name = StringField('Sobrenome', render_kw={"placeholder": "Sobrenome"})
    email = StringField('E-mail', render_kw={"placeholder": "E-mail"}, validators=[Email(message='E-mail inválido!'), InputRequired()]) #email com validação automática de formato
    password = PasswordField('senha', render_kw={"placeholder": "Senha"}, validators=[InputRequired(), EqualTo('confirm', message='As senhas devem ser correspondentes!')]) #valida se as senhas são iguais
    confirm = PasswordField('Confirme sua senha', render_kw={"placeholder": "Confirme sua senha"})
    submit = SubmitField('CADASTRAR')