// pages/repwd1-1/repwd1-1.js
const app = getApp();
// pages/password/password.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    newpwd:"",
    newpwd2:"",
  },

  new(e){
    this.setData({
      newpwd:e.detail.value
    })
  },

  again(e){
    this.setData({
      newpwd2:e.detail.value
    })
  },

  formSubmit: function () {
    // console.log(e);
    this.setData({
      newpwd:this.data.newpwd,
      newpwd2:this.data.newpwd2,
    })
    // console.log(no);
    if (newpwd == '' || newpwd2 == '') {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 1000
      })
    } else if (newpwd != newpwd2) {
      wx.showToast({
        title: '两次输入不一致',
        icon: 'none',
        duration: 1000
      })
    } else {
      wx.request({
        url: url, //仅为示例，并非真实的接口地址
        method: 'POST',
        data: {
          user:app.globalData.user,
          newpwd: newpwd,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        success: (res) => {
          console.log(res.data);
          if (res.statusCode == 200) {
            wx.showToast({
              title: "修改成功！",
              icon: 'success',
              duration: 2000
            })
            wx.redirectTo({
              url: '../login/login',
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