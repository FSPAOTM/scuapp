// pages/sfeedback/sfeedback.js
const app = getApp();
Page({
  data: {
    staticImg: app.globalData.staticImg,
    ow_number: "",
    iw_number: "",
    current: 0,
    attitude: true,
    time: true,
    efficiency: true,
    environment: true,
    professional: true,
    trust: "",
    timely: "",
    flexible: "",
    salary: "",
    meaning: "",
    more:"",
    content:"",
    code: 1,
    code1: 2,
    userStars: [
      "sx.png",
      "sx.png",
      "sx.png",
      "sx.png",
      "sx.png",
    ],
    wjxScore: 5,
    // textarea
    max: 200, //最多字数 (根据自己需求改变)
    pics: [],
  },
  // 星星点击事件
  starTap: function (e) {
    var that = this;
    var index = e.currentTarget.dataset.index; // 获取当前点击的是第几颗星星
    var tempUserStars = this.data.userStars; // 暂存星星数组
    var len = tempUserStars.length; // 获取星星数组的长度
    for (var i = 0; i < len; i++) {
      if (i <= index) { // 小于等于index的是满心
        tempUserStars[i] = "sx.png";
        that.setData({
          wjxScore: i + 1,
        })
      } else { // 其他是空心
        tempUserStars[i] = "kx.png"
      }
    }
    // 重新赋值就可以显示了
    that.setData({
      userStars: tempUserStars
    })
  },
  // 标签
  label: function (e) {
    var that = this;
    that.setData({
      attitude: !e.currentTarget.dataset.index,
      trust: "可以信任"
    })
  },
  label1: function (e) {
    var that = this;
    that.setData({
      time: !e.currentTarget.dataset.index,
      timely: "反馈及时"
    })
  },
  label2: function (e) {
    var that = this;
    that.setData({
      efficiency: !e.currentTarget.dataset.index,
      flexible: "时间灵活"
    })
  },
  label3: function (e) {
    var that = this;
    that.setData({
      environment: !e.currentTarget.dataset.index,
      salary: "工资可观"
    })
  },
  label4: function (e) {
    var that = this;
    that.setData({
      professional: !e.currentTarget.dataset.index,
      meaning: "工作有意义"
    })
  },
  // 留言
  //字数限制
  inputs: function (e) {
    // 获取输入框的内容
    var value = e.detail.value;
    // 获取输入框内容的长度
    var len = parseInt(value.length);
    //最多字数限制
    if (len > this.data.max)
      return;
    // 当输入框内容的长度大于最大长度限制（max)时，终止setData()的执行
    this.setData({
      currentWordNumber: len, //当前字数
      more: value
    });
  },

  change() {
    let that = this;
    var ow_number = -1
    var ow_number = wx.getStorageSync("ow_number");
    app.globalData.ow_number = ow_number;
    wx.removeStorageSync("ow_number");
    this.setData({
      ow_number: ow_number
    })
    console.log(this.data.ow_number)
    var iw_number = -1
    var iw_number = wx.getStorageSync("iw_number");
    wx.removeStorageSync("iw_number");
    this.setData({
      iw_number: iw_number
    })



    wx.request({
      url: app.globalData.url + '/feedbackEr/', 
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber: app.globalData.user,
        ow_number: that.data.ow_number,
        iw_number: that.data.iw_number,
        score: that.data.wjxScore,
        trust: that.data.trust,
        timely: that.data.timely,
        flexible: that.data.flexible,
        salary: that.data.salary,
        meaning: that.data.meaning,
        more: that.data.more,
        content:that.data.content,
      },
      success: (res) => {
        if (res.statusCode == 200) {
          wx.showToast({
            title: '评价成功',
            icon: 'success',
            duration: 1500,
            mask: true,
          })
          setTimeout(function () {
            wx.reLaunch({
              url: '../smyJob/smyJob?pingjia=1'
            })
          }, 1500)
        }
      }
    })
  },

})