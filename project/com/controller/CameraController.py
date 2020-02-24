from flask import request, render_template, redirect, url_for

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.AreaDAO import AreaDAO
from project.com.dao.CameraDAO import CameraDAO
from project.com.dao.CrossroadDAO import CrossroadDAO
from project.com.vo.CameraVO import CameraVO


@app.route('/admin/loadCamera')
def adminLoadCamera():
    try:

        if adminLoginSession() == 'admin':

            areaDAO = AreaDAO()
            crossroadDAO = CrossroadDAO()
            areaVOList = areaDAO.viewArea()
            crossroadVOList = crossroadDAO.viewCrossroad()

            return render_template('admin/addCamera.html', crossroadVOList=crossroadVOList, areaVOList=areaVOList)
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/insertCamera', methods=['POST'])
def adminInsertCamera():
    try:
        if adminLoginSession() == 'admin':

            print('inside cameraconroller')
            cameraCode = request.form['cameraCode']
            camera_AreaId = request.form['camera_AreaId']
            camera_CrossroadId = request.form['camera_CrossroadId']
            print("++++++++++++++++", cameraCode, camera_AreaId, camera_CrossroadId)
            cameraVO = CameraVO()
            cameraDAO = CameraDAO()

            cameraVO.cameraCode = cameraCode
            cameraVO.camera_AreaId = camera_AreaId
            cameraVO.camera_CrossroadId = camera_CrossroadId
            print('dataset')
            cameraDAO.insertCamera(cameraVO)

            return redirect(url_for('adminViewCamera'))
        else:
            return adminLogoutSession()


    except Exception as ex:
        print(ex)


@app.route('/admin/viewCamera', methods=['GET'])
def adminViewCamera():
    try:
        if adminLoginSession() == 'admin':
            print("inside view......")
            cameraDAO = CameraDAO()
            cameraVOList = cameraDAO.viewCamera()
            print("__________________+++++=", cameraVOList)

            return render_template('admin/viewCamera.html', cameraVOList=cameraVOList)
        else:
            return adminLogoutSession()


    except Exception as ex:
        print(ex)


@app.route('/admin/deleteCamera', methods=['GET'])
def adminDeleteCamera():
    try:

        if adminLoginSession() == 'admin':
            cameraVO = CameraVO()

            cameraDAO = CameraDAO()

            cameraId = request.args.get('cameraId')

            cameraVO.cameraId = cameraId

            cameraDAO.deleteCamera(cameraVO)
            return redirect(url_for('adminViewCamera'))
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/editCamera', methods=['GET'])
def adminEditCamera():
    try:
        if adminLoginSession() == 'admin':
            print('in adminEditCamera')
            cameraVO = CameraVO()

            cameraDAO = CameraDAO()

            cameraId = request.args.get('cameraId')

            cameraVO.cameraId = cameraId

            cameraVOList = cameraDAO.editCamera(cameraVO)
            areaDAO = AreaDAO()
            crossroadDAO = CrossroadDAO()
            areaVOList = areaDAO.viewArea()
            crossroadVOList = crossroadDAO.viewCrossroad()

            print("=======cameraVOList=======", cameraVOList, areaVOList, crossroadVOList)

            print("=======type of cameraVOList=======", type(cameraVOList))

            return render_template('admin/editCamera.html', cameraVOList=cameraVOList, crossroadVOList=crossroadVOList,
                                   areaVOList=areaVOList)
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/updateCamera', methods=['POST'])
def adminUpdateCamera():
    try:
        if adminLoginSession == 'admin':
            cameraId = request.form['cameraId']
            cameraCode = request.form['cameraCode']
            camera_AreaId = request.form['camera_AreaId']
            camera_CrossroadId = request.form['camera_CrossroadId']

            cameraVO = CameraVO()
            cameraDAO = CameraDAO()

            cameraVO.cameraId = cameraId
            cameraVO.cameraCode = cameraCode
            cameraVO.camera_AreaId = camera_AreaId
            cameraVO.camera_CrossroadId = camera_CrossroadId

            cameraDAO.updateCamera(cameraVO)

            return redirect(url_for('adminViewCamera'))
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)
