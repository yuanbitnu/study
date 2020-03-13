<template>
  <div class="loginMain">
    <div class="login_box">
      <div class="logoImg">
        <img src="../../assets/logo.png" alt="logo" />
      </div>
      <el-form
        ref="loginFormRef"
        label-width="0px"
        class="loginForm"
        :model="loginForm"
        :rules="loginRules"
      >
        <el-form-item prop="username">
          <el-input
            placeholder="请输入用户名"
            prefix-icon="iconfont icon-yonghu"
            v-model="loginForm.username"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            placeholder="请输入密码"
            prefix-icon="iconfont icon-mima"
            v-model="loginForm.password"
            @keyup.enter.native="loginBtn"
          ></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="primary" @click="loginBtn">登录</el-button>
          <el-button type="info" @click="loginFromReset">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      // 表单数据绑定
      loginForm: {
        username: 'admin',
        password: '123456'
      },
      // 表单验证规则对象
      loginRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
<<<<<<< HEAD
          { min: 3, max: 5, message: '长度在 3-5 个字符', trigger: 'blur' }
=======
          { min: 3, message: '最短 3 个字符', trigger: 'blur' }
>>>>>>> a95a82a66dd7af3d0c0579e4b191463633e1d7e7
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 12, message: '密码长度在6-12个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    loginBtn () {
      this.$refs.loginFormRef.validate(async result => {
        if (result) {
          const { data: result } = await this.$http.post('login', this.loginForm)
          if (result.meta.status === 200) {
            this.$message({
              message: '登陆成功',
              type: 'success'
            })
            // 登录成功后需要将服务器返回的token值写入到客户端的sessionStorage中,为登录后的后续操作提供token值
            window.sessionStorage.setItem('token', result.data.token)
            this.$router.push('/home')
          } else {
            this.$message({
              message: '登录失败',
              type: 'error'
            })
          }
        } else {
          return false
        }
      })
    },
    loginFromReset () {
      this.$refs.loginFormRef.resetFields()
    }
  }
}
</script>

<style lang="less" scoped>
.loginMain {
  background-color: #2b4b6b;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.logoImg {
  width: 130px;
  height: 130px;
  border: 1px solid #eee;
  border-radius: 50%;
  padding: 10px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  box-shadow: 0 0 10px #ddd; //阴影
  img {
    height: 100%;
    width: 100%;
    border-radius: 50%;
    background-color: #eee;
  }
}
.btns {
  display: flex;
  justify-content: flex-end; //flex布局中指定x轴方向上的元素排列,flex-end(右对齐)
}
.loginForm {
  position: absolute;
  bottom: 0; //绝对定位中定位在左下角
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box; //为元素指定的任何内边距和边框都会在指定的width和height内进行绘制,元素内容的尺寸会从已经设定的高宽中减去border和padding
}
</style>
