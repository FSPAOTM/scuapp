// pages/ccenter/ccenter.js企业端个人中心
const app = getApp();
Page({
  data: {
    name: "",
    phone: "",
  },

  // 企业详细信息完善入口
  infofill() {
    wx.navigateTo({
      url: '../cinfoFill/cinfoFill'
    })
  },

  // 查看我的历史评价和评价我的
  cpingjia() {
    wx.navigateTo({
      url: '../cpingjia/cpingjia'
    })
  },

  // 退出登录
  exitlogin() {
    wx.redirectTo({
      url: '../index/index'
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: app.globalData.url + '/Show_company_name/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        phone: app.globalData.user,
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

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    app.editTabBar();
  }
})