<template>
    <div id="userInfo">
        <h1>用户ID:{{id}}</h1>
        <button @click="backUsers">返回用户列表</button>
    </div>
</template>
<script>
export default {
  name: 'userInfo',
  props: ['id'],
  methods: {
    backUsers () {
      this.$router.go(-1)
    }
  }
}
</script>
