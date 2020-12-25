// pages/sbaoming/sbaoming.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
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
   * 生命周期函数--监听页面加载
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
    } else /* if(this.data.iw_number!=null)*/ {
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
              ddl: res.data.ddl,
              ps: res.data.ps,
              already: res.data.already,
            })
          }
        }
      })
    }
  },

spingjiashow(){
  wx.navigateTo({
    url: '../spingjiashow/spingjiashow?ow_number='+this.data.ow_number,
  })
},

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
                  url: '../smyJob/smyJob?show=refresh&currentTab=0',
                })
              }, 2000)
            }else if(res.data == "该学生已报名"){
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