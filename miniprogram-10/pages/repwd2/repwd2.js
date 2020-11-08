// pages/repwd/repwd.js
const app = getApp();
// pages/password/password.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    oldpwd: "",
    newpwd: "",
    newpwd2: "",
    no: "",
  },

  old(e) {
    this.setData({
      oldpwd: e.detail.value
    })
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

  formSubmit: function (e) {
    // console.log(e);
    if (this.data.oldpwd == '' || this.data.newpwd == '' || this.data.newpwd2 == '') {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 3000
      })
    } else if (this.data.newpwd != this.data.newpwd2) {
      wx.showToast({
        title: '两次密码输入不一致，请重新输入',
        icon: 'none',
        duration: 3000
      })
    } else {
      wx.request({
        url: app.globalData.url + '/Reset_password/', 
        method: 'POST',
        data: {
          no: app.globalData.user,
          oldpwd: this.data.oldpwd,
          newpwd: this.data.newpwd,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        success: (res) => {
          console.log(res.data);
          if (res.data == "原密码输入不正确，请重新输入") {
            wx.showToast({
              title: "原密码输入不正确，请重新输入！",
              icon: 'none',
              duration: 2000
            })
          } else if (res.data == "密码修改成功") {
            wx.showToast({
              title: "修改成功！",
              icon: 'success',
              duration: 2000,
              success: function () {
                setTimeout(function () {
                  wx.navigateBack({
                    belta: 1
                  })
                }, 2000)
              }
            })
          } else {
            wx.showToast({
              title: "请求错误",
              icon: 'none',
              duration: 2000
            })
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