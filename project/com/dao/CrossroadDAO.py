from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.CrossroadVO import CrossroadVO


class CrossroadDAO:
    def insertCrossroad(self, crossroadVO):
        db.session.add(crossroadVO)

        db.session.commit()

    def viewCrossroad(self):
        crossroadList = db.session.query(CrossroadVO, AreaVO).join(AreaVO,
                                                                   CrossroadVO.crossroad_AreaId == AreaVO.areaId).all()

        return crossroadList

    def deleteCrossroad(self, crossroadId):
        crossroadList = CrossroadVO.query.get(crossroadId)

        db.session.delete(crossroadList)

        db.session.commit()

    def editCrossroad(self, crossroadVO):
        crossroadList = CrossroadVO.query.filter_by(crossroadId=crossroadVO.crossroadId)

        return crossroadList

    def updateCrossroad(self, crossroadVO):
        db.session.merge(crossroadVO)

        db.session.commit()


