from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.CameraVO import CameraVO
from project.com.vo.CrossroadVO import CrossroadVO


class CameraDAO:
    def insertCamera(self, cameraVO):
        db.session.add(cameraVO)
        db.session.commit()

    def viewCamera(self):
        print("--------------")
        cameraList = db.session.query(CameraVO, CrossroadVO, AreaVO).join(CrossroadVO,
                                                                          CrossroadVO.crossroadId == CameraVO.camera_CrossroadId).join(
            AreaVO, AreaVO.areaId == CameraVO.camera_AreaId).all()
        print(cameraList)
        return cameraList

    def deleteCamera(self, cameraVO):
        cameraList = CameraVO.query.get(cameraVO.cameraId)

        db.session.delete(cameraList)

        db.session.commit()

    def editCamera(self, cameraVO):
        # cameraList = CameraVO.query.get(cameraVO.cameraId)

        # cameraList = CameraVO.query.filter_by(cameraId=cameraVO.cameraId)

        cameraList = CameraVO.query.filter_by(cameraId=cameraVO.cameraId).all()

        return cameraList

    def updateCamera(self, cameraVO):
        db.session.merge(cameraVO)

        db.session.commit()
