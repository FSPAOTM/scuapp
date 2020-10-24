// pages/infoFill/infoFill.js
const app = getApp();
//var uploadFileUrl = app.d.ceshiUrl + "/Api/Renzheng/uploadimg";
Page({
  data: {
    array: ['请选择学历', '专科', '本科', '研究生'],
    objectArray: [{
        id: 0,
        name: '请选择学历'
      },
      {
        id: 1,
        name: '专科'
      },
      {
        id: 2,
        name: '本科'
      },
      {
        id: 3,
        name: '研究生'
      },

    ],
    edu: 0,
    name: "",
    age: "",
    gender: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
    stuNumber:"",
  },

  onLoad: function (e) {
    console.log(e);
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Insert_resume/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber:app.globalData.stuNumber,
      },
    }),
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Insert_resume/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "GET",
      success: function (res) {
        console.log(res.data);
        app.globalData.user = res.data;
        console.log(app.globalData.user);
        this.setData({
          name: app.globalData.user,
        })
      }
    })
  },

  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      edu: e.detail.value
    })
  },

  formSubmit: function (e) {
    //console.log(e.detail.value);
    if (e.detail.value.age.length == 0) {
      wx.showToast({
        title: '性别不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (e.detail.value.gender != 0 && e.detail.value.gender != 1) {
      wx.showToast({
        title: '性别不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (e.detail.value.edu != 0 && e.detail.value.edu != 1 && e.detail.value.edu != 2 && e.detail.value.edu != 3) {
      wx.showToast({
        title: '教育背景不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else {

      wx.request({
        url: 'http://127.0.0.1:8000/wechat/Insert_resume/',
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        method: "POST",
        data: {
          stuNumber:app.globalData.stuNumber,
          name: e.detail.value.name,
          age: e.detail.value.age,
          gender: e.detail.value.gender,
          edu: e.detail.value.edu,
          tech: e.detail.value.tech,
          job: e.detail.value.job,
          project: e.detail.value.project,
          practice: e.detail.value.practice,
          works: e.detail.value.works
        },
        success: function (res) {
          console.log(res.data);
          if (res.data.status == 0) {
            wx.showToast({
              title: '提交失败！！！',
              icon: 'loading',
              duration: 1500
            })
          } else {
            wx.showToast({
              title: '提交成功！！！', //这里打印出登录成功
              icon: 'success',
              duration: 1000
            })
            setTimeout(function () {
              wx.redirectTo({
                url: '../infoShow/infoShow',
              })
            }, 2000)
          }
        }
      })
    }
  },




  // 上传图片
  logo: function () {
    var self = this
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'],
      success: function (res) {
        console.log('chooseImage success, temp path is', res.tempFilePaths)
        var imageSrc = res.tempFilePaths[0];

        wx.uploadFile({
          url: uploadFileUrl,
          filePath: imageSrc,
          name: 'data',
          success: function (res) {
            console.log('uploadImage success, res is:', res)

            wx.showToast({
              title: '上传成功',
              icon: 'success',
              duration: 1000
            })

            self.setData({
              logo: imageSrc,
              uplogo: res.data
            })
          },
          fail: function ({
            errMsg
          }) {
            console.log('uploadImage fail, errMsg is', errMsg)
          }
        })

      },
      fail: function ({
        errMsg
      }) {
        console.log('chooseImage fail, err is', errMsg)
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