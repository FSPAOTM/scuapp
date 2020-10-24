// pages/infoModify/infoModify.js
var app = getApp()
Page({
 
  /**
   * 页面的初始数据
   */
  data: {
    myinfo:null,
    hiddenmodalput: true,
  },
 
  exit:function(e){
    wx.showModal({
      title: '提示',
      content: '是否确认退出',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          wx.removeStorageSync('student');
          //页面跳转
          wx.redirectTo({
            url: '../login/login',
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },

//点击按钮痰喘指定的hiddenmodalput弹出框
 
modalinput: function () {
 
this.setData({
 
hiddenmodalput:!this.data.hiddenmodalput,
})
 
},
 
//取消按钮
 
cancel: function () {
 
this.setData({
 
hiddenmodalput: true,
});
 
},
 
//确认
 
confirm: function () {
 
this.setData({
 
hiddenmodalput: true,

})
 
}
 
})