from project import db
from project.com.vo.LoginVO import LoginVO


class LoginDAO:
    def insertLogin(self, loginVO):
        db.session.add(loginVO)
        db.session.commit()

    def validateLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername, loginPassword=loginVO.loginPassword,
                                            loginStatus=loginVO.loginStatus)

        return loginList

    def ViewRegisterLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginId=loginVO.loginId, loginUsername=loginVO.loginUsername)
        return loginList

    def viewLogin(self):
        loginList = LoginVO.query.all()
        return loginList

    def deleteLogin(self, loginVO):
        loginList = LoginVO.query.get(loginVO.loginId)
        db.session.delete(loginList)
        db.session.commit()


    def updateLogin(self, loginVO):
        db.session.merge(loginVO)
        db.session.commit()
