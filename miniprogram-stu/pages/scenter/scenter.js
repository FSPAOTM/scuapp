// pages/scenter/scenter.js学生个人中心
//获取应用实例
const app = getApp()
Page({

  data: {
    sno: "",
    name: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: app.globalData.url + '/Show_student_name/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        sno: app.globalData.user,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            name: res.data.name,
          })
        }
      }
    })
  },

  // 点击修改个人信息
  infoModify() {
    wx.navigateTo({
      url: '../sinfoModify/sinfoModify'
    })
  },

  // 点击填写在线简历
  infoFill() {
    wx.navigateTo({
      url: '../sinfoShow/sinfoShow'
    })
  },

  // 点击退出登录
  exitlogin() {
    this.dislinkSocket();
    wx.redirectTo({
      url: '../index/index'
    })
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    app.editTabBar();
  }
})