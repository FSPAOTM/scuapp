// pages/spingjiashow/spingjiashow.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    pingjia: [],
    com_name: "",
    score: "",
    show: true,
    isShow:false
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
              isShow:true
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
        }else{
          that.setData({
            show: false,
            isShow:true
          })
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