from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.LoginVO import LoginVO


class TrafficPoliceStationVO(db.Model):
    __tablename__ = 'trafficpolicestationmaster'
    trafficPoliceStationId = db.Column('trafficPoliceStationId', db.Integer, primary_key=True, autoincrement=True)
    trafficPoliceStationName = db.Column('trafficPoliceStationName', db.String(100))
    trafficPoliceStationContact = db.Column('trafficPoliceStationContact', db.String(100))
    trafficPoliceStationAddress = db.Column('trafficPoliceStationAddress', db.String(500))
    trafficPoliceStation_AreaId = db.Column('trafficPoliceStation_AreaId', db.Integer, db.ForeignKey(AreaVO.areaId))
    trafficPoliceStation_LoginId = db.Column('trafficPoliceStation_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))


    def as_dict(self):
        return {
            'trafficPoliceStationId': self.trafficPoliceStationId,
            'trafficPoliceStationName': self.trafficPoliceStationName,
            'trafficPoliceStationContact': self.trafficPoliceStationContact,
            'trafficPoliceStationAddress': self.trafficPoliceStationAddress,
            'trafficPoliceStation_AreaId': self.trafficPoliceStation_AreaId,
            'trafficPoliceStation_LoginId': self.trafficPoliceStation_LoginId
        }


db.create_all()
