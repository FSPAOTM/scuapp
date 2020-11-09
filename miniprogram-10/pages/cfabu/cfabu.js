// pages/cfabu/cfabu.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    jobinfo: [],
  },

  fabu() {
    wx.navigateTo({
      url: '../cjobRelease/cjobRelease',
    })
  },

  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let self = this;
    wx.request({
      url: app.globalData.url + '/Get_outwork_info/',
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
          self.setData({
            jobinfo: res.data
          })

        }
      }
    })
  },


  cjobshow: function (ev) {
    var that = this;
    console.log(that.data.jobinfo);
    var e = ev.currentTarget.dataset.index;
    console.log(e);
    console.log(that.data.jobinfo[e]);
    var ow_number=that.data.jobinfo[e].ow_number;
    console.log("++++++", ev, that)
    wx.setStorageSync("ow_number", ow_number), wx.navigateTo({
      url: "../cjobShow/cjobShow"
    })
  },
/*
  cjobshow: function (ev) {
    var that = this;
    var e = ev.currentTarget.dataset.id;
    console.log("++++++", ev, that)
    wx.setStorageSync("job_id", e), wx.navigateTo({
      url: "../cjobShow/cjobShow?jobinfo=" + JSON.stringify(infojob)
    })
  },*/
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    if (typeof this.getTabBar === 'function' && this.getTabBar()) {
      this.getTabBar().setData({
        selected: 1 //选中效果 当前tabBar页面在list中对应的下标， 
      })
    }
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