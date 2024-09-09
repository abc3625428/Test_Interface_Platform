from flask import Blueprint
from flask_restful import Api


from output import output_json
from . import interfaceCase,interfaceClass


# 响应结构处理
interface_bp = Blueprint('interface_bp', __name__)
data = Api(interface_bp, catch_all_404s=True)
data.representation('application/json')(output_json)


# case列表
data.add_resource(interfaceCase.GEAINTERFACEDATA,'/admin/interface/getinterface/<path:currentPage>',endpoint='getinterfacedata')
data.add_resource(interfaceCase.INTERFACE_ADD,'/admin/interface/interfaceadd',endpoint='interfaceadd')

data.add_resource(interfaceClass.GETINTERFACELIST,'/admin/interface_class/<path:currentPage>',endpoint='interfaceclasslist')
data.add_resource(interfaceClass.INTERFACECLASS_DELETE,'/admin/interface_class/<path:id>/delete',endpoint='deleteinterfacelistpick')
data.add_resource(interfaceClass.ADDINTERFACELIST,'/admin/interface_class',endpoint='interfaceclassadd')