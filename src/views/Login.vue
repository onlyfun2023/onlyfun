<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avatar_box">
        <img src="../assets/fire.jpeg" alt="" />
      </div>
      <div class="login_area">
        <div class="wallet_login" @click="walletLogin">钱包登录</div>
      </div>
      <!-- 登录表单区域 -->
      <el-form ref="loginFormRef" :model="loginForm" :rule="rules" label-width="0px" class="login_form">
        <div class="form_container">
          <!-- 账号 -->
          <el-form-item prop="user">
            <el-input prefix-icon="el-icon-user" v-model="loginForm.user" placeholder="请输入账号" clearable></el-input>
          </el-form-item>
          <!-- 密码 -->
          <el-form-item prop="password" class="password">
            <el-input show-password prefix-icon="el-icon-lock" v-model="loginForm.password" placeholder="请输入密码" clearable></el-input>
          </el-form-item>
          <div class="register_btn" @click="toggle">{{ userType==='login'?'新用户注册' : '登录' }}</div>
        </div>
        <!-- 按钮 -->
        <el-form-item class="btns">
          <el-button class="btn" type="primary" @click="passwordLogin">{{ userType==='login'?'登录' : '注册' }}</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import MD5 from 'MD5'
import { login, register } from '@/api/store/login'
import { setToken } from '@/utils/auth'
export default {
  mounted() {
    this.invitedId = this.$route.query.invitedId
  },
  data() {
    return {
      invitedId: '',
      userType: 'login',
      // 这是登录表单的数据绑定对象
      loginForm: {
        user: '',
        password: ''
      },
      passwordStatus: 'hide',
      statusImgUrl: '../../assets/img/showPassword.jpeg',
      statusType: 'password',
      // 这是表单验证规则对象
      rules: {
        user: [
          {
            pattern: '/^[a-zA-Z0-9_-]{4,16}$/',
            required: true,
            message: '请输入正确的账号',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  computed: {},
  methods: {
    ...mapActions({
      getUser: 'getUserInfo'
    }),
    // 点击重置按钮，重置登录表单
    resetLoginForm() {
      this.$refs.loginFormRef.resetFields()
    },
    walletLogin() {
      // this.loginType = 'wallet'
      const self = this
      if (window.ethereum) {
        if (typeof window.ethereum.isMetaMask === 'undefined') {
          self.$message.error('请安装 MetaMask！')
        } else {
          window.ethereum
            .request({ method: 'eth_requestAccounts' })
            .catch(function (reason) {
              self.$message.error('出错了！' + reason.message)
            })
            .then(function (accounts) {
              // console.log('account', accounts)
              const web3 = new self.Web3(
                self.Web3.givenProvider || 'ws://some.local-or-remote.node:8546'
              )
              web3.eth.personal.sign(
                web3.utils.utf8ToHex('welcometoonlyfun!!!'),
                accounts[0],
                (err, res) => {
                  if (err) {
                    self.$message.error('签名失败，因为' + err.message)
                  } else {
                    console.log('签名后的数据：', res)
                    login({
                      type: 'eth',
                      data: [accounts[0], res]
                    }).then((data) => {
                      setToken(data.token)
                      self.$message.success('登录成功！')
                      self.$store.dispatch('getUserInfo', {
                        id: accounts[0],
                        token: data.token
                      })
                      setTimeout(() => {
                        self.$router.push({
                          path: '/home',
                          query: {
                            user: accounts[0]
                          }
                        })
                      }, 500)
                    })
                  }
                }
              )
            })
        }
      } else {
        self.$message.error('请安装 MetaMask！')
      }
    },
    passwordLogin() {
      // getUserInfo({ id: '0xd538be09d562cd9644a486d499cdf1e706259994' }).then(
      //   (data) => {
      //     console.log(data)
      //   }
      // )
      this.$refs.loginFormRef.validate(async (valid) => {
        if (!valid) return
        const user = this.loginForm.user
        const password = this.loginForm.password
        const reg = /^[a-zA-Z0-9_-]{4,16}$/
        if (user === '') {
          this.$message.error('请输入账号')
        } else if (password === '') {
          this.$message.error('请输入密码')
        } else if (!reg.test(user)) {
          this.$message.error('请输入4到16位字母，数字，下划线，减号')
        } else {
          if (this.userType === 'login') {
            login({
              type: 'password',
              data: [user, MD5(password)]
            }).then((data) => {
              setToken(data.token)
              this.$message.success('登录成功！')
              this.$store.dispatch('getUserInfo', {
                id: user,
                token: data.token
              })
              setTimeout(() => {
                this.$router.push({
                  path: '/home',
                  query: {
                    user: encodeURIComponent(user)
                  }
                })
              }, 500)
            })
          }

          if (this.userType === 'register') {
            register({
              user: user,
              password: MD5(password),
              eth_account: '',
              captcha: '',
              invitedId: this.invitedId || ''
            }).then((data) => {
              this.$message.success('注册成功！')
              this.toggle()
            })
          }
        }
      })
    },
    toggle() {
      this.resetLoginForm()
      if (this.userType === 'login') {
        this.userType = 'register'
      } else {
        this.userType = 'login'
      }
    }
  }
}
</script>

<style scoped>
.login_container {
  background-color: #409eff;
  height: 100%;
}

.login_box {
  position: relative;
  color: #c0c0c0;
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.avatar_box {
  height: 100px;
  width: 100px;
  /* border: 1px solid #eee; */
  /* border-radius: 50%; */
  /* padding: 10px; */
  /* box-shadow: 0 0 10px #ddd; */
  position: absolute;
  left: 50%;
  transform: translate(-50%, -50%);
  /* background-color: #fff;s */
}

img {
  display: block;
  width: 100px;
  height: 100px;
  /* border-radius: 50%; */
  /* background-color: #eee; */
}

.login_area {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  position: absolute;
  right: 10px;
  top: 10px;
}

.login_area .wallet_login {
  display: inline-block;
  cursor: pointer;
}
.login_area .wallet_login:hover {
  color: #409eff;
}
.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 10px 20px;
  box-sizing: border-box;
}
.btns {
  display: flex;
  justify-content: space-between;
}

.btns .btn {
  margin-top: 20px;
  width: 300px;
}
.form_container {
  position: relative;
}
.form_container .password {
  position: relative;
}
.password .status_img {
  width: 13px;
  height: 10px;
  position: absolute;
  right: 10px;
  bottom: 15px;
  cursor: pointer;
}
.form_container .register_btn {
  position: absolute;
  right: 10px;
  bottom: -30px;
  cursor: pointer;
}

.form_container .register_btn:hover {
  color: #409eff;
}
</style>
