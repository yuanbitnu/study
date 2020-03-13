import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Setting from '../components/Setting.vue'
import Company from '../components/settings/Company.vue'
import CompanyManage from '../components/settings/CompanyManage.vue'
import CompanyRelationship from '../components/settings/CompanyRelationship.vue'
import UkeyManage from '../components/settings/UkeyManage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/setting',
    name: 'Setting',
    component: Setting,
    children: [
      { path: '/company', component: Company },
      { path: '/companyManage', component: CompanyManage },
      { path: '/companyRelationship', component: CompanyRelationship },
      { path: '/ukeyManage', component: UkeyManage }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
