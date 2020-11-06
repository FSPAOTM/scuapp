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
    url: 'http://127.0.0.1:8000/wechat/Insert_resume_show/',/*待修改*/
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
        if(res.data="身份信息有误"){
          wx.showToast({
            title: '身份信息有误，请重新输入！',
            icon: 'none',
            duration: 1000
          })
          wx.redirectTo({
            url: '../repwd1/repwd1',
          })
        }else{
          if(res.data="信息核验正确"){
            wx.redirectTo({
              url: '../repwd1-1/repwd1-1',
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