from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.TrafficpolicestationVO import TrafficPoliceStationVO
from project.com.vo.LoginVO import LoginVO


class TrafficPoliceStationDAO:
    def insertTrafficPoliceStation(self, trafficPoliceStationVO):
        db.session.add(trafficPoliceStationVO)
        db.session.commit()

    def viewTrafficPoliceStation(self):
        trafficPoliceStationList = db.session.query(TrafficPoliceStationVO, AreaVO, LoginVO)\
            .join(AreaVO,TrafficPoliceStationVO.trafficPoliceStation_AreaId == AreaVO.areaId)\
            .join(LoginVO, TrafficPoliceStationVO.trafficPoliceStation_LoginId == LoginVO.loginId).all()
        return trafficPoliceStationList

    def deleteTrafficPoliceStation(self, trafficPoliceStationVO):
        trafficPoliceStationList = TrafficPoliceStationVO.query.get(trafficPoliceStationVO.trafficPoliceStationId)

        db.session.delete(trafficPoliceStationList)

        db.session.commit()

    def editTrafficPoliceStation(self, trafficPoliceStationVO):
        trafficPoliceStationList = db.session.query(TrafficPoliceStationVO, LoginVO).filter_by(
            trafficPoliceStationId=trafficPoliceStationVO.trafficPoliceStationId).join(LoginVO,
                                                                                       TrafficPoliceStationVO.trafficPoliceStation_LoginId == LoginVO.loginId).all()

        return trafficPoliceStationList

    def updateTrafficPoliceStation(self, trafficPoliceStationVO):
        db.session.merge(trafficPoliceStationVO)

        db.session.commit()
