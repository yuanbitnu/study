<template>
    <div id="users">
        <h1>用户列表</h1>
        <table>
          <thead>
            <tr>
              <th>Id</th>
              <th>用户名</th>
              <th>密码</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for = "(item, index) in userList" :key="index">
              <td>{{item.id}}</td>
              <td>{{item.name}}</td>
              <td>{{item.pwd}}</td>
              <td><a href="javascript:;" @click="goUserInfo(item.id)">详情</a></td>
            </tr>
          </tbody>
        </table>
    </div>
</template>
<script>
export default {
  name: 'users',
  data () {
    return {
      userList: [
        { id: 1, name: 'tom', pwd: '12' },
        { id: 2, name: 'jack', pwd: '23' },
        { id: 3, name: 'jarry', pwd: '15' },
        { id: 4, name: 'cat', pwd: '54' }
      ]
    }
  },
  methods: {
    goUserInfo (id) {
      this.$router.push('/users/userInfo/' + id)
    }
  }
}
</script>
