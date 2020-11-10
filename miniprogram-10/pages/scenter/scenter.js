// pages/scenter/scenter.js
//获取应用实例
const app = getApp()
//var openid = wx.getStorageSync("openid");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //hasUserInfo: openid == "",
    sno:"",
    name:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: app.globalData.url + '/Show_student_name/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        sno: app.globalData.user,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            name: res.data.name,
          })
        }
      }
    })
  },

  infoModify() {
    wx.navigateTo({
      url: '../sinfoModify/sinfoModify'
    })
  },

  infoFill() {
      wx.navigateTo({
        url: '../sinfoShow/sinfoShow'
      })
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
    app.editTabBar();  
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