// pages/pingjia/pingjia.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    stupingjia: [],
    mypingjia: [],
    winWidth: 0,
    winHeight: 0,
    isShow1: [],
    isShow2: [],
    //isShow: false,
    currentTab: 0,
    count1: 0,
    count2: 0
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
      data: {
        user: app.globalData.user
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
      data: {
        user: app.globalData.user
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

  toChange(e) {
    let that = this;
    var j =that.data.count1+1
    that.setData({
      count1: j
    })
    //let name = e.currentTarget.dataset.show;
    let id = e.currentTarget.dataset.index
    if (that.data.count1 == 1) {
      var i;
      var middle = []
      for (i = 0; i < that.data.mypingjia.length; i++) {
        middle[i] = false
      }
      middle[id] = !middle[id]
      that.setData({
        isShow1: middle
      })
    } else {
      var middle1 = that.data.isShow1
      middle1[id] = !middle1[id]
      that.setData({
        isShow1: middle1
      })
    }
    //that.data.isShow[id] = !that.data.isShow[id]
    //let param = {};
    //param[name] = !that.data[name];
    // that.setData({
    //...param
    //})
  },

  toChange2(e) {
    let that = this;
    var j =that.data.count2+1
    that.setData({
      count2: j
    })
    //let name = e.currentTarget.dataset.show;
    let id = e.currentTarget.dataset.index
    if (that.data.count2 == 1) {
      var i;
      var middle = []
      for (i = 0; i < that.data.stupingjia.length; i++) {
        middle[i] = false
      }
      middle[id] = !middle[id]
      that.setData({
        isShow2: middle
      })
    } else {
      var middle1 = that.data.isShow2
      middle1[id] = !middle1[id]
      that.setData({
        isShow2: middle1
      })
    }
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