// pages/sbaoming/sbaoming.js工作详情界面，可看评价可报名
var app = getApp();
Page({
  data: {
    type: "",
    iw_number: "",
    ow_number: "",
    post: "",
    time: "",
    location: "",
    detail: "",
    salary: "",
    description: "",
    ask: "",
    num: "",
    ddl: "",
    ps: "",
    already: "",
  },

  /**
   * 加载工作信息
   */
  onLoad: function (options) {
    var ow_number = -1
    var ow_number = wx.getStorageSync("ow_number");
    app.globalData.ow_number = ow_number;
    wx.removeStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
    console.log(this.data.ow_number)
    var iw_number = -1
    var iw_number = wx.getStorageSync("iw_number");
    wx.removeStorageSync("iw_number");
    this.setData({
      iw_number: iw_number
    })
    var type = wx.getStorageSync("type");
    wx.removeStorageSync("type");
    this.setData({
      type: type
    })
    console.log(ow_number)
    if (type == "校外") {
      wx.request({
        url: app.globalData.url + '/Show_outwork_detail/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          ow_number: ow_number,
        },
        success: (res) => {
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              post: res.data.post,
              time: res.data.time,
              location: res.data.location,
              detail: res.data.location + res.data.detail,
              salary: res.data.salary,
              description: res.data.description,
              ask: res.data.ask,
              num: res.data.num,
              ddl: res.data.ddl,
              ps: res.data.ps,
              already: res.data.already,
            })
          }
        }
      })
    } else {
      wx.request({
        url: app.globalData.url + '/Show_inwork_detail/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          iw_number: iw_number,
        },
        success: (res) => {
          if (res.statusCode == 200) {
            this.setData({
              post: res.data.post,
              time: res.data.time,
              detail: res.data.detail,
              salary: res.data.salary,
              description: res.data.description,
              ask: res.data.ask,
              num: res.data.num,
              ddl: res.data.ddl,
              ps: res.data.ps,
              already: res.data.already,
            })
          }
        }
      })
    }
  },

  // 点击查看公司历史评价
  spingjiashow() {
    wx.navigateTo({
      url: '../spingjiashow/spingjiashow?ow_number=' + this.data.ow_number,
    })
  },

  // 点击报名
  reason() {
    if (this.data.type == "校内") {
      wx.request({
        url: app.globalData.url + '/Enroll_in_inwork/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          iw_number: this.data.iw_number,
          user: app.globalData.user,
        },
        success: (res) => {
          if (res.statusCode == 200) {
            if (res.data == "报名成功") {
              wx.showToast({
                title: '报名成功',
                icon: 'success',
                duration: 2000
              })
              setTimeout(function () {
                wx.switchTab({
                  url: '../smyJob/smyJob?show=refresh&currentTab=0',
                })
              }, 2000)
            } else if (res.data == "该学生已报名") {
              wx.showToast({
                title: '请勿重复报名',
                icon: 'none',
                duration: 2000
              })
            }
          }
        }
      })
    } else {
      wx.navigateTo({
        url: '../sreason/sreason',
      })
    }
  }
})