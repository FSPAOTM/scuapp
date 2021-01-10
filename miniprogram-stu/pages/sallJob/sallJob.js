// pages/sallJob/sallJob.js学生查看所有可报名工作
const app = getApp();
Page({
  data: {
    tabTxt: ['类型', '综合排序', '区域'], //分类
    tab: [true, true, true],
    leixing_id: 0, //类型
    leixing_txt: '',
    paixu_id: 0, //排序
    paixu_txt: '',
    area_id: 0, //筛选
    area_txt: '',

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
        console.log(this.data.leixing_txt)
        console.log(this.data.paixu_txt)
        console.log(this.data.area_txt)
        self.onRefresh();
        break;
      case '1':
        tabTxt[1] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          paixu_id: id,
          paixu_txt: txt
        });
        self.onRefresh();
        break;
      case '2':
        tabTxt[2] = txt;
        self.setData({
          tab: [true, true, true],
          tabTxt: tabTxt,
          area_id: id,
          area_txt: txt
        });
        self.onRefresh();
        break;
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let self = this;
    wx.request({
      url: app.globalData.url + '/Show_work/',
      method: "GET",
      data: {
        stu_number: app.globalData.user,
        type: this.data.leixing_txt,
        order: this.data.paixu_txt,
        area: this.data.area_txt
      },
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
  },

  // 点击进入工作详情页
  sjobinfo: function (ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    var type = that.data.workinfo[e].type;
    if (that.data.workinfo[e].iw_number != "NULL") {
      var iw_number = that.data.workinfo[e].iw_number;
      console.log("++++++", ev, that)
      wx.setStorageSync("iw_number", iw_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sbaoming/sbaoming"
      })
    } else {
      var ow_number = that.data.workinfo[e].ow_number;
      console.log(ow_number);
      console.log("++++++", ev, that)
      wx.setStorageSync("ow_number", ow_number), wx.setStorageSync('type', type), wx.navigateTo({
        url: "../sbaoming/sbaoming"
      })
    }
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
    app.editTabBar();
  },

// 刷新动作
  onRefresh() {
    //在当前页面显示导航条加载动画
    wx.showNavigationBarLoading();
    //显示 loading 提示框。需主动调用 wx.hideLoading 才能关闭提示框
    wx.showLoading({
      title: '刷新中...',
      duration: 2000
    })
    this.getData();
  },
  //网络请求，获取数据
  getData() {
    let self = this;
    wx.request({
      url: app.globalData.url + '/Show_work/',
      method: "GET",
      data: {
        stu_number: app.globalData.user,
        type: this.data.leixing_txt,
        order: this.data.paixu_txt,
        area: this.data.area_txt
      },
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
  }
})