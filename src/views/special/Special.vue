<!--
 * @Author: gerrardlt 305690790@qq.com
 * @Date: 2023-01-12 14:01:22
 * @LastEditors: gerrardlt 305690790@qq.com
 * @LastEditTime: 2023-01-30 06:51:32
 * @FilePath: \quhu\src\views\special\Special.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
  <div class="main-content-container">
    <div class="post-container">
      <div @click="postArticle" class="post-topic-head">
        <div class="tip">点击发表主题...</div>
      </div>
      <div class="post-topic-footer">
        <div class="post-topic-btn">
          <div class="left"></div>
          <div class="post-action">
            <div class="common post-article">
              <span>写文章</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-for="(item,index) in articleList" :key="index">
      <div class="topic-container">
        <div style="padding:10px;">
          <div class="header-container">
            <div class="author">
              <img class="avatar" src="../../assets/heima.png" alt="">
              <div class="info">
                <div class="role owner">{{ item.body.author }}</div>
                <div class="date">{{ item.updated.replace('T','  ') }}</div>
              </div>
            </div>
          </div>
          <div class="talk-content-container">
            <div class="content">
              <div>{{ item.title }}</div><br />
              <div v-html="item.body.body"></div>
            </div>
          </div>
          <div class="operation-icon-container">
            <div class="operation-icon">
              <div title="点赞" class="like">
                <Icon name="praise" />
              </div>
              <div title="评论" class="comment" @click="isEditReply = true">
                <Icon name="discuss" />
              </div>
              <div title="收藏" class="subscribe">
                <Icon name="collect" />
              </div>
            </div>
            <div class="details-container" @click="goDetail(item)">
              <div class="text">查看详情</div>
              <div class="icon">
                <Icon name="arrowR" />
              </div>
            </div>

          </div>
          <el-input v-show="isEditReply" placeholder="请输入内容" v-model="reply" class="reply_input">
            <el-button slot="append" @click="submitReply(item)">回复</el-button>
          </el-input>
          <!-- <div class="comment-item-container">
            <div class="text"><span class="comment group-owner-light">ywnwa</span>
              <span>：</span>
              <span parsetype="pure" class="text">123123</span>
            </div>
            <div  class="operations">
              <div  class="time">2023-01-29 22:36</div>
              <div  class="operation"><span >置顶</span>
                <span  class="space">删除</span>
              </div>
            </div>
          </div> -->
        </div>
      </div>
    </div>
    <div v-if="isShowDetailDialog" id="topic-detail-container" class="topic-detail">
      <div class="content">
        <!-- <div class="skeleton-container" hidden="">
          <div class="skeleton">
            <div class="header">
              <div class="avatar"></div>
              <div class="author-info">
                <div class="item1"></div>
                <div class="item2"></div>
              </div>
            </div>
            <div class="card-layout">
              <div></div>
              <div></div>
              <div class="item1"></div>
              <div class="content"></div>
              <div></div>
              <div class="item2"></div>
            </div>
          </div>
        </div> -->
        <div class="topic-detail-panel">
          <!-- <div class="enter-group"><span class="left">来自：非暴力不合作</span><span class="right">进入星球<div class="icon"></div></span>

          </div> -->
          <div class="header-container">
            <div class="author"><img class="avatar" src="../../assets/heima.png">
              <div class="info">
                <div class="role owner">{{ currentDetail.body.author }}</div>
                <div class="date">
                  {{ currentDetail.updated.replace('T','  ') }}
                </div>
              </div>
            </div>
            <div @click="closeDetail" class="close-icon">
              <Icon name="cancel" />
            </div>
          </div>

          <div class="">
            <div class="talk-content-container">
              <div class="content">
                <div>{{ currentDetail.title }}</div><br />
                <div v-html="currentDetail.body.body"></div>
              </div>
            </div>

          </div>

          <div class="operation-icon">
            <div title="点赞" class="like">
              <Icon name="praise" />
            </div>
            <div title="评论" class="comment">
              <Icon name="discuss" />
            </div>
            <div title="收藏" class="subscribe">
              <Icon name="collect" />
            </div>
          </div>

        </div>

      </div>
    </div>
    <div v-if="showEditor" class="create-topic-container">
      <div class="create-topic-panel">
        <div class="head">
          <div class="title">
            <input type="text" v-model="titleText" class="titie_text" placeholder="请输入标题">
          </div>
          <div @click="closeEditor" class="close-icon">
            <Icon name="cancel" />
          </div>
        </div>
        <div>
          <div class="horizontal-line"></div>
          <div class="content-container"><img class="avatar" src="../../assets/heima.png">
            <div style="width: calc(100% - 40px); min-height: 110px; margin: 5px 0px; max-height: 497px;">
              <quill-editor v-model="content" :options="editorOption" spellcheck="false" class="quill-editor">
                <!-- <div quill-editor-element="" class="ql-container ql-snow">
                  <div class="ql-editor" contenteditable="true" aria-owns="quill-mention-list" data-placeholder="点击发表主题...">
                    <p>驱蚊器翁</p>
                  </div>
                </div> -->
              </quill-editor>
            </div>
          </div>
          <div class="horizontal-line"></div>

        </div>
        <div class="upload-container">
          <div class="operation-icon">
            <div class="left">
              <!-- <button  class="emoji"></button> -->
              <!-- <div  class="pic"></div>
                <div  class="file"></div>
                <div  class="video" hidden=""></div><button  class="tag"></button>
                <div  class="scheduled"></div> -->
            </div>
            <div class="right">
              <div class="text-range">(4～10000)</div>
              <div @click="submit" class="submit-btn">发布</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- <quill-editor v-model="content" ref="myQuillEditor" :options="editorOption" @blur="onEditorBlur($event)" @focus="onEditorFocus($event)" @ready="onEditorReady($event)">
    </quill-editor> -->
    <!-- <el-row class="special_container">
      <el-col :span="10" v-for="(item, index) in articleList" :key="index" :offset="index % 2 !==0? 4 : 0">
        <el-card :body-style="{ padding: '0px' }">
          <img v-if="index!==articleList.length-1" src="../../assets/quhu.png" class="image">
          <div v-if="index!==articleList.length-1" style="padding: 8px;">
            <span>趣乎专栏</span>
            <div class="bottom clearfix">
              <span>趣乎专栏</span>
              <el-button type="text" class="button">操作</el-button>
            </div>
          </div>
          <div v-if="index===articleList.length-1" class="empty">
            <el-button type="text" class="button">创建专栏</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row> -->
  </div>
</template>

<script>
import {
  subscriptions,
  post,
  getArticles,
  getArticleDetail
} from '@/api/special/special'
import { getToken } from '@/utils/auth'
import Icon from '@/components/Icon/index'
export default {
  components: {
    Icon
  },
  data() {
    return {
      articleList: [],
      content: '',
      reply: '',
      editorOption: {
        modules: {
          toolbar: ''
        },
        placeholder: '请输入正文'
      },
      showEditor: false,
      titleText: '',
      currentDetail: {},
      isShowDetailDialog: false,
      isEditReply: false
    }
  },
  async created() {
    const userInfo = JSON.parse(localStorage.getItem('quhu-userInfo'))
    if (localStorage.getItem('quhu-userInfo')) {
      const res = await getArticles({
        id: userInfo.user !== 'none' ? userInfo.user : userInfo.eth_account,
        jsonrpc: '2.0',
        method: 'bridge.get_ranked_posts',
        params: { sort: 'created', tag: 'd-' + userInfo.steem_id }
      })
      const formatRes = res.result && res.result.concat()
      formatRes.forEach((element) => {
        element.body = this.eval(element.body)
      })

      if (res.result.length !== 0) {
        this.articleList = formatRes
      }

      // this.articleList.push({})
    }
  },
  // 此时页面上的元素已经渲染完毕了
  async mounted() {},
  methods: {
    async submitReply(v) {
      const userInfo = JSON.parse(localStorage.getItem('quhu-userInfo'))
      const res = await post({
        type: 'comment',
        id: userInfo.user !== 'none' ? userInfo.user : userInfo.eth_account,
        token: getToken(),
        user_name: userInfo.user_name,
        steem_id: userInfo.steem_id,
        subscriptions_name: '',
        permlink: [v.author, v.permlink],
        title: '',
        body: this.reply
      })

      if (res && res.success === 'ok') {
        this.$message.success('回复成功')
        this.isEditReply = false
        this.reply = ''
      } else {
        this.$message.error('发文失败！ 请重新发文')
        this.closeEditor()
        this.isEditReply = false
        this.reply = ''
      }
    },
    postArticle() {
      this.showEditor = true
    },
    async submit() {
      //   {
      //   id: userInfo.user,
      //   token: getToken(),
      //   user_name: userInfo.username,
      //   steem_id: userInfo.steem_id
      //  }
      const userInfo = JSON.parse(localStorage.getItem('quhu-userInfo'))
      const res = await post({
        type: 'post',
        id: userInfo.user !== 'none' ? userInfo.user : userInfo.eth_account,
        token: getToken(),
        user_name: userInfo.user_name,
        steem_id: userInfo.steem_id,
        subscriptions_name: '',
        permlink: '',
        title: this.titleText,
        body: this.content
      })

      if (res && res.success === 'ok') {
        this.$message.success('发文成功')
        this.closeEditor()
      } else {
        this.$message.error('发文失败！ 请重新发文')
        this.closeEditor()
      }
    },
    closeEditor() {
      this.showEditor = false
      this.content = ''
      this.titleText = ''
    },
    closeDetail() {
      this.isShowDetailDialog = false
    },
    async goDetail(val) {
      const userInfo = JSON.parse(localStorage.getItem('quhu-userInfo'))
      const res = await getArticleDetail({
        id: userInfo.user !== 'none' ? userInfo.user : userInfo.eth_account,
        jsonrpc: '2.0',
        method: 'bridge.get_discussion',
        params: { author: val.author, permlink: val.permlink }
      })
      const obj = res.result[val.author + '/' + val.permlink]
      if (obj) {
        obj.body = this.eval(obj.body)
        this.currentDetail = obj
        console.log(this.currentDetail)
        this.isShowDetailDialog = true
      }
    },
    onEditorBlur() {},
    onEditorFocus() {},
    onEditorReady() {},
    eval(fn) {
      const Fn = Function
      return new Fn('return ' + fn)()
    }
  }
}
</script>

<style scoped>
.topic-container .comment-box .comment-item-container {
  padding: 12px 12px 0;
  margin: 0 20px 0 56px;
  background-color: #f7f9fa;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}
.comment-item-container .text {
  line-height: 20px;
  color: #5a5c66;
  word-wrap: break-word;
  white-space: pre-wrap;
}
.comment-item-container .text .group-owner-light {
  color: #fda956;
  cursor: pointer;
}
.comment-item-container .operations {
  margin-top: 2px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 16px;
  font-size: 12px;
  color: #c5c6cb;
}
.reply_input input {
  width: 100%;
  height: 50px;
  line-height: 50px;
}
.topic-detail {
  position: fixed;
  width: 100%;
  height: 100%;
  overflow-y: scroll;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 998;
}
.topic-detail .content {
  width: 80%;
  min-width: 200px;
  margin: 60px auto;
}
.header-container {
  position: relative;
}
.header-container .close-icon {
  position: absolute;
  right: 0px;
  top: 0px;
  width: 10px;
  height: 10px;
  cursor: pointer;
}

.operation-icon {
  display: flex;
  align-items: center;
}
.topic-detail-panel .operation-icon div {
  width: 21px;
  height: 21px;
  margin-right: 30px;
  cursor: pointer;
}
.main-content-container {
  margin: 10px 0 0 0;
}
.post-container {
  padding-top: 20px;
  margin-bottom: 5px;
  background-color: #fff;
  border-radius: 4px;
}
.post-topic-head {
  display: flex;
  align-items: center;
  margin: 0 20px;
  padding: 20px;
  cursor: pointer;
  border-radius: 4px;
  background: #f8f9fa;
}
.tip {
  font-family: PingFangSC-Regular;
  font-size: 14px;
  color: #8b8e9d;
  letter-spacing: 0;
  margin-left: 10px;
  width: 300px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.post-topic-footer {
  height: 60px;
  margin: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  -webkit-user-select: none;
  user-select: none;
}

.post-topic-btn {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: flex-end;
}
.titie_text {
  font-family: PingFangSC-Medium;
  border: none;
  outline: none;
  flex: 1;
  font-size: 14px;
  color: #1a1a1a;
  height: 30px;
  line-height: normal;
  padding: 0;
}
.left {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.post-action {
  display: flex;
  align-items: center;
}
.post-article {
  position: relative;
  padding-left: 16px;
  margin-left: 16px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  font-size: 12px;
  font-weight: 700;
  color: #8b8e9d;
  cursor: pointer;
}

.topic-container {
  background: #fff;
  margin-bottom: 10px;
  border-radius: 4px;
}

.topic-container .header-container {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px 10px 10px;
}

.header-container .author {
  display: flex;
  align-items: center;
  height: 36px;
  position: relative;
}

.header-container .info {
  margin-left: 46px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.info .owner {
  height: 20px;
  line-height: 20px;
  cursor: pointer;
  color: #fda956;
}

.info .date {
  display: flex;
  align-items: center;
  font-size: 12px;
  color: #c5c6cb;
}
.talk-content-container {
  padding-left: 56px;
  padding-right: 20px;
  margin-bottom: 10px;
  line-height: 21px;
  color: #2f3034;
}
.talk-content-container .content {
  white-space: pre-wrap;
  word-wrap: break-word;
  overflow: hidden;
}

.topic-container .operation-icon-container {
  padding-left: 56px;
  padding-right: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 15px 0;
}
.topic-container .operation-icon-container .operation-icon {
  display: flex;
}
.topic-container .operation-icon-container .operation-icon div {
  width: 21px;
  height: 21px;
  margin-right: 30px;
  cursor: pointer;
}
.topic-container .operation-icon-container .details-container {
  display: flex;
  align-items: center;
  cursor: pointer;
}
.topic-container .operation-icon-container .details-container .text {
  font-size: 12px;
  color: #c5c6cb;
}

.topic-container .operation-icon-container .details-container .icon {
  width: 20px;
  height: 30px;
  /* background-image: url(assets/resources/sprite@1x.fb4b9063d37e9252.png); */
  /* background-position: -297px -197px; */
}
.create-topic-container {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
  overflow-y: scroll;
}
.header-container .author .avatar {
  position: absolute;
  top: 0;
  left: 0;
  height: 30px;
  width: 30px;
  border-radius: 50%;
  background-color: #f5f6f7;
  cursor: pointer;
}
.create-topic-container .create-topic-panel {
  margin: 60px auto;
  background: #fff;
  width: 80%;
  min-width: 200px;
  min-height: 220px;
  border-radius: 4px;
  padding: 0 20px 20px;
  box-sizing: border-box;
}
@media screen and (max-width: 1600px) {
  .create-topic-container .create-topic-panel {
    width: 80%;
  }
}

.create-topic-container .create-topic-panel .head {
  position: relative;
}
.create-topic-container .create-topic-panel .head .title {
  color: #2f3034;
  text-align: left;
  font-size: 16px;
  height: 50px;
  font-weight: 700;
  display: flex;
  align-items: center;
}
.create-topic-container .create-topic-panel .content-container .avatar {
  width: 30px;
  height: 30px;
  border-radius: 15px;
  background: #f5f6f7;
  margin-right: 10px;
  flex-shrink: 0;
}
.create-topic-container .create-topic-panel .head .close-icon {
  position: absolute;
  right: 0px;
  top: calc(50% - 5px);
  /* background-image: url(assets/resources/sprite@1x.fb4b9063d37e9252.png); */
  background-position: -357px -197px;
  width: 10px;
  height: 10px;
  cursor: pointer;
}
.create-topic-container .create-topic-panel .horizontal-line {
  height: 1px;
  background: rgba(0, 0, 0, 0.05);
}

.create-topic-container .create-topic-panel .content-container {
  position: relative;
  margin: 10px 0;
  display: flex;
}

.quill-editor .ql-container {
  border: none;
  font-family: PingFangSC-Regular;
  font-size: 14px !important;
}

.quill-editor .ql-container .ql-editor {
  padding: 0;
  color: #2f3034;
  line-height: 20px;
}
.ql-editor {
  box-sizing: border-box;
  counter-reset: list-0 list-1 list-2 list-3 list-4 list-5 list-6 list-7 list-8
    list-9;
  height: 100%;
  outline: none;
  overflow-y: auto;
  tab-size: 4;
  text-align: left;
  white-space: pre-wrap;
  word-wrap: break-word;
}
.upload-container {
  position: relative;
}

.create-topic-container .create-topic-panel .operation-icon {
  height: 24px;
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  -webkit-user-select: none;
  user-select: none;
}
.create-topic-container .create-topic-panel .operation-icon .left {
  display: flex;
  align-items: center;
  position: relative;
}

.create-topic-container .create-topic-panel .operation-icon .right {
  display: flex;
}
.upload-container .image-list-container {
  margin-top: 10px;
  margin-bottom: 4px;
  width: 318px;
}
.create-topic-container .create-topic-panel .operation-icon .right .text-range {
  margin-right: 16px;
  font-size: 12px;
  color: #c5c6cb;
  height: 24px;
  line-height: 24px;
  text-align: center;
}
.create-topic-container .create-topic-panel .operation-icon .right .submit-btn {
  min-width: 50px;
  height: 24px;
  padding: 0 6px;
  box-sizing: border-box;
  line-height: 24px;
  text-align: center;
  background: #16b998;
  box-shadow: 0 1px 2px #0000000d;
  border-radius: 2px;
  color: #fff;
  cursor: pointer;
}

.topic-detail .content .topic-detail-panel {
  background: #fff;
  border-radius: 4px;
  padding: 20px 30px 30px;
}
.el-col {
  margin-bottom: 20px;
}
.el-col:last-child {
  margin-bottom: 0;
}
.special_container {
  padding: 40px;
}
.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.empty {
  width: 100%;
  height: 140px;
  background: url('../../assets/quhu.png') no-repeat center center;
  background-size: 140px 140px;
}
.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}

.clearfix:after {
  clear: both;
}
</style>
