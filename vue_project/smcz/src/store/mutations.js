// 包含多个由action触发去直接更新状态的方法的对象
import { GETCOMTREELIS, SETCURRENTCOMPANY, GETUKEYLIST } from './mutation_types'
export default {
  [GETCOMTREELIS] (state, { data, meta }) {
    state.companyData.companyLis = data
    state.companyData.meta = meta
  },
  [SETCURRENTCOMPANY] (state, { obj }) {
    state.currentCompanyInfo = obj
  },
  [GETUKEYLIST] (state, { data, meta }) {
    state.ukeyData.ukeyLis = data
    state.ukeyData.meta = meta
  }
}
