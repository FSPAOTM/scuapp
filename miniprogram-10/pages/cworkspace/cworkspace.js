// pages/cworkspace/cworkspace.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //tap切换自定义宽高
    winWidth: 0,
    winHeight: 0,
    // tab切换，方法一

    scrollleft: 0,
    currentTab: 0,

    idArr: [

    ],
    details: [{
        position: 'XXX职位',
        title: '王雨欣 2018141093040',
      },

      {
        position: 'XXX职位',
        title: '姓名 12345565676',
      },
      {
        position: 'XXX职位',
        title: '姓名 12345565676',
      },

      {
        position: 'XXX职位',
        title: '姓名 12345565676',
      },
    ],
  },

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
  },

  itemSelected: function (e) {
    var index = e.currentTarget.dataset.index;
    var item = this.data.details[index];
    item.isSelected = !item.isSelected;
    this.setData({
      details: this.data.details,
    });
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
    app.editTabBar1();  
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