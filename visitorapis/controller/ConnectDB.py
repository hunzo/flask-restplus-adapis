from visitorapis.lib.ADLibrary import ActiveDirectoryMgmt
from visitorapis.models.dbModel import BindUserTable
from visitorapis.app.dbapp import db
from visitorapis import app_db


class ApplicationDatabase:

    def get_binduserinfo(self, domainname):

        rs = BindUserTable.query.filter_by(domain=domainname).first()

        ret = {
            'username': rs.username,
            'password': rs.password,
            'domain': rs.domain,
            'basedn': rs.basedn,
            'bindou': rs.bindou,
            'serverip': rs.serverip
        }

        return ret

    def add_binduser(self, username, password, domainname, basedn, bindou, serverip):

        addUser = BindUserTable(username=username, password=password,
                                domain=domainname, basedn=basedn, bindou=bindou, serverip=str(serverip))
        try:
            db.session.add(addUser)
            db.session.commit()
        except Exception as e:
            return str(e)

        return 'add sucessfully'

    def get_binduserinfo_context(self, domain):
        app = app_db()

        with app.app_context():
            rs = BindUserTable.query.filter_by(domain=domain).first()
            ret = {
                'username': rs.username,
                'password': rs.password,
                'domain': rs.domain,
                'basedn': rs.basedn,
                'bindou': rs.bindou,
                'serverip': rs.serverip
            }

        return ret

    def get_allbinduser(self):
        getall = BindUserTable.query.all()
        ret = []
        for i in getall:
            temp = {}
            temp['id'] = i.id
            temp['username'] = i.username
            # temp['password'] = i.password
            temp['domain'] = i.domain
            temp['basedn'] = i.basedn
            temp['bindou'] = i.bindou
            temp['serverip'] = i.serverip
            temp['timestamp'] = i.timestamp
            ret.append(temp)

        return ret

    def delete_users(self, id):
        BindUserTable.query.filter_by(id=id).delete()
        db.session.commit()

        return id
