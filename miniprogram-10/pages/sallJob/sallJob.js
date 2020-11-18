// pages/sallJob/sallJob.js
const app = getApp();
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
    areaList:[],
    pinpai_id: 0, //类型
    pinpai_txt: '',
    paixu_id: 0, //排序
    paixu_txt: '',
    area_id: 0, //筛选
    area_txt: '',

    workinfo: [],
  },

  // 选项卡
  filterTab: function (e) {
    var self = this;
    var data = [true, true, true],
      index = e.currentTarget.dataset.index;
    data[index] = !this.data.tab[index];
    this.setData({
      tab: data
    })
    /*wx.request({
      url: 'https://lbs.amap.com/api/webservice/guide/api/district',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        key:"80d1a82ecf4305a0cdd243289f293711",
        keywords:"510100",
        subdistrict:"1",
        extensions:"base",
        filter:"510100",
      },
      success: function (res) {
        console.log(res);
        if (res.status == 1) {
          self.setData({
            areaList: res.data.districts.district
          })
        }
      }
    })*/
  },


  //筛选项点击操作//待完善
  filter1: function (e) {
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

  filter2: function (e) {
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

  filter3: function (e) {
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
    let self = this;
    wx.request({
      url: 'https://lbs.amap.com/api/webservice/guide/api/district',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      data:{
        key:"80d1a82ecf4305a0cdd243289f293711",
        keywords:"510100",
        subdistrict:"1",
        extensions:"base",
        filter:"510100",
      },
      success: function (res) {
        console.log(res);
        if (res.status == 1) {
          self.setData({
            areaList: res.data.districts.district
          })
        }
      }
    })
    wx.request({
      url: app.globalData.url + '/Show_inwork/',
      /*待修改*/
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            workinfo: res.data
          })
        }
      }
    })

    /*wx.request({
      url: app.globalData.url + '/Show_outwork/',
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            oworkinfo: res.data
          })
        }
      }
    
    })*/
  },

  sijobinfo: function (ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo[e].type;
    if (that.data.workinfo[e].iw_number != "null") {
      var iw_number = that.data.workinfo[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sbaoming/sbaoming"
      })
    } else {
      var ow_number = that.data.workinfo[e].ow_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sbaoming/sbaoming"
      })
    }


  },

  /*sojobinfo: function (ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var ow_number=that.data.oworkinfo[e].ow_number;
    var type=that.data.oworkinfo[e].type;
    console.log("++++++", ev, that)
    wx.setStorageSync("ow_number", ow_number),wx.setStorageSync('type', type), wx.navigateTo({
      url: "../sbaoming/sbaoming"
    })
  },*/
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
    app.editTabBar();
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

  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    wx.showLoading({
      title: '刷新中...',
    })
    this.getData();
  },
  //网络请求，获取数据
  getData() {
    let self = this;
    wx.request({
      url: app.globalData.url + '/Show_inwork/',
      /*待修改*/
      method: "GET",
      header: {
        'Content-Type': 'application/json'
      },
      success: function (res) {
        console.log(res);
        if (res.statusCode == 200) {
          self.setData({
            workinfo: res.data
          })
        };
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
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    //调用刷新时将执行的方法
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