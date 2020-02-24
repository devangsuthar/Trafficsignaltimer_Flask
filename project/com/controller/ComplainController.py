import os
from datetime import datetime

from flask import request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO


@app.route('/user/loadComplain', methods=['GET'])
def userLoadComplain():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/addComplain.html')
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/user/insertComplain', methods=['POST'])
def userInsertComplain():
    try:
        if adminLoginSession() == 'user':
            UPLOAD_FOLDER = 'project/static/userResources/complain/'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainSubject = request.form['complainSubject']
            complainDescription = request.form['complainDescription']

            now = datetime.now()
            print("now =", now)

            complainDate = now.strftime("%Y/%m/%d")
            print("date =", complainDate)

            complainTime = now.strftime("%H:%M:%S")
            print("time =", complainTime)

            complainFile = request.files['complainFile']
            complainFileName = secure_filename(complainFile.filename)
            complainFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            complainFile.save(os.path.join(complainFilePath, complainFileName))

            complainVO.complainSubject = complainSubject
            complainVO.complainDescription = complainDescription
            complainVO.complainDate = complainDate
            complainVO.complainTime = complainTime
            complainVO.complainStatus = "pending"
            complainVO.complainFileName = complainFileName
            complainVO.complainFilePath = complainFilePath.replace("project", "..")
            complainVO.complainFrom_LoginId = session['session_loginId']

            complainDAO.insertComplain(complainVO)

            return redirect(url_for('userViewComplain'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/user/viewComplain', methods=['GET'])
def userViewComplain():
    try:
        if adminLoginSession() == 'user':
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainFrom_LoginId = session['session_loginId']

            complainList = complainDAO.viewComplain(complainVO)

            # print("__________________", complainVOList)

            return render_template('user/viewComplain.html', complainList=complainList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/user/deleteComplain', methods=['GET'])
def userDeleteComplain():
    try:
        if adminLoginSession() == 'user':
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.args.get('complainId')
            complainVO.complainId = complainId
            complainList = complainDAO.deleteComplain(complainVO)
            path = complainList.complainFilePath.replace("..", "project") + complainList.complainFileName

            if complainList.complainStatus == 'replied':
                replypath = complainList.replyFilePath.replace("..", "project") + complainList.replyFileName
                os.remove(replypath)

            os.remove(path)

            return redirect(url_for('userViewComplain'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route("/user/viewComplainReply")
def userViewComplainReply():
    try:
        if adminLoginSession() == 'user':
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.args.get("complainId")

            complainVO.complainId = complainId
            complainReplyList = complainDAO.viewComplainReply(complainVO)

            return render_template("user/viewComplainReply.html", complainReplyList=complainReplyList)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


# -----------------------admin side-----------------------

@app.route('/admin/viewComplain', methods=['GET'])
def adminViewComplain():
    try:
        if adminLoginSession() == 'admin':

            complainDAO = ComplainDAO()

            complainList = complainDAO.adminViewComplain()

            # print("__________________", complainVOList)
            return render_template('admin/viewComplain.html', complainList=complainList)

        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/loadComplainReply', methods=['GET'])
def adminLoadComplainReply():
    try:
        if adminLoginSession() == 'admin':
            complainId = request.args.get("complainId")
            return render_template('admin/addComplainReply.html', complainId=complainId)
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)


@app.route('/admin/loadReply', methods=['GET'])
def adminLoadReply():
    try:
        complainVO = ComplainVO()
        complainId = request.args.get("complainId")
        complainVO.complainId = complainId
        print("++++++++++++++++++++")
        return render_template('admin/addComplainReply.html', complainId=complainVO.complainId)

    except Exception as ex:
        print(ex)


@app.route('/admin/insertReply', methods=['POST'])
def adminInsertReply():
    try:
        if adminLoginSession() == 'admin':
            UPLOAD_FOLDER = 'project/static/adminResources/reply/'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.form['complainId']
            replySubject = request.form['replySubject']
            replyMessage = request.form['replyMessage']
            replyFile = request.files['replyFile']

            now = datetime.now()
            print("now =", now)

            replyDate = now.strftime("%Y/%m/%d")
            print("date =", replyDate)

            replyTime = now.strftime("%H:%M:%S")
            print("time =", replyTime)

            replyFileName = secure_filename(replyFile.filename)
            replyFilePath = os.path.join(app.config['UPLOAD_FOLDER'])
            replyFile.save(os.path.join(replyFilePath, replyFileName))

            complainVO.complainId = complainId
            complainVO.replySubject = replySubject
            complainVO.replyMessage = replyMessage
            complainVO.replyDate = replyDate
            complainVO.replyTime = replyTime
            complainVO.complainStatus = "replied"
            complainVO.replyFileName = replyFileName
            complainVO.replyFilePath = replyFilePath.replace("project", "..")
            complainVO.complainTo_LoginId = session['session_loginId']

            complainDAO.adminInsertReply(complainVO)

            return redirect(url_for('adminViewComplain'))
        else:
            return redirect('/admin/logoutSession')
    except Exception as ex:
        print(ex)
