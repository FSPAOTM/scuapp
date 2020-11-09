// pages/cjobShow/cjobShow.js
//还有已报名人数
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    ow_number: "",
    post: "",
    time: "",
    location: "",
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
    var ow_number = wx.getStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
    /*console.log("接收到的参数是post=" + options.jobinfo)
    this.setData({
      jobinfo: JSON.parse(options.jobinfo),
      ow_number:JSON.parse(options.ow_number),
      post: JSON.parse(options.post),
      time: JSON.parse(options.time),
      location:JSON.parse(options.location),
      location_detail: JSON.parse(options.location_detail),
      salary: JSON.parse(options.salary),
      description: JSON.parse(options.description),
      ask: JSON.parse(options.ask),
      num: JSON.parse(options.num),
      ddl: JSON.parse(options.ddl),
      ps: JSON.parse(options.ps),
      already: JSON.parse(options.already),
    })*/
    wx.request({
      url: app.globalData.url + '/Get_outwork_detail_info/',
      /*待修改*/
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
            location: res.data.location,
            location_detail: res.data.location_detail,
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
  },


  cjobrelease() {
    let that = this;
    wx.navigateTo({
      url: '../cjobRelease/cjobRelease?post=' + that.data.post + '&ow_number=' + that.data.ow_number + '&time=' + that.data.time + '&location=' + that.data.location + '&location_detail=' + that.data.location_detail + '&salary=' + that.data.salary + '&description=' + that.data.description + '&ask=' + that.data.ask + '&num=' + that.data.num + '&ddl=' + that.data.ddl + '&ps=' + that.data.ps,
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