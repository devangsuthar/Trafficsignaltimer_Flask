import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template, request

from project import app
# from project.com.controller.LoginController import adminLoginSession
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


@app.route('/admin/loadRegister', methods=['GET'])
def adminLoadRegister():
    try:

        return render_template("admin/register.html")

    except Exception as ex:
        print(ex)


@app.route('/admin/insertRegister', methods=['post'])
def adminInsertRegister():
    try:

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        registerVO = RegisterVO()
        registerDAO = RegisterDAO()

        loginUsername = request.form['loginUsername']
        registertrafficPoliceStationName = request.form['registertrafficPoliceStationName']
        registertrafficPoliceStationAreaName = request.form['registertrafficPoliceStationAreaName']
        registertrafficPoliceStationAddress = request.form['registertrafficPoliceStationAddress']
        registertrafficPoliceStationContact = request.form['registertrafficPoliceStationContact']

        loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

        print("loginPassword=" + loginPassword)

        sender = "trafficeasesignaltimer@gmail.com"

        receiver = loginUsername

        msg = MIMEMultipart()

        msg['From'] = sender

        msg['To'] = receiver

        msg['Subject'] = "TRAFFIC POLICE STATION LOGIN PASSWORD"

        msg.attach(MIMEText(loginPassword, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender, "trafficease123")

        text = msg.as_string()

        server.sendmail(sender, receiver, text)

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginRole = "user"
        loginVO.loginStatus = "active"

        print('hello')

        loginDAO.insertLogin(loginVO)

        registerVO.registertrafficPoliceStationName = registertrafficPoliceStationName
        registerVO.registertrafficPoliceStationAreaName = registertrafficPoliceStationAreaName
        registerVO.registertrafficPoliceStationAddress = registertrafficPoliceStationAddress
        registerVO.registertrafficPoliceStationContact = registertrafficPoliceStationContact

        registerVO.register_LoginId = loginVO.loginId

        registerDAO.insertRegister(registerVO)

        server.quit()

        return render_template("admin/login.html")


    except Exception as ex:
        print(ex)
