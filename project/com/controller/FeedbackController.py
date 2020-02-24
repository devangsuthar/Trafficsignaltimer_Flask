from datetime import datetime

from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO


@app.route('/user/loadFeedback', methods=['GET'])
def userLoadFeedback():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/addFeedback.html')
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/insertFeedback', methods=['POST'])
def userInsertFeedback():
    try:

        feedbackSubject = request.form['feedbackSubject']
        feedbackDescription = request.form['feedbackDescription']
        feedbackRating = request.form['feedbackRating']

        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()

        todayDate = str(datetime.now().date())
        timeNow = datetime.now().strftime("%H:%M:%S")

        feedbackVO.feedbackFrom_LoginId = session['session_loginId']
        feedbackVO.feedbackSubject = feedbackSubject
        feedbackVO.feedbackDescription = feedbackDescription
        feedbackVO.feedbackRating = feedbackRating
        feedbackVO.feedbackDate = todayDate
        feedbackVO.feedbackTime = timeNow

        feedbackDAO.insertFeedback(feedbackVO)

        return redirect(url_for('userViewFeedback'))

    except Exception as ex:
        print(ex)


@app.route("/user/viewFeedback", methods=['GET'])
def userViewFeedback():
    try:
        if adminLoginSession() == 'user':
            feedbackDAO = FeedbackDAO()
            feedbackVO = FeedbackVO()
            feedbackFrom_LoginId = session['session_loginId']
            feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId
            feedbackVOList = feedbackDAO.userViewFeedback(feedbackVO)
            print("______________", feedbackVOList)

            return render_template("user/viewFeedback.html", feedbackVOList=feedbackVOList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route('/admin/viewFeedback', methods=['GET'])
def adminViewFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackDAO = FeedbackDAO()
            feedbackVOList = feedbackDAO.adminViewFeedback()
            print("__________________", feedbackVOList)
            return render_template('admin/viewFeedback.html', feedbackVOList=feedbackVOList)
        else:
            return adminLogoutSession()
    except Exception as ex:
        print(ex)


@app.route('/user/deleteFeedback', methods=['GET'])
def userDeleteFeedback():
    try:
        feedbackVO = FeedbackVO()

        feedbackDAO = FeedbackDAO()

        feedbackId = request.args.get('feedbackId')

        feedbackVO.feedbackId = feedbackId

        feedbackDAO.deleteFeedback(feedbackVO)

        return redirect(url_for('userViewFeedback'))

    except Exception as ex:
        print(ex)


@app.route('/admin/reviewFeedback')
def adminReviewFeedback():
    try:
        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()

        feedbackId = request.args.get("feedbackId")
        feedbackTo_LoginId = session['session_loginId']

        feedbackVO.feedbackId = feedbackId
        feedbackVO.feedbackTo_LoginId = feedbackTo_LoginId

        feedbackDAO.adminReviewFeedback(feedbackVO)

        return redirect(url_for('adminViewFeedback'))
    except Exception as ex:
        print(ex)
