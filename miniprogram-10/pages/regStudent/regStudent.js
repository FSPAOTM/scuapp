// pages/regStudent/regStudent.js
var app = getApp();
Page({
  /**
   * 页面的初始数据
   */
  data: {
    disabled: true,
    focusPhoneNum: false,
    focusStuNumber: false,
    focusName: false,
    focusNickName: false,
    focusPassword: false,
    focusRePassword: false,
    phoneNum: '',
    stuNumber: '',
    Name: '',
    NickName: '',
    password: '',
    rePassword: '',
    result: ''
  },

  focusPhoneNum: function () {
    this.setData({
      focusPhoneNum: true
    })
  },
  focusStuNumber: function () {
    this.setData({
      focusStuNumber: true
    })
  },
  focusName: function () {
    this.setData({
      focusName: true
    })
  },
  focusNickName: function () {
    this.setData({
      focusNickName: true
    })
  },

  focusPassword: function () {
    this.setData({
      focusPassword: true
    })
  },
  focusRePassword: function () {
    this.setData({
      focusRePassword: true
    })
  },
  blurPhoneNum: function (e) {
    this.setData({
      focusPhoneNum: false
    })
    let myreg = /^1[3456789]\d{9}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '手机号不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '请输入正确的手机号',
        icon: 'none',
        duration: 2000
      })
    }
  },

  blurStuNumber: function (e) {
    this.setData({
      focusStuNumber: false
    })
    let myreg = /^(20)\d{11}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '学号不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '请输入正确的学号',
        icon: 'none',
        duration: 2000
      })
    }
    app.globalData.stuNumber = e.detail.value;
    console.log(app.globalData.stuNumber);
  },
  blurName: function (e) {
    this.setData({
      focusName: false
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '姓名不能为空',
        icon: 'none',
        duration: 2000
      })
    }
  },
  blurNickName: function (e) {
    this.setData({
      focusNickName: false
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '昵称不能为空',
        icon: 'none',
        duration: 2000
      })
    }
  },

  blurPassword: function (e) {
    this.setData({
      focusPassword: false
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (e.detail.value.length < 6) {
      wx.showToast({
        title: '密码不得少于6位',
        icon: 'none',
        duration: 2000
      })
    }
  },
  blurRePassword: function (e) {
    console.log(this.data.password);
    this.setData({
      focusRePassword: false
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '请确认密码',
        icon: 'none',
        duration: 2000
      })
    } else if (e.detail.value != this.data.password) {
      wx.showToast({
        title: '与第一次输入密码不同，请再次确认密码',
        icon: 'none',
        duration: 2000
      })
    }
  },

  //提交时验证
  formSubmit: function (e) {
    if (this.data.password = this.data.rePassword) {
      wx.request({
        url: 'http://127.0.0.1:8000/wechat/Student_register/',
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          phoneNum: this.data.phoneNum,
          stuNumber: this.data.stuNumber,
          Name: this.data.Name,
          NickName: this.data.NickName,
          password: this.data.password
        },
        success: (res) => {
          console.log(res);
          console.log(this.data.stuNumber);
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data == "用户已存在") {
              wx.showToast({
                title: "用户已存在",
                icon: 'none',
                duration: 2000
              })
              setTimeout(function () {
                wx.navigateTo({
                  url: '../login/login',
                })
              }, 2000)
            } else {
              if (res.data == "注册成功") {
                wx.showToast({
                  title: '注册成功',
                  icon: 'success',
                  duration: 2000
                })
                setTimeout(function () {
                  wx.redirectTo({
                    url: '../index/index',
                  })
                }, 2000)
              } else {
                wx.showToast({
                  title: '请求错误',
                  icon: 'none',
                  duration: 2000
                })
              };
            }
          }
        }
      })
    } else {
      wx.showToast({
        title: '两次输入密码不同，请再次确认密码',
        icon: 'none',
        duration: 2000
      })
    }
  },


  /**
   * 生命周期函数--监听页面加载
   */
  inputwatch: function (e) {
    console.log(e);
    let item = e.currentTarget.dataset.model;
    this.setData({
      [item]: e.detail.value
    });
    if (this.data.phoneNum.length >= 11 && this.data.stuNumber.length == 13 && this.data.password.length >= 6 && this.data.rePassword.length >= 6 && this.data.Name && this.data.NickName) {
      this.setData({
        disabled: false
      })
    } else {
      this.setData({
        disabled: true
      })
    }
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})