// pages/repwd1-1/repwd1-1.js
const app = getApp();
// pages/password/password.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    newpwd: "",
    newpwd2: "",
  },

  new(e) {
    this.setData({
      newpwd: e.detail.value
    })
  },

  again(e) {
    this.setData({
      newpwd2: e.detail.value
    })
  },

  formSubmit: function () {
    let myreg = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$]{8,18}$/;
    if (this.data.newpwd == '' || this.data.newpwd2 == '') {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 1000
      })
    } else if (this.data.newpwd != this.data.newpwd2) {
      wx.showToast({
        title: '两次输入不一致',
        icon: 'none',
        duration: 1000
      })
    } else if (!myreg.test(this.data.newpwd) || !myreg.test(this.data.newpwd2)) {
      wx.showToast({
        title: '密码必须包含数字与字母，可以包含或不包含特殊符号！',
        icon: 'none',
        duration: 2000
      })
    } else {
      wx.request({
        url: app.globalData.url + '/Reset_password_f2/',
        method: 'POST',
        data: {
          user: app.globalData.user,
          newpwd: this.data.newpwd,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        success: (res) => {
          console.log(res.data);
          if (res.statusCode == 200) {
            if (res.data == "密码修改成功") {
              wx.showToast({
                title: "修改成功，请重新登录",
                icon:'none',
                duration: 2000
              })
              setTimeout(function () {
                wx.redirectTo({
                  url: '../login/login',
                })
              }, 2000)
            }
          }
        }
      })
    }

  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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