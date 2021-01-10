// pages/sjieguotongzhi/sjieguotongzhi.js学生确认录用结果
const app = getApp()
Page({
  data: {
    isShow: false,
    jieguotongzhi1: [],
    jieguotongzhi2: []
  },

  // 加载待确认的录用结果
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Stu_result_show/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        stu_id: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          var i
          for (i = 0; i < res.data.length; i++) {
            if (res.statusCode == 200) {
              if (res.data[i].type == "校内兼职") {
                that.data.jieguotongzhi1.push(res.data[i])
                that.setData({
                  jieguotongzhi1: that.data.jieguotongzhi1
                })
              } else if (res.data[i].type == "校外兼职") {
                that.data.jieguotongzhi2.push(res.data[i])
                that.setData({
                  jieguotongzhi2: that.data.jieguotongzhi2
                })
              }
            }
          }
          if (that.data.jieguotongzhi1.length == 0 && that.data.jieguotongzhi2.length == 0) {
            that.setData({
              isShow: true
            })
          }
        }
      }
    })
  },

  // 校内录用确认
  sure1(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi1[e].iw_number;
    var type = that.data.jieguotongzhi1[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/',
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type: type,
        number: number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          wx.showToast({
            title: '如需再次查看，请前往【我的兼职】',
            icon: 'none',
            duration: 3000
          })
        };
        setTimeout(function () {
          that.onRefresh()
        }, 3000)
      }
    })
  },

  // 校内未录用确认
  sure11(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi1[e].iw_number;
    var type = that.data.jieguotongzhi1[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/',
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type: type,
        number: number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          wx.showToast({
            title: '确认成功',
            icon: 'none',
            duration: 3000
          })
        };
        setTimeout(function () {
          that.onRefresh()
        }, 3000)
      }
    })
  },

  // 校外录用确认
  sure2(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi2[e].ow_number;
    var type = that.data.jieguotongzhi2[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/',
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type: type,
        number: number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          wx.showToast({
            title: '如需再次查看，请前往【我的兼职】',
            icon: 'none',
            duration: 3000
          })
        };
        setTimeout(function () {
          that.onRefresh()
        }, 3000)
      }
    })
  },

  // 校外未录用确认
  sure22(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi2[e].ow_number;
    var type = that.data.jieguotongzhi2[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/',
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type: type,
        number: number
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          wx.showToast({
            title: '确认成功',
            icon: 'none',
            duration: 3000
          })
        };
        setTimeout(function () {
          that.onRefresh()
        }, 3000)
      }
    })
  },

  // 刷新
  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    this.getData();
  },
  getData() {
    let that = this;
    that.setData({
      jieguotongzhi1: [],
      jieguotongzhi2: []
    })
    wx.request({
      url: app.globalData.url + '/Stu_result_show/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          var i;
          for (i = 0; i < res.data.length; i++) {
            if (res.statusCode == 200) {
              if (res.data[i].type == "校内兼职") {
                that.data.jieguotongzhi1.push(res.data[i])
                that.setData({
                  jieguotongzhi1: that.data.jieguotongzhi1
                })
              } else if (res.data[i].type == "校外兼职") {
                that.data.jieguotongzhi2.push(res.data[i])
                that.setData({
                  jieguotongzhi2: that.data.jieguotongzhi2
                })
              }
            }
          }
          if (that.data.jieguotongzhi1.length == 0 && that.data.jieguotongzhi2.length == 0) {
            that.setData({
              isShow: true
            })
          }
        }
        //隐藏loading 提示框
        wx.hideLoading();
        //隐藏导航条加载动画
        wx.hideNavigationBarLoading();
        //停止下拉刷新
        wx.stopPullDownRefresh();
      }
    })
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.onRefresh();
  }
})