from visitorapis.lib.ADLibrary import ActiveDirectoryMgmt
from visitorapis.controller.ConnectDB import ApplicationDatabase


attributes_list = ['CN', 'Distinguishedname', 'displayname', 'mail', 'department', 'samaccountname',
                   'objectCategory', 'company', 'givenName', 'logonCount',
                   'lastlogontimestamp', 'info', 'pwdlastset', 'accountexpires',
                   'userPrincipalName', 'memberof', 'title', 'objectclass', 'userAccountControl', 'description']


BASE_DOMAIN_MGMT = 'visitor.local'

conn = ApplicationDatabase()
ret = conn.get_binduserinfo_context(BASE_DOMAIN_MGMT)

DOMAIN_NAME = ret['domain']
BASE_DN = ret['basedn']
BIND_USER = ret['username']
BIND_PASSWORD = ret['password']
AD_SERVER = ret['serverip']


class ADOperation:

    ConnectActiveDirectory = ActiveDirectoryMgmt(
        AD_SERVER, DOMAIN_NAME, BASE_DN, BIND_USER, BIND_PASSWORD, attributes_list)

    # def __init__(self, username, password, domain, basedn, bindou):
    #     self.username = username
    #     self.password = password
    #     self.domain = domain
    #     self.bindou = bindou
    #     self.basedn = basedn

    def getad_info(self):
        conn = ApplicationDatabase()
        info = conn.get_binduserinfo_context(BASE_DOMAIN_MGMT)

        info['attributelist'] = attributes_list

        del info['password']
        # del info['bindou']

        return info

    def get_bind_data(self):
        conn = ApplicationDatabase()
        userInfo = conn.get_binduserinfo_context(BASE_DOMAIN_MGMT)

        return userInfo

    def check_auth(self, username, password):
        check = self.ConnectActiveDirectory.ad_auth_ldap(username, password)
        print(check)
        return check

    def get_userinfo(self, username):

        try:
            rs = self.ConnectActiveDirectory.search_adusers_information(
                username)
        except Exception as e:
            return str(e)

        return rs

    def get_mini_userinfo(self, username):

        try:
            rs = self.ConnectActiveDirectory.search_adusers_mini_information(
                username)
        except Exception as e:
            return str(e)

        return rs

    def set_user_password(self, username, newpassword):
        try:
            rs = self.ConnectActiveDirectory.set_user_password(
                username, newpassword)
        except Exception as e:
            return str(e)
        return rs

    def set_member_togroup(self, username, groupname):

        try:
            rs = self.ConnectActiveDirectory.add_member_to_group(
                username, groupname)
        except Exception as e:
            return str(e)
        print(rs)

        return rs

    def set_user_attributes(self, username, attributename, attributevalue):
        try:
            rs = self.ConnectActiveDirectory.set_user_attribute(
                username, attributename, attributevalue)
        except Exception as e:
            return str(e)
        return rs

    def remove_member_fromgroup(self, username, groupname):
        try:
            rs = self.ConnectActiveDirectory.remove_member_from_group(
                username, groupname)
        except Exception as e:
            return str(e)
        return rs

    def create_newgroup(self, newgroupname, description, group_base_dn):
        GROUP_BASE_DN = group_base_dn
        try:
            rs = self.ConnectActiveDirectory.create_group(
                GROUP_BASE_DN, newgroupname, description)
        except Exception as e:
            return str(e)
        return rs

    def create_newusers(self, newusername, newpassword, description, user_base_dn):
        USER_BASE_DN = user_base_dn
        try:
            rs = self.ConnectActiveDirectory.create_user(
                USER_BASE_DN, newusername, newpassword, description)
        except Exception as e:
            return str(e)

        return rs

    def delete_group(self, groupname):
        try:
            rs = self.ConnectActiveDirectory.delete_group(groupname)
        except Exception as e:
            return str(e)

        return rs

    def delete_user(self, username):
        try:
            rs = self.ConnectActiveDirectory.delete_user(username)
        except Exception as e:
            return str(e)

        return rs
