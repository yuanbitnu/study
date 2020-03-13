<template>
    <div>
        <!-- 面包屑导航区域 -->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/setting' }">设置</el-breadcrumb-item>
            <el-breadcrumb-item>单位管理</el-breadcrumb-item>
            <el-breadcrumb-item>单位维护</el-breadcrumb-item>
        </el-breadcrumb>
        <!-- 卡片容器区域 -->
        <el-card class="box-card">
            <el-row :gutter = '20'>
                <el-col :span="8">
                    <el-input placeholder="请输入内容"
                    v-model="queryInfo.query"
                    @clear="getCompanInfoList"
                    clearable>
                    <el-button slot="append"
                    @click="getCompanInfoList"
                    icon="el-icon-search"></el-button>
                    </el-input>
                </el-col>
                <el-col :span="4">
                  <el-button type="primary" @click="addCompanyDialogVisible = true">添加用户</el-button>
                </el-col>
            </el-row>
            <!-- 用户列表区域 -->
            <el-table :data="companyInfoList"
                    border
                    stripe
                    style="width: 100%">
              <!-- <el-table-column type="index"
                              width='80'
                              align='center'
                              header-align='center'
                              label='序号'>
              </el-table-column> -->
              <el-table-column prop="C_ID"
                              label="ID"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <el-table-column prop="C_NAME"
                              label="单位名称"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <el-table-column prop="MC_NAME"
                              label="管口股室"
                              align='center'
                              header-align='center'
                              minWidth="100">
              </el-table-column>
              <!-- 为当前模板指定了作用域插槽后,作用域插槽的内容会覆盖prop属性值,因此prop属性可以不进行设置 -->
              <el-table-column
                              label="操作"
                              align='center'
                              header-align='center'
                              minWidth="100">
                  <template v-slot:default='slotScope'>
                      <el-row>
                        <el-button type="primary" icon="el-icon-edit" circle @click="showChangeUserDialog(slotScope.row.C_ID)"></el-button>
                        <el-button type="danger" icon="el-icon-delete" circle @click="openDelUserMessageBox(slotScope.row.C_ID)"></el-button>
                        <!-- <el-tooltip content="权限设置" placement="top" :enterable='false'>
                          <el-button type="warning" icon="el-icon-setting" circle @click="changeUserRole(slotScope.row.id)"></el-button>
                        </el-tooltip> -->
                      </el-row>
                  </template>
              </el-table-column>
            </el-table>
            <!-- 分页区域 -->
            <!-- <el-pagination
                          @size-change="handleSizeChange"
                          @current-change="handleCurrentChange"
                          :current-page="queryInfo.pagenum"
                          :page-sizes="pagesizes"
                          :page-size="pagesizes[0]"
                          layout="total, sizes, prev, pager, next, jumper"
                          :total="userTotal">
            </el-pagination> -->
        </el-card>
    </div>
</template>

<script>
export default {
  data () {
    return {
      queryInfo: {
        query: ''
      },
      companyInfoList: [],
      addCompanyDialogVisible: false
    }
  },
  created () {
    this.getCompanInfoList()
  },
  mounted () {
    console.log(this.companyInfoList)
  },
  methods: {
    async getCompanInfoList () {
      const { data: res } = await this.$http.get('/companys')
      if (res.meta.status !== '1000') return this.$message.error(res.meta.msg)
      this.companyInfoList = res.data
      console.log(this.companyInfoList)
    },
    showChangeCompanyDialog (id) {
    },
    openDelUserMessageBox (id) {
    }
  }
}
</script>

<style lang="less" scoped>

</style>
