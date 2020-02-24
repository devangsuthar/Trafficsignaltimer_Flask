import os
from datetime import datetime

from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO

UPLOAD_FOLDER = 'project/static/adminResources/dataset/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/admin/loadDataset')
def adminLoadDataset():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addDataset.html')
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/insertDataset', methods=['POST'])
def adminInsertDataset():
    try:
        if adminLoginSession() == 'admin':
            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()

            file = request.files['datasetFile']
            print(file)

            datasetFilename = secure_filename(file.filename)
            print(datasetFilename)

            datasetFilepath = os.path.join(app.config['UPLOAD_FOLDER'])
            print(datasetFilepath)

            file.save(os.path.join(datasetFilepath, datasetFilename))

            todayDate = str(datetime.now().date())
            timeNow = datetime.now().strftime("%H:%M:%S")

            datasetVO.datasetFileName = datasetFilename
            datasetVO.datasetFilePath = datasetFilepath.replace("project", "..")
            datasetVO.datasetUploadDate = todayDate
            datasetVO.datasetUploadTime = timeNow

            datasetDAO.insertDataset(datasetVO)

            return redirect(url_for('adminViewDataset'))

        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/viewDataset', methods=['GET'])
def adminViewDataset():
    try:
        if adminLoginSession() == 'admin':
            datasetDAO = DatasetDAO()
            datasetVOList = datasetDAO.viewDataset()
            print("__________________", datasetVOList)

            return render_template('admin/viewDataset.html', datasetVOList=datasetVOList)
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteDataset', methods=['GET'])
def adminDeleteDataset():
    try:
        if adminLoginSession() == 'admin':
            datasetVO = DatasetVO()

            datasetDAO = DatasetDAO()

            datasetId = request.args.get('datasetId')

            datasetVO.datasetId = datasetId

            datasetList = datasetDAO.deleteDataset(datasetVO)

            datasetFileName = datasetList.datasetFileName
            datasetFilePath = datasetList.datasetFilePath.replace('..', 'project')

            fullpath = datasetFilePath + datasetFileName

            os.remove(fullpath)

            return redirect(url_for('adminViewDataset'))
        else:
            return adminLogoutSession()

    except Exception as ex:
        print(ex)
