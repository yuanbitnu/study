<template>
	<view class="content">
		<view class="header">
			<image class="userImg" :src="imgSrc" mode=""></image>
			<button v-if="!hasLogin" class="loginbtn" type="default" size="mini" plain="true" @click="login">点击登录</button>
			<text class="nickName" v-if="hasLogin">{{userInfo.nickName}}</text>
			<vus-layer></vus-layer>
		</view>
		<view class="listMenu">
			<view class="order">
				<uni-list >
				    <uni-list-item title="我的订单" :show-extra-icon="true" :extra-icon="{color: '#4cd964',size: '22',type: 'cart'}"></uni-list-item>
				</uni-list>
			</view>
			<view>
				<view>
					<svg class="icon" aria-hidden="true">
					  <use xlink:href="#icon-daifukuan"></use>
					</svg>
					<text>代付款</text>
				</view>
				<view></view>
				<view></view>
				<view></view>
			</view>
			<view class="list">
				
			</view>
		</view>
	</view>
</template>
<script src="./iconfont.js"></script>
<script>
	import {mapState,mapGetters,mapActions} from 'vuex'
	export default {
		data() {
			return {
				title: this.$store.state.myGander,
				imgSrc:'../../static/logo.png',
			}
		},
		onLoad() {
			
		},
		methods: {
			...mapActions(['storageUserInfo','setHasLogin']),
			login(){
				if (!this.hasLogin){
					console.log(111)
					uni.getProvider({
						service:'oauth',
						success: (res) => {
							console.log(res)
							if(res.provider.includes('weixin')){
								uni.getUserInfo({
									provider:'weixin',
									success: (res) => {
										this.vusui.msg('登录成功',{
											anim:0,
											icon:['0','color:#4CD964;'],
											time:1000
										})
										this.imgSrc = res.userInfo.avatarUrl
										this.storageUserInfo(res.userInfo)
										uni.setStorage({
											key:'localSession',
											data:'123456',
											success: () => {
												this.setHasLogin(!this.hasLogin)
												console.log(this.userInfo)
											}
										})
									},
									fail: (res) => {
										console.log('login fail')
									},
								})
							}
						}
					})
				}
			}
		},
		computed:{
			...mapState(['hasLogin','userInfo'])
		}
	}
</script>

<style lang="scss">
	.header{
		width: 100%;
		height: 230rpx;
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
		margin-top: 50rpx;
		.userImg{
			border-radius: 50%;
			width: 120rpx;
			height: 120rpx;
		}
		.loginbtn{
			margin: 30rpx;
			// border: 1rpx solid #C8C7CC;
			height: 50rpx;
			width: 160rpx;
			font-size: 20rpx;
			line-height: 50rpx;
			letter-spacing: 5rpx;
		}
		.nickName{
			margin-top: 30rpx;
		}
	}
    .listMenu{
		margin-top: 30rpx;
		width: 100%;
		.order{
			width: 100%;
		}
	}
	

	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: #F1F1F1;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
	.input {
		width: 100rpx;
		height: 100rpx;
		border: #007AFF 1rpx solid;
	}
	
</style>
