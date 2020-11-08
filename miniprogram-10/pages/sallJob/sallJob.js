// pages/sallJob/sallJob.js
const app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tabTxt: ['类型', '综合排序', '区域'], //分类
    tab: [true, true, true],
    pinpaiList: [{
        'id': '1',
        'title': '家教'
      },
      {
        'id': '2',
        'title': '调研'
      },
      {
        'id': '3',
        'title': '服务员'
      },
      {
        'id': '4',
        'title': '实习'
      },
      {
        'id': '5',
        'title': '客服'
      },
      {
        'id': '6',
        'title': '安保'
      },
      {
        'id': '7',
        'title': '会展活动'
      },
      {
        'id': '8',
        'title': '代理'
      },
      {
        'id': '9',
        'title': '演出'
      },
      {
        'id': '10',
        'title': '送餐'
      },
      {
        'id': '11',
        'title': '摄影剪辑'
      },
      {
        'id': '12',
        'title': '翻译'
      },
      {
        'id': '13',
        'title': '设计'
      },
      {
        'id': '14',
        'title': '文案编辑'
      }
    ],

    pinpai_id: 0, //类型
    pinpai_txt: '',
    paixu_id: 0, //排序
    paixu_txt: '',
    xiaoliang_id: 0, //筛选
    xiaoliang_txt: '',

    workinfo: [],
  },

  // 选项卡
  filterTab: function (e) {
    var data = [true, true, true],
      index = e.currentTarget.dataset.index;
    data[index] = !this.data.tab[index];
    this.setData({
      tab: data
    })
  },


  //筛选项点击操作
  filter: function (e) {
    var self = this,
      id = e.currentTarget.dataset.id,
      txt = e.currentTarget.dataset.txt,
      tabTxt = this.data.tabTxt;
    switch (e.currentTarget.dataset.index) {
      case '0':
        tabTxt[0] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          leixing_id: id,
          leixing_txt: txt
        });
        break;
      case '1':
        tabTxt[1] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          paixu_id: id,
          paixu_txt: txt
        });
        break;

    }
    //数据筛选
    self.getDataList();
  },

  //加载数据
  getDataList: function () {
    //调用数据接口，获取数据
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let self=this;
    wx.request({
      url: app.globalData.url + '/show/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data: {
        jobtype: "校内",
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          /*for(var index in res.data){*/
          self.setData({
            workinfo:res.data
            /*type:res.data[index].type,
            title:res.data[index].title,待修改*/
            /*amount:res.data[index].amount,
            place:res.data[index].place,
            salary:res.data[index].salary,
            depart:res.data[index].depart,*/
          })
        /*}*/
      }
    }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    this.animation = wx.createAnimation()
  },

  translate: function () {
    this.setData({
      isRuleTrue: true
    })
    this.animation.translate(-245, 0).step()
    this.setData({
      animation: this.animation.export()
    })
  },

  success: function () {
    this.setData({
      isRuleTrue: false
    })
    this.animation.translate(0, 0).step()
    this.setData({
      animation: this.animation.export()
    })
  },
  tryDriver: function () {
    this.setData({
      background: "#89dcf8"
    })
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