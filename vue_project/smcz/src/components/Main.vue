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
              @node-click ="nodeClick"
              :highlight-current ='true'
              node-key="compid"
              current-node-key="0"
              ref="tree">
            </el-tree>
          </el-card>
        </el-aside>
        <el-main>
          <el-card :style = bodyClientHeight>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="Ukey管理" name="ukeyManage"></el-tab-pane>
              <el-tab-pane label="单位记录查询" name="recordByCompany"></el-tab-pane>
              <el-tab-pane label="Ukey记录查询" name="recordByUkey"></el-tab-pane>
            </el-tabs>
            <router-view></router-view>
          </el-card>
        </el-main>
      </el-container>
    </el-container>
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
      activeName: 'ukeyManage'
    }
  },
  beforeCreate () {
    this.$store.dispatch('getComTreeLis') // 出发需要调用得VUEx Action中得函数
  },
  created () { // 生命周期函数,页面加载完调用该方法
    this.bodyClientHeight.height = document.body.clientHeight - 142 + 'px' // 获取当前body高度
  },
  computed: {
    ...mapState(['companyData', 'ukeyData', 'isTab'])
  },
  watch: {
    filterText (newVlaue) {
      this.$refs.tree.filter(newVlaue)
    },
    isTab () {
      this.$refs.tree.setCurrentKey(0)
    }
  },
  mounted () {
    this.$router.push('/main')
    this.$store.dispatch('setIsTab') // 改变store.state中isTab属性的状态，从而触发Main.vue中watch中的isTa()
  },
  methods: {
    // data 为tree组件传递给data属性的值,value为watch属性中filterText方法中的newvalue
    filterNode (value, data) {
      if (!value) return true
      console.log(data)
      return data.compname.indexOf(value) !== -1
    },
    nodeClick (obj) {
      console.log(obj)
      if (obj.levelid === 1) {
        this.$message.error('请选择正确的单位名称')
      } else {
        this.$store.dispatch('setCurrentCompany', obj)
        this.$store.dispatch('getUkeyList', obj.compid)
      }
    },
    handleClick (tab) {
      if (tab.name === 'ukeyManage') {
        this.$router.push('/main/list')
      } else if (tab.name === 'recordByCompany') {
        this.$router.push('/main/recordByCompany')
      } else if (tab.name === 'recordByUkey') {
        this.$router.push('/main/recordByUkey')
      }
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
.el-tooltip{
  margin-left: 10px;
}
</style>
