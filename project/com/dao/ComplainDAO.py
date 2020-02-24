from project import db
from project.com.vo.ComplainVO import ComplainVO
from project.com.vo.LoginVO import LoginVO


class ComplainDAO:
    def insertComplain(self, complainVO):
        db.session.add(complainVO)
        db.session.commit()

    def viewComplain(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainFrom_LoginId=complainVO.complainFrom_LoginId)

        return complainList

    def deleteComplain(self, complainVO):
        complainList = ComplainVO.query.get(complainVO.complainId)

        db.session.delete(complainList)

        db.session.commit()

        return complainList

    def adminViewComplain(self):
        complainList = db.session.query(ComplainVO, LoginVO). \
            join(LoginVO, ComplainVO.complainFrom_LoginId == LoginVO.loginId).all()

        return complainList

    def adminInsertReply(self, complainVO):
        db.session.merge(complainVO)
        db.session.commit()

    def viewComplainReply(self, complainVO):
        complainReplyList = ComplainVO.query.filter_by(complainId=complainVO.complainId)
        return complainReplyList


