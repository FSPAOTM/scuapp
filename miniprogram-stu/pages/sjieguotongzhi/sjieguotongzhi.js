// pages/sjieguotongzhi/sjieguotongzhi.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isShow: false,
    jieguotongzhi1:[],
    jieguotongzhi2:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
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

  sure1(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi1[e].number;
    var type = that.data.jieguotongzhi1[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/', //待修改
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type:type,
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

  sure2(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var number = that.data.jieguotongzhi2[e].number;
    var type = that.data.jieguotongzhi2[e].type;
    console.log("++++++", ev, that)
    wx.request({
      url: app.globalData.url + '/Stu_result_sure/', //待修改
      method: "POST",
      header: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      data: {
        user: app.globalData.user,
        type:type,
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

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    this.getData();
  },
  getData() {
    let that = this;
    that.setData({
      jieguotongzhi1:[],
      jieguotongzhi2:[]
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
    this.onRefresh();
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