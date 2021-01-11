// pages/contact/contact.js聊天界面
const app = getApp();
var chat = require('../../utils/chat.js')
var inputVal = '';
var msgList = [];
var windowWidth = wx.getSystemInfoSync().windowWidth;
var windowHeight = wx.getSystemInfoSync().windowHeight;
var keyHeight = 0;

Page({
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
    if (!(options.name in app.globalData.msgList)) {
      app.globalData.msgList[options.name] = [];
    }
    this.setData({
      to: options.name,
      name: app.globalData.user,
      msgList: app.globalData.msgList[options.name],
    });
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    chat.update_chatting_history(this.data.to); //将与当前聊天用户的记录均置为已读
    wx.onSocketMessage((result) => {
      console.log("我在chatting.js")
      let msg = JSON.parse(result.data)["message"];
      chat.update_globalData_msgList_chatting(msg, this.data.to)
      this.setData({ //更新消息列表
        msgList: app.globalData.msgList[this.data.to]
      });
    })
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
    app.globalData.msgList[this.data.to].push(message);
    inputVal = '';
    this.setData({ //更新消息列表
      inputVal,
      msgList: app.globalData.msgList[this.data.to]
    });
  },

  receivemsg: function () {
    console.log("receivemsg");
    //接收消息后，添加到消息列表
    wx.onSocketMessage((result) => {
      console.log("我在chatting.js")
      let msg = JSON.parse(result.data)["message"];
      chat.update_globalData_msgList(msg, this.data.to)
      this.setData({ //更新消息列表
        msgList: app.globalData.msgList[this.data.to]
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