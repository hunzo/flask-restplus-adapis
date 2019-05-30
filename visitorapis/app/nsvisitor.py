from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from visitorapis.models.apiModel import UsersModels as model
from visitorapis.controller.ClassVisitor import ADOperation
from visitorapis.lib.TokenAuth import token_required, authorizations
from visitorapis.controller.ConnectDB import ApplicationDatabase


visitor_api = Namespace(
    'Rest APIs for ActiveDirectory Services', description='Active Directory visitor.local domain services', authorizations=authorizations)


Con = ADOperation()


# @visitor_api.route('/binduserinfo')
# class TEST(Resource):
#     @visitor_api.doc(security='apikey')
#     @token_required
#     def get(self):
#         """Get Bind User to Active Directory Informations
#         """
#         # test call by defauls application
#         con = ApplicationDatabase()
#         rs = con.get_binduserinfo('visitor.local')

#         return rs


@visitor_api.route('/getadinfo')
class GetActiveDirectoryInformation(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    def get(self):
        """Get Active Directory Informations
        """
        rs = Con.getad_info()
        return rs


@visitor_api.route('/checkauth')
class CheckUserAuth(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.CheckAuthModel)
    def post(self):
        """Check Username and Password Authentications
        """
        r = request.get_json('username')
        r = request.get_json('password')
        # print(r)

        rs = Con.check_auth(r['username'], r['password'])
        return jsonify(rs)


@visitor_api.route('/getfulluserinfo')
class GetUserInformation(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.UserinfoModel)
    def post(self):
        """Get User Informations
        """
        r = request.get_json('username')
        rs = Con.get_userinfo(r['username'])
        return jsonify({'result': rs})


@visitor_api.route('/getuserinfo')
class GetUserMiniInformation(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.UserinfoModel)
    def post(self):
        """Get User Informations
        """
        r = request.get_json('username')
        rs = Con.get_mini_userinfo(r['username'])
        return jsonify({'result': rs})


@visitor_api.route('/setuserpassword')
class SetUserPassword(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.SetUserPasswordModel)
    def put(self):
        """Set user Passwords 
        """
        r = request.get_json('username')
        r = request.get_json('newpassword')
        rs = Con.set_user_password(r['username'], r['newpassword'])

        return jsonify({'result': rs})


@visitor_api.route('/setuserattribute')
class SetUserAttribute(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.SetUserAttributeModel)
    def put(self):
        """Modified Attributes Users 
        """
        r = request.get_json('username')
        r = request.get_json('attributename')
        r = request.get_json('attributevalue')
        rs = Con.set_user_attributes(
            r['username'], r['attributename'], r['attributevalue'])

        return jsonify({'result': rs})


@visitor_api.route('/addmembertogroup')
class AddMemberToGrop(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.AddMemberToGroupModel)
    def put(self):
        """Add User to Groups  
        """
        r = request.get_json('username')
        r = request.get_json('groupname')
        rs = Con.set_member_togroup(r['username'], r['groupname'])

        return jsonify({'result': rs})


@visitor_api.route('/removememberfromgroup')
class RemoveMemberFromGroup(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.RemoveMemberFromGroupModel)
    def put(self):
        """Remove Users From Group 
        """
        r = request.get_json('username')
        r = request.get_json('groupname')
        rs = Con.remove_member_fromgroup(r['username'], r['groupname'])

        return jsonify({'result': rs})


@visitor_api.route('/creategroup')
class CreateGroup(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.CreateNewGroupModel)
    def post(self):
        """Create New Group 
        """
        r = request.get_json('group')
        r = request.get_json('description')
        r = request.get_json('groupbasedn')
        rs = Con.create_newgroup(
            r['group'], r['description'], r['groupbasedn'])

        return jsonify({'result': rs})


@visitor_api.route('/createuser')
class CreateUser(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.CreateNewUsersModel)
    def post(self):
        """Create New User 
        """
        r = request.get_json('username')
        r = request.get_json('password')
        r = request.get_json('description')
        r = request.get_json('userbasedn')
        rs = Con.create_newusers(r['username'], r['password'],
                                 r['description'], r['userbasedn'])

        return jsonify({'result': rs})


@visitor_api.route('/deletegroup')
class DeleteGroup(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.DeleteGroupModel)
    def delete(self):
        """Delete Group
        """
        r = request.get_json('groupname')
        rs = Con.delete_group(r['groupname'])

        return jsonify({'result': rs})


@visitor_api.route('/deleteuser')
class DeleteUser(Resource):
    @visitor_api.doc(security='apikey')
    @token_required
    @visitor_api.expect(model.DeleteUserModel)
    def delete(self):
        """Delete User
        """
        r = request.get_json('username')
        rs = Con.delete_user(r['username'])

        return jsonify({'result': rs})
