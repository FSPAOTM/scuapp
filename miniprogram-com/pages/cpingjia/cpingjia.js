// pages/pingjia/pingjia.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    stupingjia:[],
    mypingjia:[],
    winWidth: 0,
    winHeight: 0,
    isShow: false,
    currentTab: 0,
  },

  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  },

  checkCor: function () {
    if (this.data.currentTab > 4) {
      this.setData({
        scrollleft: 300
      })
    } else {
      this.setData({
        scrollleft: 0
      })
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    /** 
     * 获取系统信息,系统宽高
     */
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          winWidth: res.windowWidth,
          winHeight: res.windowHeight
        });
      }
    });
    wx.request({
      url: app.globalData.url + '/Com_my_pingjia/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        user:app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            mypingjia: res.data
          })
        }
      }
    })
    wx.request({
      url: app.globalData.url + '/Com_pingjia_me/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        user:app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            stupingjia: res.data
          })
        }
      }
    })
  },

  toChange (e) {
    let that = this;
    let name = e.currentTarget.dataset.show;
    let param = {};
    param[name] = !that.data[name];
    that.setData({
      ...param
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