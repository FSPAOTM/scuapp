// pages/sluyongxinxi/sluyongxinxi.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isShow: false,
    ow_number:"",
    iw_number:"",
    luyongxinxi: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    this.setData({
      iw_number:options.iw_number,
      ow_number:options.ow_number
    })
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/', //待修改
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        stu_number:app.globalData.user,
        ow_number:this.data.ow_number,
        iw_number:this.data.iw_number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            luyongxinxi: res.data
          })
        }
        if (that.data.luyongxinxi.length == 0) {
          that.setData({
            isShow: true
          })
        }
      }
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