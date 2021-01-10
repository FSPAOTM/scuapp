// pages/repwd/repwd.js重置密码
const app = getApp();
Page({
  data: {
    oldpwd: "",
    newpwd: "",
    newpwd2: "",
    no: "",
  },

  // 表单值获取
  old(e) {
    this.setData({
      oldpwd: e.detail.value
    })
  },

  new(e) {
    let myreg = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$]{8,18}$/;
    if (e.detail.value == "") {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 2000
      })
    } else if (!myreg.test(e.detail.value)) {
      wx.showToast({
        title: '密码必须包含数字与字母，可以包含或不包含特殊符号！',
        icon: 'none',
        duration: 2000
      })
    }
    this.setData({
      newpwd: e.detail.value
    })
  },

  again(e) {
    this.setData({
      newpwd2: e.detail.value
    })
  },

  formSubmit: function (e) {
    if (this.data.oldpwd == '' || this.data.newpwd == '' || this.data.newpwd2 == '') {
      wx.showToast({
        title: '密码不能为空',
        icon: 'none',
        duration: 3000
      })
    } else if (this.data.newpwd != this.data.newpwd2) {
      wx.showToast({
        title: '两次密码输入不一致，请重新输入',
        icon: 'none',
        duration: 3000
      })
    } else {
      wx.request({
        url: app.globalData.url + '/Reset_password/',
        method: 'POST',
        data: {
          no: app.globalData.user,
          oldpwd: this.data.oldpwd,
          newpwd: this.data.newpwd,
        },
        header: {
          'content-type': 'application/x-www-form-urlencoded'
        },
        success: (res) => {
          console.log(res.data);
          if (res.data == "原密码输入不正确，请重新输入") {
            wx.showToast({
              title: "原密码输入不正确，请重新输入！",
              icon: 'none',
              duration: 2000
            })
          } else if (res.data == "密码修改成功") {
            wx.showToast({
              title: "修改成功！",
              icon: 'success',
              duration: 2000,
              success: function () {
                setTimeout(function () {
                  wx.navigateBack({
                    belta: 1
                  })
                }, 2000)
              }
            })
          } else {
            wx.showToast({
              title: "请求错误",
              icon: 'none',
              duration: 2000
            })
          }
        }
      })
    }
  }
})