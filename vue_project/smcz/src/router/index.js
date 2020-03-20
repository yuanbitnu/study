import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Main from '../components/Main.vue'
import List from '../components/subMian/List.vue'
import Setting from '../components/Setting.vue'
import RecordByCompany from '../components/subMian/RecordByCompany.vue'
import RecordByUkey from '../components/subMian/RecordByUkey.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    redirect: '/main/list',
    children: [
      { path: '/main/list', name: 'List', component: List },
      { path: '/main/recordByCompany', name: 'RecordByCompany', component: RecordByCompany },
      { path: '/main/recordByUkey', name: 'RecordByUkey', component: RecordByUkey }
    ]
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
