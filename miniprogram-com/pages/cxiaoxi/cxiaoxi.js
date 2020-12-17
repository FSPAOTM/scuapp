// pages/cxiaoxi/cxiaoxi.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    mianshitongzhi:[],
    dahuitongzhi:[],
    count1:"",
    count2:"",
    show1:true,
    show2:true
  },

  /**
   * 生命周期函数--监听页面加载
   */

  tongzhi() {
    wx.navigateTo({
      url: '../cmianshitongzhi/cmianshitongzhi?user=' + app.globalData.user,
    })
  },

  dahui() {
    wx.navigateTo({
      url: '../cmianshidahui/cmianshidahui?user=' + app.globalData.user,
    })
  },

  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Com_interview_notice_show/', 
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
            count1:res.data.length
          })
          if(that.data.count1==0){
            that.setData({
              show1:false
            })
          }
        }
      }
    })

    wx.request({
      url: app.globalData.url + '/Com_interview_back_show/', //待修改
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
            dahuitongzhi: res.data,
            count2:res.data.length
          })
          if(that.data.count2==0){
            that.setData({
              show2:false
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