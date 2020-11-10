// pages/smyJob/smyJob.js
const app = getApp()
var openid = wx.getStorageSync("openid");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    iworkinfo: [],
    oworkinfo: [],
    //tap切换自定义宽高
    winWidth: 0,
    winHeight: 0,
    // tab切换，方法一

    scrollleft: 0,
    currentTab: 0,

  },


  /** 
   * 点击tab切换 方法一
   */
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
    let self = this;
    wx.request({
      url: app.globalData.url + '/Show_myijob/',
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        user:app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            iworkinfo: res.data
          })
        }
      }
    });
     wx.request({
      url: app.globalData.url + '/Show_myojob/',
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        user:app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            oworkinfo: res.data
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
    app.editTabBar();  
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