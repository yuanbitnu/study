<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div id="nav">
      <router-link to="/about/tab_one">tab_one</router-link> |
      <router-link :to= "{ name: 'tab_two', params: {id: 9} }" >tab_two</router-link> |
      <router-link to="/about/1" >user1</router-link> |
      <router-link to="/about/2" >user2</router-link> |
      <router-link to="/about/7" >user3</router-link>
      <router-view />
    </div>

  </div>
</template>

<script>
// eslint-disable-next-line camelcase
import tab_one from '../components/tab_one.vue'
// eslint-disable-next-line camelcase
import tab_two from '../components/tab_two.vue'
import user from '../components/user.vue'
export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    tab_one,
    // eslint-disable-next-line vue/no-unused-components
    tab_two,
    // eslint-disable-next-line vue/no-unused-components
    user
  }
}
</script>

<style>
.about {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
