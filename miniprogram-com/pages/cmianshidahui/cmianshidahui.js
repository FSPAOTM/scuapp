// pages/cmianshidahui/cmianshidahui.js企业兼职或面试申请打回确认
const app = getApp()
Page({
  data: {
    isShow: false,
    user: "",
    mianshidahui: []
  },

  // 显示未确认的打回通知
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Com_interview_back_show/',
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
          that.setData({
            mianshidahui: res.data
          })
        }
        if (that.data.mianshidahui.length == 0) {
          that.setData({
            isShow: true
          })
        }
      }
    })
  },

  // 修改申请入口
  reapply(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.mianshidahui[e].ow_number;
    console.log("++++++", ev, that)
    if (that.data.mianshidahui[e].type == "面试申请") {
      wx.navigateTo({
        url: '../cinterviewModify/cinterviewModify?ow_number=' + ow_number,
      })
    } else if (that.data.mianshidahui[e].type == "兼职申请") {
      wx.navigateTo({
        url: '../cjobModify/cjobModify?ow_number=' + ow_number + '&show02=true&operation=dahui', //差接口
      })
    }
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
    wx.request({
      url: app.globalData.url + '/Com_interview_back_show/',
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
          that.setData({
            mianshidahui: res.data
          })
        }
        if (that.data.mianshidahui.length == 0) {
          that.setData({
            isShow: true
          })
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