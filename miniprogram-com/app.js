//app.js
var app = getApp()
App({
  onLaunch: function () {
    var that = this;
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        if (res.code) {
          wx.request({
            url: that.globalData.url + '//', //待修改
            header: {
              'content-type': 'application/json'
            },
            data: {
              code: res.code
            },
            method: 'GET',
            success: res => {
              if (res.statusCode == 200) {
                wx.request({
                  url: that.globalData.url + "Login/setuser", //待修改
                  method: "POST",
                  data: {
                    openid: res.data.openid
                  },
                  header: {
                    'content-type': 'application/x-www-form-urlencoded'
                  },
                  success(res) {
                    //如果有该用户，把用户信息放到公共数组中
                    if (res.data) {
                      that.globalData.userInfo = res.data
                    }
                  },
                })
              }
            }
          })
        }
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },

  //第一种底部  
  editTabBar: function () {
    //使用getCurrentPages可以获取当前加载中所有的页面对象的一个数组，数组最后一个就是当前页面。

    var pagePath = "../miniprogram-com/pages/login/login"; //当前页面url
    if (pagePath.indexOf('/') != 0) {
      pagePath = '/' + pagePath;
    }
  },


  globalData: {
    list: [],
    url: 'http://49.235.199.231:8003/wechat',
    userInfo: "",
    user: "",
    age: "",
    gender: "",
    edu: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
    stuNumber: "",
    jobType: "",
    ow_number: "",
    friendlist: ["2018141093036", "2018141093032", "2018141093042", "2018141093001", "2018141093040"],
    msgList: {
      "2018141093036": [{
        from: '2018141093036',
        to: 'text',
        content: '你好！',
        time: '2020.10.10',
        isread: 0
      }],
    },
  }
})