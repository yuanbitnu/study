<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>用户管理</el-breadcrumb-item>
            <el-breadcrumb-item>用户列表</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 卡片容器区域 -->
        <el-card class="box-card">
            <el-row :gutter = '20'>
                <el-col :span="8">
                    <el-input placeholder="请输入内容"
                    v-model="queryInfo.query"
                    @clear="getUserList"
                    clearable>
                    <el-button slot="append"
                    @click="getUserList"
                    icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
                <el-col :span="4">
                  <el-button type="primary" @click="addUserDialogVisible = true">添加用户</el-button>
                </el-col>
            </el-row>
            <!-- 用户列表区域 -->
            <el-table :data="userList"
                    border
                    stripe
                    style="width: 100%">
              <el-table-column type="index"
                              width='80'
                              align='center'
                              header-align='center'
                              label='序号'>
              </el-table-column>
              <el-table-column prop="username"
                              label="姓名"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <el-table-column prop="email"
                              label="邮箱"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <el-table-column prop="mobile"
                              label="电话"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <el-table-column prop="role_name"
                              label="角色"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <!-- 为当前模板指定了作用域插槽后,作用域插槽的内容会覆盖prop属性值,因此prop属性可以不进行设置 -->
              <el-table-column
                              label="状态"
                              align='center'
                              header-align='center'
                              minWidth="100">
                  <!-- el-table-column 中有一个默认插槽(默认名为default) 使用v-slot指令绑定一个属性(slotScope--[该名称自定义])用于接收传递给插槽的属性传递过来的属性对象有三个属性(row--包含当前该对象的所有数据;colum--包含该列所有设置属性的值;$index--表示该行是第几行)-->
                  <template v-slot='slotScope'>
                      <el-switch
                                v-model="slotScope.row.mg_state"
                                @change='userStateChanged(slotScope.row)'
                                active-color="#13ce66">
                      </el-switch>
                  </template>
              </el-table-column>
              <el-table-column prop="username"
                              label="操作"
                              align='center'
                              header-align='center'
                              minWidth="100">
                  <template v-slot:default='slotScope'>
                      <el-row>
                        <el-button type="primary" icon="el-icon-edit" circle @click="showChangeUserDialog(slotScope.row)"></el-button>
                        <el-button type="danger" icon="el-icon-delete" circle @click="openDelUserMessageBox(slotScope.row.id)"></el-button>
                        <el-tooltip content="权限设置" placement="top" :enterable='false'>
                          <el-button type="warning" icon="el-icon-setting" circle @click="changeUserRole(slotScope.row.id)"></el-button>
                        </el-tooltip>
                      </el-row>
                  </template>
              </el-table-column>
            </el-table>
            <!-- 分页区域 -->
            <el-pagination
                          @size-change="handleSizeChange"
                          @current-change="handleCurrentChange"
                          :current-page="queryInfo.pagenum"
                          :page-sizes="pagesizes"
                          :page-size="pagesizes[0]"
                          layout="total, sizes, prev, pager, next, jumper"
                          :total="userTotal">
            </el-pagination>
        </el-card>
        <!-- 添加用户的对话框 -->
        <el-dialog
                  title="添加用户"
                  :visible.sync="addUserDialogVisible"
                  width="30%"
                  @close='closeAddUserDialog'>
          <!-- 添加用户表单验证区域 -->
          <el-form :model="addUserForm" :rules="addUsewrRules" ref="addUserFormRef" label-width="100px" class="demo-ruleForm" status-icon>
            <el-form-item label="用户名" prop="username">
              <el-input v-model="addUserForm.username"
              ></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password" >
              <el-input v-model="addUserForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPwd" >
              <el-input v-model="addUserForm.checkPwd" show-password></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="addUserForm.email"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="mobile">
              <el-input v-model="addUserForm.mobile"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="resetAddUserDialog">重置</el-button>
            <el-button type="primary" @click="btnAddUserDialog">确 定</el-button>
          </span>
        </el-dialog>
        <!-- 修改用户对话框 -->
        <el-dialog title="修改"
                   :visible.sync="changeUserDialogVisible"
                   width="30%"
                   @close='closechangeUserDialog'>
           <el-form :model="changeUserForm" :rules="addUsewrRules" ref="changeUserFormRef" label-width="100px" >
            <el-form-item label="用户名" prop="username">
              <el-input v-model="changeUserForm.username" disabled
              ></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="changeUserForm.email"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="mobile">
              <el-input v-model="changeUserForm.mobile"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer"
                class="dialog-footer">
            <el-button @click="changeUserDialogVisible = false">取 消</el-button>
            <el-button type="primary"
                       @click="changeUser">确 定</el-button>
          </span>
        </el-dialog>
    </div>
</template>

<script>
export default {
  data () {
    // 密码输入框验证规则方法
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.addUserForm.checkPwd !== '') {
          this.$refs.addUserFormRef.validateField('checkPwd')
        }
        callback()
      }
    }
    // checkpwd输入框验证规则方法
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.addUserForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    // 电话号码输入框验证规则方法
    var isMobileNumber = (rule, value, callback) => {
      if (!value) {
        return new Error('请输入电话号码')
      } else {
        const reg = /^1[3|4|5|7|8][0-9]\d{8}$/
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
    return {
      // 添加用户表单数据
      addUserForm: {
        username: 'administrator',
        password: '',
        checkPwd: '',
        email: '',
        mobile: ''
      },
      changeUserForm: {
        id: '',
        username: '',
        email: '',
        mobile: ''
      },
      // 添加用户表单验证规则
      addUsewrRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, message: '最短 3 个字符', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, validator: validatePass, trigger: 'blur' }
        ],
        checkPwd: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ],
        mobile: [
          { required: true, message: '请电话号码', trigger: 'blur' },
          { validator: isMobileNumber, trigger: 'blur' }
        ]
      },
      // 添加用户表单对话框是否可见
      addUserDialogVisible: false,
      changeUserDialogVisible: false,
      userList: [],
      userTotal: 0,
      pagesizes: [10, 30, 40, 50], // 每页显示数下拉组件值
      // 获取用户数据列表的参数对象
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      }
    }
  },
  // 生命周期created(页面加载完之后的调用)
  created () {
    this.getUserList()
  },
  methods: {
    // 请求用户列表函数
    async getUserList () {
      let { data: res } = await this.$http.get('users', {
        params: this.queryInfo
      })
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      this.userList = res.data.users
      this.userTotal = res.data.total
    },
    // 点击用户列表中修改用户按钮时的单击事件
    showChangeUserDialog (userData) {
      this.changeUserForm.id = userData.id
      this.changeUserForm.username = userData.username
      this.changeUserForm.email = userData.email
      this.changeUserForm.mobile = userData.mobile
      this.changeUserDialogVisible = true
    },
    // 打开删除用户的提示对话框
    openDelUserMessageBox (id) {
      this.$messageBox.confirm('此操作将永久删除该用户,是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(async () => {
        let { data: res } = await this.$http.delete(`users/${id}`)
        if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
        this.getUserList()
        this.$message.success(res.meta.msg)
      }).catch(() => {
        this.$message.info('已取消删除')
      })
    },
    changeUserRole (id) {
    },
    // 分页功能每页显示数量改变事件函数
    handleSizeChange (val) {
      this.queryInfo.pagesize = val
      this.getUserList()
    },
    // 跳转页面时的事件函数
    handleCurrentChange (val) {
      this.queryInfo.pagenum = val
      this.getUserList()
    },
    // 监听switch状态的改变
    async userStateChanged (rowUesrObj) {
      let{ data: res } = await this.$http.put(`users/${rowUesrObj.id}/state/${rowUesrObj.mg_state}`)
      if (res.meta.status !== 200) {
        rowUesrObj.mg_state = !rowUesrObj.mg_state // 如果修改状态写入数据库失败,则需要将mg_state数据还原,已保证页面显示用户状态的一致性
        return this.$message.error(res.meta.msg)
      }
      this.$message({
        message: res.meta.msg,
        type: 'success'
      })
    },
    // 关闭添加用户对话框之前的事件回调函数
    closeAddUserDialog () {
      this.$refs.addUserFormRef.resetFields() // 重置表单数据及表单验证结果
    },
    // 关闭修改用户对话框之前的事件回调函数
    closechangeUserDialog () {
      this.$refs.changeUserFormRef.resetFields() // 重置表单数据及表单验证结果
    },
    // 添加用户对话框确定按钮点击事件
    btnAddUserDialog () {
      delete this.addUserForm.checkPwd // 作为请求参数前删除不要的参数
      this.$refs.addUserFormRef.validate(async result => {
        if (result) {
          const { data: res } = await this.$http.post(`users`, this.addUserForm)
          if (res.meta.status !== 201) {
            this.$message.error(res.meta.msg)
            this.$refs.addUserFormRef.resetFields()
          } else {
            this.$message.success(res.meta.msg)
            this.$refs.addUserFormRef.resetFields()
            this.getUserList()
          }
        }
      }
      )
    },
    // 添加用户对话框"重置"按钮点击事件
    resetAddUserDialog () {
      this.$refs.addUserFormRef.resetFields()
    },
    // 修改用户对话框'确定'按钮点击事件
    changeUser () {
      // 修改前使用input规则进行预验证
      this.$refs.changeUserFormRef.validate(async result => {
        if (result) {
          const { data: res } = await this.$http.put(`users/${this.changeUserForm.id}`, { email: this.changeUserForm.email, mobile: this.changeUserForm.mobile })
          if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
          this.$message.success(res.meta.msg)
          let index = this.userList.findIndex(item => item.id === this.changeUserForm.id)
          this.userList[index].email = res.data.email
          this.userList[index].mobile = res.data.mobile
          this.changeUserDialogVisible = false
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>

</style>
