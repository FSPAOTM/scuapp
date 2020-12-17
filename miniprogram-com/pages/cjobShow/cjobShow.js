// pages/cjobShow/cjobShow.js
//还有已报名人数
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show1: true,
    show2: true,
    show3: true,
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

  //点击按钮痰喘指定的hiddenmodalput弹出框


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var ow_number = wx.getStorageSync("ow_number");
    this.setData({
      ow_number: ow_number,
      show1: (options.show1 == 'true') ? true : false,
      show2: (options.show2 == 'true') ? true : false,
      show3: (options.show3 == 'true') ? true : false
    })
    console.log(this.data.show2)
    /*console.log("接收到的参数是post=" + options.jobinfo)
    this.setData({
      jobinfo: JSON.parse(options.jobinfo),
      ow_number:JSON.parse(options.ow_number),
      post: JSON.parse(options.post),
      time: JSON.parse(options.time),
      location:JSON.parse(options.location),
      detail: JSON.parse(options.detail),
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
  },


  cjobrelease1() {
    let that = this;
    wx.navigateTo({
      url: '../cjobModify/cjobModify?post=' + that.data.post + '&ow_number=' + that.data.ow_number + '&time=' + that.data.time + '&location=' + that.data.location + '&detail=' + that.data.detail + '&salary=' + that.data.salary + '&description=' + that.data.description + '&ask=' + that.data.ask + '&num=' + that.data.num + '&ddl=' + that.data.ddl + '&ps=' + that.data.ps + '&show01=true&show02=false',
    })
  },

  cjobrelease2() {
    let that = this;
    wx.navigateTo({
      url: '../cjobModify/cjobModify?post=' + that.data.post + '&ow_number=' + that.data.ow_number + '&time=' + that.data.time + '&location=' + that.data.location + '&detail=' + that.data.detail + '&salary=' + that.data.salary + '&description=' + that.data.description + '&ask=' + that.data.ask + '&num=' + that.data.num + '&ddl=' + that.data.ddl + '&ps=' + that.data.ps + '&show01=false&show02=true',
    })
  },

  cinterview(){
    wx.navigateTo({
      url: "../cinterview/cinterview?ow_number=" + this.data.ow_number+ '&user=' + app.globalData.user+'&post=' + this.data.post
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