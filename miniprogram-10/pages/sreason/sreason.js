// pages/sreason/sreason.js
const app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    reason: "",
    ow_number: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var ow_number = wx.getStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
  },

  reasoninput(e) {
    this.setData({
      reason: e.detail.value
    })
  },

  formsubmit() {
    wx.request({
      url: app.globalData.url + '/Get_outwork_detail_info/',
      /*待修改*/
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        ow_number: this.data.ow_number,
        reason:this.data.reason,
        user:app.globalData.user,
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
          if(res.data=="报名成功"){
            wx.showToast({
              title: '报名成功',
              icon: 'success',
              duration: 2000
            })
            setTimeout(function () {
              wx.navigateTo({
                url: '../smyjob/smyjob',
              })
            }, 2000)
          }
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