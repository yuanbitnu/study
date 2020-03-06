import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/css/global.css'
import './assets/font/iconfont.css'
import './assets/font/iconfont.js'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8888/api/private/v1/' // 为axios指定默认的URL

axios.interceptors.request.use(config => { // 使用axios的request拦截器 为请求头添加'token'属性及值,axios在每次请求时会自动调用该拦截器,相当于请求前的预处理
  config.headers.Authorization = window.sessionStorage.getItem('token')
  return config
})
Vue.config.productionTip = false
Vue.prototype.$http = axios // axios需要挂载到Vue的原型上

new Vue({
  router,
  render: h => h(App)
}).$mount('#app') // 如果VUE在实例化的时候没有收到'el'选项,则处于未挂载状态,可以使用vm.$mount()手动挂在一个未挂载的实例
