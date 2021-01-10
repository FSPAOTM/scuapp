// pages/spingjiashow/spingjiashow.js查看发布兼职企业历史被评价信息
const app = getApp()
Page({
  data: {
    pingjia: [],
    com_name: "",
    score: "",
    show: true,
    isShow: false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this
    var ow_number = options.ow_number
    wx.request({
      url: app.globalData.url + '/outwork_feedback_com/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        ow_number: ow_number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          if (res.data != "该公司暂无评价") {
            that.setData({
              com_name: res.data.com_name,
              score: res.data.score
            })
          } else {
            that.setData({
              show: false,
              isShow: true
            })
          }
        }
      }
    })

    wx.request({
      url: app.globalData.url + '/outwork_feedback_detail/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        ow_number: ow_number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          if (res.data != "该公司暂无评价") {
            that.setData({
              pingjia: res.data
            })
          } else {
            that.setData({
              show: false,
              isShow: true
            })
          }
        }
      }
    })
  }
})