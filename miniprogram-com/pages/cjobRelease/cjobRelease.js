// pages/cjobRelease/cjobRelease.js
var dateTimePicker = require('outer3.js');
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    judge: "",
    company: "",
    ow_number: "",
    Name: "",
    jobtime: "",
    location: "",
    detail: "",
    description: "",
    salary: "",
    ask: "",
    num: "",
    endingtime: "",
    ps: "",
    dateTimeArray: null,
    dateTime: null,
    dateTimeArray1: null,
    dateTime1: null,
    startYear: 2020,
    endYear: 2021
  },

  onLoad: function (options) {
    // 获取完整的年月日 时分秒，以及默认显示的数组
    var obj = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    var obj1 = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    // 精确到分的处理，将数组的秒去掉
    var lastArray = obj1.dateTimeArray.pop();
    var lastTime = obj1.dateTime.pop();

    this.setData({
      dateTime: obj.dateTime,
      dateTimeArray: obj.dateTimeArray,
      dateTimeArray1: obj1.dateTimeArray,
      dateTime1: obj1.dateTime
    });
  },

  
  changeDateTimeColumn1(e) {
    var arr = this.data.dateTime1,
      dateArr = this.data.dateTimeArray1;

    arr[e.detail.column] = e.detail.value;
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);

    this.setData({
      dateTimeArray1: dateArr,
      dateTime1: arr,
      endingtime:(2020+arr[0]) +"-"+ (1+arr[1]) +"-"+ (1+arr[2]) +" "+ arr[3] +":"+ arr[4]
    });
  },


  blurname: function (e) {
    this.setData({
      Name: e.detail.value
    })
  },

  blurjobtime: function (e) {
    this.setData({
      jobtime: e.detail.value
    })
  },

  blurlocation: function (e) {
    this.setData({
      location: e.detail.value
    })
  },


  blurdetail: function (e) {
    this.setData({
      detail: e.detail.value
    })
  },


  blurdescription: function (e) {
    this.setData({
      description: e.detail.value
    })
  },

  blursalary: function (e) {
    this.setData({
      salary: e.detail.value
    })
  },

  blurask: function (e) {
    this.setData({
      ask: e.detail.value
    })
  },

  blurnum: function (e) {
    this.setData({
      num: e.detail.value
    })
  },

  blurps: function (e) {
    this.setData({
      ps: e.detail.value
    })
    var ps=this.data.ps
  },

  formSubmit: function (e) {
    let that = this;
    if (this.data.Name.length == 0) {
      wx.showToast({
        title: '岗位名称不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.jobtime.length == 0) {
      wx.showToast({
        title: '工作时间不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.location.length == 0) {
      wx.showToast({
        title: '工作地点所在地区不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.detail == null) {
      wx.showToast({
        title: '工作详细地址不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.description.length == 0) {
      wx.showToast({
        title: '职位描述不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.salary.length == 0) {
      wx.showToast({
        title: '薪酬不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.ask.length == 0) {
      wx.showToast({
        title: '招聘要求不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.num.length == 0) {
      wx.showToast({
        title: '招聘人数不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.endingtime.length == 0) {
      wx.showToast({
        title: '报名截止时间不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else {
      wx.request({
        url: app.globalData.url + '/Part_time_post/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          company: app.globalData.user,
          Name: that.data.Name,
          jobtime: that.data.jobtime,
          location: that.data.location,
          detail: that.data.detail,
          description: that.data.description,
          salary: that.data.salary,
          ask: that.data.ask,
          num: that.data.num,
          endingtime: that.data.endingtime,
          ps: that.data.ps,
        },
        success: (res) => {
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data == "发布成功") {
              wx.showToast({
                title: '提交成功！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.switchTab({
                  url: '../cfabu/cfabu?show=refresh',
                })
              }, 2000)
            }
          } else {
            wx.showToast({
              title: '请求错误',
              icon: 'none',
              duration: 1000
            })
          }
        }
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