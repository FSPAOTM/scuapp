// pages/smyJob/smyJob.js//这一页只能显示3个工作【高度不对】
const app = getApp()
var openid = wx.getStorageSync("openid");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show: "",
    isShow: true,
    workinfo1: [],
    workinfo2: [],
    workinfo3: [],
    workinfo5: [],
    pingjia: "",
    //tap切换自定义宽高
    winWidth: 0,
    winHeight: 0,
    // tab切换，方法一

    scrollleft: 0,
    currentTab: 0,

  },


  /** 
   * 点击tab切换 方法一
   */
  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  },

  checkCor: function () {
    if (this.data.currentTab > 4) {
      this.setData({
        scrollleft: 300
      })
    } else {
      this.setData({
        scrollleft: 0
      })
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    if (options.currentTab != '') {
      that.setData({
        currentTab: options.currentTab
      })
    }
    that.setData({
      show: options.show
    })
    if (that.data.show == "refresh") {
      that.onRefresh();
    } else {
      /** 
       * 获取系统信息,系统宽高
       */
      wx.getSystemInfo({
        success: function (res) {
          that.setData({
            winWidth: res.windowWidth,
            winHeight: res.windowHeight
          });
        }
      });
      wx.request({
        url: app.globalData.url + '/Show_myjob/',
        header: {
          'Content-Type': 'application/json'
        },
        method: "GET",
        data: {
          user: app.globalData.user
        },
        success: function (res) {
          console.log(res);
          var i;
          for (i = 0; i < res.data.length; i++) {
            if (res.statusCode == 200) {
              if (res.data[i].status == "待审核") {
                that.data.workinfo1.push(res.data[i])
                that.setData({
                  workinfo1: that.data.workinfo1
                })
              } else if (res.data[i].status == "表筛通过") {
                that.data.workinfo1.push(res.data[i])
                that.setData({
                  workinfo1: that.data.workinfo1
                })
              } else if (res.data[i].status == "已报名") {
                that.data.workinfo1.push(res.data[i])
                that.setData({
                  workinfo1: that.data.workinfo1
                })
              } else if (res.data[i].status == "面试中") {
                that.data.workinfo2.push(res.data[i])
                that.setData({
                  workinfo2: that.data.workinfo2
                })
              } else if (res.data[i].status == "已录用") {
                that.data.workinfo3.push(res.data[i])
                that.setData({
                  workinfo3: that.data.workinfo3
                })
              } else if (res.data[i].status == "工作结束") {
                that.data.workinfo5.push(res.data[i])
                that.setData({
                  workinfo5: that.data.workinfo5
                })
              } else if (res.data[i].status == "待评价") {
                that.data.workinfo5.push(res.data[i])
                that.setData({
                  workinfo5: that.data.workinfo5
                })
              } else if (res.data[i].status == "已评价") {
                that.data.workinfo5.push(res.data[i])
                that.setData({
                  workinfo5: that.data.workinfo5
                })
              }
            }
          }
        }
      })
    }
  },

  xq1(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo1[e].type;
    if (that.data.workinfo1[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo1[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    } else {
      var ow_number = that.data.workinfo1[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    }
  },

  xq2(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo2[e].type;
    if (that.data.workinfo2[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo2[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    } else {
      var ow_number = that.data.workinfo2[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    }
  },

  ms(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.workinfo2[e].ow_number;
    console.log(ow_number);
    console.log("++++++", ev, that)
    wx.navigateTo({
      url: "../smianshixinxi/smianshixinxi?ow_number=" + ow_number
    })
  },

  ms3(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number = that.data.workinfo3[e].ow_number;
    console.log(ow_number);
    console.log("++++++", ev, that)
    wx.navigateTo({
      url: "../smianshixinxi/smianshixinxi?ow_number=" + ow_number
    })
  },

  ly(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    if (that.data.workinfo3[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo3[e].iw_number;
      console.log("++++++", ev, that)
      wx.navigateTo({
        url: "../sluyongxinxi/sluyongxinxi?iw_number=" + iw_number+"&ow_number=null"
      })
    } else {
      var ow_number = that.data.workinfo3[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.navigateTo({
        url: "../sluyongxinxi/sluyongxinxi?ow_number=" + ow_number+"&iw_number=null"
      })
    }
  },

  xq3(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo3[e].type;
    if (that.data.workinfo3[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo3[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    } else {
      var ow_number = that.data.workinfo3[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    }
  },

  

  xq5(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo5[e].type;
    if (that.data.workinfo5[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo5[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    } else {
      var ow_number = that.data.workinfo5[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sjobShow/sjobShow"
      })
    }
  },

  pingjia(ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    if (that.data.workinfo5[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo5[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.navigateTo({
        url: "../sfeedback/sfeedback"
      })
    } else {
      var ow_number = that.data.workinfo5[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.navigateTo({
        url: "../sfeedback/sfeedback"
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
    app.editTabBar();
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

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    wx.showLoading({
      title: '刷新中...',
      duration: 2000
    })
    this.getData();
  },
  //网络请求，获取数据
  getData() {
    let that = this;
    that.setData({
      workinfo1: [],
      workinfo2: [],
      workinfo3: [],
      workinfo5: []
    })
    wx.request({
      url: app.globalData.url + '/Show_myjob/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        var i;
        for (i = 0; i < res.data.length; i++) {
          if (res.statusCode == 200) {
            if (res.data[i].status == "待审核") {
              that.data.workinfo1.push(res.data[i])
              that.setData({
                workinfo1: that.data.workinfo1
              })
            } else if (res.data[i].status == "表筛通过") {
              that.data.workinfo1.push(res.data[i])
              that.setData({
                workinfo1: that.data.workinfo1
              })
            } else if (res.data[i].status == "已报名") {
              that.data.workinfo1.push(res.data[i])
              that.setData({
                workinfo1: that.data.workinfo1
              })
            } else if (res.data[i].status == "面试中") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "已录用") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "待评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            } else if (res.data[i].status == "已评价") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            }
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
    //调用刷新时将执行的方法
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