import $ from 'jquery'
import './css/index.css'
import './css/index.less'
import './css/index.scss'

$(function(){
    $('li:odd').css('backgroundColor','blue')
    $('li:even').css('backgroundColor','red')
})
//----------------------------------------------------
import App from './components/App.vue'
import Vue from 'vue'

const vm = new Vue({
    el:'#vue',
    date:{

    },
    render: (creatEle) => creatEle(App),
})