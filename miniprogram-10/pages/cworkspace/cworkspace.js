// pages/cworkspace/cworkspace.js
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //tap切换自定义宽高
    winWidth: 0,
    winHeight: 0,
    // tab切换，方法一

    scrollleft: 0,
    currentTab: 0,

    idArr: [

    ],
    workinfo1: [],
    workinfo2: [],
    workinfo3: [],
    workinfo4: [],
    workinfo5: [],
  },

  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  },

  checkCor: function () {
    if (this.data.currentTab > 4) {
      this.setData({
        scrollleft: 300
      })
    } else {
      this.setData({
        scrollleft: 0
      })
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    /** 
     * 获取系统信息,系统宽高
     */
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          winWidth: res.windowWidth,
          winHeight: res.windowHeight
        });
      }
    });

    that.setData({
      'stu1.index':'',  //给教师对象增加名字属性
      'stu1.name':''
    })

    wx.request({
      url: app.globalData.url + '/Show_applicant/',
      header: {
        'Content-Type': 'application/json'
      },
      method: "GET",
      data: {
        user: app.globalData.user
      },
      success: function (res) {
        console.log(res);
        console.log(res.data[0].status);
        var i;
        for (i = 0; i < res.data.length; i++) {
          if (res.statusCode == 200) {
            if (res.data[i].status == "已报名") {
              that.data.workinfo1.push(res.data[i])
              //that.data.user1.push(res.data[i].user)
              that.setData({
                workinfo1: that.data.workinfo1
              })
              console.log(that.data.workinfo1)
            } else if (res.data[i].status == "表筛未通过") {
              that.data.workinfo2.push(res.data[i])
              that.setData({
                workinfo2: that.data.workinfo2
              })
            } else if (res.data[i].status == "表筛通过") {
              that.data.workinfo3.push(res.data[i])
              that.setData({
                workinfo3: that.data.workinfo3
              })
            } else if (res.data[i].status == "已录用") {
              that.data.workinfo4.push(res.data[i])
              that.setData({
                workinfo4: that.data.workinfo4
              })
            } else if (res.data[i].status == "已结算") {
              that.data.workinfo5.push(res.data[i])
              that.setData({
                workinfo5: that.data.workinfo5
              })
            }
          }
        }
      }
    });
  },

  itemSelected: function (e) {
    var index = e.currentTarget.dataset.index;
    var item = this.data.workinfo3[index];
    item.isSelected = !item.isSelected;
    this.setData({
      workinfo3: this.data.workinfo3,
    });
  },

  yibaoming: function (ev) {
    var that = this;
    var e = ev.currentTarget.dataset.index;
    console.log(e)
    console.log(that.data.workinfo1[e])
    var ow_number = that.data.workinfo1[e].ow_number;
    var stu_number = that.data.workinfo1[e].stu_number;
    console.log("++++++", ev, that)
    wx.setStorageSync("ow_number", ow_number), wx.setStorageSync("stu_number", stu_number), wx.navigateTo({
      url: "../cresumeReview/cresumeReview"
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
    app.editTabBar1();
  },
  /*userlist(e) {
    var index = e.currentTarget.dataset.index;
    if (this.data.selectedFlag[index]){
      this.data.selectedFlag[index] = false;
    }else{
      this.data.selectedFlag[index] = true;
    }

    this.setData({
      selectedFlag: this.data.selectedFlag
    })
  },*/

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