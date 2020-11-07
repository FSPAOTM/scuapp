// pages/cinfoFill/cinfoFill.js
var app=getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cno:"",
    phone:"",
    company:"",
    manname:"",
    email:"",
    address:"",
    contents:"",
    condition:"",
    result:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Insert_resume_show/',/*待修改*/
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        cno: app.globalData.user,
      },
      success: (res) => {
        console.log(res);
        console.log(this.data.cno);
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            cno:app.globalData.user,
            phone: res.data.phone_num,
            company: res.data.com_name,
            manname: res.data.com_leader,
            email: res.data.e_mail,
            address: res.data.com_address,
            contents: res.data.com_business,
            condition: res.data.com_condition,
          })
        }
      }
    })
  },

  blurphone: function (e) {
    if (e.detail.value != "null") {
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
    let that=this;
    //console.log(e.detail.value);
    app.globalData.age = this.data.age;
    app.globalData.gender = this.data.gender;
    app.globalData.tech = this.data.tech;
    app.globalData.job = this.data.job;
    app.globalData.project = this.data.project;
    app.globalData.practice = this.data.practice;
    app.globalData.works = this.data.works;
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
    } else if (this.data.address.length == 0) {
      wx.showToast({
        title: '公司地址不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else{
      wx.request({
        url: 'http://127.0.0.1:8000/wechat/Insert_resume_change/',/*待修改*/
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        method: "POST",
        data: {
          cno: app.globalData.user,
          phone: this.data.phone,
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
                wx.switchTab({
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