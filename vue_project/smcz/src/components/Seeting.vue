<template>
  <el-container>
    <el-header height="100px">
      <div class="logoImg">
        <img src="../assets/logo.png" alt="logo" />
        <span>石门财政Ukey后台管理</span>
      </div>
      <el-button size="small" type="info" @click="logout">退出登录</el-button>
    </el-header>
    <el-container>
      <el-aside :width="iscollapse ? '80px':'350px'" :style= "bodyClientHeight">
        <div class="menuCollapse" @click="menuCollClick">|||</div>
        <el-menu
          :default-active="$route.path"
          background-color="#313743"
          text-color="#fff"
          active-text-color="#0078D7"
          :unique-opened= "true"
          :default-openeds = 'defaultOpens'
          :router = 'true'
          :collapse-transition = 'false'
          :collapse = 'iscollapse'
        >
          <el-submenu :index="'/' + menu.path" v-for="menu in menuList" :key="menu.id">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use :xlink:href="iconsList[menu.id]"></use>
              </svg>
              <span>{{menu.menuName}}</span>
            </template>
            <el-menu-item :index="'/' +item.path + ''" v-for="item in menu.children" :key ="item.id">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{item.menuName}}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      bodyClientHeight: { // 为el-aside组件设置高度样式，以撑满整个浏览器
        height: ''
      },
      activeName: '',
      /* isUniqueOpen: true, */
      iscollapse: false,
      defaultOpens: ['100'],
      menuList: [],
      iconsList: {
        125: '#icon-usergroup',
        103: '#icon-permission',
        101: '#icon-goodsmanagement',
        102: '#icon-6',
        145: '#icon-kujialeqiyezhan_shujutongji'
      }
    }
  },
  created () { // 生命周期函数,页面加载完调用该方法
    this.getMenuList()
    this.bodyClientHeight.height = document.body.clientHeight - 100 + 'px' // 获取当前body高度
  },
  methods: {
    async getMenuList () {
      const { data: res } = await this.$http.get('/menus')
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      this.menuList = res.data
      console.log(res.data)
    },
    menuCollClick () {
      this.iscollapse = !this.iscollapse
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
.menuCollapse{
  text-align: center;
  line-height: 21px;
  font-size: 10px;
  color: #fff;
  background-color: #4C718C;
  cursor: pointer;
}
.icon {
  width: 2em;
  height: 2em;
  vertical-align: middle;
  fill: currentColor;
  overflow: hidden;
}
.icon_nex_levl {
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  fill: currentColor;
  overflow: hidden;
}
.el-menu{
  border-right: none;
  .el-submenu{
    margin-top: 20px;
  }
  span{
    font-size: 18px;
    padding-left: 14px;
  }
  .el-menu-item{
    i{
      font-size: 1.5em;
      padding-left: 25px;
    }
  }
}
.el-header {
  background-color: #363d40;
  color: #e9edf1;
  font-size: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 0px;
  div {
    display: flex;
    align-items: center;
  }
  span {
    padding-left: 10px;
  }
  .logoutBtn {
    size: small;
  }
}
.el-aside {
  background-color: #313743;
  color: #e9edf1;
}
.el-main {
  background-color: #e9edf1;
/*   color: #333;
  text-align: center;
  line-height: 160px; */
  height: 100%;
}
body > .el-container {
  margin-bottom: 40px;
  height: 100%;
}
.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}
.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.el-container {
  height: 100%;
}
</style>
