from project import db
from project.com.vo.RegisterVO import RegisterVO


class RegisterDAO:
    def insertRegister(self, registerVO):
        db.session.add(registerVO)
        db.session.commit()

    def viewRegister(self):
        registerList = RegisterVO.query.all()
        return registerList
