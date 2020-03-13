<template>
  <div>
    <el-container>
      <el-header height="100px">
        <div class="logoImg">
          <img src="../assets/logo.png" alt="logo" />
          <span>石门财政Ukey后台管理</span>
        </div>
        <el-button size="small" type="info" @click="logout">退出登录</el-button>
      </el-header>
      <el-container>
        <el-aside width="350px" >
          <el-card :style = bodyClientHeight>
            <el-input placeholder="输入关键字进行过滤" v-model="filterText"></el-input>
            <el-tree
              class="filter-tree"
              :data="companyData.companyLis"
              :props="defaultProps"
              default-expand-all
              :filter-node-method="filterNode"
              :expand-on-click-node = "false"
              @node-click = "nodeClick"
              :highlight-current = 'true'
              ref="tree">
            </el-tree>
          </el-card>
        </el-aside>
        <el-main>
          <el-card :style = bodyClientHeight>
            <el-page-header @back="goBack" content="详情页面"></el-page-header>
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
                  <el-col :span="4">
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
                <el-table-column prop="ownermobilee"
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
                                minWidth="100">
                    <template v-slot:default='slotScope'>
                        <el-row>
                          <el-button type="primary" icon="el-icon-edit" circle @click="showChangeUserDialog(slotScope.row)"></el-button>
                          <el-button type="danger" icon="el-icon-delete" circle @click="openDelUserMessageBox(slotScope.row.C_ID)"></el-button>
                          <!-- <el-tooltip content="权限设置" placement="top" :enterable='false'>
                            <el-button type="warning" icon="el-icon-setting" circle @click="changeUserRole(slotScope.row.id)"></el-button>
                          </el-tooltip> -->
                        </el-row>
                    </template>
                </el-table-column>
              </el-table>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
    <!-- 添加ukey对话框 -->
    <el-dialog title="添加角色" :visible.sync="ukeyDialogFormVisible">
      <el-form :model="ukeyForm">
        <el-form-item label="ukeyId" :label-width="formLabelWidth">
          <el-input v-model="ukeyForm.ukeyId" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="岗位" :label-width="formLabelWidth">
          <el-select v-model="ukeyForm.roleId" placeholder="请选择岗位">
            <el-option v-for=" item in roleData.roleLis"
            :key="item.r_id"
            :label="item.r_name"
            :value="item.r_id">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth">
          <el-input v-model="ukeyForm.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="电话" :label-width="formLabelWidth">
          <el-input v-model="ukeyForm.mobile" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="身份证号码" :label-width="formLabelWidth">
          <el-input v-model="ukeyForm.carNum" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="单位名称" :label-width="formLabelWidth">
          <el-input v-model="currentCompanyInfo.companyname" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="启用状态" :label-width="formLabelWidth">
          <el-switch
            v-model="ukeyForm.isUse"
            @change='isUseStateChanged(ukeyForm.isUse)'
            active-color="#13ce66"
            inactive-color="#ff4949">
          </el-switch>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="ukeyDialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="ukeyDialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data () {
    return {
      bodyClientHeight: { // 为el-aside组件设置高度样式，以撑满整个浏览器
        height: ''
      },
      filterText: '',
      defaultProps: {
        children: 'children',
        label: 'compname'
      },
      queryInfo: {
        query: ''
      },
      ukeyData: {
        ukeyLis: [],
        meta: {}
      },
      roleData: {
        roleLis: [],
        meta: {}
      },
      ukeyDialogFormVisible: false,
      ukeyForm: {
        ukeyId: null,
        roleId: null,
        name: '',
        mobile: '',
        carNum: '',
        companyNum: null,
        useTime: '',
        unuseTiem: '',
        isUse: true,
        idDestroy: false
      },
      formLabelWidth: '120px',
      currentCompanyInfo: {}
    }
  },
  created () { // 生命周期函数,页面加载完调用该方法
    this.bodyClientHeight.height = document.body.clientHeight - 142 + 'px' // 获取当前body高度
    this.$store.dispatch('getComTreeLis') // 出发需要调用得VUEx Action中得函数
    this.getUkeyList(0)
  },
  computed: {
    ...mapState(['companyData'])
  },
  watch: {
    filterText (newVlaue) {
      this.$refs.tree.filter(newVlaue)
    }
  },
  mounted () {
  },
  methods: {
    async getRoleLis () {
      const { data: res } = await this.$http.get('/roles')
      if (res.meta.status !== 1000) {
        this.roleData.meta = res.meta
      } else {
        this.roleData.roleLis = res.data
        this.roleData.meta = res.meta
      }
    },
    isUseStateChanged (isUse) {
      isUse = !isUse
    },
    // data 为tree组件传递给data属性的值,value为watch属性中filterText方法中的newvalue
    filterNode (value, data) {
      if (!value) return true
      console.log(data)
      return data.compname.indexOf(value) !== -1
    },
    async getUkeyList (compayId = null) {
      if (compayId == null) {
        const { data: res } = await this.$http.get('/ukeys')
        if (res.meta.status !== 1000) {
          this.ukeydata.meta = res.meta
        } else {
          this.ukeyData.ukeyLis = res.data
          this.ukeyData.meta = res.meta
        }
      } else {
        const { data: res } = await this.$http.get('/ukeys', {
          params: {
            compayId: compayId
          }
        })
        if (res.meta.status !== 1000) {
          this.ukeydata.meta = res.meta
        } else {
          this.ukeyData.ukeyLis = res.data
          this.ukeyData.meta = res.meta
        }
      }
    },
    nodeClick (obj) {
      this.getUkeyList(obj.compid)
      this.currentCompanyInfo = obj
      console.log(this.currentCompanyInfo)
    },
    goBack () {
      this.$router.push('/')
    },
    getUkeyRecordList () {

    },
    addUkeyDialogVisible () {
      this.getRoleLis()
      this.ukeyDialogFormVisible = true
    },
    showChangeUserDialog (obj) {
      console.log(obj)
    },
    logout () {
      window.sessionStorage.removeItem('token')
      this.$router.push('/login')
      const token = window.sessionStorage.getItem('token')
      if (!token) {
        this.$message({
          message: '退出登录',
          type: 'success'
        })
      }
    }
  }
}
</script>

<style lang="less" scoped>
.el-header {
  background-color:#363d40;
  color: #e9edf1;
  font-size: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 0px;
  div {
    display: flex;
    align-items: center;
    img{
      height: 100px;
      width: 100px;
    }
  }
  span {
    padding-left: 10px;
  }
  .logoutBtn {
    size: small;
  }
}
.el-aside {
  background-color: #e9edf1;
  color: #e9edf1;
  .el-card{
    margin-top: 20px;
  }
}
.el-tree{
  // background-color:rgb(168, 176, 225);
  // box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
}
.el-main {
  background-color: #e9edf1;
/*   color: #333;
  text-align: center;
  line-height: 160px; */
  height: 100%;
  .el-card{
    .el-page-header{
      margin-bottom: 20px;
    }
  }
}
body > .el-container {
  margin-bottom: 40px;
  height: 100%;
}
.el-container {
  height: 100%;
}
</style>
