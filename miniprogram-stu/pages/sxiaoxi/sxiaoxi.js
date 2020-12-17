// pages/sxiaoxi/sxiaoxi.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    mianshitongzhi:[],
    count1:"",
    count2:"",
  },

  mianshi() {
    wx.navigateTo({
      url: '../smianshitongzhi/smianshitongzhi?user=' + app.globalData.user,
    })
  },

  jieguo() {
    wx.navigateTo({
      url: '../sjieguotongzhi/sjieguotongzhi?user=' + app.globalData.user,
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/', 
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
            mianshitongzhi: res.data,
            count1:res.data[0].count//待修改
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