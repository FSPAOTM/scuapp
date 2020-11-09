// pages/sbaoming/sbaoming.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    iw_number:"",
    ow_number: "",
    post: "",
    time: "",
    location: "",
    detail: "",
    salary: "",
    description: "",
    ask: "",
    num: "",
    ddl: "",
    ps: "",
    already: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var ow_number = wx.getStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
    var iw_number = wx.getStorageSync("iw_number");
    this.setData({
      iw_number: iw_number
    })
    if(this.data.ow_number!=null){
    wx.request({
      url: app.globalData.url + '/Show_outwork_detail/',/*待修改*/
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        ow_number: ow_number,
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
          this.setData({
            post: res.data.post,
            time: res.data.time,
            /*location: res.data.location,*/
            detail: res.data.detail,
            salary: res.data.salary,
            description: res.data.description,
            ask: res.data.ask,
            num: res.data.num,
            ddl: res.data.ddl,
            ps: res.data.ps,
            already: res.data.already,
          })
        }
      }
    })
  }else if(this.data.iw_number!=null){
    wx.request({
      url: app.globalData.url + '/Show_inwork_detail/',/*待修改*/
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        iw_number: iw_number,
      },
      success: (res) => {
        /*console.log(res.data);*/
        if (res.statusCode == 200) {
          this.setData({
            post: res.data.post,
            time: res.data.time,
            detail: res.data.detail,
            salary: res.data.salary,
            description: res.data.description,
            ask: res.data.ask,
            num: res.data.num,
            ddl: res.data.ddl,
            ps: res.data.ps,
            already: res.data.already,
          })
        }
      }
    })
  }
  },


  reason(){
    wx.navigateTo({
      url: '../sreason/sreason',
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