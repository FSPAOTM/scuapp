// pages/regCompany/regCompany.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    disabled: true,
    focusPhoneNum: false,
    focusComName: false,
    focusComLicense: false,
    focusPassword: false,
    focusRePassword: false,
    phoneNum: "",
    ComName: "",
    ComLicense: "",
    password: "",
    rePassword: "",
    result: ""
  },

  focusPhoneNum: function () {
    this.setData({
      focusPhoneNum: true
    })
  },

  focusComName: function () {
    this.setData({
      focusComName: true
    })
  },

  focusComLicense: function () {
    this.setData({
      focusComLicense: true
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
      focusPhoneNum: false,
      phoneNum: e.detail.value
    })
    let myreg = /^1[3456789]\d{9}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '联系方式不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '请输入正确的联系方式',
        icon: 'none',
        duration: 2000
      })
    }
  },

  blurComLicense: function (e) {
    this.setData({
      focusComLicense: false,
      ComLicense: e.detail.value
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '统一信用代码不能为空',
        icon: 'none',
        duration: 2000
      })
    }
  },
  blurComName: function (e) {
    this.setData({
      focusComName: false,
      ComName: e.detail.value
    })
    if (e.detail.value == "") {
      wx.showToast({
        title: '企业名称不能为空',
        icon: 'none',
        duration: 2000
      })
    }
  },




  blurPassword: function (e) {
    this.setData({
      focusPassword: false,
      password: e.detail.value
    })
    let myreg = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$]{8,18}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '密码必须包含数字与字母，可以包含或不包含特殊符号！',
        icon: 'none',
        duration: 2000
      })
    }
  },
  blurRePassword: function (e) {
    console.log(this.data.password);
    this.setData({
      focusRePassword: false,
      rePassword: e.detail.value
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
        url: app.globalData.url + '/Company_register/',
        method: 'POST',
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        data: {
          ComName: this.data.ComName,
          phoneNum: this.data.phoneNum,
          ComLicense: this.data.ComLicense,
          password: this.data.password
        },
        success: (res) => {
          console.log(res);
          console.log(this.data.ComLicense);
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data == "电话号码已注册") {
              wx.showToast({
                title: "电话号码已注册",
                icon: 'none',
                duration: 2000
              })
              setTimeout(function () {
                wx.navigateTo({
                  url: '../regCompany/regCompany',
                })
              }, 2000)
            } else {
              if (res.data == "统一信用代码已注册") {
                wx.showToast({
                  title: "统一信用代码已注册",
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
                      url: '../login/login',
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
    if (this.data.phoneNum.length >= 11 && this.data.ComLicense.length >= 18 && this.data.password.length >= 8 && this.data.rePassword.length >= 8 && this.data.ComName) {
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