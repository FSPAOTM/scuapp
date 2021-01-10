// pages/smianshitongzhi/smianshitongzhi.js学生查看未确认的面试通知
const app = getApp()
Page({
  data: {
    isShow: false,
    user: "",
    mianshitongzhi: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/',
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
            mianshitongzhi: res.data
          })
        }
        if (that.data.mianshitongzhi.length == 0) {
          that.setData({
            isShow: true
          })
        }
      }
    })
  },

  sure(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.mianshitongzhi[e].ow_number;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_sure/',
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        ow_number: ow_number
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

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    this.getData();
  },
  getData() {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/', //res.data里面包括post/time/place/ow_number
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
            mianshitongzhi: res.data
          })
        }
        if (that.data.mianshitongzhi.length == 0) {
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