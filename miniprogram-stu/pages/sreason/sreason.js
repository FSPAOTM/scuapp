// pages/sreason/sreason.js学生填写校外应聘理由
const app = getApp();
Page({
  data: {
    reason: "",
    ow_number: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      ow_number: app.globalData.ow_number
    })
    console.log(this.data.ow_number)
  },

  reasoninput(e) {
    this.setData({
      reason: e.detail.value
    })
  },

  formsubmit: function (e) {
    wx.request({
      url: app.globalData.url + '/Enroll_in_work/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        ow_number: this.data.ow_number,
        reason: this.data.reason,
        user: app.globalData.user,
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
          if (res.data == "报名成功") {
            wx.showToast({
              title: '报名成功',
              icon: 'success',
              duration: 2000
            })
            setTimeout(function () {
              wx.switchTab({
                url: '../smyJob/smyJob?currentTab=0',
              })
            }, 2000)
          } else if (res.data == "该学生已报名") {
            wx.showToast({
              title: '请勿重复报名！',
              icon: 'none',
              duration: 2000
            })
            setTimeout(function () {
              wx.switchTab({
                url: '../smyJob/smyJob?currentTab=0',
              })
            }, 2000)
          }
        }
      }
    })
  }
})