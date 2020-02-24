from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


#
@app.route('/', methods=['GET'])
def adminLoadLogin():
    try:
        session.clear()
        # print("in /")
        return render_template('admin/Login.html')
    except Exception as ex:
        print(ex)


#


@app.route("/admin/validateLogin", methods=['POST'])
def adminValidateLogin():
    loginUsername = request.form['loginUsername']
    loginPassword = request.form['loginPassword']

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.loginUsername = loginUsername
    loginVO.loginPassword = loginPassword
    loginVO.loginStatus = "active"

    loginVOList = loginDAO.validateLogin(loginVO)

    loginDictList = [i.as_dict() for i in loginVOList]

    print(loginDictList)

    lenLoginDictList = len(loginDictList)

    if lenLoginDictList == 0:

        msg = 'Username Or Password is Incorrect !'

        return render_template('admin/Login.html', error=msg)

    else:

        for row1 in loginDictList:

            loginId = row1['loginId']

            loginUsername = row1['loginUsername']

            loginRole = row1['loginRole']

            session['session_loginId'] = loginId

            session['session_loginUsername'] = loginUsername

            session['session_loginRole'] = loginRole

            session.permanent = False

            if loginRole == 'admin':
                return redirect(url_for('adminLoadDashboard'))

            else:
                return render_template('user/Index.html ')


@app.route('/admin/loadDashboard', methods=['GET'])
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/Index.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/loadDashboard', methods=['GET'])
def userLoadDashboard():
    try:
        return render_template('user/Index.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/loginSession')
def adminLoginSession():
    if 'session_loginId' and 'session_loginRole' in session:

        if session['session_loginRole'] == 'admin':

            return 'admin'

        elif session['session_loginRole'] == 'user':

            return 'user'

        print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

    else:

        print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

        return False


@app.route("/admin/logoutSession", methods=['GET'])
def adminLogoutSession():
    print('In adminLogoutSession')
    session.clear()

    return redirect(url_for('adminLoadLogin'))
