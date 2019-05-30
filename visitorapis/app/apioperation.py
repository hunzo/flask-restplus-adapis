from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from visitorapis.models.apiModel import UsersModels as model
from visitorapis.controller.ClassVisitor import attributes_list
from visitorapis.lib.TokenAuth import token_required, authorizations, token_admin_required
from visitorapis.controller.ConnectDB import ApplicationDatabase


apioperation_api = Namespace(
    'Rest APIs Configuration', description='AD RestAPIs Configuration', authorizations=authorizations)

CON = ApplicationDatabase()


@apioperation_api.route('/binuserinfo')
class GetBindUserInformation(Resource):
    @apioperation_api.doc(security='apikey')
    @token_admin_required
    def get(self):
        """Get Bind User to Active Directory Informations
        """
        # test call by defauls application

        rs = CON.get_binduserinfo('visitor.local')

        del rs['password']
        rs['attributelist'] = attributes_list

        return rs


@apioperation_api.route('/getallbinduser')
class GetALLBindUserInformation(Resource):
    @apioperation_api.doc(security='apikey')
    @token_admin_required
    def get(self):
        """Get Bind User to Active Directory Informations
        """
        # test call by defauls application
        rs = CON.get_allbinduser()

        return jsonify({'users': rs})


@apioperation_api.route('/addbinduser')
class AddBindUser(Resource):
    @apioperation_api.doc(security='apikey')
    @token_admin_required
    @apioperation_api.expect(model.AddBindUserModel)
    def post(self):
        r = request.get_json('username')
        r = request.get_json('password')
        r = request.get_json('domain')
        r = request.get_json('bindou')
        r = request.get_json('basedn')
        r = request.get_json('serverip')

        print(r)

        try:
            rs = CON.add_binduser(
                r['username'], r['password'], r['domain'], r['basedn'], r['bindou'], r['serverip'])
        except Exception as e:
            return jsonify({'error-----Views': str(e)})

        return jsonify({'status': rs})


@apioperation_api.route('/deleteid')
class DeleteBindUser(Resource):
    @apioperation_api.doc(security='apikey')
    @token_admin_required
    @apioperation_api.expect(model.UserIDModel)
    def post(self):
        r = request.get_json('id')

        print(r)

        try:
            rs = CON.delete_users(r['id'])
        except Exception as e:
            return jsonify({'error-----Views': str(e)})

        return jsonify({'msg': rs})
