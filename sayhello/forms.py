# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField, DateField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    s_date = DateTimeField('起始时间', validators=[DataRequired()])
    e_date = DateTimeField('结束时间', validators=[DataRequired()])
    submit = SubmitField()
    # /^[1-9]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$/


class EditForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    s_date = DateTimeField('起始时间', validators=[DataRequired()])
    e_date = DateTimeField('结束时间', validators=[DataRequired()])
    submit = SubmitField('修改签到记录')


class DeleteForm(FlaskForm):
    submit = SubmitField('删除签到记录')
