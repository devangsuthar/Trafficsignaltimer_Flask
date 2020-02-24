from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.PackageVO import PackageVO


class PurchaseVO(db.Model):
    __tablename__ = 'purchasemaster'
    purchaseId = db.Column('purchaseId', db.Integer, primary_key=True, autoincrement=True)
    purchaseDate = db.Column('purchaseDate', db.Date)
    purchaseTime = db.Column('purchaseTime', db.Time)
    purchase_loginId = db.Column('purchase_loginId', db.Integer, db.ForeignKey(LoginVO.loginId))
    purchase_packageId = db.Column('purchase_packageId', db.Integer, db.ForeignKey(PackageVO.packageId))

    def as_dict(self):

        return {
            'purchaseId': self.purchaseId,
            'purchaseDate': self.purchaseDate,
            'purchaseTime': self.purchaseTime,
            'purchase_loginId': self.purchase_loginId,
            'purchase_packageId': self.purchase_packageId
        }


db.create_all()
