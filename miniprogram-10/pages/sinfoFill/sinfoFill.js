// pages/infoFill/infoFill.js
const app = getApp();
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
    edu: '请选择学历',
    name: "",
    age: "",
    gender: "",
    tech: "",
    job: "",
    project: "",
    practice: "",
    works: "",
    stuNumber: "",
    result:"",
  },

  onLoad: function (e) {
    wx.request({
      url: 'http://127.0.0.1:8000/wechat/Insert_resume_show/',
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      method: "POST",
      data: {
        stuNumber: app.globalData.user,
      },
      success: (res) => {
        console.log(res);
        console.log(this.data.stuNumber);
        if (res.statusCode == 200) {
          console.log(res.data);
          this.setData({
            name: res.data.name,
            age: res.data.age,
            gender: res.data.sex,
            tech: res.data.res_asses,
            edu: res.data.res_edu,
            job: res.data.res_work,
            project: res.data.res_proj,
            practice: res.data.res_extra,
            works: res.data.res_per,
          })
          app.globalData.age = this.data.age;
        }
      }
    })
  },

  blurname: function (e) {
    if (e.detail.value != "null") {
    this.setData({
      name: e.detail.value
    })
  }
  },

  blurage: function (e) {
    if (e.detail.value != "null") {
    this.setData({
      age: e.detail.value
    })
  }
  },

  genderchange: function (e) {
    if (e.detail.value != "null") {
    this.setData({
      gender: e.detail.value
    })
  }
  },

  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      edu: this.data.array[e.detail.value]
    })
    app.globalData.edu = this.data.array[e.detail.value];
  },

  blurtech: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        tech: e.detail.value
      })
    }
  },

  blurjob: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        job: e.detail.value
      })
    }
  },

  blurproject: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        project: e.detail.value
      })
    }
  },

  blurpractice: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        practice: e.detail.value
      })
    }
  },

  blurworks: function (e) {
    if (e.detail.value != "null") {
      this.setData({
        works: e.detail.value
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
    if (this.data.age.length == 0) {
      wx.showToast({
        title: '年龄不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.gender != "男" && this.data.gender != "女") {
      wx.showToast({
        title: '性别不能为空!',
        icon: 'none',
        duration: 2000
      })
      setTimeout(function () {
        wx.hideToast()
      }, 2000)
    } else if (this.data.edu != "专科" && this.data.edu != "本科" && this.data.edu != "研究生") {
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
        url: 'http://127.0.0.1:8000/wechat/Insert_resume_change/',
        header: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        method: "POST",
        data: {
          stuNumber: app.globalData.user,
          name: this.data.name,
          age: this.data.age,
          gender: this.data.gender,
          edu: this.data.edu,
          tech: this.data.tech,
          job: this.data.job,
          project: this.data.project,
          practice: this.data.practice,
          works: this.data.works
        },
        success: (res) => {
          /*console.log(res.data);*/
          if (res.statusCode == 200) {
            this.setData({
              result: res.data
            })
            if (res.data = "填写完成") {
              wx.showToast({
                title: '提交成功！！！', //这里打印出登录成功
                icon: 'success',
                duration: 1000
              })
              setTimeout(function () {
                wx.switchTab({
                  url: '../scenter/scenter',
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




  // 上传图片
  /*logo: function () {
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
  },*/

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