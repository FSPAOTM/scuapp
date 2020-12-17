// pages/sfeedback/sfeedback.js
const app = getApp();
Page({
  data: {
    ow_number: "",
    stu_number:"",
    staticImg: app.globalData.staticImg,
    current: 0,
    attitude: true,
    time: true,
    efficiency: true,
    environment: true,
    professional: true,
    serious: "",
    manner: "",
    timely: "",
    labor: "",
    ability: "",
    more:"",
    code:1,
    code1:2,
    userStars: [
      "sx2.png",
      "sx2.png",
      "sx2.png",
      "sx2.png",
      "sx2.png",
    ],
    wjxScore: 5,
    // textarea
    min: 10,//最少字数
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
        tempUserStars[i] = "sx2.png";
        that.setData({
          wjxScore: i + 1,
        })
      } else { // 其他是空心
        tempUserStars[i] = "kx2.png"
      }
    }
    // 重新赋值就可以显示了
    that.setData({
      userStars: tempUserStars
    })
  },
  // 标签
  label: function (e) {
    console.log(e)
    var that = this;
    that.setData({
      attitude: !e.currentTarget.dataset.index,
      serious: "认真负责"
    })
  },
  label1: function (e) {
    console.log(e)
    var that = this;
    that.setData({
      time: !e.currentTarget.dataset.index,
      manner: "态度端正"
    })
  },
  label2: function (e) {
    console.log(e)
    var that = this;
    that.setData({
      efficiency: !e.currentTarget.dataset.index,
      timely: "联系及时"
    })
  },
  label3: function (e) {
    console.log(e)
    var that = this;
    that.setData({
      environment: !e.currentTarget.dataset.index,
      labor: "吃苦耐劳"
    })
  },
  label4: function (e) {
    console.log(e)
    var that = this;
    that.setData({
      professional: !e.currentTarget.dataset.index,
      ability: "工作能力强"
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
    var stu_number = -1
    var stu_number = wx.getStorageSync("stu_number");
    wx.removeStorageSync("stu_number");
    this.setData({
      stu_number: stu_number
    })



    wx.request({
      url: app.globalData.url + '/feedbackEr/', //待修改
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        com:app.globalData.user,
        stuNumber:that.data.stuNumber,
        ow_number: that.data.ow_number,
        score: that.data.wjxScore,
        serious: that.data.serious,
        manner: that.data.manner,
        timely: that.data.timely,
        labor: that.data.labor,
        ability: that.data.ability,
        more: that.data.more
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
              url: '../cworkspace/cworkspace?pingjia=1'
            })
          }, 1500)
        }
      }
    })
  }
})