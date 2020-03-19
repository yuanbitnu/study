import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import List from '../components/List.vue'
import Setting from '../components/Setting.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/list',
    name: 'List',
    component: List
  },
  {
    path: '/setting',
    name: 'Setting',
    component: Setting
  }
]

const router = new VueRouter({
  routes
})

export default router
