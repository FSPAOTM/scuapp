// pages/cresumeDecide/cresumeDecide.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    myinfo: null,
    hiddenmodalput: true,
    hiddenmodalput2: true,
    ow_number: "",
    stu_number: "",
    ap_time: "",
    name: "",
    age: "",
    gender: "",
    edu: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
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

    var stu_number = -1
    var stu_number = wx.getStorageSync("stu_number");
    wx.removeStorageSync("stu_number");
    this.setData({
      stu_number: stu_number
    })
    console.log(this.data.stu_number)

    var ap_time = -1
    var ap_time = wx.getStorageSync("ap_time");
    wx.removeStorageSync("ap_time");
    this.setData({
      ap_time: ap_time
    })
    console.log(this.data.ap_time)
    wx.request({
      url: app.globalData.url + '/Show_outwork_detail/', //*待修改
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        stu_number: this.data.stu_number
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
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

  //确认

  confirm1: function () {
    wx.request({
      url: app.globalData.url + '/Reset_myinfo_name/', //待修改：状态改为“已通过”
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        user: app.globalData.user,
        ow_number: this.data.ow_number,
        stu_number: this.data.stu_number,
        ap_time: this.data.ap_time,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.reLaunch({
            url: '../cworkspace/cworkspace',
          })
          this.setData({

            hiddenmodalput: true,
            hiddenmodalput2: true,
      
          })
        }
      }
    })
  },

  confirm2: function () {
    wx.request({
      url: app.globalData.url + '/Reset_myinfo_name/', //待修改：状态改为“未通过”
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        user: app.globalData.user,
        ow_number: this.data.ow_number,
        stu_number: this.data.stu_number,
        ap_time: this.data.ap_time,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.reLaunch({
            url: '../cworkspace/cworkspace',
          })
          this.setData({

            hiddenmodalput: true,
            hiddenmodalput2: true,
      
          })
        }
      }
    })
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