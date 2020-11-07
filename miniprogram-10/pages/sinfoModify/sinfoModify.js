// pages/infoModify/infoModify.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    hiddenmodalput1: true,
    hiddenmodalput2: true,
    hiddenmodalput3: true,
    hiddenmodalput4: true,
    stuNumber: app.globalData.user,
    name: "",
    nickName: "",
    phoneNum: "",
    eMail: "",
    mName: "",
    mNick: "",
    mPhone: "",
    mEmail: "",
  },

  onLoad: function (e) {
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Reset_show/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber: app.globalData.user,
      },
      success: (res) => {
        console.log(res);
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            stuNumber: app.globalData.user,
            name: res.data.name,
            nickName: res.data.nickname,
            phoneNum: res.data.phonenumber,
            eMail: res.data.e_mail,
          })
        }
      }
    })
  },

  confirm1: function (e) {
    wx.showModal({//有问题，查弹出框组件
      title: '提示',
      content: '是否确认退出',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          this.setData({
            mName: e.detail//待修改部分
          })
          console.log(this.data.mName)
          wx.request({
            url: 'http://127.0.0.1:8000/wechat/Reset_myinfo_name/',
            header: {
              "Content-Type": "application/x-www-form-urlencoded"
            },
            method: "POST",
            data: {
              stuNumber: app.globalData.user,
              name: this.data.name,
            },
            success: (res) => {
              if (res.statusCode == 200) {
                wx.showToast({
                  title: '修改成功',
                  icon: 'success',
                  duration: 1000
                })
              }
              this.setData({
                hiddenmodalput1: true,
              })
            }
          })
        } else if (res.cancel) {
          this.setData({
            hiddenmodalput1: true,
          })
        }
      }
    })


  },

  confirm2: function (e) {
    this.setData({
      nickName: this.data.mNick
    })
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Reset_myinfo_nickname/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber: app.globalData.user,
        nickName: this.data.nickName,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.showToast({
            title: '修改成功',
            icon: 'success',
            duration: 1000
          })
        }
        this.setData({
          hiddenmodalput2: true,
        })
      }
    })
  },

  confirm3: function (e) {
    this.setData({
      stuNumber: app.globalData.user,
      phoneNum: this.data.mPhone
    })
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Reset_myinfo_phonenumber/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        phoneNum: this.data.phoneNum,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.showToast({
            title: '修改成功',
            icon: 'success',
            duration: 1000
          })
        }
        this.setData({
          hiddenmodalput3: true,
        })
      }
    })
  },

  confirm4: function (e) {
    this.setData({
      stuNumber: app.globalData.user,
      eMail: this.data.mEmail
    })
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Reset_myinfo_e_mail/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        eMail: this.data.eMail,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.showToast({
            title: '绑定成功',
            icon: 'success',
            duration: 1000
          })
        }
        this.setData({
          hiddenmodalput4: true,
        })
      }
    })
  },

  exit: function (e) {
    wx.showModal({
      title: '提示',
      content: '是否确认退出',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          //页面跳转
          wx.switchTab({
            url: '../scenter/scenter',
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },

  //点击按钮痰喘指定的hiddenmodalput弹出框

  modalinput1: function () {

    this.setData({

      hiddenmodalput1: !this.data.hiddenmodalput1,
    })

  },

  modalinput2: function () {

    this.setData({

      hiddenmodalput2: !this.data.hiddenmodalput2,
    })

  },

  modalinput3: function () {

    this.setData({

      hiddenmodalput3: !this.data.hiddenmodalput3,
    })

  },

  modalinput4: function () {

    this.setData({

      hiddenmodalput4: !this.data.hiddenmodalput4,
    })

  },

  //取消按钮

  cancel: function () {

    this.setData({

      hiddenmodalput: true,
    });

  },

  //确认

  confirm: function () {

    this.setData({

      hiddenmodalput: true,

    })

  },

  repwd: function () {
    wx.navigateTo({
      url: '../repwd2/repwd2',
    })
  }

})