from exception import tools,errorLogger,statuCode
from model import zf_company,zf_manage_company,zf_role,zf_ukey,zf_ukey_record
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app,supports_credentials = True)

@app.route('/menus',methods=['GET'])
def getMenus():
    menus = {"data":[{"id":100,"menuName":"单位管理","path":"null","children":[
        {"id":101,"menuName":"单位维护","path":"company","children":[]},
        {"id":102,"menuName":"管口股室维护","path":"companyManage","children":[]},
        {"id":103,"menuName":"管口权限设置","path":"companyRelationship","children":[]},]},

        {"id":200,"menuName":"Ukey管理","path":"null","children":[
        {"id":201,"menuName":"Ukey维护","path":"ukeyManage","children":[]},]}, 
    ],
     "meta": {
      "msg": '获取权限列表成功',
      "status": 200
    }
    }
    return json.dumps(menus,ensure_ascii= False)

@app.route('/companys',methods=['GET'])
def getCompanyTree():
    companyTreeList = zf_company.getcompanyTree()
    if companyTreeList == statuCode.StatuCode.errorCode.value:
        respon = {"meta":{"msg":"获取单位信息列表失败","status":statuCode.StatuCode.errorCode.value}}
    else:
        respon = {"data":companyTreeList,"meta":{"msg":"获取单位信息列表成功","status":statuCode.StatuCode.successCode.value}}
    res = json.dumps(respon,ensure_ascii= False)
    return res

# 获取正在使用的Ukey
@app.route('/ukeys',methods = ['GET'])
def getUkeysLis():
    paramId = request.args.get('companyId')
    compayId = None
    if type(paramId) is str:
        compayId = int(paramId)
    else:
        compayId  = paramId
    ukeys = None
    if compayId == None or compayId == 0:
        ukeys = zf_ukey.getUkeysBycompanyId()
    else:
        ukeys = zf_ukey.getUkeysBycompanyId(companyId=compayId)
    if ukeys == statuCode.StatuCode.errorCode.value:
        respon = {"meta":{"msg":"获取ukey列表失败","status":statuCode.StatuCode.errorCode.value}}
    else:
        respon = {"data":ukeys,"meta":{"msg":"获取ukey列表成功","status":statuCode.StatuCode.successCode.value}}
    res = json.dumps(respon,ensure_ascii= False)
    return res
@app.route('/ukeyids',methods = ['GET'])
def getUkeyIdLis():
    ukeyIdLisDict = zf_ukey.getUkeyIdLis()
    if ukeyIdLisDict == statuCode.StatuCode.errorCode.value:
        respon = {"meta":{"msg":"获取ukeyID列表失败","status":statuCode.StatuCode.errorCode.value}}
    else:
        respon = {"data":ukeyIdLisDict,"meta":{"msg":"获取ukeyID列表成功","status":statuCode.StatuCode.successCode.value}}
    res = json.dumps(respon,ensure_ascii= False)
    return res

@app.route('/roleids',methods = ['GET'])
def getRoleIdLis():
    companyId = request.args.get('companyId')
    roleIdLisDict = zf_ukey.getHasRoleIdLis(companyId)
    if roleIdLisDict == statuCode.StatuCode.errorCode.value:
        respon = {"meta":{"msg":"获取roleID列表失败","status":statuCode.StatuCode.errorCode.value}}
    else:
        respon = {"data":roleIdLisDict,"meta":{"msg":"获取roleID列表成功","status":statuCode.StatuCode.successCode.value}}
    res = json.dumps(respon,ensure_ascii= False)
    return res

@app.route('/insUkey',methods = ['post'])
def insertUkey():
    data = request.get_json(silent=True)
    # print(data)
    # print(type(data))
    if data['ukeyId'] != '':
        usetime = tools.ToolsHelp.getCurrentTime()
        res = zf_ukey.insertUkey(data['ukeyId'],data['name'],data['mobile'],data['carNum'],data['companyId'],data['roleId'],useTime = usetime,isUse=1)
        if res != statuCode.StatuCode.successCode.value:
            return {"meta":{"msg":"插入Ukey失败","status":statuCode.StatuCode.errorCode.value}}
        else:
            return {"data":data,"meta":{"msg":"插入Ukey成功","status":statuCode.StatuCode.successCode.value}}
    else:
        return {"meta":{"msg":"插入Ukey失败","status":statuCode.StatuCode.errorCode.value}}


@app.route('/roles',methods = ['GET'])
def getRoleLis():
    roles = zf_role.getRoles()
    if roles == statuCode.StatuCode.errorCode.value:
        respon = {"meta":{"msg":"获取role列表失败","status":statuCode.StatuCode.errorCode.value}}
    else:
        respon = {"data":roles,"meta":{"msg":"获取role列表成功","status":statuCode.StatuCode.successCode.value}}
    res = json.dumps(respon,ensure_ascii= False)
    return res

def main():
    app.run(host='0.0.0.0',port='80')