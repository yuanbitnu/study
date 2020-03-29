<template>
    <div>
      <el-collapse accordion>
        <el-collapse-item v-for="(role, index) in roleData.roleLis" :name="role.r_id" :key="index">
            <template slot="title">
              <i class="header el-icon-user"></i> {{role.r_name}}
            </template>
            <el-timeline>
              <el-timeline-item v-for="(item, index) in activities" :timestamp="item.time" placement="top" :key="index" :type="item.type" color = "#0bbd87" :size="item.size">
                <el-card>
                  <h4>{{item.operation}}Ukey:{{item.ukeyId}}</h4>
                  <p>申请人: {{item.propors}}</p>
                </el-card>
              </el-timeline-item>
            </el-timeline>
        </el-collapse-item>
      </el-collapse>
    </div>
</template>
<script>
import { mapState } from 'vuex'
export default {
  data () {
    return {
      activities: [
        {
          id: '1',
          size: 'large',
          type: 'primary',
          ukeyId: '4001',
          name: '陈平安',
          propors: '陈平安',
          operation: '注册',
          content: '注册主管陈平安的Ukey',
          time: '2020-02-20'
        },
        {
          id: '2',
          size: 'large',
          type: 'primary',
          ukeyId: '4000',
          name: '张三',
          propors: '陈平安',
          operation: '销毁',
          content: '销毁主管张三的Ukey',
          time: '2020-01-13'
        },
        {
          id: '3',
          size: 'large',
          type: 'primary',
          ukeyId: '4000',
          name: '张三',
          propors: '李四',
          operation: '注册',
          content: '张三领取主管Ukey',
          time: '2019-12-31'
        }
      ],
      roleData: {
        roleLis: [],
        meta: {}
      }
    }
  },
  beforeCreate () {
  },
  created () {
  },
  computed: {
    ...mapState(['currentCompanyInfo'])
  },
  methods: {
    async getRoleLis () {
      const { data: res } = await this.$http.get('/roles')
      if (res.meta.status !== 1000) {
        this.roleData.meta = res.meta
        this.$message.error(res.meta.msg)
      } else {
        this.roleData.roleLis = res.data
        this.roleData.meta = res.meta
        this.$message.success(res.meta.msg)
      }
    }
  }
}
</script>
<style lang="less" scoped>
.el-collapse-item{
  font-size: 18px;
}
</style>
