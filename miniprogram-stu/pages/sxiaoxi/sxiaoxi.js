// pages/sxiaoxi/sxiaoxi.js
const app=getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    mianshitongzhi:[],
    jieguotongzhi:[],
    show1:true,
    show2:true,
    count1:"",
    count2:"",
    name: '',
    list: [{
      id: "001",
      name: "18310086086",
      count: "2",
      avatar: "../../images/head.png",
      text: "正在载入聊天列表，请稍候",
      updated: "2020.11.02"
    }, {
      id: "002",
      name: "show",
      count: "2",
      avatar: "../../images/head.png",
      text: "正在载入聊天列表，请稍候",
      updated: new Date()
    }, {
      id: "003",
      name: "as先生",
      count: "2",
      avatar: "../../images/head.png",
      text: "正在载入聊天列表，请稍候",
      updated: new Date()
    }, {
      id: "004",
      name: "练习生",
      count: "0",
      avatar: "../../images/head.png",
      text: "邮票吗",
      updated: new Date()
    }, {
      id: "005",
      name: "练习生o",
      count: "2",
      avatar: "../../images/head.png",
      text: "正在载入聊天列表，请稍候",
      updated: new Date()
    }],
  },

  mianshi() {
    wx.navigateTo({
      url: '../smianshitongzhi/smianshitongzhi?user=' + app.globalData.user,
    })
  },

  jieguo() {
    wx.navigateTo({
      url: '../sjieguotongzhi/sjieguotongzhi?user=' + app.globalData.user,
    })
  },

  goPage(e) {
    let newlist = this.data.list
    const index = e.currentTarget.dataset.index
    newlist[index].count = 0;
    this.setData({
      list: newlist
    })
    wx.navigateTo({
      url: '../schatting/schatting?name=' + e.currentTarget.dataset.name  /**?? */
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/', 
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            mianshitongzhi: res.data,
            count1:res.data.length
          })
        }
      }
    })

    wx.request({
      url: app.globalData.url + '/Stu_interview_notice_show/', //待修改
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          that.setData({
            jieguotongzhi: res.data,
            count2:res.data.length//待修改
          })
        }
      }
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