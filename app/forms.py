#建立用户登陆表单
from flask_wtf import FlaskForm,Form, validators
from wtforms import SubmitField, PasswordField, TextField, StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from .models import User
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField

class NameForm(FlaskForm):
    name=TextField('what is your name?',validators=[DataRequired()])
    password=PasswordField('what is your password?',validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    login=SubmitField('login')
    logout=SubmitField('logout')

#创建用户注册表单
class RegistrationForm(Form):
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    ###WTForms提供的Regexp验证函数，确保username字段只包含字母，数字，下划线和点号。这个验证函数中的正则表达式后面的两个参数分别是正则表达式的旗标和验证失败时显示的错误消息。
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
        ###EqualTo验证函数可以验证两个密码字段中的值是否一致，他附属在两个密码字段上，另一个字段作为参数传入。
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
    ###表单类中定义了以validate_开头且后面跟着字段名的方法，这种方法就和常规的验证函数一起调用。

    #创建卡片写作表单
class CardForm(Form):
    title = TextAreaField("卡片标题", validators=[Required(), Length(1, 20)])
    #length为汉字+标点+markdown的符号+数字等不超过420
    body = PageDownField('卡片内容，支持Markdown', validators=[Length(1, 420)])
    submit = SubmitField('Submit')
