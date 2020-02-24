from project import db


class DatasetVO(db.Model):
    __tablename__ = 'datasetmaster'
    datasetId = db.Column('datasetId', db.Integer, primary_key=True, autoincrement=True)
    datasetFilePath = db.Column('datasetFilePath', db.String(200))
    datasetFileName = db.Column('datasetFileName', db.String(100))
    datasetUploadDate = db.Column('datasetUploadDate', db.Date)
    datasetUploadTime = db.Column('datasetUploadTime', db.Time)

    def as_dict(self):
        return {
            'datasetId': self.datasetId,
            'datasetFilePath': self.datasetFilePath,
            'datasetFileName': self.datasetFileName,
            'datasetUploadDate': self.datasetUploadDate,
            'datasetUploadTime': self.datasetUploadTime,

        }


db.create_all()
