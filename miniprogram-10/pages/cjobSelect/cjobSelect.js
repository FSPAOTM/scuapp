// pages/cjobSelect/cjobSelect.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    buttons: [{
        id: 1,
        name: '家教'
      },
      {
        id: 2,
        name: '服务员'
      },
      {
        id: 3,
        name: '实习'
      },
      {
        id: 4,
        name: '客服'
      },
      {
        id: 5,
        name: '调研'
      },
      {
        id: 6,
        name: '摄影剪辑'
      },
      {
        id: 7,
        name: '文案编辑'
      },
      {
        id: 8,
        name: '安保'
      },
      {
        id: 9,
        name: '送餐'
      },
      {
        id: 10,
        name: '主播'
      },
      {
        id: 11,
        name: '会展活动'
      },
      {
        id: 12,
        name: '代理'
      },
      {
        id: 13,
        name: '演出'
      },
      {
        id: 14,
        name: '翻译'
      },
      {
        id: 15,
        name: '模特礼仪'
      },
      {
        id: 17,
        name: '设计'
      },
      {
        id: 18,
        name: '其他'
      }
    ],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.data.buttons[0].checked = true;
    this.setData({
      buttons: this.data.buttons,
    })
  },

  /**
   * 事件监听,实现单选效果
   * e是获取e.currentTarget.dataset.id所以是必备的，跟前端的data-id获取的方式差不多
   */



  radioButtonTap: function (e) {
    console.log(e);
    let id = e.currentTarget.dataset.id;
    console.log(id);//打印不出来
    for (let i = 0; i < this.data.buttons.length; i++) {
      if (this.data.buttons[i].id == id) {
        //当前点击的位置为true即选中
        this.data.buttons[i].checked = true;
        app.globalData.jobType = this.data.buttons[i].name;
      } else {
        //其他的位置为false
        this.data.buttons[i].checked = false;
      }
    }

  },

  submit() {
    console.log(app.globalData.jobType);
    wx.navigateTo({
      url: '../cjobRelease/cjobRelease',
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