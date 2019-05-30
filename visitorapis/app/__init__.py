from flask import Blueprint
from flask_restplus import Api
from visitorapis.app.nsvisitor import visitor_api
from visitorapis.app.apioperation import apioperation_api
from visitorapis.models.apiModel import UsersModels

bp = Blueprint('bp', __name__)

api = Api(bp, title='RestAPI Services', version='0.1', description='Active Directory Rest API Services\n author : TKO\n date : 2019-05-01\n version : 0.1')

# api = Api(title='RestAPI Services', version='0.1', description='Active Directory Rest API Services\n author : TKO\n date : 2019-05-01\n version : 0.1')

api.models[UsersModels.CheckAuthModel.name] = UsersModels.CheckAuthModel
api.models[UsersModels.UserinfoModel.name] = UsersModels.UserinfoModel
api.models[UsersModels.SetUserPasswordModel.name] = UsersModels.SetUserPasswordModel
api.models[UsersModels.SetUserAttributeModel.name] = UsersModels.SetUserAttributeModel
api.models[UsersModels.AddMemberToGroupModel.name] = UsersModels.AddMemberToGroupModel
api.models[UsersModels.RemoveMemberFromGroupModel.name] = UsersModels.RemoveMemberFromGroupModel
api.models[UsersModels.CreateNewGroupModel.name] = UsersModels.CreateNewGroupModel
api.models[UsersModels.CreateNewUsersModel.name] = UsersModels.CreateNewUsersModel
api.models[UsersModels.DeleteUserModel.name] = UsersModels.DeleteUserModel
api.models[UsersModels.DeleteGroupModel.name] = UsersModels.DeleteGroupModel
api.models[UsersModels.AddBindUserModel.name] = UsersModels.AddBindUserModel
api.models[UsersModels.UserIDModel.name] = UsersModels.UserIDModel


api.add_namespace(visitor_api, path='/admgmt')
api.add_namespace(apioperation_api, path='/apiconfig')
