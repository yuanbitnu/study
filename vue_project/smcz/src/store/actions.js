// 包含多个接收组件 通知触发 mutation中的调用 间接更新状态的方法 的对象
import { GETCOMTREELIS, SETCURRENTCOMPANY, GETUKEYLIST, SETISTAB } from './mutation_types'
import axios from 'axios'

export default {
  // 异步连接数据库取数
  async getComTreeLis ({ commit }) {
    const { data: res } = await axios.get('/companys')
    var data = []
    var meta = {}
    if (res.meta.status !== 1000) {
      meta = res.meta
    } else {
      data = res.data
      meta = res.meta
    }
    // 触发mutations中的方法
    commit(GETCOMTREELIS, { data, meta })
  },
  setCurrentCompany ({ commit }, obj) {
    commit(SETCURRENTCOMPANY, { obj })
  },
  async getUkeyList ({ commit }, companyId = null) {
    if (companyId == null) {
      const { data: res } = await axios.get('/ukeys')
      var data = []
      var meta = {}
      if (res.meta.status !== 1000) {
        meta = res.meta
      } else {
        data = res.data
        meta = res.meta
      }
    } else {
      const { data: res } = await axios.get('/ukeys', {
        params: {
          companyId: companyId
        }
      })
      if (res.meta.status !== 1000) {
        meta = res.meta
      } else {
        data = res.data
        meta = res.meta
      }
    }
    commit(GETUKEYLIST, { data, meta })
  },
  setIsTab ({ commit }) {
    commit(SETISTAB)
  }
}
