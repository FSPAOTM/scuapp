// pages/cjobShow/cjobShow.js
//还有已报名人数
Page({

  /**
   * 页面的初始数据
   */
  data: {
    post: "",
    time: "",
    location_detail: "",
    salary: "",
    description: "",
    ask: "",
    num: "",
    ddl: "",
    ps: "",
    already: "",
  },

  //点击按钮痰喘指定的hiddenmodalput弹出框


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log("接收到的参数是post=" + options.post)
    this.setData ({
      post: options.post,
      time: options.time,
      location_detail: options.location_detail,
      salary: options.salary,
      description: options.description,
      ask: options.ask,
      num: options.num,
      ddl: options.ddl,
      ps: options.ps,
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