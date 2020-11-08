// pages/repwd1/repwd1.js
var app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    user:"",
    phone:"",
  },

  usser(e){
    this.setData({
      user:e.detail.value
    });
    app.globalData.user=this.data.user;
  },

  phhone(e){
    this.setData({
      phone:e.detail.value
    })
  },

formSubmit(){
  wx.request({
    url: app.globalData.url + '/Reset_password_f1/',
    header: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    method: "POST",
    data: {
      user: this.data.user,
      phone:this.data.phone,
    },
    success: (res) => {
      if (res.statusCode == 200) {
        console.log(res.data);
        if(res.data=="身份验证失败"){
          wx.showToast({
            title: '身份信息有误，请重新输入！',
            icon: 'none',
            duration: 3000
          })
          wx.redirectTo({
            url: '../repwd1/repwd1',
          })
        }else{
          if(res.data=="身份验证成功"){
            wx.redirectTo({
              url: '../repwd1-1/repwd1-1',
            })
          }else{
            wx.showToast({
              title: '请求错误',
              icon: 'none',
              duration: 1000
            })
          }
        }
      }
    }
  })
},


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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