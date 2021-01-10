// pages/pingjia/pingjia.js企业查看我的和评价我的历史评价
const app = getApp()
Page({
  data: {
    stupingjia: [],
    mypingjia: [],
    winWidth: 0,
    winHeight: 0,
    isShow1: [],
    isShow2: [],
    currentTab: 0,
    count1: 0,
    count2: 0
  },

  // 切换子tab
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

  // 显示评价
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

  // 折叠列表的收缩与展开1
  toChange(e) {
    let that = this;
    var j = that.data.count1 + 1
    that.setData({
      count1: j
    })
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
  },

  // 折叠列表的收缩与展开2
  toChange2(e) {
    let that = this;
    var j = that.data.count2 + 1
    that.setData({
      count2: j
    })
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
  }
})