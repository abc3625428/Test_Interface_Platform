from flask import Blueprint
from flask_restful import Api


from output import output_json
from . import user_api,res_api,login,userinfo,userquit,getStatistics1,getStatistics2,imagelist,imagelistpick,noticeData,userListGetData,interfacereport,user_role


#user_mode
user_bp = Blueprint('user', __name__)
user = Api(user_bp, catch_all_404s=True)
user.representation('application/json')(output_json)


#request_mode
user_data = Blueprint('user_data',__name__)
use_data = Api(user_data,catch_all_404s=True)
use_data.representation('application/json')(output_json)

#report_mode
report = Blueprint('report',__name__)
report_data = Api(report,catch_all_404s=True)
report_data.representation('application/json')(output_json)

#登录/退出
user.add_resource(login.USER_LOGIN,'/user/login',endpoint='User_Login')
user.add_resource(userquit.USER_QUIT,'/user/userquit',endpoint='userquit')

#主页数据
user.add_resource(getStatistics1.GETSTATISTICS1,'/admin/getStatistics1',endpoint='getStatistics1')
user.add_resource(getStatistics2.GETSTATISTICS2,'/admin/getStatistics2',endpoint='getStatistics2')

#图片模块 图片列表
user.add_resource(imagelist.GETEMAGELIST,'/admin/image_class/<path:currentPage>',endpoint='imagelist')
user.add_resource(imagelist.PICKTURELIST_DELETE,'/admin/image_class/<path:id>/delete',endpoint='deleteimagelistpick')
user.add_resource(imagelist.ADDEMAGELIST,'/admin/image_class',endpoint='addimagelistpick')
#图片
user.add_resource(noticeData.NOTICEGETSTATISTICS1,'/admin/notice/1',endpoint='noticeData')
user.add_resource(imagelistpick.GETEMAGELISTPICK,'/admin/image_class/<path:classpage>/image/<path:currentPage>',endpoint='imagelistpick')
user.add_resource(imagelistpick.ADDEMAGELI,'/admin/image/upload',endpoint='imageupload')

#用户
user.add_resource(user_api.USER_DATA_ADD,'/user/adduser',endpoint='useradd')
user.add_resource(user_api.USER_DATA_TABLE,'/user/usertable',endpoint='usertable')
user.add_resource(user_api.USER_DATA_UPDATE,'/user/updateuser',endpoint='updateuser')
user.add_resource(user_api.USER_DATA_DELETE,'/user/deleteuser',endpoint='deleteuser')
user.add_resource(userinfo.USER_USERINFO,'/user/getuserinfo',endpoint='getuserinfo')
#用户列表
user.add_resource(userListGetData.USERLISTGETDATA,'/admin/manager/<path:currentPage>',endpoint='getuserlist')
user.add_resource(userListGetData.USER_ADD,'/admin/manager',endpoint='adduser')
user.add_resource(userListGetData.USER_DELETE,'/admin/manager/<path:id>/delete',endpoint='userdelete')
user.add_resource(userListGetData.USERSEARCH,'/admin/manager/<path:currentPage>',endpoint='usersearch')



#登录退出
use_data.add_resource(res_api.USER_ACCOUNT_DATA_LOGIN,'/user_data/login')
use_data.add_resource(res_api.USER_DATA_UNSEALING,'/user_data/unsealing')
use_data.add_resource(res_api.USER_DATA_UNSEALING_DEL,'/user_data/unsealing/del')

#用户role模块
use_data.add_resource(user_role.USER_ROLE,'/admin/user_data/role')


#报告模块
report_data.add_resource(interfacereport.REPORT_DATA_ADD,'/admin/addreportdata',endpoint='getuserlist')
report_data.add_resource(interfacereport.REPORT_DATA_TABLE,'/admin/getreportdata/<path:currentPage>',endpoint='getreportdata')
report_data.add_resource(interfacereport.REPORT_DATA_DELETE,'/admin/deletereport/<path:id>/delete',endpoint='deletereport')