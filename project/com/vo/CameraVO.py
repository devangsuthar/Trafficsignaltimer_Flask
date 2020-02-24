from project import db
from project.com.vo.AreaVO import AreaVO
from project.com.vo.CrossroadVO import CrossroadVO


class CameraVO(db.Model):
    __tablename__ = 'cameramaster'
    cameraId = db.Column('cameraId', db.Integer, primary_key=True, autoincrement=True)
    cameraCode = db.Column('cameraCode', db.Integer)
    camera_AreaId = db.Column('camera_AreaId', db.Integer, db.ForeignKey(AreaVO.areaId))
    camera_CrossroadId = db.Column('camera_CrossroadId', db.Integer, db.ForeignKey(CrossroadVO.crossroadId))

    def as_dict(self):
        return {
            'cameraId': self.cameraId,
            'cameraCode': self.cameraCode,
            'camera_AreaId': self.camera_AreaId,
            'camera_CrossroadId': self.camera_CrossroadId
        }


db.create_all()
