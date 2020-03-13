<template>
  <el-container>
    <el-header height="100px">
      <div class="logoImg">
        <img src="../../assets/img/heima.png" alt="logo" />
        <span>电商后台管理系统</span>
      </div>
      <el-button size="small" type="info" @click="logout">退出登录</el-button>
    </el-header>
    <el-container>
<<<<<<< HEAD
      <el-aside width="350px">
        <el-menu
          :default-active="activeIndex"
          @open="handleOpen"
          @close="handleClose"
          background-color="#313743"
          text-color="#fff"
          active-text-color="#ffd04b"
          :unique-opened= "isUniqueOpen"
          :default-openeds = 'defaultOpens'
        >
          <el-submenu index="1">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-usergroup"></use>
              </svg>
              <span>用户管理</span>
            </template>
            <el-menu-item index="1-1-1" >
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
            </el-menu-item>
            <el-menu-item index="1-2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-permission"></use>
              </svg>
              <span>权限管理</span>
            </template>
              <el-menu-item index="2-1">
                <template slot="title">
                  <i class="el-icon-menu"></i>
                  <span>item一</span>
                </template>
              </el-menu-item>
              <el-menu-item index="2-2">
                <template slot="title">
                  <i class="el-icon-menu"></i>
                  <span>item一</span>
                </template>
              </el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-goodsmanagement"></use>
              </svg>
              <span>商品管理</span>
            </template>
            <el-menu-item index="3-1">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
            </el-menu-item>
            <el-menu-item index="3-2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
            </el-menu-item>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-6"></use>
              </svg>
              <span>订单管理</span>
            </template>
              <el-menu-item index="4-1">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
              </el-menu-item>
              <el-menu-item index="4-2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
              </el-menu-item>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">
              <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-kujialeqiyezhan_shujutongji"></use>
              </svg>
              <span>数据统计</span>
            </template>
            <el-menu-item index="5-1">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
              </template>
            </el-menu-item>
            <el-menu-item index="5-2">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>item一</span>
=======
      <el-aside :width="iscollapse ? '80px':'350px'">
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
              <span>{{menu.authName}}</span>
            </template>
            <el-menu-item :index="'/' +item.path + ''" v-for="item in menu.children" :key ="item.id">
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{item.authName}}</span>
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
<<<<<<< HEAD
      <el-main>Main</el-main>
=======
      <el-main>
        <router-view></router-view>
      </el-main>
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      activeName: '',
<<<<<<< HEAD
      activeIndex: '1',
      isUniqueOpen: true,
      defaultOpens: ['1']
    }
  },
  methods: {
    handleOpen (index, indexPath) {
      console.log(index, indexPath)
    },
    handleClose (index, indexPath) {
      console.log(index, indexPath)
=======
      /* isUniqueOpen: true, */
      iscollapse: false,
      defaultOpens: ['125'],
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
  },
  methods: {
    async getMenuList () {
      const { data: res } = await this.$http.get('menus')
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      this.menuList = res.data
    },
    menuCollClick () {
      this.iscollapse = !this.iscollapse
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
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
<<<<<<< HEAD
=======
.menuCollapse{
  text-align: center;
  line-height: 21px;
  font-size: 10px;
  color: #fff;
  background-color: #4C718C;
  cursor: pointer;
}
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
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
<<<<<<< HEAD
  .el-submenu{
    margin-top: 20px
;  }
  svg{
    padding-left: 20px;
=======
  border-right: none;
  .el-submenu{
    margin-top: 20px;
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
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
<<<<<<< HEAD
  color: #333;
  text-align: center;
  line-height: 160px;
=======
/*   color: #333;
  text-align: center;
  line-height: 160px; */
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
}
body > .el-container {
  margin-bottom: 40px;
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
