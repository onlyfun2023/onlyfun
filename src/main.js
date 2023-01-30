/*
 * @Author: gerrardlt 305690790@qq.com
 * @Date: 2023-01-12 14:01:22
 * @LastEditors: gerrardlt 305690790@qq.com
 * @LastEditTime: 2023-01-29 03:46:49
 * @FilePath: \quhu\src\main.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './utils/element.js'
// 导入字体图标
import './assets/fonts/iconfont.css'
import '@/assets/index'
// 导入全局样式表
import './assets/css/global.css'
import TreeTable from 'vue-table-with-tree-grid'
import store from './store'
import axios from 'axios'
import Web3 from 'web3'

// 引入quill-editor编辑器
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'
import * as Quill from 'quill'
// import { ImageDrop } from 'quill-image-drop-module'
// import ImageResize from 'quill-image-resize-module'

// 实现quill-editor编辑器拖拽上传图片
Vue.use(VueQuillEditor)
// Quill.register('modules/imageDrop', ImageDrop)

// 实现quill-editor编辑器调整图片尺寸

// Quill.register('modules/imageResize', ImageResize)

// const user = {
//   login_Info: {
//     phone_num: '', //手机号
//     eth_account: '', //eth账号
//     steem_id: '', // steem id
//     invitedId: '', // 邀请人Id
//     integral: 0, // 积分 周期性清空
//     token_num: 0 //token数量
//   },
//   special_column: {
//     auth_info: {}, // 权限设置
//     spread_award_info: {}, //推广奖励信息
//     auction_info: {}, // 拍卖信息
//     article_info: [] // 专栏文章信息
//   },
//   short_essay: {
//     essay_info: [], //文章信息 包括点赞  评论等
//   },
//   advert_auction: {
//     countdown: 0, // 拍卖倒计时
//     prepare_info: '', // 拍卖预告
//     goods: [], // 商品列表
//     status: {} // 当前拍卖状态
//   }
// }

Vue.prototype.Web3 = Web3

Vue.prototype.$http = axios

Vue.prototype.$store = store

Vue.config.productionTip = false

Vue.component('tree-table', TreeTable)

Vue.filter('dateFormat', function (originVal) {
  const dt = new Date(originVal)
  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0') // 如果不是两位前面用0填充
  const d = (dt.getDate() + '').padStart(2, '0')
  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')
  return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
})

// new Vue({
//   el: '#app',
//   router,
//   store, // 把store对象添加到vue实例上
//   components: { App },
//   template: '<App/>',
// });
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
