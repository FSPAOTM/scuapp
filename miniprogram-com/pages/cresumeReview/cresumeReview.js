// pages/cresumeReview/cresumeReview.js学生简历审核（表筛）
const app = getApp()
Page({
  data: {
    myinfo: null,
    hiddenmodalput: true,
    hiddenmodalput2: true,
    status: "",
    ow_number: "",
    stu_number: "",
    name: "",
    age: "",
    gender: "",
    edu: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
    reason: ""
  },

  // 显示列表页所点击学生简历
  onLoad: function (options) {
    var ow_number = -1
    var ow_number = wx.getStorageSync("ow_number");
    app.globalData.ow_number = ow_number;
    wx.removeStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
    console.log(this.data.ow_number)

    var stu_number = -1
    var stu_number = wx.getStorageSync("stu_number");
    wx.removeStorageSync("stu_number");
    this.setData({
      stu_number: stu_number
    })
    console.log(this.data.stu_number)

    wx.request({
      url: app.globalData.url + '/Com_Insert_resume_show/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        stuNumber: this.data.stu_number,
        ow_number: this.data.ow_number
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
          console.log(res.data)
          this.setData({
            name: res.data.name,
            age: res.data.age,
            gender: res.data.sex,
            tech: res.data.res_asses,
            edu: res.data.res_edu,
            job: res.data.res_work,
            project: res.data.res_proj,
            practice: res.data.res_extra,
            works: res.data.res_per,
            reason: res.data.reason
          })
        }
      }
    })
  },



  modalinput: function () {

    this.setData({
      hiddenmodalput: !this.data.hiddenmodalput,
    })
  },

  modalinput2: function () {

    this.setData({
      hiddenmodalput2: !this.data.hiddenmodalput2,
    })

  },

  //取消按钮

  cancel: function () {

    this.setData({
      hiddenmodalput: true,
      hiddenmodalput2: true,
    });

  },

  //确认，通过
  confirm1: function () {
    wx.request({
      url: app.globalData.url + '/Modify_applystatus/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        status: "已通过",
        ow_number: this.data.ow_number,
        stu_number: this.data.stu_number,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.reLaunch({
            url: '../cworkspace/cworkspace?currentTab=2',
          })
          this.setData({
            hiddenmodalput: true,
            hiddenmodalput2: true,
          })
        }
      }
    })
  },

  // 确认，未通过
  confirm2: function () {
    wx.request({
      url: app.globalData.url + '/Modify_applystatus/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        status: "未通过",
        ow_number: this.data.ow_number,
        stu_number: this.data.stu_number,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.reLaunch({
            url: '../cworkspace/cworkspace?currentTab=1',
          })
          this.setData({
            hiddenmodalput: true,
            hiddenmodalput2: true,
          })
        }
      }
    })
  }
})