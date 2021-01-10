// pages/cjobShow/cjobShow.js企业查看已发布兼职详细信息
const app = getApp();
Page({
  data: {
    show1: true,
    show2: true,
    show3: true,
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

  // 显示兼职详细信息
  onLoad: function (options) {
    var ow_number = wx.getStorageSync("ow_number");
    this.setData({
      ow_number: ow_number,
      show1: (options.show1 == 'true') ? true : false,
      show2: (options.show2 == 'true') ? true : false,
      show3: (options.show3 == 'true') ? true : false
    })
    wx.request({
      url: app.globalData.url + '/Get_outwork_detail_info/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        ow_number: ow_number,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          this.setData({
            post: res.data.post,
            time: res.data.time,
            location: res.data.location,
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
  },

  // 根据工作状态不同判断下一步操作
  // 修改兼职申请入口
  cjobrelease1() {
    let that = this;
    wx.navigateTo({
      url: '../cjobModify/cjobModify?post=' + that.data.post + '&ow_number=' + that.data.ow_number + '&time=' + that.data.time + '&location=' + that.data.location + '&detail=' + that.data.detail + '&salary=' + that.data.salary + '&description=' + that.data.description + '&ask=' + that.data.ask + '&num=' + that.data.num + '&ddl=' + that.data.ddl + '&ps=' + that.data.ps + '&show01=true&show02=false',
    })
  },

  // 再次发布
  cjobrelease2() {
    let that = this;
    wx.navigateTo({
      url: '../cjobModify/cjobModify?post=' + that.data.post + '&ow_number=' + that.data.ow_number + '&time=' + that.data.time + '&location=' + that.data.location + '&detail=' + that.data.detail + '&salary=' + that.data.salary + '&description=' + that.data.description + '&ask=' + that.data.ask + '&num=' + that.data.num + '&ddl=' + that.data.ddl + '&ps=' + that.data.ps + '&show01=false&show02=true',
    })
  },

  // 申请面试时间
  cinterview() {
    wx.navigateTo({
      url: "../cinterview/cinterview?ow_number=" + this.data.ow_number + '&user=' + app.globalData.user + '&post=' + this.data.post
    })
  }
})