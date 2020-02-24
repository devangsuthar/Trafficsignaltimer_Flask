from project import db
from project.com.vo.PackageVO import PackageVO


class PackageDAO:
    def insertPackage(self, packageVO):
        db.session.add(packageVO)
        db.session.commit()

    def viewPackage(self):
        packageList = PackageVO.query.all()

        return packageList

    def deletePackage(self, packageVO):
        packageList = PackageVO.query.get(packageVO.packageId)

        db.session.delete(packageList)

        db.session.commit()

    def editPackage(self, packageVO):
        # areaList = AreaVO.query.get(areaVO.areaId)

        # areaList = AreaVO.query.filter_by(areaId=areaVO.areaId)

        packageList = PackageVO.query.filter_by(packageId=packageVO.packageId).all()

        return packageList

    def updatePackage(self, packageVO):
        db.session.merge(packageVO)

        db.session.commit()
