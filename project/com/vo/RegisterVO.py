from project import db
from project.com.vo.LoginVO import LoginVO


class RegisterVO(db.Model):
    __tablename__ = 'registermaster'
    registerId = db.Column('registerId', db.Integer, primary_key=True, autoincrement=True)
    registertrafficPoliceStationName = db.Column('registertrafficPoliceStationName', db.String(100), nullable=False)
    registertrafficPoliceStationAreaName = db.Column('registertrafficPoliceStationAreaName', db.String(100),
                                                     nullable=False)
    registertrafficPoliceStationAddress = db.Column('registertrafficPoliceStationAddress', db.String(500),
                                                    nullable=False)
    registertrafficPoliceStationContact = db.Column('registertrafficPoliceStationContact', db.String(100),
                                                    nullable=False)
    register_LoginId = db.Column('register_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'registerId': self.registerId,
            'registertrafficPoliceStationName': self.registertrafficPoliceStationName,
            'registertrafficPoliceStationAreaName': self.registertrafficPoliceStationAreaName,
            'registertrafficPoliceStationAddress': self.registertrafficPoliceStationAddress,
            'registertrafficPoliceStationContact': self.registertrafficPoliceStationContact,
            'register_LoginId': self.register_LoginId
        }


db.create_all()
