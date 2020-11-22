// pages/smyJob/smyJob.js
const app = getApp()
var openid = wx.getStorageSync("openid");
Page({

  /**
   * 页面的初始数据
   */
  data: {
    /*iworkinfo: [
      {
        type:"校内",
        title:"信息管理中心值班人员",
        depart:"信息管理中心",
      }
    ],*/
    workinfo1: [],
    workinfo2: [],
    workinfo3: [],
    workinfo4: [],
    workinfo5: [],
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
    let self = this;
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
        if (res.statusCode == 200) {
          if (res.data.status == "已报名")  {
            self.setData({
              workinfo1: res.data
            })
          } else if (res.data.status == "面试中") /*待修改*/ {
            self.setData({
              workinfo2: res.data
            })
          } else if (res.data.status == "已录用") /*待修改*/ {
            self.setData({
              workinfo3: res.data
            })
          } else if (res.data.status == "已到岗") /*待修改*/ {
            self.setData({
              workinfo4: res.data
            })
          } else if (res.data.status == "已结算") /*待修改*/ {
            self.setData({
              workinfo5: res.data
            })
          }
        }
      }
    });
    /*wx.request({
      url: app.globalData.url + '/Show_myojob/',
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        user:app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            oworkinfo: res.data
          })
        }
      }
    })*/
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
    })
    this.getData();
  },
  //网络请求，获取数据
  getData() {
    let self = this;
    wx.request({
      url: app.globalData.url + '/Show_mywork/',
      /*待修改*/
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          if (res.data.status == "已报名") /*待修改*/ {
            self.setData({
              workinfo1: res.data
            })
          } else if (res.data.status == "面试中") /*待修改*/ {
            self.setData({
              workinfo2: res.data
            })
          } else if (res.data.status == "已录用") /*待修改*/ {
            self.setData({
              workinfo3: res.data
            })
          } else if (res.data.status == "已到岗") /*待修改*/ {
            self.setData({
              workinfo4: res.data
            })
          } else if (res.data.status == "已结算") /*待修改*/ {
            self.setData({
              workinfo5: res.data
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