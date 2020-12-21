// pages/contact/contact.js
const app = getApp();

var inputVal = '';
var msgList = [];
var windowWidth = wx.getSystemInfoSync().windowWidth;
var windowHeight = wx.getSystemInfoSync().windowHeight;
var keyHeight = 0;

/**
 * 初始化数据
 */
// function initData(that) {
//   inputVal = '';


//   that.setData({
//     msgList,
//     inputVal
//   })
// }

Page({

  /**
   * 页面的初始数据
   */
  data: {
    scrollHeight: '100vh',
    inputBottom: 0,
    to: '',
    name: '',
    msgList: '',
    inputVal: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      //to: options.stu_number,
      //to_name:options.name,
      to:options.name,
      name: app.globalData.user,
      msgList: app.globalData.msgList,
    }); 
    this.receivemsg();
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {


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
   * 获取聚焦
   */
  focus: function (e) {
    keyHeight = e.detail.height;
    this.setData({
      scrollHeight: (windowHeight - keyHeight) + 'px'
    });
    this.setData({
      toView: 'msg-' + (msgList.length - 1),
      inputBottom: keyHeight + 'px'
    })
    //计算msg高度
    // calScrollHeight(this, keyHeight);

  },

  //失去聚焦(软键盘消失)
  blur: function (e) {
    this.setData({
      scrollHeight: '100vh',
      inputBottom: 0
    })
    this.setData({
      toView: 'msg-' + (msgList.length - 1)
    })

  },

  /**
   * 发送点击监听
   */
  sendClick: function (e) {
    var message = {}; //一条消息
    message["from"] = this.data.name;
    message["to"] = this.data.to;
    message["time"] = Date.now();
    message["content"] = e.detail.value;
    message['isread'] = 1;

    //发送消息
    wx.sendSocketMessage({
      data: JSON.stringify(message),
      complete: this.updatemsglist(message),
    })
  },

  updatemsglist: function (message) {
    console.log("我在updatemsglist");
    this.data.msgList.push(message);
    inputVal = '';
    this.setData({ //更新消息列表
      inputVal,
      msgList: this.data.msgList
    });
  },

  receivemsg: function () {
    console.log("receivemsg");
    wx.showToast({
      title: '收到一条新消息',
    })
    //接收消息后，添加到消息列表
    wx.onSocketMessage((result) => {
      var that = this;
      let msg = JSON.parse(result.data)["message"];
      for (var i = 0; i < msg.length; i++) {
        that.data.msgList.push(msg[i]);
      }
      console.log(that.data.msgList)
      this.setData({ //更新消息列表
        msgList: that.data.msgList
      });
    })
  },

  /**
   * 退回上一页
   */
  toBackClick: function () {
    wx.navigateBack({})
  }

})