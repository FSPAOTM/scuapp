// pages/cmianshidahui/cmianshidahui.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isShow:false,
    user: "",
    info: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    this.setData({
      user: options.user
    })
    wx.request({
      url: app.globalData.url + '/Show_work/', //待修改,res.data里面包括post/reason/ow_number
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            info: res.data
          })
        }
        if (that.data.mianshitongzhi.length == 0) {
          that.setData({
            isShow: true
          })
        }
      }
    })
  },

  reapply(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.info[e].ow_number;
    console.log("++++++", ev, that)
    wx.navigateTo({
      url: '../cinterviewModify/cinterviewModify?ow_number='+ow_number,
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