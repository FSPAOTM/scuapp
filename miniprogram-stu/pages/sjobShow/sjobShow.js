// pages/sjobShow/sjobShow.js日常查看兼职信息
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
    ps: "",
  },

  /**
   * 获取上一个列表界面所点击兼职的兼职号并展示详细兼职信息
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
              ps: res.data.ps,
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
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              post: res.data.post,
              time: res.data.time,
              detail: res.data.detail,
              salary: res.data.salary,
              description: res.data.description,
              ask: res.data.ask,
              num: res.data.num,
              ps: res.data.ps,
            })
          }
        }
      })
    }
  }
})