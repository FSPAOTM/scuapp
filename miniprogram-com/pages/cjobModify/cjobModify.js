// pages/cjobModify/cjobModify.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show01:false,
    show02:false,
    company: "",
    ow_number:"",
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
  },

  onLoad: function (options) {
    this.setData({
      ow_number:options.ow_number,
      Name: options.post,
      jobtime: options.time,
      location: options.location,
      detail: options.detail,
      salary: options.salary,
      description: options.description,
      ask: options.ask,
      num: options.num,
      endingtime: options.ddl,
      ps: options.ps,
      show01: (options.show01 == 'true') ? true : false,
      show02: (options.show02 == 'true') ? true : false,
    })
    console.log(this.data.show01)
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

  blurendingtime: function (e) {
    this.setData({
      endingtime: e.detail.value
    })
  },

  blurps: function (e) {
    this.setData({
      ps: e.detail.value
    })
  },

  formSubmit1: function (e) {
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
    } else{
      wx.request({
        url: app.globalData.url + '/Modify_outwork_info/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          ow_number:that.data.ow_number,
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
            if (res.data == "修改成功") {
              wx.showToast({
                title: '修改成功！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.navigateTo({
                  url: '../cfabu/cfabu',
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

  formSubmit2: function (e) {
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
                title: '提交成功！！！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.navigateTo({
                  url: '../cfabu/cfabu',
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