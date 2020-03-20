import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/components/Login.vue'
import Home from '../views/components/Home.vue'
import Welcome from '../views/components/Welcome.vue'
import Users from '../views/components/users/Users.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/home',
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome', component: Welcome },
      { path: '/users', component: Users }
    ]
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  // 导航守卫
  // to:表示要访问的页面 from:表示从哪个页面来 next() 表示允许跳转的页面  无参数表示放行 有参数表示需要挑战到的具体页面
  if (to.path === '/login') return next()
  if (to.path !== '/login') {
    const token = window.sessionStorage.getItem('token')
    if (!token) {
      next('/login')
    } else {
      next()
    }
  }
})
export default router
