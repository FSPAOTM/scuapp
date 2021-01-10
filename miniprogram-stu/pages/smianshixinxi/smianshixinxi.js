// pages/smianshixinxi/smianshixinxi.js学生确认后查看面试信息
const app = getApp()
Page({
  data: {
    isShow: false,
    ow_number: "",
    mianshixinxi: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    this.setData({
      ow_number: options.ow_number
    })
    wx.request({
      url: app.globalData.url + '/Stu_interview_information_show/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        stu_number: app.globalData.user,
        ow_number: this.data.ow_number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            mianshixinxi: res.data
          })
        }
        if (that.data.mianshixinxi.length == 0) {
          that.setData({
            isShow: true
          })
        }
      }
    })
  }
})