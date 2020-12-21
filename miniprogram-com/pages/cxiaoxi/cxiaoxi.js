// pages/cxiaoxi/cxiaoxi.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    mianshitongzhi:[],
    dahuitongzhi:[],
    count1:"",
    count2:"",
    show1:true,
    show2:true,
    name: '',
    list: [{
      id: "001",
      name: "2018141093036",
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

  /**
   * 生命周期函数--监听页面加载
   */

  tongzhi() {
    wx.navigateTo({
      url: '../cmianshitongzhi/cmianshitongzhi?user=' + app.globalData.user,
    })
  },

  dahui() {
    wx.navigateTo({
      url: '../cmianshidahui/cmianshidahui?user=' + app.globalData.user,
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
  onLoad: function (options) {
    this.setData({
      name: app.globalData.user
    })
    let that = this;
    wx.request({
      url: app.globalData.url + '/Com_interview_notice_show/', 
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
          if(that.data.count1==0){
            that.setData({
              show1:false
            })
          }
        }
      }
    })

    wx.request({
      url: app.globalData.url + '/Com_interview_back_show/',
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
            dahuitongzhi: res.data,
            count2:res.data.length
          })
          if(that.data.count2==0){
            that.setData({
              show2:false
            })
          }
        }
        
      }
    })
  },

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    this.getData();
  },
  getData() {
    let that = this;
    wx.request({
      url: app.globalData.url + '/Com_interview_notice_show/', 
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
          if(that.data.count1==0){
            that.setData({
              show1:false
            })
          }
        }
      }
    })

    wx.request({
      url: app.globalData.url + '/Com_interview_back_show/', 
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
            dahuitongzhi: res.data,
            count2:res.data.length
          })
          if(that.data.count2==0){
            that.setData({
              show2:false
            })
          }
        }
        //隐藏loading 提示框
        wx.hideLoading();
        //隐藏导航条加载动画
        wx.hideNavigationBarLoading();
        //停止下拉刷新
        wx.stopPullDownRefresh();
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
    this.onRefresh();
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