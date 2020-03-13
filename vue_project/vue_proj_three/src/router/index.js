import Vue from 'vue'
import VueRouter from 'vue-router'
/* import Home from '../views/Home.vue' */
import users from '../components/users.vue'
import power from '../components/power.vue'
import goods from '../components/goods.vue'
import order from '../components/order.vue'
import system from '../components/system.vue'
import userInfo from '../components/userInfo.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: users
  },
  {
    path: '/users',
    name: 'users',
    component: users
  },
  {
    path: '/power',
    name: 'power',
    component: power
  },
  {
    path: '/goods',
    name: 'goods',
    component: goods
  },
  {
    path: '/order',
    name: 'order',
    component: order
  },
  {
    path: '/system',
    name: 'system',
    component: system
  },
  {
    path: '/users/userInfo/:id',
    name: 'userInfo',
    component: userInfo,
    props: true
  }
]

const router = new VueRouter({
  routes
})

export default router
