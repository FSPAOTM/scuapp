// pages/cinfoFill/cinfoFill.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cno: "",
    phone: "",
    company: "",
    manname: "",
    email: "",
    address: "",
    contents: "",
    condition: "",
    result: "",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    console.log(app.globalData.user);
    wx.request({
      url: app.globalData.url + '/Company_info_showmodiify/',
      method: "POST",
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      data: {
        phone: app.globalData.user,
      },
      success: (res) => {
        console.log(res);
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            cno: res.data.cno,
            phone: app.globalData.user,
            company: res.data.company,
            manname: res.data.manname,
            email: res.data.email,
            address: res.data.address,
            contents: res.data.contents,
            condition: res.data.condition,
          })
        }
      }
    })
  },

  blurphone: function (e) {
    let myreg = /^1[3456789]\d{9}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '手机号不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '请输入正确的手机号',
        icon: 'none',
        duration: 2000
      })
    } else {
      this.setData({
        phone: e.detail.value
      })
    }
  },

  blurman: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        manname: e.detail.value
      })
    }
  },

  bluremail: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        email: e.detail.value
      })
    }
  },

  bluradd: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        address: e.detail.value
      })
    }
  },


  blurcontents: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        contents: e.detail.value
      })
    }
  },

  blurcondition: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        condition: e.detail.value
      })
    }
  },

  formSubmit: function (e) {
    let that = this;
    //console.log(e.detail.value);
    app.globalData.user = this.data.phone;
    if (this.data.phone.length != 11) {
      wx.showToast({
        title: '联系电话有误!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.manname.length == 0) {
      wx.showToast({
        title: '负责人不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.email.length == 0) {
      wx.showToast({
        title: '邮箱不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (!(/^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(.[a-zA-Z0-9-]+)*.[a-zA-Z0-9]{2,6}$/.test(that.data.email))) {
      wx.showToast({
        title: '邮箱输入有误!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.address.length == 0) {
      wx.showToast({
        title: '公司地址不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else {
      wx.request({
        url: app.globalData.url + '/Company_info_modiify/',
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        method: "POST",
        data: {
          cno: this.data.cno,
          phone: app.globalData.user,
          manname: this.data.manname,
          email: this.data.email,
          address: this.data.address,
          contents: this.data.contents,
          condition: this.data.condition,
        },
        success: (res) => {
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data = "填写完成") {
              wx.showToast({
                title: '提交成功！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.redirectTo({
                  url: '../ccenter/ccenter',
                })
              }, 2000)
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