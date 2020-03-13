export default {
	storageUserInfo(state,{userInfo}){
		state.userInfo = userInfo
	},
	setHasLogin(state,{isLogin}){
		state.hasLogin = isLogin
	}
}