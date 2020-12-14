# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import flash, redirect, url_for, render_template, request, abort

from sayhello import app, db
from sayhello.forms import HelloForm, EditForm, DeleteForm, SignForm
from sayhello.models import Message
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        s_date = form.s_date.data
        e_date = form.e_date.data
        t1 = s_date.strftime("%Y-%m-%d %H:%M:%S")
        t1 = datetime.strptime(t1, r"%Y-%m-%d %H:%M:%S")
        t2 = e_date.strftime("%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(t2, r"%Y-%m-%d %H:%M:%S")
        all_date = t2 - t1
        message = Message(s_date=s_date, e_date=e_date, name=name, all_date=all_date)
        db.session.add(message)
        db.session.commit()
        flash('%s，你已经签到成功！！' % name)
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)
    per_page = 10  # 10
    pagination = Message.query.order_by(Message.s_date.desc()).paginate(page, per_page=per_page)
    messages = pagination.items
    # messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages, pagination=pagination)


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = DeleteForm()
    page = request.args.get('page', 1, type=int)
    per_page = 10  # 10
    pagination = Message.query.order_by(Message.s_date.desc()).paginate(page, per_page=per_page)
    messages = pagination.items
    # messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('test.html', messages=messages, pagination=pagination, form=form)


@app.route('/edit/<int:message_id>', methods=['GET', 'POST'])
def edit_note(message_id):
    form = EditForm()
    message = Message.query.get(message_id)
    if form.validate_on_submit():
        name = form.name.data
        s_date = form.s_date.data
        e_date = form.e_date.data
        t1 = s_date.strftime("%Y-%m-%d %H:%M:%S")
        t1 = datetime.strptime(t1, r"%Y-%m-%d %H:%M:%S")
        t2 = e_date.strftime("%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(t2, r"%Y-%m-%d %H:%M:%S")
        all_date = t2 - t1
        message = Message(s_date=s_date, e_date=e_date, name=name, all_date=all_date)
        db.session.add(message)
        db.session.commit()
        flash('签到记录修改成功！！')
        return redirect(url_for('index'))
    form.name.data = message.name  # preset form input's value
    form.s_date.data = message.s_date
    form.e_date.data = message.e_date
    return render_template('edit_note.html', form=form)


@app.route('/delete/<int:message_id>', methods=['POST'])
def delete_note(message_id):
    form = DeleteForm()
    if form.validate_on_submit():
        message = Message.query.get(message_id)
        db.session.delete(message)
        db.session.commit()
        flash('签到记录已删除！！')
    else:
        abort(400)
    return redirect(url_for('test'))


@app.route('/sign', methods=['POST'])
def sign():
    form = SignForm()
    if form.validate_on_submit():
        name = 'lgm'
        s_date = datetime.now().replace(microsecond=0)
        e_date = '2020/12/14 9:45:32'
        t1 = s_date.strftime("%Y-%m-%d %H:%M:%S")
        t1 = datetime.strptime(t1, r"%Y-%m-%d %H:%M:%S")
        # t2 = e_date.strftime("%Y-%m-%d %H:%M:%S")
        # t2 = datetime.strptime(t2, r"%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(e_date, r"%Y/%m/%d %H:%M:%S")
        all_date = t2 - t1
        message = Message(s_date=s_date, e_date=e_date, name=name, all_date=all_date)
        db.session.add(message)
        db.session.commit()
        flash('%s，你已经签到成功！！' % name)
        return redirect(url_for('test'))
    else:
        abort(400)
    return redirect(url_for('test'))
