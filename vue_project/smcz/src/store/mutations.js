// 包含多个由action触发去直接更新状态的方法的对象
import { GETCOMTREELIS } from './mutation_types'
export default {
  [GETCOMTREELIS] (state, { data, meta }) {
    state.companyData.companyLis = data
    state.companyData.meta = meta
  }
}
