// pages/index/index.js用户登录及忘记密码+注册的入口
var app = getApp()
var chat = require('../../utils/chat.js')
Page({
  data: {
    no: '',
    pwd: '',
    noinput: false,
    pwdinput: false,
    result: '',
  },
  // 获取输入学号
  noinput: function (e) {
    this.setData({
      no: e.detail.value
    });
    this.setData({
      noinput: true
    });
    if (this.data.noinput == true && this.data.pwdinput == true) {
      this.setData({
        disabled: false
      });
    }
  },
  // 获取输入密码
  pwdinput: function (e) {
    this.setData({
      pwd: e.detail.value
    });
    this.setData({
      pwdinput: true
    });
    if (this.data.pwd.length >= 8 && this.data.pwd.length <= 18)
      if (this.data.noinput == true && this.data.pwdinput == true) {
        this.setData({
          disabled: false
        });
      }
    if (this.data.pwd.length < 8) {
      this.setData({
        disabled: true
      });
    }
  },

  formSubmit: function (e) {
    var self = this;
    this.linkSocket();
    console.log(e);
    wx.onSocketMessage((result) => {
      let msg = JSON.parse(result.data)["message"];
      chat.update_globalData_msgList_default(msg); //更新消息列表
      console.log("我在login.js");
      wx.showToast({
        title: '收到一条新消息',
      })
    })
    self.setData({
      disabled: true
    });
    wx.request({
      url: app.globalData.url + '/dengluzhuce_login/',
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      data: {
        no: this.data.no,
        pwd: this.data.pwd
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            result: res.data
          })
          if (res.data == "用户名或密码错误") {
            wx.showToast({
              title: '用户名或密码错误',
              icon: 'none',
              duration: 2000
            })
          } else {
            if (res.data == "用户名不存在") {
              wx.showToast({
                title: '用户名不存在',
                icon: 'none',
                duration: 2000
              })
              setTimeout(function () {
                wx.redirectTo({
                  url: '../index/index',
                })
              }, 2000)
            } else {
              if (res.data == "登录成功！") {
                wx.setStorageSync('student', res.data.no);
                wx.showToast({
                  title: '登录成功',
                  icon: 'success',
                  duration: 1000
                })
                if (self.data.no.length == 11) {
                  setTimeout(function () {
                    wx.switchTab({
                      url: '../cworkspace/cworkspace',
                    })
                  }, 2000)
                }
                app.globalData.user = self.data.no;
                console.log(app.globalData.user);
              } else {
                wx.showToast({
                  title: '请求错误',
                  icon: 'none',
                  duration: 2000
                })
              }
            }
          }
        }
      }
    })
  },

  linkSocket() {
    wx.connectSocket({
      url: "ws://127.0.0.1:8000/ws/chat/" + this.data.no + "/",
      header: {
        'content-type': 'application/json'
      },
    });

    wx.onSocketOpen((result) => {
      console.log('connect success')
    })
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    if (this.data.no == '' || this.data.pwd == '') {
      this.setData({
        disabled: true
      });
    } else {
      this.setData({
        disabled: false
      });
    }
  }
})