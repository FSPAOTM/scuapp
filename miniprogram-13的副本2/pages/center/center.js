// pages/center/center.js
//index.js
//获取应用实例
const app = getApp()
var openid = wx.getStorageSync("openid");
Page({
  data: {
    hasUserInfo: openid == ""
  },
 
  // 事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
 
})

