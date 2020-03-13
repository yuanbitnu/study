import Vue from 'vue'
/* import App from './App.vue' */
import router from './router/index.js'
import MyApp from './MyApp.vue'

Vue.config.productionTip = false

new Vue({
  router,
  /* render: h => h(App) */
  render: h => h(MyApp)
}).$mount('#app')
