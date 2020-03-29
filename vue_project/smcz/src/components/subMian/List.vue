<template>
  <div>
    <el-row :gutter = '20'>
          <el-col :span="8">
              <el-input placeholder="请输入内容"
              v-model="queryInfo.query"
              @clear="getUkeyRecordList"
              clearable>
              <el-button slot="append"
              @click="getUkeyRecordList"
              icon="el-icon-search"></el-button>
              </el-input>
          </el-col>
          <el-col :span="8">
            <el-button type="primary" @click="addUkeyDialogVisible ">添加角色</el-button>
          </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <el-table :data="ukeyData.ukeyLis"
              border
              stripe
              style="width: 100%">
        <!-- <el-table-column type="index"
                        width='80'
                        align='center'
                        header-align='center'
                        label='序号'>
        </el-table-column> -->
        <el-table-column prop="ukey_id"
                        label="ID"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="compname"
                        label="单位"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="r_name"
                        label="角色"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="ownername"
                        label="姓名"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="ownermobile"
                        label="电话"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="ownercarnum"
                        label="身份证号码"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <el-table-column prop="usetime"
                        label="启用时间"
                        align='center'
                        header-align='center'
                        minWidth="100">
        </el-table-column>
        <!-- 为当前模板指定了作用域插槽后,作用域插槽的内容会覆盖prop属性值,因此prop属性可以不进行设置 -->
        <el-table-column
                        label="操作"
                        align='center'
                        header-align='center'
                        class-name = tableCellStyle
                        minWidth="120">
            <template v-slot:default='slotScope'>
                <div class="visi">
                  <el-button type="primary" icon="el-icon-edit" circle @click="showChangeUserDialog(slotScope.row)"></el-button>
                  <el-button type="danger" icon="el-icon-delete" circle @click="openDelUserMessageBox(slotScope.row.C_ID)"></el-button>
                </div>
            </template>
        </el-table-column>
      </el-table>
    <!-- 添加ukey对话框 -->
    <el-dialog @close="addUkeyDialogClose" title="添加角色" :visible.sync="ukeyDialogFormVisible">
      <el-form :model="ukeyForm" ref="addUkeyFormRef" :rules="addUkeyRules" :label-width="formLabelWidth">
        <el-form-item label="ukeyId" prop="ukeyId" >
          <el-input v-model="ukeyForm.ukeyId"></el-input>
        </el-form-item>
        <el-form-item label="岗位" prop="roleId">
          <el-select v-model="ukeyForm.roleId" placeholder="请选择岗位">
            <el-option v-for=" item in roleData.roleLis"
            :key="item.r_id"
            :label="item.r_name"
            :value="item.r_id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
          <el-input v-model="ukeyForm.name"></el-input>
        </el-form-item>
        <el-form-item label="电话" prop="mobile">
          <el-input v-model="ukeyForm.mobile"></el-input>
        </el-form-item>
        <el-form-item label="身份证号码" prop="carNum">
          <el-input v-model="ukeyForm.carNum"></el-input>
        </el-form-item>
        <el-form-item label="单位名称" prop="companyId">
          <el-select v-model="ukeyForm.companyId">
            <el-option
            :key="currentCompanyInfo.compid"
            :label="currentCompanyInfo.compname"
            :value="currentCompanyInfo.compid">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="注册说明" prop="appContent">
          <el-input type="textarea" v-model="ukeyForm.appContent"></el-input>
        </el-form-item>
        <el-form-item label="申请人" prop="proposer">
          <el-input v-model="ukeyForm.proposer"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="resetAddUkeyDialog">重置</el-button>
        <el-button type="primary" @click="btnUkeyInsert">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data () {
    var isMobileNumber = (rule, value, callback) => {
      if (!value) {
        return new Error('请输入电话号码')
      } else {
        const reg = /^1[3|4|5|7|8|9][0-9]\d{8}$/
        const isPhone = reg.test(value)
        value = Number(value) // 转换为数字
        if (typeof value === 'number' && !isNaN(value)) { // 判断是否为数字
          value = value.toString() // 转换成字符串
          if (value.length < 0 || value.length > 12 || !isPhone) { // 判断是否为11位手机号
            callback(new Error('手机号码格式如:138xxxx8754'))
          } else {
            callback()
          }
        } else {
          callback(new Error('请输入电话号码'))
        }
      }
    }
    var isCarNumber = (rule, value, callback) => {
      if (!value) {
        return new Error('请输入身份证号码')
      } else {
        const reg = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/
        const isCarNum = reg.test(value)
        value = Number(value) // 转换为数字
        if (typeof value === 'number' && !isNaN(value)) { // 判断是否为数字
          value = value.toString() // 转换成字符串
          if (value.length < 0 || value.length > 18 || !isCarNum) { // 判断是否为18位以下的身份证号码
            callback(new Error('身份证号码格式为18位或15位'))
          } else {
            callback()
          }
        } else {
          callback(new Error('请输入身份证号码'))
        }
      }
    }
    // async getUkeyIdLis (){
    //   const { data: res } = await this.$http.get('/ukeyids')
    //   if (res.meta.status !== 1000) {
    //     this.ukeyIdData.meta = res.meta
    //     this.$message.error(res.meta.msg)
    //   } else {
    //     this.ukeyIdData.ukeyIdLis = res.data.ukey_id
    //     this.ukeyIdData.meta = res.meta
    //     this.$message.success(res.meta.msg)
    //   }
    // }
    var isUkeyId = (rule, value, callback) => {
      if (!value) {
        return new Error('请输入ukeyId')
      } else {
        const reg = /^\d{4}$/
        const isUkeyNum = reg.test(value)
        value = Number(value) // 转换为数字
        if (typeof value === 'number' && !isNaN(value)) { // 判断是否为数字
          value = value.toString() // 转换成字符串
          if (value.length < 0 || value.length !== 4 || !isUkeyNum) { // 判断是否为6位数字
            callback(new Error('UkeyId为4位数字'))
            // 此处访问已获取的ukeyidList进行判断
          } else if (this.ukeyIdData.ukeyIdLis.includes(Number(value))) {
            callback(new Error('该UkeyId已存在,请核对后重新输入'))
          } else {
            callback()
          }
        } else {
          callback(new Error('请输入4位数字'))
        }
      }
    }
    var isRoleId = (rule, value, callback) => {
      console.log(value)
      console.log(this.roleIdData.roleIdLis)
      console.log(this.roleIdData.roleIdLis.includes(value))
      if (this.roleIdData.roleIdLis.includes(value)) {
        callback(new Error('当前岗位已存在,请先进行相岗位Ukey的销毁后再登记'))
      } else {
        callback() // 不抛出错误整明验证没有问题
      }
    }
    return {
      queryInfo: {
        query: ''
      },
      bodyClientHeight: {
        height: ''
      },
      ukeyIdData: {
        ukeyIdLis: [],
        meta: {}
      },
      roleIdData: {
        roleIdLis: [],
        meta: {}
      },
      roleData: {
        roleLis: [],
        meta: {}
      },
      ukeyDialogFormVisible: false,
      ukeyForm: {
        ukeyId: '',
        roleId: '',
        name: '',
        mobile: '',
        carNum: '',
        companyId: '',
        useTime: '',
        unuseTiem: '',
        isUse: true,
        idDestroy: false,
        appContent: ' xxx 申请 (注册/修改/注销/销毁) UkeyId: xxxx',
        proposer: ''
      },
      formLabelWidth: '120px',
      addUkeyRules: {
        mobile: [
          { required: true, message: '请输入电话号码', trigger: 'blur' },
          { validator: isMobileNumber, trigger: 'blur' }
        ],
        companyId: [
          { required: true, message: '请选择单位', trigger: 'change' }
        ],
        roleId: [
          { required: true, message: '请选择岗位', trigger: 'change' },
          { validator: isRoleId, trigger: 'change' }
        ],
        carNum: [
          { required: true, message: '请输入身份证号码', trigger: 'blur' },
          { validator: isCarNumber, trigger: 'blur' }
        ],
        ukeyId: [
          { required: true, message: '请输入UkeyId', trigger: 'blur' },
          { validator: isUkeyId, trigger: 'blur' }
        ],
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' },
          { min: 2, message: '最短 2个字符', trigger: 'blur' }
        ],
        appContent: [
          { required: true, message: '请填写注册说明内容', trigger: 'blur' },
          { min: 15, message: '最短 15 个字符', trigger: 'blur' }
        ],
        proposer: [
          { required: true, message: '请填写申请人', trigger: 'blur' },
          { min: 2, message: '最短 2 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.bodyClientHeight.height = document.body.clientHeight - 142 + 'px' // 获取当前body高度
    this.$store.dispatch('getUkeyList')
    this.$store.dispatch('setIsTab') // 改变store.state中isTab属性的状态，从而触发Main.vue中watch中的isTa()
  },
  mounted () {
  },
  computed: {
    ...mapState(['currentCompanyInfo', 'ukeyData'])
  },
  methods: {
    async getRoleLis () {
      const { data: res } = await this.$http.get('/roles')
      if (res.meta.status !== 1000) {
        this.roleData.meta = res.meta
        this.$message.error(res.meta.msg)
      } else {
        this.roleData.roleLis = res.data
        this.roleData.meta = res.meta
        this.$message.success(res.meta.msg)
      }
    },
    async getUkeyIdLis () {
      const { data: res } = await this.$http.get('/ukeyids')
      if (res.meta.status !== 1000) {
        this.ukeyIdData.meta = res.meta
        this.$message.error(res.meta.msg)
      } else {
        this.ukeyIdData.ukeyIdLis = res.data.ukey_id
        this.ukeyIdData.meta = res.meta
        this.$message.success(res.meta.msg)
      }
    },
    async getRoleIdLis (companyId) {
      const { data: res } = await this.$http.get('/roleids', {
        params: {
          companyId: companyId
        }
      })
      if (res.meta.status !== 1000) {
        this.roleIdData.meta = res.meta
        this.$message.error(res.meta.msg)
      } else {
        this.roleIdData.roleIdLis = res.data.role_id
        this.roleIdData.meta = res.meta
        this.$message.success(res.meta.msg)
      }
    },
    isUseStateChanged (isUse) {
      isUse = !isUse
    },
    // 注册一个ukey,并创建相应的记录
    btnUkeyInsert () {
      this.$refs.addUkeyFormRef.validate(async result => {
        if (result) {
          const postData = this.ukeyForm
          postData.ukeyId = Number(postData.ukeyId)
          postData.isUse = postData.isUse === true ? 1 : 0
          postData.idDestroy = postData.isDistroy === true ? 1 : 0
          const { data: res } = await this.$http.post('/insUkey', postData)
          if (res.meta.status !== 1000) {
            this.$message.error('添加角色失败')
          } else {
            this.$message.success('添加角色 ' + res.data.name + ' 成功:')
            // 刷新列表
            this.$store.dispatch('getUkeyList', this.currentCompanyInfo.compid)
            // 关闭添加对话框
            this.ukeyDialogFormVisible = false
          }
        }
      })
    },
    addUkeyDialogVisible () {
      if (this.currentCompanyInfo.levelid === 2 || this.currentCompanyInfo.levelid === 3) {
        this.getRoleLis()
        this.ukeyForm.isUse = true
        this.ukeyDialogFormVisible = true
        this.getUkeyIdLis()
        this.getRoleIdLis(this.currentCompanyInfo.compid)
      } else {
        this.$message.error('请在左侧选择单位后添加角色')
      }
    },
    addUkeyDialogClose () {
      console.log('222222222222')
      console.log(this.ukeyForm)
      this.$refs.addUkeyFormRef.resetFields() // 重置表单及验证结果
      console.log('333333333333')
      console.log(this.ukeyForm)
    },
    resetAddUkeyDialog () {
      this.$refs.addUkeyFormRef.resetFields() // 重置表单及验证结果
    },
    getUkeyRecordList () {

    }
  }
}
</script>

<style lang="less" scoped>
  .el-row{
    margin-top: 20px;
  }
</style>
