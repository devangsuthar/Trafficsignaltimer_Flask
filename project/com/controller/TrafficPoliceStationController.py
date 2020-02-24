import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, redirect, url_for

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.AreaDAO import AreaDAO
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.TrafficpolicestationDAO import TrafficPoliceStationDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.TrafficpolicestationVO import TrafficPoliceStationVO


@app.route('/admin/loadTrafficPoliceStation', methods=['GET'])
def adminLoadTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':
            areaDAO = AreaDAO()
            areaVOList = areaDAO.viewArea()
            print('--------------', areaVOList)
            return render_template('admin/addTrafficPoliceStation.html', areaVOList=areaVOList)
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/insertTrafficPoliceStation', methods=['POST'])
def adminInsertTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':
            loginVO = LoginVO()
            loginDAO = LoginDAO()

            trafficPoliceStationVO = TrafficPoliceStationVO()
            trafficPoliceStationDAO = TrafficPoliceStationDAO()

            trafficPoliceStationName = request.form['trafficPoliceStationName']
            trafficPoliceStationContact = request.form['trafficPoliceStationContact']
            trafficPoliceStation_AreaId = request.form['trafficPoliceStation_AreaId']
            trafficPoliceStationAddress = request.form['trafficPoliceStationAddress']

            loginUsername = request.form['loginUsername']


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

            loginDAO.insertLogin(loginVO)

            trafficPoliceStationVO.trafficPoliceStationName = trafficPoliceStationName
            trafficPoliceStationVO.trafficPoliceStationContact = trafficPoliceStationContact
            trafficPoliceStationVO.trafficPoliceStation_AreaId = trafficPoliceStation_AreaId
            trafficPoliceStationVO.trafficPoliceStationAddress = trafficPoliceStationAddress
            trafficPoliceStationVO.trafficPoliceStation_LoginId = loginVO.loginId

            trafficPoliceStationDAO.insertTrafficPoliceStation(trafficPoliceStationVO)

            server.quit()

            return redirect(url_for('adminViewTrafficPoliceStation'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewTrafficPoliceStation', methods=['GET'])
def adminViewTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':
            trafficPoliceStationDAO = TrafficPoliceStationDAO()

            trafficPoliceStationVOList = trafficPoliceStationDAO.viewTrafficPoliceStation()

            return render_template('admin/viewTrafficPoliceStation.html',
                                   trafficPoliceStationVOList=trafficPoliceStationVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteTrafficPoliceStation', methods=['GET'])
def adminDeleteTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':

            loginDAO = LoginDAO()
            loginVO = LoginVO()

            trafficPoliceStationVO = TrafficPoliceStationVO()
            trafficPoliceStationDAO = TrafficPoliceStationDAO()

            loginId = request.args.get('loginId')
            trafficPoliceStationId = request.args.get('trafficPoliceStationId')

            loginVO.loginId = loginId

            trafficPoliceStationVO.trafficPoliceStationId = trafficPoliceStationId

            trafficPoliceStationDAO.deleteTrafficPoliceStation(trafficPoliceStationVO)

            loginDAO.deleteLogin(loginVO)

            return redirect(url_for('adminViewTrafficPoliceStation'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/editTrafficPoliceStation', methods=['GET'])
def adminEditTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':
            trafficPoliceStationVO = TrafficPoliceStationVO()

            trafficPoliceStationDAO = TrafficPoliceStationDAO()

            trafficPoliceStationId = request.args.get('trafficPoliceStationId')

            trafficPoliceStationVO.trafficPoliceStationId = trafficPoliceStationId

            trafficPoliceStationVOList = trafficPoliceStationDAO.editTrafficPoliceStation(trafficPoliceStationVO)

            areaDAO = AreaDAO()
            areaVOList = areaDAO.viewArea()

            print("=======trafficPoliceStationVOList=======", trafficPoliceStationVOList)

            print("=======type of trafficPoliceStationVOList=======", type(trafficPoliceStationVOList))

            return render_template('admin/editTrafficPoliceStation.html',
                                   trafficPoliceStationVOList=trafficPoliceStationVOList, areaVOList=areaVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/updateTrafficPoliceStation', methods=['POST'])
def adminUpdateTrafficPoliceStation():
    try:
        if adminLoginSession() == 'admin':
            loginVO = LoginVO()
            loginDAO = LoginDAO()

            trafficPoliceStationVO = TrafficPoliceStationVO()
            trafficPoliceStationDAO = TrafficPoliceStationDAO()

            trafficPoliceStationId = request.form['trafficPoliceStationId']
            trafficPoliceStationName = request.form['trafficPoliceStationName']
            trafficPoliceStationContact = request.form['trafficPoliceStationContact']
            trafficPoliceStation_AreaId = request.form['trafficPoliceStation_AreaId']
            trafficPoliceStationAddress = request.form['trafficPoliceStationAddress']
            loginId = request.form['loginId']
            loginUsername = request.form['loginUsername']

            loginVO.loginId = loginId
            loginVO.loginUsername = loginUsername

            loginDAO.updateLogin(loginVO)

            trafficPoliceStationVO.trafficPoliceStationId = trafficPoliceStationId
            trafficPoliceStationVO.trafficPoliceStationName = trafficPoliceStationName
            trafficPoliceStationVO.trafficPoliceStationContact = trafficPoliceStationContact
            trafficPoliceStationVO.trafficPoliceStation_AreaId = trafficPoliceStation_AreaId
            trafficPoliceStationVO.trafficPoliceStationAddress = trafficPoliceStationAddress
            trafficPoliceStationVO.trafficPoliceStation_LoginId = loginId

            trafficPoliceStationDAO.updateTrafficPoliceStation(trafficPoliceStationVO)

            return redirect(url_for('adminViewTrafficPoliceStation'))
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)
