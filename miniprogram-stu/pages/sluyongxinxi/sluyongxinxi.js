// pages/sluyongxinxi/sluyongxinxi.js学生确认后查看录用信息（报道信息）
const app = getApp()
Page({
  data: {
    isShow: false,
    ow_number: "",
    iw_number: "",
    luyongxinxi: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    this.setData({
      iw_number: options.iw_number,
      ow_number: options.ow_number
    })
    wx.request({
      url: app.globalData.url + '/Stu_result_information_show/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        stu_number: app.globalData.user,
        ow_number: this.data.ow_number,
        iw_number: this.data.iw_number
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
  }
})