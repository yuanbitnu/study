export default {
	storageUserInfo({commit},userInfo){
		commit('storageUserInfo',{userInfo})
	},
	setHasLogin({commit},isLogin){
		commit('setHasLogin',{isLogin})
	}
}