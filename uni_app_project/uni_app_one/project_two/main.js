import Vue from 'vue'
import App from './App'
import store from './store/index.js'

import vusLayerInit from './components/vusui-app-layer/vusui-layer.js'
import vusLayer from './components/vusui-app-layer/vusui-layer.vue'
import uniCard from '@/components/uni-card/uni-card.vue'
import uniIcons from './components/uni-icons/uni-icons.vue'
import uniList from "@/components/uni-list/uni-list.vue"
import uniListItem from "@/components/uni-list-item/uni-list-item.vue"

Vue.use(vusLayerInit)
Vue.component('vus-layer', vusLayer)//设置组件名称
Vue.component('uni-card',uniCard)
Vue.component('uni-icons',uniIcons)
Vue.component('uni-list',uniList)
Vue.component('uni-list-item',uniListItem)

Vue.config.productionTip = false

App.mpType = 'app'
// Vue.prototype.$store = store

const app = new Vue({
    ...App,
	store
})
app.$mount()
