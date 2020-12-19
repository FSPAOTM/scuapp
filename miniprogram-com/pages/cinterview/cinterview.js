// pages/cinterview/cinterview.js
var dateTimePicker = require('outer.js');
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    ow_number:"",
    user:"",
    post:"",
    manager:"",
    phonenum:"",
    applytime1:"",
    applytime2:"",
    applytime3:"",
    dateTimeArray: null,
    dateTime: null,
    dateTimeArray1: null,
    dateTime1: null,
    dateTimeArray2: null,
    dateTime2: null,
    dateTimeArray3: null,
    dateTime3: null,
    startYear: 2020,
    endYear: 2022
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      post:options.post,
      ow_number:options.ow_number
    })
    // 获取完整的年月日 时分秒，以及默认显示的数组
    var obj = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    var obj1 = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    var obj2 = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    var obj3 = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
    // 精确到分的处理，将数组的秒去掉
    var lastArray = obj1.dateTimeArray.pop();
    var lastTime = obj1.dateTime.pop();
    
    this.setData({
      dateTime: obj.dateTime,
      dateTimeArray: obj.dateTimeArray,
      dateTimeArray1: obj1.dateTimeArray,
      dateTime1: obj1.dateTime,
      dateTimeArray2: obj2.dateTimeArray,
      dateTime2: obj2.dateTime,
      dateTimeArray3: obj3.dateTimeArray,
      dateTime3: obj3.dateTime,
    });
  },

  /*changeDate(e){
    this.setData({ date:e.detail.value});
  },
  changeTime(e){
    this.setData({ time: e.detail.value });
  },
  changeDateTime(e){
    this.setData({ dateTime: e.detail.value });
  },
  changeDateTime1(e) {
    this.setData({ dateTime1: e.detail.value });
  },*/

  changeDateTimeColumn1(e) {
    var arr = this.data.dateTime1, dateArr = this.data.dateTimeArray1;

    arr[e.detail.column] = e.detail.value;
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);

    this.setData({ 
      dateTimeArray1: dateArr,
      dateTime1: arr,
      applytime1:(2020+arr[0]) +"-"+ (1+arr[1]) +"-"+ (1+arr[2]) +" "+ arr[3] +":"+ arr[4]
    });
  },

  changeDateTimeColumn2(e) {
    var arr = this.data.dateTime2, dateArr = this.data.dateTimeArray2;

    arr[e.detail.column] = e.detail.value;
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);

    this.setData({ 
      dateTimeArray2: dateArr,
      dateTime2: arr,
      applytime2:(2020+arr[0]) +"-"+ (1+arr[1]) +"-"+ (1+arr[2]) +" "+ arr[3] +":"+ arr[4]
    });
  },

  changeDateTimeColumn3(e) {
    var arr = this.data.dateTime3, dateArr = this.data.dateTimeArray3;

    arr[e.detail.column] = e.detail.value;
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);

    this.setData({ 
      dateTimeArray3: dateArr,
      dateTime3: arr,
      applytime3:(2020+arr[0]) +"-"+ (1+arr[1]) +"-"+ (1+arr[2]) +" "+ arr[3] +":"+ arr[4]
    });
  },

  blurpost: function (e) {
    this.setData({
      post: e.detail.value
    })
  },

  blurmanager: function (e) {
    this.setData({
      manager: e.detail.value
    })
  },

  blurphone: function (e) {
    this.setData({
      phonenum: e.detail.value
    })
  },

  formSubmit: function (e) {
    let that = this;
    if (this.data.post.length == 0) {
      wx.showToast({
        title: '面试岗位不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.manager.length == 0) {
      wx.showToast({
        title: '面试负责人不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.phonenum.length == 0) {
      wx.showToast({
        title: '手机号不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    }else if (this.data.applytime1.length == 0) {
      wx.showToast({
        title: '面试申请时间不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    }else {
      wx.request({
        url: app.globalData.url + '/Company_apply_interviewtime/',
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        data: {
          ow_number: that.data.ow_number,
          post: that.data.post,
          manager: that.data.manager,
          phonenum: that.data.phonenum,
          applytime1: that.data.applytime1,
          applytime2: that.data.applytime2,
          applytime3: that.data.applytime3,
        },
        success: (res) => {
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data == "提交成功") {
              wx.showToast({
                title: '申请提交成功！！！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.reLaunch({
                  url: '../cfabu/cfabu?operation=已申请',
                })
              }, 2000)
            }else if (res.data == "存在学生简历未初步审核,无法申请面试"){
              wx.showToast({
                title: '存在学生简历未初步审核,无法申请面试',
                icon:'none',
                duration: 2000
              })
            }
          } else {
            wx.showToast({
              title: '请求错误',
              icon: 'none',
              duration: 1000
            })
          }
        }
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