const app = getApp()
var openid = wx.getStorageSync("openid");
Page({
data: {
    
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

},
})
