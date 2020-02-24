from project import db
from project.com.vo.PurchaseVO import PurchaseVO


class PurchaseDAO:

    def insertPurchase(self, purchaseVO):
        db.session.add(purchaseVO)
        db.session.commit()

    def viewPurchase(self):
        purchaseList = PurchaseVO.query.all()
        return purchaseList

    def deletePurchase(self, purchaseVO):
        purchaseList = PurchaseVO.query.get(purchaseVO.purchaseId)
        db.session.delete(purchaseList)
        db.session.commit()

    def editPurchase(self, purchaseVO):
        purchaseList = PurchaseVO.query.filter_by(purchaseId=purchaseVO.purchaseId).all()
        return purchaseList

    def updatePurchase(self, purchaseVO):
        db.session.merge(purchaseVO)
        db.session.commit()

    def viewUserPurchase(self, purchaseVO):
        purchaseList = PurchaseVO.query.filter_by(purchase_loginId=purchaseVO.purchase_loginId).all()
        return purchaseList
