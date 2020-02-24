from datetime import datetime, date
from flask import request, render_template, redirect, url_for, session
from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.PackageDAO import PackageDAO
from project.com.dao.PurchaseDAO import PurchaseDAO
from project.com.vo.PurchaseVO import PurchaseVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.PackageVO import PackageVO


@app.route('/user/loadPurchase')
def userLoadPurchase():
    try:

        if adminLoginSession() == 'user':
            packageDAO = PackageDAO()
            packageVOList = packageDAO.viewPackage()
            return render_template('user/addPurchase.html', packageVOList=packageVOList)

        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/insertPurchase', methods=['post'])
def adminInsertpurchase():
    try:
        if adminLoginSession() == 'user':
            purchaseDate = date.today()
            purchaseTime = datetime.now().strftime("%H:%M:%S")
            purchase_loginId = session['session_LoginId']
            packageId = request.form['packageId']
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",packageId)
            purchaseVO = PurchaseVO()
            purchaseDAO = PurchaseDAO()

            purchaseVO.purchaseDate = purchaseDate
            purchaseVO.purchaseTime = purchaseTime
            purchaseVO.purchase_loginId = purchase_loginId
            purchaseVO.purchase_packageId = int(packageId)
            purchaseDAO.insertPurchase(purchaseVO)

            return redirect(url_for('userViewPurchase'))
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/viewPurchase', methods=['GET'])
def adminViewPurchase():
    try:
        if adminLoginSession() == 'admin':
            purchaseDAO = PurchaseDAO()
            purchaseVOList = purchaseDAO.viewPurchase()
            print("__________________", purchaseVOList)
            loginVO = LoginVO()
            loginDAO = LoginDAO()
            packageVO = PackageVO()
            packageDAO = PackageDAO()
            purchaseDictList = [i.as_dict() for i in  purchaseVOList]
            print('$$$$$$$$$$$$$$$$',purchaseDictList)

            loginVO.loginId = purchaseDictList[0]['purchase_loginId']
            packageVO.packageId = purchaseDictList[0]['purchase_packageId']

            packageVOList = packageDAO.viewUserPackage(packageVO)
            loginVOList = loginDAO.registerLogin(loginVO)
            print('ok')
            return render_template('admin/viewPurchase.html', purchaseVOList=purchaseVOList,packageVOList =packageVOList, loginVOList = loginVOList)
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/deletePurchase', methods=['GET'])
def adminDeletePurchase():
    try:
        if adminLoginSession() == 'admin':
            purchaseVO = PurchaseVO()

            purchaseDAO = PurchaseDAO()

            purchaseId = request.args.get('purchaseId')

            purchaseVO.purchaseId = purchaseId

            purchaseDAO.deletePurchase(purchaseVO)

            return redirect(url_for('adminViewPurchase'))
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/editPurchase', methods=['GET'])
def adminEditPurchase():
    try:
        if adminLoginSession() == 'admin':

            purchaseVO = PurchaseVO()

            purchaseDAO = PurchaseDAO()

            purchaseId = request.args.get('purchaseId')

            purchaseVO.purchaseId = purchaseId

            purchaseVOList = purchaseDAO.editPurchase(purchaseVO)

            print("=======purchaseVOList=======", purchaseVOList)

            print("=======type of purchaseVOList=======", type(purchaseVOList))

            return render_template('admin/editPurchase.html', purchaseVOList=purchaseVOList)
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/admin/updatePurchase', methods=['POST'])
def adminUpdatePurchase():
    try:
        if adminLoginSession() == 'admin':
            purchaseDate = date.today()
            purchaseTime = datetime.now().strftime("%H:%M:%S")
            purchase_loginId = session['session_LoginId']
            packageId = request.form['packageId']
            purchaseId = request.form['purchaseId']

            purchaseVO = PurchaseVO()
            purchaseDAO = PurchaseDAO()

            purchaseVO.purchaseId = purchaseId
            purchaseVO.purchaseDate = purchaseDate
            purchaseVO.purchaseTime = purchaseTime
            purchaseVO.purchase_loginId = purchase_loginId
            purchaseVO.purchase_packageId = packageId
            purchaseDAO.insertPurchase(purchaseVO)

            purchaseDAO.updatePurchase(purchaseVO)

            return redirect(url_for('adminViewPurchase'))
        else:
            adminLogoutSession()

    except Exception as ex:
        print(ex)


@app.route('/user/viewPurchase', methods=['GET'])
def userViewPurchase():
    try:
        if adminLoginSession() == 'user':
            purchaseDAO = PurchaseDAO()
            purchaseVO = PurchaseVO()
            packageVO = PackageVO()
            packageDAO = PackageDAO()
            purchaseVO.purchase_loginId = session['session_LoginId']
            purchaseVOList = purchaseDAO.viewUserPurchase(purchaseVO)
            print("__________________", purchaseVOList)
            purchaseDictList = [i.as_dict() for i in purchaseVOList]
            print(purchaseDictList)
            packageVO.packageId = purchaseDictList[0]['purchase_packageId']
            packageVOList = packageDAO.viewUserPackage(packageVO)
            print("__________________", packageVOList)
            return render_template('user/viewPurchase.html', purchaseVOList=purchaseVOList,packageVOList = packageVOList)
        else:
            adminLogoutSession()
    except Exception as ex:
        print(ex)
